from collections.abc import Callable
from typing import Any, Generic, ParamSpec, TypeVar, cast

from gyver.attrs import define
from lazyfields import lazyfield
from typing_extensions import Self

P = ParamSpec('P')
T = TypeVar('T')


@define
class package_attrs(Generic[T]):
    """Class for managing attributes with a specific naming convention.

    Attributes:
        _name (str): The base name for the attributes.
    """

    _name: str

    @lazyfield
    def name(self):
        """Generate the full attribute name based on the base name.

        Returns:
            str: The full attribute name.
        """
        return f"__fflags_{self._name.strip('_')}__"

    def get(self, obj: Any) -> T | None:
        """Get the value of the attribute from the given object.

        Args:
            obj (Any): The object from which to get the attribute.

        Returns:
            T | None: The value of the attribute or None if not present.
        """
        return getattr(obj, self.name, None)

    def put(self, obj: Any, value: T) -> None:
        """Set the value of the attribute on the given object.

        Args:
            obj (Any): The object on which to set the attribute.
            value (T): The value to set.

        Raises:
            ValueError: If the object does not accept new attributes.
        """
        try:
            setattr(obj, self.name, value)
        except AttributeError as err:
            raise ValueError(
                f'Cannot mark object {obj} because object'
                'does not accept new attributes'
            ) from err

    def active(self, obj: Any) -> bool:
        """Check if the attribute is present on the given object.

        Args:
            obj (Any): The object to check.

        Returns:
            bool: True if the attribute is present, False otherwise.
        """
        return hasattr(obj, self.name)


class Singleton:
    """A base class for implementing singleton pattern."""

    _instance = None

    def __singleton_init(self, *args, **kwargs) -> None:
        """No-op method to avoid calling __init__
        twice due to CPython's behavior."""

    def __new__(cls, *args, **kwargs) -> Self:
        """Create or return the single instance of the class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Self: The single instance of the class.
        """
        if cls._instance is None:
            self = object.__new__(cls)
            cls._instance = self
            self.__init__(*args, **kwargs)
            old_init = cls.__init__
            cls.__init__ = Singleton.__singleton_init
            cls.__old_init__ = old_init
        return cls._instance

    @classmethod
    def _revert_init(cls):
        """Revert the __init__ method to the original initializer."""
        if hasattr(cls, '__old_init__'):
            cls.__init__ = cls.__old_init__

    @classmethod
    def singleton_clear(cls):
        """Clear the singleton instance and revert the __init__ method."""
        cls._instance = None
        cls._revert_init()

    @classmethod
    def singleton_ensure_new(
        cls: Callable[P, T], *args: P.args, **kwargs: P.kwargs
    ) -> T:
        klass = cast(type[T], cls)
        self = object.__new__(klass)
        init = getattr(klass, '__old_init__', klass.__init__)
        init(self, *args, **kwargs)
        return self


class Defer(Generic[P, T]):
    """Class for deferring the instantiation of a class.

    Attributes:
        cls (Callable[P, T]): The class to instantiate.
        args (tuple): Positional arguments to pass to the class constructor.
        kwargs (dict): Keyword arguments to pass to the class constructor.
        _instance (T | None): The deferred instance of the class.
    """

    def __init__(self, cls: Callable[P, T], *args: P.args, **kwargs: P.kwargs):
        self.cls = cls
        self.args = args
        self.kwargs = kwargs
        self._instance: T | None = None

    def __call__(self) -> T:
        """Instantiate the class if not already done and return the instance.

        Returns:
            T: The instance of the class.
        """
        if self._instance is None:
            self._instance = self.cls(*self.args, **self.kwargs)
        return self._instance  # type: ignore

    def get_instance(self) -> T | None:
        """Get the deferred instance if it has been created.

        Returns:
            T | None: The deferred instance or None if not created.
        """
        return self._instance


def defer(
    cls: Callable[P, T], *args: P.args, **kwargs: P.kwargs
) -> Defer[P, T]:
    """Create a callable that defers the instantiation of a class with given arguments.

    Args:
        cls (Callable[P, T]): The class to instantiate.
        *args (P.args): Positional arguments to pass to the class constructor.
        **kwargs (P.kwargs): Keyword arguments to pass to the class constructor.

    Returns:
        Callable[[], T]: A callable that returns an instance of the class when called.
    """

    return Defer(cls, *args, **kwargs)
