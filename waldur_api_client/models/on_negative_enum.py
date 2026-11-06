from enum import Enum


class OnNegativeEnum(str, Enum):
    CANCEL = "cancel"
    CONTINUE = "continue"
    REJECT = "reject"

    def __str__(self) -> str:
        return str(self.value)
