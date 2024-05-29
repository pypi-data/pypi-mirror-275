from typing import Protocol, TypeAlias

Flag: TypeAlias = str
Value: TypeAlias = bool


class Loader(Protocol):
    def load(self, flag: Flag) -> Value | None:
        """Load the value of the specified flag from the loader backend.

        Args:
            flag: The name of the flag to load.

        Returns:
            The value of the flag if found, otherwise None.
        """

    def load_all(self) -> dict[Flag, Value]:
        """Load all flags and their values from the loader backend.

        Returns:
            A dictionary of all flags and their corresponding values.
        """
        ...

    def refresh(self) -> None:
        """Refresh the loader to update any cached values,
        ensuring it has the latest data from the backend."""
