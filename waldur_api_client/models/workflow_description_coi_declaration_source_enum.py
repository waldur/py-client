from enum import Enum


class WorkflowDescriptionCoiDeclarationSourceEnum(str, Enum):
    CALL = "call"
    PLATFORM = "platform"
    STEP = "step"

    def __str__(self) -> str:
        return str(self.value)
