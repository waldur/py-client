from enum import Enum


class OrderFlowDescriptionOrdererEnum(str, Enum):
    ANY = "any"
    PROPOSAL_ALLOCATION = "proposal_allocation"
    PROVIDER_OWNER = "provider_owner"
    ROLE = "role"
    STAFF = "staff"

    def __str__(self) -> str:
        return str(self.value)
