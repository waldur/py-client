from enum import Enum


class StepDiscussionStateEnum(str, Enum):
    CLOSED = "closed"
    NOT_OPENED = "not_opened"
    OPEN = "open"

    def __str__(self) -> str:
        return str(self.value)
