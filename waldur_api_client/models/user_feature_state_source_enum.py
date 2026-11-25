from enum import Enum


class UserFeatureStateSourceEnum(str, Enum):
    GLOBAL = "global"
    OFF = "off"
    RULE = "rule"

    def __str__(self) -> str:
        return str(self.value)
