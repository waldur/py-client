from enum import Enum


class ConflictsOfInterestCountStatusItem(str, Enum):
    DISMISSED = "dismissed"
    PENDING = "pending"
    RECUSED = "recused"
    WAIVED = "waived"

    def __str__(self) -> str:
        return str(self.value)
