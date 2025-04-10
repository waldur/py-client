from enum import Enum


class MarketplacePublicOfferingsRetrieveFieldItem(str, Enum):
    ACCESS_URL = "access_url"
    ATTRIBUTES = "attributes"
    BACKEND_ID = "backend_id"
    BACKEND_METADATA = "backend_metadata"
    BILLABLE = "billable"
    CATEGORY = "category"
    CATEGORY_TITLE = "category_title"
    CATEGORY_UUID = "category_uuid"
    CITATION_COUNT = "citation_count"
    COMPONENTS = "components"
    COUNTRY = "country"
    CREATED = "created"
    CUSTOMER = "customer"
    CUSTOMER_NAME = "customer_name"
    CUSTOMER_UUID = "customer_uuid"
    DATACITE_DOI = "datacite_doi"
    DESCRIPTION = "description"
    ENDPOINTS = "endpoints"
    FILES = "files"
    FULL_DESCRIPTION = "full_description"
    GETTING_STARTED = "getting_started"
    GOOGLE_CALENDAR_IS_PUBLIC = "google_calendar_is_public"
    GOOGLE_CALENDAR_LINK = "google_calendar_link"
    IMAGE = "image"
    INTEGRATION_GUIDE = "integration_guide"
    LATITUDE = "latitude"
    LONGITUDE = "longitude"
    NAME = "name"
    OPTIONS = "options"
    ORDER_COUNT = "order_count"
    ORGANIZATION_GROUPS = "organization_groups"
    PARENT_DESCRIPTION = "parent_description"
    PARENT_NAME = "parent_name"
    PARENT_UUID = "parent_uuid"
    PAUSED_REASON = "paused_reason"
    PLANS = "plans"
    PLUGIN_OPTIONS = "plugin_options"
    PRIVACY_POLICY_LINK = "privacy_policy_link"
    PROJECT = "project"
    PROJECT_NAME = "project_name"
    PROJECT_UUID = "project_uuid"
    PROMOTION_CAMPAIGNS = "promotion_campaigns"
    QUOTAS = "quotas"
    RESOURCE_OPTIONS = "resource_options"
    ROLES = "roles"
    SCOPE = "scope"
    SCOPE_ERROR_MESSAGE = "scope_error_message"
    SCOPE_NAME = "scope_name"
    SCOPE_STATE = "scope_state"
    SCOPE_UUID = "scope_uuid"
    SCREENSHOTS = "screenshots"
    SHARED = "shared"
    SLUG = "slug"
    STATE = "state"
    TERMS_OF_SERVICE = "terms_of_service"
    TERMS_OF_SERVICE_LINK = "terms_of_service_link"
    THUMBNAIL = "thumbnail"
    TOTAL_COST = "total_cost"
    TOTAL_COST_ESTIMATED = "total_cost_estimated"
    TOTAL_CUSTOMERS = "total_customers"
    TYPE = "type"
    URL = "url"
    UUID = "uuid"
    VENDOR_DETAILS = "vendor_details"

    def __str__(self) -> str:
        return str(self.value)
