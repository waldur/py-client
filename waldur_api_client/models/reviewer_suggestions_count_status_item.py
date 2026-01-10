from enum import Enum


class ReviewerSuggestionsCountStatusItem(str, Enum):
    CONFIRMED = "confirmed"
    INVITED = "invited"
    PENDING = "pending"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
