from enum import Enum


class BookingResourcesRetrieveFieldItem(str, Enum):
    ATTRIBUTES = "attributes"
    AVAILABLE_ACTIONS = "available_actions"
    BACKEND_ID = "backend_id"
    BACKEND_METADATA = "backend_metadata"
    CAN_TERMINATE = "can_terminate"
    CATEGORY_ICON = "category_icon"
    CATEGORY_TITLE = "category_title"
    CATEGORY_UUID = "category_uuid"
    CONSUMER_REVIEWED_BY = "consumer_reviewed_by"
    CONSUMER_REVIEWED_BY_FULL_NAME = "consumer_reviewed_by_full_name"
    CONSUMER_REVIEWED_BY_USERNAME = "consumer_reviewed_by_username"
    CREATED = "created"
    CREATED_BY = "created_by"
    CREATED_BY_FULL_NAME = "created_by_full_name"
    CREATED_BY_USERNAME = "created_by_username"
    CREATION_ORDER = "creation_order"
    CURRENT_USAGES = "current_usages"
    CUSTOMER_NAME = "customer_name"
    CUSTOMER_UUID = "customer_uuid"
    DESCRIPTION = "description"
    DOWNSCALED = "downscaled"
    EFFECTIVE_ID = "effective_id"
    ENDPOINTS = "endpoints"
    END_DATE = "end_date"
    END_DATE_REQUESTED_BY = "end_date_requested_by"
    ERROR_MESSAGE = "error_message"
    ERROR_TRACEBACK = "error_traceback"
    IS_LIMIT_BASED = "is_limit_based"
    IS_USAGE_BASED = "is_usage_based"
    LAST_SYNC = "last_sync"
    LIMITS = "limits"
    LIMIT_USAGE = "limit_usage"
    MODIFIED = "modified"
    NAME = "name"
    OFFERING = "offering"
    OFFERING_BILLABLE = "offering_billable"
    OFFERING_CUSTOMER_UUID = "offering_customer_uuid"
    OFFERING_DESCRIPTION = "offering_description"
    OFFERING_IMAGE = "offering_image"
    OFFERING_NAME = "offering_name"
    OFFERING_PLUGIN_OPTIONS = "offering_plugin_options"
    OFFERING_SHARED = "offering_shared"
    OFFERING_TERMS_OF_SERVICE = "offering_terms_of_service"
    OFFERING_THUMBNAIL = "offering_thumbnail"
    OFFERING_TYPE = "offering_type"
    OFFERING_UUID = "offering_uuid"
    OPTIONS = "options"
    ORDER_IN_PROGRESS = "order_in_progress"
    PARENT_NAME = "parent_name"
    PARENT_OFFERING_NAME = "parent_offering_name"
    PARENT_OFFERING_UUID = "parent_offering_uuid"
    PARENT_UUID = "parent_uuid"
    PAUSED = "paused"
    PLAN = "plan"
    PLAN_DESCRIPTION = "plan_description"
    PLAN_NAME = "plan_name"
    PLAN_UNIT = "plan_unit"
    PLAN_UUID = "plan_uuid"
    PROJECT = "project"
    PROJECT_DESCRIPTION = "project_description"
    PROJECT_END_DATE = "project_end_date"
    PROJECT_END_DATE_REQUESTED_BY = "project_end_date_requested_by"
    PROJECT_NAME = "project_name"
    PROJECT_UUID = "project_uuid"
    PROVIDER_NAME = "provider_name"
    PROVIDER_UUID = "provider_uuid"
    REPORT = "report"
    RESOURCE_TYPE = "resource_type"
    RESOURCE_UUID = "resource_uuid"
    RESTRICT_MEMBER_ACCESS = "restrict_member_access"
    SCOPE = "scope"
    SLOTS = "slots"
    SLUG = "slug"
    STATE = "state"
    URL = "url"
    USERNAME = "username"
    UUID = "uuid"

    def __str__(self) -> str:
        return str(self.value)
