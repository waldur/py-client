from enum import Enum


class BillingChangesJobStateEnum(str, Enum):
    DONE = "done"
    FAILED = "failed"
    RUNNING = "running"

    def __str__(self) -> str:
        return str(self.value)
