from enum import Enum


class RejectionCauseEnum(str, Enum):
    DECLINED = "declined"
    EXPIRED = "expired"
    PROPOSAL_DECIDED = "proposal_decided"
    WITHDRAWN = "withdrawn"

    def __str__(self) -> str:
        return str(self.value)
