from collections.abc import Callable, Coroutine
from functools import wraps
from typing import Any, ParamSpec, TypeAlias, TypeVar

from code_flags.flag import FlagGroup
from code_flags.stores import get_store
from code_flags.utils import package_attrs

flag_state_attr = package_attrs[FlagGroup]('flag_name')

P = ParamSpec('P')
T = TypeVar('T')
S = TypeVar('S')


def mark(obj: T, name: str, flag_default: bool = False) -> T:
    group = flag_state_attr.get(obj) or FlagGroup()
    group.get_or_create(name, flag_default)
    flag_state_attr.put(obj, group)
    return obj


def is_feature_flagged(obj: Any, name: str) -> bool:
    group = flag_state_attr.get(obj)
    return group is not None and name in group


def is_enabled_in_cache(obj: Any, name: str) -> bool:
    group = flag_state_attr.get(obj)
    return (group is not None and name in group) and group.get(
        name
    ).enabled is not None


def is_enabled(obj: Any, name: str) -> bool:
    group = flag_state_attr.get(obj)
    if group is None:
        # TODO: add FlagNotFound error
        raise Exception
    in_cache = is_enabled_in_cache(obj, name)
    flag = group.get(name)
    if in_cache:
        return flag.enabled  # type: ignore
    store = get_store()
    value = store.get(name)
    if value is None:
        value = flag.default
    else:
        group.upsert(name, value)
    return value


def _no_op(*args, **kwargs) -> None:
    return


async def _async_noop(*args: Any, **kwargs: Any) -> None:
    return


def flag(
    name: str,
    *,
    default_enabled: bool = False,
    on_disabled: Callable[..., S] = _no_op,
) -> Callable[[Callable[P, T]], Callable[P, T | S]]:
    def _decorator(func: Callable[P, T]) -> Callable[P, T | S]:
        func = mark(func, name, default_enabled)

        @wraps(func)
        def _inner(*args: P.args, **kwargs: P.kwargs) -> T | S:
            if is_enabled(func, name):
                return func(*args, **kwargs)
            return on_disabled(*args, **kwargs)

        return _inner

    return _decorator


AnyCoroutine: TypeAlias = Coroutine[Any, Any, T]


def async_flag(
    name: str,
    *,
    default_enabled: bool = False,
    on_disabled: Callable[..., AnyCoroutine[S]] = _async_noop,
) -> Callable[
    [Callable[P, AnyCoroutine[T]]], Callable[P, AnyCoroutine[T | S]]
]:
    def _decorator(
        func: Callable[P, AnyCoroutine[T]],
    ) -> Callable[P, AnyCoroutine[T | S]]:
        func = mark(func, name, default_enabled)

        @wraps(func)
        async def _inner(*args: P.args, **kwargs: P.kwargs) -> T | S:
            if is_enabled(func, name):
                return await func(*args, **kwargs)
            return await on_disabled(*args, **kwargs)

        return _inner

    return _decorator
