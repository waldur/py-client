from enum import Enum


class ConflictsOfInterestListStatusItem(str, Enum):
    DISMISSED = "dismissed"
    PENDING = "pending"
    RECUSED = "recused"
    WAIVED = "waived"

    def __str__(self) -> str:
        return str(self.value)
