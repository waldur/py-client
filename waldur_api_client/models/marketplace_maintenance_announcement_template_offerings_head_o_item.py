from enum import Enum


class MarketplaceMaintenanceAnnouncementTemplateOfferingsHeadOItem(str, Enum):
    CREATED = "created"
    VALUE_0 = "-created"

    def __str__(self) -> str:
        return str(self.value)
