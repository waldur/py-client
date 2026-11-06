from enum import Enum


class ProposalRunStateEnum(str, Enum):
    APPROVED = "approved"
    EXPIRED = "expired"
    OPEN = "open"
    REJECTED = "rejected"
    WITHDRAWN = "withdrawn"

    def __str__(self) -> str:
        return str(self.value)
