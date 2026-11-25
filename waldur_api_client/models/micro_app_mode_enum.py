from enum import Enum


class MicroAppModeEnum(str, Enum):
    ALL = "all"
    AUDIENCE = "audience"
    OFF = "off"

    def __str__(self) -> str:
        return str(self.value)
