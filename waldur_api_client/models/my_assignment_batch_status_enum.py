from enum import Enum


class MyAssignmentBatchStatusEnum(str, Enum):
    EXPIRED = "expired"
    RESPONDED = "responded"
    SENT = "sent"

    def __str__(self) -> str:
        return str(self.value)
