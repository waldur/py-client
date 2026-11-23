from enum import Enum


class OrderFlowStepStatusEnum(str, Enum):
    CONDITIONAL = "conditional"
    RUNS = "runs"
    SKIPPED = "skipped"

    def __str__(self) -> str:
        return str(self.value)
