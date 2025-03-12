from enum import Enum


class MarketplaceOrdersRetrieveFieldItem(str, Enum):
    ACCEPTING_TERMS_OF_SERVICE = "accepting_terms_of_service"
    ACTIVATION_PRICE = "activation_price"
    ATTRIBUTES = "attributes"
    BACKEND_ID = "backend_id"
    CALLBACK_URL = "callback_url"
    CAN_TERMINATE = "can_terminate"
    CATEGORY_ICON = "category_icon"
    CATEGORY_TITLE = "category_title"
    CATEGORY_UUID = "category_uuid"
    COMPLETED_AT = "completed_at"
    CONSUMER_REVIEWED_AT = "consumer_reviewed_at"
    CONSUMER_REVIEWED_BY = "consumer_reviewed_by"
    CONSUMER_REVIEWED_BY_FULL_NAME = "consumer_reviewed_by_full_name"
    CONSUMER_REVIEWED_BY_USERNAME = "consumer_reviewed_by_username"
    COST = "cost"
    CREATED = "created"
    CREATED_BY_CIVIL_NUMBER = "created_by_civil_number"
    CREATED_BY_FULL_NAME = "created_by_full_name"
    CREATED_BY_USERNAME = "created_by_username"
    CUSTOMER_NAME = "customer_name"
    CUSTOMER_SLUG = "customer_slug"
    CUSTOMER_UUID = "customer_uuid"
    ERROR_MESSAGE = "error_message"
    FIXED_PRICE = "fixed_price"
    ISSUE = "issue"
    LIMITS = "limits"
    MARKETPLACE_RESOURCE_UUID = "marketplace_resource_uuid"
    MODIFIED = "modified"
    NEW_COST_ESTIMATE = "new_cost_estimate"
    NEW_PLAN_NAME = "new_plan_name"
    NEW_PLAN_UUID = "new_plan_uuid"
    OFFERING = "offering"
    OFFERING_BILLABLE = "offering_billable"
    OFFERING_DESCRIPTION = "offering_description"
    OFFERING_IMAGE = "offering_image"
    OFFERING_NAME = "offering_name"
    OFFERING_PLUGIN_OPTIONS = "offering_plugin_options"
    OFFERING_SHARED = "offering_shared"
    OFFERING_TERMS_OF_SERVICE = "offering_terms_of_service"
    OFFERING_THUMBNAIL = "offering_thumbnail"
    OFFERING_TYPE = "offering_type"
    OFFERING_UUID = "offering_uuid"
    OLD_COST_ESTIMATE = "old_cost_estimate"
    OLD_PLAN_NAME = "old_plan_name"
    OLD_PLAN_UUID = "old_plan_uuid"
    OUTPUT = "output"
    PLAN = "plan"
    PLAN_DESCRIPTION = "plan_description"
    PLAN_NAME = "plan_name"
    PLAN_UNIT = "plan_unit"
    PLAN_UUID = "plan_uuid"
    PROJECT_DESCRIPTION = "project_description"
    PROJECT_NAME = "project_name"
    PROJECT_SLUG = "project_slug"
    PROJECT_UUID = "project_uuid"
    PROVIDER_NAME = "provider_name"
    PROVIDER_REVIEWED_AT = "provider_reviewed_at"
    PROVIDER_REVIEWED_BY = "provider_reviewed_by"
    PROVIDER_REVIEWED_BY_FULL_NAME = "provider_reviewed_by_full_name"
    PROVIDER_REVIEWED_BY_USERNAME = "provider_reviewed_by_username"
    PROVIDER_UUID = "provider_uuid"
    RESOURCE_NAME = "resource_name"
    RESOURCE_TYPE = "resource_type"
    RESOURCE_UUID = "resource_uuid"
    STATE = "state"
    TERMINATION_COMMENT = "termination_comment"
    TYPE = "type"
    UUID = "uuid"

    def __str__(self) -> str:
        return str(self.value)
