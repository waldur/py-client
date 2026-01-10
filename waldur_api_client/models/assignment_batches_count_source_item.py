from enum import Enum


class AssignmentBatchesCountSourceItem(str, Enum):
    ALGORITHM = "algorithm"
    MANUAL = "manual"

    def __str__(self) -> str:
        return str(self.value)
