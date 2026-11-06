from enum import Enum


class RoundStatusEnum(str, Enum):
    ENDED = "ended"
    OPEN = "open"
    SCHEDULED = "scheduled"

    def __str__(self) -> str:
        return str(self.value)
