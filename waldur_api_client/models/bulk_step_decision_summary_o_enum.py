from enum import Enum


class BulkStepDecisionSummaryOEnum(str, Enum):
    COMPLETED_AT = "completed_at"
    CREATED = "created"
    STATE = "state"
    VALUE_0 = "-completed_at"
    VALUE_1 = "-created"
    VALUE_2 = "-state"

    def __str__(self) -> str:
        return str(self.value)
