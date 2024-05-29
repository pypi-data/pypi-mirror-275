from typing import Any

from gyver.attrs import define, info


@define
class Flag:
    name: str
    enabled: bool | None
    default: bool


class NOT_SENT:
    pass


@define
class FlagGroup:
    flags: set[Flag] = info(default_factory=set)

    def __contains__(self, flag: Flag | str | Any):
        if isinstance(flag, Flag):
            return flag in self.flags
        if isinstance(flag, str):
            return any(item.name == flag for item in self.flags)
        return NotImplemented

    def get_or_create(self, name: str, default: bool) -> Flag:
        if name in self:
            return self.get(name)
        flag = Flag(name, None, default)
        self.flags.add(flag)
        return flag

    def get(self, name: str) -> Flag:
        flag = next((flag for flag in self.flags if flag.name == name), None)
        if flag is None:
            # TODO: Create FlagNotFound exception
            raise Exception
        return flag

    def upsert(
        self,
        name: str,
        enabled: bool | None | type[NOT_SENT] = NOT_SENT,
        default: bool | type[NOT_SENT] = NOT_SENT,
    ) -> Flag:
        flag = self.get_or_create(
            name,
            False if default is NOT_SENT else default,  # type: ignore
        )
        new_flag = Flag(
            flag.name,  # type: ignore
            flag.enabled if enabled is NOT_SENT else enabled,  # type: ignore
            flag.default if default is NOT_SENT else default,  # type: ignore
        )
        self.flags.remove(flag)
        self.flags.add(new_flag)
        return new_flag
