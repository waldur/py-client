from enum import Enum


class AssignmentBatchesListSourceItem(str, Enum):
    ALGORITHM = "algorithm"
    MANUAL = "manual"

    def __str__(self) -> str:
        return str(self.value)
