from enum import Enum


class InfrastructureModeEnum(str, Enum):
    CUSTOMER_CHOICE = "customer_choice"
    PROVIDER_FIXED = "provider_fixed"

    def __str__(self) -> str:
        return str(self.value)
