from enum import Enum


class ResolutionEnum(str, Enum):
    CANCELLED = "cancelled"
    LAPSED = "lapsed"
    SUBMITTED = "submitted"
    WITHDRAWN = "withdrawn"

    def __str__(self) -> str:
        return str(self.value)
