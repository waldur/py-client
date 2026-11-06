from enum import Enum


class RoundReportRowStatusEnum(str, Enum):
    CALL_ARCHIVED = "call_archived"
    CALL_DRAFT = "call_draft"
    ENDED = "ended"
    OPEN = "open"
    SCHEDULED = "scheduled"

    def __str__(self) -> str:
        return str(self.value)
