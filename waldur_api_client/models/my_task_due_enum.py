from enum import Enum


class MyTaskDueEnum(str, Enum):
    DUE_SOON = "due_soon"
    OVERDUE = "overdue"

    def __str__(self) -> str:
        return str(self.value)
