from enum import Enum


class ConfigurationSourceEnum(str, Enum):
    LOCAL = "local"
    WALDUR = "waldur"

    def __str__(self) -> str:
        return str(self.value)
