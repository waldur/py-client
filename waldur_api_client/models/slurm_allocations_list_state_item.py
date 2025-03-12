from enum import Enum


class SlurmAllocationsListStateItem(str, Enum):
    CREATING = "CREATING"
    CREATION_SCHEDULED = "CREATION_SCHEDULED"
    DELETING = "DELETING"
    DELETION_SCHEDULED = "DELETION_SCHEDULED"
    ERRED = "ERRED"
    OK = "OK"
    UPDATE_SCHEDULED = "UPDATE_SCHEDULED"
    UPDATING = "UPDATING"

    def __str__(self) -> str:
        return str(self.value)
