from enum import Enum


class AssignmentBatchesListStatusItem(str, Enum):
    CANCELLED = "cancelled"
    DRAFT = "draft"
    EXPIRED = "expired"
    RESPONDED = "responded"
    SENT = "sent"

    def __str__(self) -> str:
        return str(self.value)
