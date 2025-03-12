from enum import Enum


class GoogleAuthAuthorizeRetrieveFieldItem(str, Enum):
    CALENDAR_REFRESH_TOKEN = "calendar_refresh_token"
    CALENDAR_TOKEN = "calendar_token"
    CREATED = "created"
    CUSTOMER = "customer"
    CUSTOMER_ABBREVIATION = "customer_abbreviation"
    CUSTOMER_COUNTRY = "customer_country"
    CUSTOMER_IMAGE = "customer_image"
    CUSTOMER_NAME = "customer_name"
    CUSTOMER_NATIVE_NAME = "customer_native_name"
    CUSTOMER_SLUG = "customer_slug"
    CUSTOMER_UUID = "customer_uuid"
    DESCRIPTION = "description"
    GOOGLE_AUTH_URL = "google_auth_url"
    IMAGE = "image"
    OFFERING_COUNT = "offering_count"
    ORGANIZATION_GROUPS = "organization_groups"
    URL = "url"
    UUID = "uuid"

    def __str__(self) -> str:
        return str(self.value)
