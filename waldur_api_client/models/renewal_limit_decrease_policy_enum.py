from enum import Enum


class RenewalLimitDecreasePolicyEnum(str, Enum):
    NO_CREDIT = "no_credit"
    STRETCH_PAID_TERM = "stretch_paid_term"

    def __str__(self) -> str:
        return str(self.value)
