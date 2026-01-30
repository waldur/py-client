from enum import Enum


class ModeEnum(str, Enum):
    EMULATOR = "emulator"
    PRODUCTION = "production"

    def __str__(self) -> str:
        return str(self.value)
