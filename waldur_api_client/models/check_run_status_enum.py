from enum import Enum


class CheckRunStatusEnum(str, Enum):
    IDLE = "idle"
    RUNNING = "running"

    def __str__(self) -> str:
        return str(self.value)
