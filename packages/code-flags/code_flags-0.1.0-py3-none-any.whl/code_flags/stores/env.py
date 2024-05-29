from collections.abc import Callable, Sequence

from config import Config, boolean_cast
from config.interface import ConfigLike

from code_flags.utils import Singleton

from .proxy import _default_store
from .store import Store


def from_kebab(string: str) -> str:
    return '_'.join(string.split('-'))


class EnvironmentStore(Store, Singleton):
    def __init__(
        self,
        config: ConfigLike = Config(),
        fallback_store: Store | None = None,
        key_transform: Sequence[Callable[[str], str]] = (
            str,
            from_kebab,
            lambda v: from_kebab(v).upper(),
        ),
    ):
        self._config = config
        self._fallback_store = fallback_store or _default_store()
        self._key_transform = key_transform

    def save(self, flag: str, value: bool) -> None:
        # Environment store is read-only, so saving is not supported
        self._fallback_store.save(flag, value)

    def save_bulk(self, flags: dict[str, bool]) -> None:
        # Environment store is read-only, so saving is not supported
        self._fallback_store.save_bulk(flags)

    def get(self, flag: str) -> bool | None:
        for transform in self._key_transform:
            value = self._config.get(
                transform(flag), boolean_cast.optional, None
            )
            if value is not None:
                return value
        # If flag not found in environment variables, fallback to the provided store
        return self._fallback_store.get(flag)

    def get_all(self) -> dict[str, bool]:
        # Environment store is read-only, so getting all flags is not supported
        return self._fallback_store.get_all()

    def clear(self) -> None:
        # Environment store is read-only, so clearing is not supported
        self._fallback_store.clear()
