from enum import Enum


class WorkflowChangeKind(str, Enum):
    BEHAVIOUR = "behaviour"
    COSMETIC = "cosmetic"

    def __str__(self) -> str:
        return str(self.value)
