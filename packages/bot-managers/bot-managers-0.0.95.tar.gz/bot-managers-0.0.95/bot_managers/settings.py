from tg_logger.settings import SyncTgLoggerSettings

from bot_managers.utils import TGBotAbstractModel

LOGGER_SETTINGS: SyncTgLoggerSettings = None
NUMBER_OF_MANAGERS: int = 1
DEFAULT_REQUEST_RETRY_DELAYS: tuple[int, int, int] = (1, 4, 10)
TG_BOT_MODEL: TGBotAbstractModel = None
