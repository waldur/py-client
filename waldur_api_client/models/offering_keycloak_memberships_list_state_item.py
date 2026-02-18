from enum import Enum


class OfferingKeycloakMembershipsListStateItem(str, Enum):
    ACTIVE = "active"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
