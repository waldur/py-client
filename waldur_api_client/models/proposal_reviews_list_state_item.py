from enum import Enum


class ProposalReviewsListStateItem(str, Enum):
    IN_REVIEW = "in_review"
    REJECTED = "rejected"
    SUBMITTED = "submitted"

    def __str__(self) -> str:
        return str(self.value)
