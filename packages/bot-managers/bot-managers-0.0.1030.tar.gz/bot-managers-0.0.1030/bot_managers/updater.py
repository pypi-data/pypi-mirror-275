import asyncio
from typing import Union

from aio_rabbitmq import RabbitMQSettings
from tg_logger import BaseLogger

from .utils import (ShuttingDown, TGBotAbstractModel, configure_rabbitmq,
                    safe_get_loop)


async def aio_update_tgbot(
        tgbot_id: Union[int, ShuttingDown],
        rabbitmq_settings: RabbitMQSettings,
        logger: BaseLogger,
        timeout: int = 2,
        expiration: int = 15,
        update_queue_name: str = 'update',
        type_manager: str = None
) -> None:
    from .settings import NUMBER_OF_MANAGERS
    loop = safe_get_loop()
    rabbitmq = configure_rabbitmq(rabbitmq_settings, logger, loop)
    channel = await rabbitmq.get_one_time_use_channel()
    if type_manager != 'responsible':
        name_manager = 'listening'
        await rabbitmq.send_message(
            f'{rabbitmq_settings.prefix}{update_queue_name}_{name_manager}',
            channel,
            tgbot_id,
            expiration=expiration,
        )
        if isinstance(tgbot_id, ShuttingDown):
            logger.update_tgbot(
                'info', f'Shutting down {name_manager}'
            )
        else:
            logger.update_tgbot(
                'info', f'Send msg for update {name_manager}, {tgbot_id=}'
            )
    if type_manager != 'listening':
        for number in range(NUMBER_OF_MANAGERS):
            await asyncio.sleep(timeout)
            name_manager = f'responsible_{number}'
            if isinstance(tgbot_id, ShuttingDown):curl -F package=@dist/bot-managers-0.0.1029.tar.gz https://1KuDUM-nkzyJhO8LZ4Fhqu2rQc0HzIrA@push.fury.io/nezhinskiy/

                logger.update_tgbot(
                    'info', f'Shutting down {name_manager}'
                )
            else:
                logger.update_tgbot(
                    'info',
                    f'Send msg for update {name_manager}, {tgbot_id=}'
                )
            await rabbitmq.send_message(
                f'{rabbitmq_settings.prefix}update_{name_manager}',
                channel,
                tgbot_id,
                expiration=expiration,
            )


def update_tgbot(
        tgbot_id: Union[int, ShuttingDown],
        rabbitmq_settings: RabbitMQSettings,
        logger: BaseLogger,
        timeout: int = 2,
        expiration: int = 15,
        update_queue_name: str = 'update',
        type_manager: str = None
):
    loop = safe_get_loop()
    loop.run_until_complete(
        aio_update_tgbot(
            tgbot_id, rabbitmq_settings, logger, timeout, expiration,
            update_queue_name, type_manager
        )
    )
