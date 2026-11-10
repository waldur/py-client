from enum import Enum


class RegistrationSourceEnum(str, Enum):
    CIMD = "cimd"
    DCR = "dcr"
    MANUAL = "manual"

    def __str__(self) -> str:
        return str(self.value)
