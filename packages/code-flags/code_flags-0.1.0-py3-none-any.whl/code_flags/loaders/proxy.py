from code_flags.utils import Singleton

from .loader import Flag, Loader, Value


class ProxyLoader(Loader, Singleton):
    def __new__(cls, loader: Loader) -> 'ProxyLoader':
        if isinstance(loader, cls):
            return loader
        return super().__new__(cls, loader)

    def __init__(self, loader: Loader):
        self._loader = loader

    def load(self, flag: Flag) -> Value | None:
        return self._loader.load(flag)

    def load_all(self) -> dict[Flag, Value]:
        return self._loader.load_all()

    def refresh(self) -> None:
        self._loader.refresh()
