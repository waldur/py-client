from enum import Enum


class UsersRetrieveFieldItem(str, Enum):
    AFFILIATIONS = "affiliations"
    AGREEMENT_DATE = "agreement_date"
    AGREE_WITH_POLICY = "agree_with_policy"
    CIVIL_NUMBER = "civil_number"
    DATE_JOINED = "date_joined"
    DESCRIPTION = "description"
    EMAIL = "email"
    FIRST_NAME = "first_name"
    FULL_NAME = "full_name"
    HAS_ACTIVE_SESSION = "has_active_session"
    IDENTITY_PROVIDER_FIELDS = "identity_provider_fields"
    IDENTITY_PROVIDER_LABEL = "identity_provider_label"
    IDENTITY_PROVIDER_MANAGEMENT_URL = "identity_provider_management_url"
    IDENTITY_PROVIDER_NAME = "identity_provider_name"
    IDENTITY_SOURCE = "identity_source"
    IMAGE = "image"
    IS_ACTIVE = "is_active"
    IS_STAFF = "is_staff"
    IS_SUPPORT = "is_support"
    JOB_TITLE = "job_title"
    LAST_NAME = "last_name"
    NATIVE_NAME = "native_name"
    ORGANIZATION = "organization"
    PERMISSIONS = "permissions"
    PHONE_NUMBER = "phone_number"
    PREFERRED_LANGUAGE = "preferred_language"
    REGISTRATION_METHOD = "registration_method"
    REQUESTED_EMAIL = "requested_email"
    SLUG = "slug"
    TOKEN = "token"
    TOKEN_LIFETIME = "token_lifetime"
    URL = "url"
    USERNAME = "username"
    UUID = "uuid"

    def __str__(self) -> str:
        return str(self.value)
