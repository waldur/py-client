from enum import Enum


class AgentServiceStateEnum(str, Enum):
    ACTIVE = "Active"
    ERROR = "Error"
    IDLE = "Idle"

    def __str__(self) -> str:
        return str(self.value)
