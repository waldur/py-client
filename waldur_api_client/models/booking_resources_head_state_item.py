from enum import Enum


class BookingResourcesHeadStateItem(str, Enum):
    CREATING = "Creating"
    ERRED = "Erred"
    OK = "OK"
    TERMINATED = "Terminated"
    TERMINATING = "Terminating"
    UPDATING = "Updating"

    def __str__(self) -> str:
        return str(self.value)
