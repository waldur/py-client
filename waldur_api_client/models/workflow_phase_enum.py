from enum import Enum


class WorkflowPhaseEnum(str, Enum):
    CLOSING = "closing"
    EVALUATION = "evaluation"
    EXTENSION = "extension"

    def __str__(self) -> str:
        return str(self.value)
