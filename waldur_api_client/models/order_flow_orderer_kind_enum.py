from enum import Enum


class OrderFlowOrdererKindEnum(str, Enum):
    ANY = "any"
    PROPOSAL_ALLOCATION = "proposal_allocation"
    PROVIDER_OWNER = "provider_owner"
    ROLE = "role"
    STAFF = "staff"
    SYSTEM = "system"

    def __str__(self) -> str:
        return str(self.value)
