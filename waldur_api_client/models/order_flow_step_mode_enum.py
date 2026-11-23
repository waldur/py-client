from enum import Enum


class OrderFlowStepModeEnum(str, Enum):
    CALLBACK = "callback"
    SYNC = "sync"

    def __str__(self) -> str:
        return str(self.value)
