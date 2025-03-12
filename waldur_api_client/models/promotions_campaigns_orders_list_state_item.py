from enum import Enum


class PromotionsCampaignsOrdersListStateItem(str, Enum):
    ACTIVE = "Active"
    DRAFT = "Draft"
    TERMINATED = "Terminated"

    def __str__(self) -> str:
        return str(self.value)
