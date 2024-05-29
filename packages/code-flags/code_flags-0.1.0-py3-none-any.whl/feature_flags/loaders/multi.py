from .loader import Flag, Loader, Value


class MultiLoader(Loader):
    def __init__(self, *loaders: Loader):
        self._loaders = loaders

    def load(self, flag: Flag) -> Value | None:
        for loader in self._loaders:
            value = loader.load(flag)
            if value is not None:
                return value
        return None

    def load_all(self) -> dict[Flag, Value]:
        all_flags = {}
        for loader in reversed(self._loaders):
            all_flags.update(
                (key, value)
                for key, value in loader.load_all().items()
                if value is not None
            )
        return all_flags

    def refresh(self) -> None:
        for loader in self._loaders:
            loader.refresh()
