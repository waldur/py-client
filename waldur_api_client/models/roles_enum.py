from enum import Enum


class RolesEnum(str, Enum):
    MEMBERSHIP_SYNC = "membership_sync"
    ORDER_PROCESSING = "order_processing"
    REPORTING = "reporting"
    USERNAME_MANAGEMENT = "username_management"

    def __str__(self) -> str:
        return str(self.value)
