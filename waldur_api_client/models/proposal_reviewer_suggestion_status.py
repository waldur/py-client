from enum import Enum


class ProposalReviewerSuggestionStatus(str, Enum):
    ACCEPTED = "accepted"
    DECLINED = "declined"
    DISCARDED = "discarded"
    EXPIRED = "expired"
    INVITED = "invited"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
