from tg_logger import BaseLogger
from tg_logger.settings import SyncTgLoggerSettings, configure_logger

LOGGER_SETTINGS: SyncTgLoggerSettings = None
NUMBER_OF_MANAGERS: int = 1
DEFAULT_REQUEST_RETRY_DELAYS: tuple[int, int, int] = (1, 4, 10)
logger: BaseLogger = None


def get_logger():
    global logger
    if logger is None:
        configure_logger(LOGGER_SETTINGS.bot_token, LOGGER_SETTINGS.recipient_id)
        logger = BaseLogger()
    return logger
