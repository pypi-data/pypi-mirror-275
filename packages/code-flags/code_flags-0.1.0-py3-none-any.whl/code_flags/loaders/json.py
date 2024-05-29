import json
from pathlib import Path

from lazyfields import dellazy, lazyfield

from .loader import Flag, Loader, Value


class JsonLoader(Loader):
    def __init__(
        self, filename: str | Path = 'flags.json', key: str | None = None
    ):
        self.filename = filename
        self.key = key

    @lazyfield
    def flags(self) -> dict[Flag, Value]:
        return self._load_flags()

    def _load_flags(self) -> dict[Flag, Value]:
        try:
            with open(self.filename) as file:
                data = json.load(file)
                if self.key:
                    return data.get(self.key, {})
                else:
                    return data
        except FileNotFoundError:
            return {}

    def load(self, flag: Flag) -> Value | None:
        return self.flags.get(flag)

    def load_all(self) -> dict[Flag, Value]:
        return self.flags

    def refresh(self) -> None:
        dellazy(self, 'flags')
