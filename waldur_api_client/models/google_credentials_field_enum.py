from enum import Enum


class GoogleCredentialsFieldEnum(str, Enum):
    ACCOUNT_HOMEDIR_PREFIX = "account_homedir_prefix"
    ACCOUNT_LOGIN_SHELL = "account_login_shell"
    ACCOUNT_SCOPE = "account_scope"
    ACCOUNT_USERNAME_ANONYMIZED_PREFIX = "account_username_anonymized_prefix"
    ACCOUNT_USERNAME_GENERATION_POLICY = "account_username_generation_policy"
    ALLOWED_DOMAINS = "allowed_domains"
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
    ENABLE_NOTIFICATIONS = "enable_notifications"
    GOOGLE_AUTH_URL = "google_auth_url"
    IMAGE = "image"
    OFFERING_COUNT = "offering_count"
    ORGANIZATION_GROUPS = "organization_groups"
    URL = "url"
    UUID = "uuid"

    def __str__(self) -> str:
        return str(self.value)
