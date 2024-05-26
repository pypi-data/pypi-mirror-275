import abc
import asyncio
import os
import traceback
from typing import Union

from aio_rabbitmq import RabbitMQSettings
from tg_logger import BaseLogger, ResponsibleLogger

from .client_manager import TelethonClientManager
from .telethon.client import PatchedTelegramClient
from .utils import (AsyncList, ShuttingDown, TGBotAbstractModel,
                    configure_rabbitmq)
from .voices import VoiceTranscription


class TGBotManager:
    client_class: TelethonClientManager
    responsible: bool
    receive_updates: bool
    timeout: int = 2
    try_limit: int = 5
    rabbitmq_settings: RabbitMQSettings = RabbitMQSettings()

    def __init__(
            self,
            tgbots_list: list[TGBotAbstractModel],
            number: Union[int, str]
    ) -> None:
        self.logger = BaseLogger()
        self.loop = asyncio.new_event_loop()
        self.tasks_config = []
        self.rabbitmq = configure_rabbitmq(
            self.rabbitmq_settings, self.logger, self.loop
        )
        self.tgbots_list = AsyncList(tgbots_list)
        self.number = number
        self.manager_name = 'responsible' if self.responsible else 'listening'
        self.client_manager = self.client_class(
            self.number, tgbots_list, self.responsible, self.loop, self.logger,
            self.send_msgs_for_update_client, self.receive_updates
        )

    async def get_client(self, tgbot_id: int) -> PatchedTelegramClient:
        return await self.client_manager.get_client(tgbot_id)

    async def aio_stop(self):
        await self.client_manager.aio_stop()
        await self.rabbitmq.aio_stop()

    def stop(self, **kwargs):
        self.loop.run_until_complete(
            self.aio_stop()
        )
        self.loop.stop()

    async def send_msgs_for_update_client(
            self, tgbot: TGBotAbstractModel, channel=None
    ):
        if channel is None:
            channel = await self.rabbitmq.get_one_time_use_channel()
        queue_name = (f'{self.rabbitmq_settings.prefix}update'
                      f'_{self.manager_name}')
        if self.responsible:
            queue_name += f'_{self.number}'
        await self.rabbitmq.send_message(
            queue_name,
            channel,
            tgbot,
        )

    @abc.abstractmethod
    async def start_tasks(self):
        pass

    def start_chatting(self):
        self.logger.start_chatting('info')
        asyncio.set_event_loop(self.loop)
        try:
            self.loop.run_until_complete(self.start_tasks())
        except asyncio.exceptions.CancelledError as ce:
            raise RuntimeError('CancelledError detected') from ce


class ListeningTGBotManager(TGBotManager):
    responsible: bool = False
    receive_updates: bool = False

    def __init__(self, tgbots_list: list[TGBotAbstractModel]):
        self.number = 'listening'
        super().__init__(tgbots_list, self.number)

    async def aio_stop(self):
        async for tgbot_id, _ in self.client_manager.clients:
            await self.stop_handlers(tgbot_id)
        await super().aio_stop()

    @abc.abstractmethod
    async def wait_messages(self, tgbot: TGBotAbstractModel, tgbot_id, client):
        pass

    async def start_handlers(self, tgbot: TGBotAbstractModel) -> None:
        client = await self.get_client(tgbot.tgbot_id)
        asyncio.create_task(
            self.wait_messages(tgbot, tgbot.tgbot_id, client),
            name=f'wait_messages_{tgbot.tgbot_id}'
        )

    async def stop_handlers(self, tgbot_id: int) -> None:
        for task in asyncio.all_tasks():
            if task.get_name() == f'wait_messages_{tgbot_id}':
                task.cancel()
                self.logger.stop_handlers(
                    'info', f'Waiting messages for {tgbot_id=}, was cancelled'
                )

    async def process_update_listener_tgbot(
            self, tgbot: TGBotAbstractModel, at_start: bool = False
    ) -> None:
        if not isinstance(tgbot, ShuttingDown):
            await self.stop_handlers(tgbot.tgbot_id)
            await self.client_manager.process_update_tgbot(
                tgbot, at_start=at_start
            )
            await self.start_handlers(tgbot)
        else:
            async for tgbot_id in self.client_manager.clients:
                await self.stop_handlers(tgbot_id)
            await self.client_manager.process_update_tgbot(tgbot)

    async def start_tasks(self) -> None:
        self.logger.start_tasks_listener('info')
        await self.client_manager.run()
        await asyncio.sleep(10)
        async for tgbot in self.tgbots_list:
            await self.start_handlers(tgbot)
        channel = await self.rabbitmq.get_channel(robust=True)
        try:
            await asyncio.gather(
                self.rabbitmq.consume_queue(
                    f'{self.rabbitmq_settings.prefix}update'
                    f'_{self.manager_name}',
                    channel,
                    self.process_update_listener_tgbot
                )
            )
        except asyncio.exceptions.CancelledError as exc:
            trace = traceback.format_exc()
            self.logger.start_chatting_error('error', f'{exc}\n{trace}')
            raise exc


class ResponsibleTGBotManager(TGBotManager):
    responsible: bool = True
    receive_updates: bool = True
    transcription_openai_key: str

    def __init__(
            self,
            tgbots_list: list[TGBotAbstractModel],
            number: int
    ) -> None:
        super().__init__(tgbots_list, number)
        self.logger = ResponsibleLogger(number)
        self.rabbitmq.logger = self.logger
        self.voice_transcription = VoiceTranscription(
            self.transcription_openai_key, self.logger
        )

    async def _get_input_message_data(self, client, event):
        data = {}
        if event.voice is not None:
            try:
                voice = await self.voice_transcription.get_voice_wav(
                    client, event)
                data['transcription'] = (
                    await self.voice_transcription.get_text_transcription(
                        voice)
                )
                os.unlink(voice)
            except Exception as exc:
                trace = traceback.format_exc()
                self.logger.get_input_message(
                    'error', f'Error: {exc}. Traceback: {trace}.'
                )
            else:
                data['is_voice'] = True
        self.logger.get_input_message_data('info')
        return data

    async def start_tasks(self) -> None:
        self.logger.start_tasks('info')
        await self.client_manager.run()
        await asyncio.sleep(10)
        channel = await self.rabbitmq.get_channel(robust=True)
        print(f">>>> Start tasks {self.client_manager.clients}")
        tasks = []
        for queue_suffix, callback, kwargs in self.tasks_config:
            queue_name = f'{self.rabbitmq_settings.prefix}{queue_suffix}_{self.number}'
            tasks.append(
                self.rabbitmq.consume_queue(
                    queue_name, channel, callback, **kwargs
                )
            )
        try:
            await asyncio.gather(*tasks)
        except asyncio.exceptions.CancelledError as exc:
            trace = traceback.format_exc()
            self.logger.start_chatting_error('error', f'{exc}\n{trace}')
            raise exc
