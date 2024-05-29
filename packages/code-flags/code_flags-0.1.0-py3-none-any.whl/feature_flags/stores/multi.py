from .store import Store


class MultiStore(Store):
    def __init__(self, *stores: 'Store'):
        self._stores = stores

    def save(self, flag: str, value: bool) -> None:
        for store in self._stores:
            store.save(flag, value)

    def save_bulk(self, flags: dict[str, bool]) -> None:
        for store in self._stores:
            store.save_bulk(flags)

    def get(self, flag: str) -> bool | None:
        for store in self._stores:
            value = store.get(flag)
            if value is not None:
                return value
        return None

    def get_all(self) -> dict[str, bool]:
        all_flags = {}
        for store in reversed(self._stores):
            flags = store.get_all()
            for flag, value in flags.items():
                all_flags[flag] = value
        return all_flags

    def clear(self) -> None:
        for store in self._stores:
            store.clear()
