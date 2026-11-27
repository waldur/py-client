from enum import Enum


class BulkStepDecisionStateEnum(str, Enum):
    DONE = "done"
    FAILED = "failed"
    PENDING = "pending"
    RUNNING = "running"

    def __str__(self) -> str:
        return str(self.value)
