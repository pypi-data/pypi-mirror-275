from code_flags.utils import Singleton

from .store import Flag, Store, Value


class InMemoryStore(Store, Singleton):
    def __init__(self) -> None:
        self._store = {}

    def save(self, flag: Flag, value: Value) -> None:
        self._store[flag] = value

    def save_bulk(self, flags: dict[Flag, Value]) -> None:
        self._store.update(flags)

    def get(self, flag: Flag) -> Value | None:
        return self._store.get(flag)

    def get_all(self) -> dict[Flag, Value]:
        return dict(self._store)

    def clear(self) -> None:
        self._store.clear()
