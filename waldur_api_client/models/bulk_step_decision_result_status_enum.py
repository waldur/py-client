from enum import Enum


class BulkStepDecisionResultStatusEnum(str, Enum):
    DECIDED = "decided"
    REFUSED = "refused"

    def __str__(self) -> str:
        return str(self.value)
