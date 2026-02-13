from enum import Enum


class ChatRequestModeEnum(str, Enum):
    RELOAD = "reload"

    def __str__(self) -> str:
        return str(self.value)
