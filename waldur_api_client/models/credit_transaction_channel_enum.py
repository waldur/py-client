from enum import Enum


class CreditTransactionChannelEnum(str, Enum):
    API = "api"
    GATEWAY = "gateway"
    MANUAL = "manual"

    def __str__(self) -> str:
        return str(self.value)
