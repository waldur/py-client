from enum import Enum


class ProposalProtectedCallsSuggestionsListStateItem(str, Enum):
    ACTIVE = "active"
    ARCHIVED = "archived"
    DRAFT = "draft"

    def __str__(self) -> str:
        return str(self.value)
