from enum import Enum


class MarketplacePublicOfferingsHeadStateItem(str, Enum):
    ACTIVE = "Active"
    ARCHIVED = "Archived"
    DRAFT = "Draft"
    PAUSED = "Paused"

    def __str__(self) -> str:
        return str(self.value)
