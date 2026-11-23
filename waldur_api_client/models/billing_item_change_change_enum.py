from enum import Enum


class BillingItemChangeChangeEnum(str, Enum):
    CREATED = "created"
    DELETED = "deleted"
    UPDATED = "updated"

    def __str__(self) -> str:
        return str(self.value)
