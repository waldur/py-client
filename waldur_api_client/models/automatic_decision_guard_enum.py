from enum import Enum


class AutomaticDecisionGuardEnum(str, Enum):
    EARLIER_STEP = "earlier_step"
    PROVIDER_FULFILMENT = "provider_fulfilment"

    def __str__(self) -> str:
        return str(self.value)
