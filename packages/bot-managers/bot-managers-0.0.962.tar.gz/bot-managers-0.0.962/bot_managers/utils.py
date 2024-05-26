import abc


class TGBotAbstractModel(abc.ABC):
    """
    Abstract class model of TGBot.
    """
    tgbot_id: int
    tg_username: str
    api_id: str
    api_hash: str
    api_key: str


class ShuttingDown:
    """Class for Shutting Down Managers"""
    pass


class AsyncList(list):
    def __aiter__(self):
        return self._AsyncListIterator(self)

    class _AsyncListIterator:
        def __init__(self, async_list):
            self.list = async_list
            self.index = 0

        async def __aiter__(self):
            return self

        async def __anext__(self):
            if self.index < len(self.list):
                value = self.list[self.index]
                self.index += 1
                return value
            else:
                raise StopAsyncIteration


class AsyncDict(dict):
    def __aiter__(self):
        return self._AsyncDictIterator(self.items())

    class _AsyncDictIterator:
        def __init__(self, items):
            self.iterator = iter(items)

        async def __aiter__(self):
            return self

        async def __anext__(self):
            try:
                return next(self.iterator)
            except StopIteration:
                raise StopAsyncIteration
