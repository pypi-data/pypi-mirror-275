from .loader import Flag, Loader, Value


class NullLoader(Loader):
    def load(self, flag: Flag) -> Value | None:
        return None

    def load_all(self) -> dict[Flag, Value]:
        return {}

    def refresh(self) -> None:
        pass
