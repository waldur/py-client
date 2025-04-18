from enum import Enum


class MarketplaceCategoryGroupsRetrieveFieldItem(str, Enum):
    DESCRIPTION = "description"
    ICON = "icon"
    TITLE = "title"
    URL = "url"
    UUID = "uuid"

    def __str__(self) -> str:
        return str(self.value)
