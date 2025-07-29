from enum import Enum


class MarketplaceIntegrationStatusesHeadOItem(str, Enum):
    LAST_REQUEST_TIMESTAMP = "last_request_timestamp"
    VALUE_0 = "-last_request_timestamp"

    def __str__(self) -> str:
        return str(self.value)
