from code_flags.utils import Singleton, defer

from .sqlite import SQLiteStore
from .store import Flag, Store, Value


class ProxyStore(Store, Singleton):
    def __new__(cls, store: Store) -> 'ProxyStore':
        if isinstance(store, cls):
            return store
        return super().__new__(cls, store)

    def __init__(self, store: Store) -> None:
        self._store = store

    def change(self, store: Store) -> None:
        self._store = store

    def save(self, flag: Flag, value: Value) -> None:
        self._store.save(flag, value)

    def save_bulk(self, flags: dict[Flag, Value]) -> None:
        self._store.save_bulk(flags)

    def get(self, flag: Flag) -> Value | None:
        return self._store.get(flag)

    def get_all(self) -> dict[Flag, Value]:
        return self._store.get_all()

    def clear(self) -> None:
        self._store.clear()


_default_store = defer(SQLiteStore, ':memory:')


def get_store() -> Store:
    return ProxyStore(_default_store())
