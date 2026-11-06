from enum import Enum


class PlannedOutcomeEnum(str, Enum):
    APPROVED = "approved"
    DECLINED = "declined"
    LEFT = "left"
    SKIPPED = "skipped"

    def __str__(self) -> str:
        return str(self.value)
