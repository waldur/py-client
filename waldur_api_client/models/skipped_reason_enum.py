from enum import Enum


class SkippedReasonEnum(str, Enum):
    CONDITION_NOT_MET = "condition_not_met"

    def __str__(self) -> str:
        return str(self.value)
