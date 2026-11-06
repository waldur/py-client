from enum import Enum


class ReviewerStandingEnum(str, Enum):
    ACTIVE = "active"
    BLOCKED = "blocked"
    SUSPENDED = "suspended"

    def __str__(self) -> str:
        return str(self.value)
