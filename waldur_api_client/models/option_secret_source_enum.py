from enum import Enum


class OptionSecretSourceEnum(str, Enum):
    CUSTOMER = "customer"
    PROVIDER = "provider"

    def __str__(self) -> str:
        return str(self.value)
