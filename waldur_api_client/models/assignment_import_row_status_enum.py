from enum import Enum


class AssignmentImportRowStatusEnum(str, Enum):
    COI_BLOCKED = "coi_blocked"
    CREATED = "created"
    ERROR = "error"
    READY = "ready"
    SKIPPED = "skipped"

    def __str__(self) -> str:
        return str(self.value)
