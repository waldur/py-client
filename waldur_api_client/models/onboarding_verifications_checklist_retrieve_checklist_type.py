from enum import Enum


class OnboardingVerificationsChecklistRetrieveChecklistType(str, Enum):
    CUSTOMER = "customer"
    INTENT = "intent"

    def __str__(self) -> str:
        return str(self.value)
