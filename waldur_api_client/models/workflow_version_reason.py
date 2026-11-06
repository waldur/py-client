from enum import Enum


class WorkflowVersionReason(str, Enum):
    ACTIVATED = "activated"
    CREATED = "created"
    CREATED_FROM_TEMPLATE = "created_from_template"
    DUPLICATED = "duplicated"
    EDITED = "edited"
    IMPORTED = "imported"

    def __str__(self) -> str:
        return str(self.value)
