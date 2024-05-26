from telethon import errors
from telethon.client import (AccountMethods, AuthMethods, BotMethods,
                             ButtonMethods, ChatMethods, DialogMethods,
                             DownloadMethods, MessageParseMethods,
                             TelegramBaseClient, UpdateMethods, UserMethods)
from telethon.extensions import markdown

from ..settings import PARSE_LANG
from .errors import patched_security_error_init
from .markdown import patched_parse
from .methods import PatchedMessageMethods, PatchedUploadMethods
from .network import PathedMTProtoSender

if PARSE_LANG:  # Патчим markdown для доступа к MarkdownV2
    markdown.parse = patched_parse

# Патчим SecurityError для log-сообщений
errors.SecurityError.__init__ = patched_security_error_init


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
