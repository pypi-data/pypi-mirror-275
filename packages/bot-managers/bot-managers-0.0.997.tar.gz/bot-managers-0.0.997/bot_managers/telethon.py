import asyncio

from telethon import errors
from telethon.client import (AccountMethods, AuthMethods, BotMethods,
                             ButtonMethods, ChatMethods, DialogMethods,
                             DownloadMethods, MessageMethods,
                             MessageParseMethods, TelegramBaseClient,
                             UpdateMethods, UploadMethods, UserMethods)
from telethon import hints
from telethon.network import MTProtoSender
from tg_logger import BaseLogger

from .utils import tg_request_with_retry


class CustomSecurityError(errors.SecurityError):
    """
    Generic security error, mostly used when generating a new AuthKey.
    """
    pass


original_security_error_init = errors.SecurityError.__init__


def patched_security_error_init(self, *args):
    original_security_error_init(self, *args)
    exc_text = args[0] if args else ""
    if isinstance(exc_text, str) and exc_text.startswith(
            'Server replied with a wrong session ID'):
        logger = BaseLogger()
        logger.decrypt_message_data('error', exc_text)


errors.SecurityError.__init__ = patched_security_error_init


class PathedMTProtoSender(MTProtoSender):
    async def _try_connect(self, attempt):
        try:
            self._log.debug('Connection attempt %d...', attempt)
            await self._connection.connect(timeout=self._connect_timeout)
            self._log.debug('Connection success!')
            return True
        except asyncio.TimeoutError as exc:
            self._log.warning('Attempt %d at connecting failed: %s: %s',
                              attempt, type(exc).__name__, exc)
            await asyncio.sleep(self._delay)
            return False
        except IOError as exc:
            self._log.warning('Attempt %d at connecting failed: %s: %s',
                              attempt, type(exc).__name__, exc)
            raise exc


class TelethonErrorHandler:
    @staticmethod
    def _get_tg_id(entity: 'hints.EntityLike', logger: BaseLogger) -> int:
        if isinstance(entity, int):
            return entity
        if hasattr(entity, 'user_id'):
            return int(entity.user_id)
        if hasattr(entity, 'id'):
            return int(entity.id)
        logger.get_tg_id('error', f'Could not get tg_id from {entity=}')
        return False

    @staticmethod
    async def set_sender_status(tg_id: int, client, status: str) -> None:
        pass

    @staticmethod
    async def get_sender_status(tg_id: int, client) -> None:
        pass

    @staticmethod
    def send_message_handler(func):
        async def wrapper(
                client: 'PatchedTelegramClient',
                entity: 'hints.EntityLike',
                *args,
                **kwargs
        ):
            logger = client.custom_logger
            try:
                return await func(client, entity, *args, **kwargs)
            except errors.InputUserDeactivatedError as exc:  # The specified user was deleted.
                tg_id = TelethonErrorHandler._get_tg_id(entity, logger)
                if tg_id:
                    await TelethonErrorHandler.set_sender_status(
                        tg_id, client, status='Deleted'
                    )
                logger.send_message(
                    'info', f'Sender {tg_id=} was deleted.{exc}'
                )
            except errors.UserBannedInChannelError as exc:  # you're banned from sending messages in supergroups/channels.
                msg = (f'You are banned from sending messages in '
                       f'supergroups/channels. {exc}')
                logger.send_message('error', msg)
            except errors.UserIsBlockedError as exc:  # User is blocked.
                tg_id = TelethonErrorHandler._get_tg_id(entity, logger)
                if tg_id:
                    await TelethonErrorHandler.set_sender_status(
                        tg_id, client, status='Banned'
                    )
                logger.send_message(
                    'info', f'Sender {tg_id=} blocked tgbot. {exc}'
                )
            except errors.RPCError as exc:
                logger.send_message('error', f'Error occured: {exc}')
            except ValueError as exc:  # Could not find the input entity for PeerUser
                logger.send_message('error', f'Error occured: {exc}')
                tg_id = TelethonErrorHandler._get_tg_id(entity, logger)
                if not tg_id:
                    return
                user = await client.get_entity(tg_id)
                try:
                    return await func(client, user, *args, **kwargs)
                except Exception as exc:
                    logger.send_message('error', f'Error occured: {exc}')
        return wrapper


class PatchedMessageMethods(MessageMethods):
    def __getattribute__(self, name):
        attr = super().__getattribute__(name)
        if callable(attr) and not name.startswith(
                '_') and asyncio.iscoroutinefunction(attr):
            async def wrapper(*args, **kwargs):
                return await tg_request_with_retry(attr, *args, **kwargs)
            return wrapper
        return attr

    @TelethonErrorHandler.send_message_handler
    async def send_message(self, *args, **kwargs):
        return await super().send_message(*args, **kwargs)

    @TelethonErrorHandler.send_message_handler
    async def safe_send_message(self, *args, **kwargs):
        sender_id = args[1]
        client = args[0]
        if isinstance(sender_id, int):
            sender_status = await TelethonErrorHandler.get_sender_status(
                sender_id, client)
            if sender_status in ['Deleted', 'Banned']:
                return
        return await super().send_message(*args, **kwargs)


class PatchedUploadMethods(UploadMethods):
    def __getattribute__(self, name):
        attr = super().__getattribute__(name)
        if callable(attr) and not name.startswith(
                '_') and asyncio.iscoroutinefunction(attr):
            async def wrapper(*args, **kwargs):
                return await tg_request_with_retry(attr, *args, **kwargs)
            return wrapper
        return attr

    @TelethonErrorHandler.send_message_handler
    async def send_file(self, *args, **kwargs):
        return await super().send_file(*args, **kwargs)

    @TelethonErrorHandler.send_message_handler
    async def safe_send_file(self, *args, **kwargs):
        sender_id = args[1]
        client = args[0]
        if isinstance(sender_id, int):
            sender_status = await TelethonErrorHandler.get_sender_status(
                sender_id, client)
            if sender_status in ['Deleted', 'Banned']:
                return
        return await super().send_file(*args, **kwargs)


class PatchedTelegramClient(
    AccountMethods, AuthMethods, DownloadMethods, DialogMethods, ChatMethods,
    BotMethods, PatchedMessageMethods, PatchedUploadMethods, ButtonMethods,
    UpdateMethods, MessageParseMethods, UserMethods, TelegramBaseClient
):
    def __init__(self, *args, **kwargs):
        self.custom_logger = kwargs.pop('custom_logger')
        super().__init__(*args, **kwargs)
        self._sender = PathedMTProtoSender(
            self.session.auth_key,
            loggers=self._log,
            retries=self._connection_retries,
            delay=self._retry_delay,
            auto_reconnect=self._auto_reconnect,
            connect_timeout=self._timeout,
            auth_key_callback=self._auth_key_callback,
            updates_queue=self._updates_queue,
            auto_reconnect_callback=self._handle_auto_reconnect
        )
