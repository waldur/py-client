from enum import Enum


class RenewalTermEnum(str, Enum):
    CURRENT_TERM = "current_term"
    EXTENSION = "extension"

    def __str__(self) -> str:
        return str(self.value)
