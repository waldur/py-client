from enum import Enum


class ProposalPublicCallsListStateItem(str, Enum):
    ACTIVE = "active"
    ARCHIVED = "archived"
    DRAFT = "draft"

    def __str__(self) -> str:
        return str(self.value)
