from code_flags.stores.store import Store

from .loader import Flag, Loader, Value


class StoreLoader(Loader):
    def __init__(self, store: Store):
        self.store = store

    def load(self, flag: Flag) -> Value | None:
        return self.store.get(flag)

    def load_all(self) -> dict[Flag, Value]:
        return self.store.get_all()

    def refresh(self) -> None:
        pass
