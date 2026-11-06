from enum import Enum


class StateGroupEnum(str, Enum):
    ACCEPTED = "accepted"
    CLOSED = "closed"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
