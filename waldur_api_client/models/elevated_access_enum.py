from enum import Enum


class ElevatedAccessEnum(str, Enum):
    STAFF = "staff"
    SUPPORT = "support"

    def __str__(self) -> str:
        return str(self.value)
