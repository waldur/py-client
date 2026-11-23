from enum import Enum


class BillingChangesRequestActionEnum(str, Enum):
    SETTLE_MONTH = "settle_month"
    SYNC_BILLING = "sync_billing"
    SYNC_CONSUMPTION = "sync_consumption"

    def __str__(self) -> str:
        return str(self.value)
