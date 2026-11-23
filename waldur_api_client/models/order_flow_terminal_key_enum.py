from enum import Enum


class OrderFlowTerminalKeyEnum(str, Enum):
    CANCELED = "canceled"
    ERRED = "erred"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
