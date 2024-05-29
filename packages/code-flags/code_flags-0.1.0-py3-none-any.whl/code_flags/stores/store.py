from typing import Protocol, TypeAlias

Flag: TypeAlias = str
Value: TypeAlias = bool


class Store(Protocol):
    def save(self, flag: Flag, value: Value) -> None:
        """Save a flag in the store backend with the value received"""

    def save_bulk(self, flags: dict[Flag, Value]) -> None:
        """Save all flags passed from the parameter."""

    def get(self, flag: Flag) -> Value | None:
        """Get the flag saved or None if the flag is not found."""

    def get_all(self) -> dict[Flag, Value]:
        """Get all flags stored."""
        ...

    def clear(self) -> None:
        """Clear all flags stored."""
