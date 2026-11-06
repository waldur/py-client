from enum import Enum


class WorkflowDescriptionFlagKindEnum(str, Enum):
    DUPLICATE = "duplicate"
    LEAK_RISK = "leak_risk"
    MISSING = "missing"
    UNREACHABLE = "unreachable"

    def __str__(self) -> str:
        return str(self.value)
