from enum import Enum


class OrderFlowActorEnum(str, Enum):
    BACKEND = "backend"
    CONSUMER = "consumer"
    PROVIDER = "provider"
    SCHEDULER = "scheduler"

    def __str__(self) -> str:
        return str(self.value)
