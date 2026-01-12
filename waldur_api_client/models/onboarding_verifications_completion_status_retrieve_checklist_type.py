from enum import Enum


class OnboardingVerificationsCompletionStatusRetrieveChecklistType(str, Enum):
    CUSTOMER = "customer"
    INTENT = "intent"

    def __str__(self) -> str:
        return str(self.value)
