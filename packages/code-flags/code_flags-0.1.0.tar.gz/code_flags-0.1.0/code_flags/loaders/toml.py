from pathlib import Path

from lazyfields import dellazy, lazyfield
from tomlkit import parse

from .loader import Flag, Loader, Value


class TomlLoader(Loader):
    def __init__(
        self,
        filename: str | Path = 'pyproject.toml',
        table: str = 'tool.feature-flags',
    ):
        self.filename = Path(filename)
        self.table = table

    @lazyfield
    def flags(self) -> dict[Flag, Value]:
        return self._load_flags()

    def _load_flags(self) -> dict[Flag, Value]:
        try:
            with open(self.filename) as file:
                config = parse(file.read())
                keys = self.table.split('.')
                table = config
                for key in keys:
                    table = table.get(key, {})
                return table
        except FileNotFoundError:
            return {}

    def load(self, flag: Flag) -> Value | None:
        return self.flags.get(flag)

    def load_all(self) -> dict[Flag, Value]:
        return self.flags

    def refresh(self) -> None:
        dellazy(self, 'flags')
