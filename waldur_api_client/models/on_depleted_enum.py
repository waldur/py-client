from enum import Enum


class OnDepletedEnum(str, Enum):
    DECLINE = "decline"
    LEAVE = "leave"

    def __str__(self) -> str:
        return str(self.value)
