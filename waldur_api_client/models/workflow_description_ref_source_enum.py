from enum import Enum


class WorkflowDescriptionRefSourceEnum(str, Enum):
    CALL = "call"
    ENGINE = "engine"
    RULE = "rule"
    STEP = "step"

    def __str__(self) -> str:
        return str(self.value)
