import asyncio
from typing import Union

from aio_rabbitmq import RabbitMQSettings
from tg_logger import BaseLogger

from .utils import (ShuttingDown, TGBotAbstractModel, configure_rabbitmq,
                    safe_get_loop)


async def aio_update_tgbot(
        tgbot: TGBotAbstractModel,
        rabbitmq_settings: RabbitMQSettings,
        logger: BaseLogger,
        timeout: int = 2,
        expiration: int = 15,
) -> None:
    from .settings import NUMBER_OF_MANAGERS
    loop = safe_get_loop()
    rabbitmq = configure_rabbitmq(rabbitmq_settings, logger, loop)
    channel = await rabbitmq.get_one_time_use_channel()
    await rabbitmq.send_message(
        f'{rabbitmq_settings.prefix}update_listening',
        channel,
        tgbot,
        expiration=expiration,
    )
    logger.update_tgbot('info', tgbot, 'listening')
    for number in range(NUMBER_OF_MANAGERS):
        await asyncio.sleep(timeout)
        logger.update_tgbot('info', tgbot, number)
        await rabbitmq.send_message(
            f'{rabbitmq_settings.prefix}update_responsible_{number}',
            channel,
            tgbot,
            expiration=expiration,
        )


def update_tgbot(
        tgbot: Union[TGBotAbstractModel, ShuttingDown],
        rabbitmq_settings: RabbitMQSettings,
        logger: BaseLogger,
        timeout: int = 2,
        expiration: int = 15,
):
    loop = safe_get_loop()
    loop.run_until_complete(
        aio_update_tgbot(
            tgbot, rabbitmq_settings, logger, timeout, expiration
        )
    )
