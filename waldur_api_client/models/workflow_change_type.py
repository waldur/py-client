from enum import Enum


class WorkflowChangeType(str, Enum):
    ADDED = "added"
    CHANGED = "changed"
    MOVED = "moved"
    REMOVED = "removed"

    def __str__(self) -> str:
        return str(self.value)
