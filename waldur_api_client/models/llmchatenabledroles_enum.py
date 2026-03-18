from enum import Enum


class LLMCHATENABLEDROLESEnum(str, Enum):
    ALL = "all"
    DISABLED = "disabled"
    STAFF = "staff"
    STAFF_AND_SUPPORT = "staff_and_support"

    def __str__(self) -> str:
        return str(self.value)
