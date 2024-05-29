from typing import TypeAlias

import redis
from gyver.attrs import define

from code_flags.utils import Singleton

from .store import Store

Flag: TypeAlias = str
Value: TypeAlias = bool


@define
class RedisConfig:
    host: str
    port: int = 6379
    db: int = 0


default_config = RedisConfig('localhost')


class RedisStore(Store, Singleton):
    def __init__(self, config: RedisConfig = default_config):
        self._redis = redis.Redis(
            host=config.host, port=config.port, db=config.db
        )
        self._config = config

    def save(self, flag: Flag, value: Value) -> None:
        """Save a flag in the Redis store backend with the value received"""
        self._redis.set(flag, int(value))

    def save_bulk(self, flags: dict[Flag, Value]) -> None:
        """Save all flags passed from the parameter."""
        pipe = self._redis.pipeline()
        for flag, value in flags.items():
            pipe.set(flag, int(value))
        pipe.execute()

    def get(self, flag: Flag) -> Value | None:
        """Get the flag saved or None if the flag is not found."""
        value = self._redis.get(flag)
        return bool(int(value)) if value is not None else None  # type: ignore

    def get_all(self) -> dict[Flag, Value]:
        """Get all flags stored."""
        flags = {}
        for key in self._redis.scan_iter():
            flags[key.decode()] = bool(int(self._redis.get(key)))  # type: ignore
        return flags

    def clear(self) -> None:
        """Clear all flags stored."""
        self._redis.flushdb()
