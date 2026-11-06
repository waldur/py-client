from enum import Enum


class WorkflowDescriptionFlagSeverityEnum(str, Enum):
    INFO = "info"
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)
