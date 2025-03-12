from enum import Enum


class AzureSqlServersListFieldItem(str, Enum):
    ACCESS_URL = "access_url"
    BACKEND_ID = "backend_id"
    CREATED = "created"
    CUSTOMER = "customer"
    CUSTOMER_ABBREVIATION = "customer_abbreviation"
    CUSTOMER_NAME = "customer_name"
    CUSTOMER_NATIVE_NAME = "customer_native_name"
    DESCRIPTION = "description"
    ERROR_MESSAGE = "error_message"
    ERROR_TRACEBACK = "error_traceback"
    FQDN = "fqdn"
    IS_LIMIT_BASED = "is_limit_based"
    IS_USAGE_BASED = "is_usage_based"
    LOCATION = "location"
    LOCATION_NAME = "location_name"
    MARKETPLACE_CATEGORY_NAME = "marketplace_category_name"
    MARKETPLACE_CATEGORY_UUID = "marketplace_category_uuid"
    MARKETPLACE_OFFERING_NAME = "marketplace_offering_name"
    MARKETPLACE_OFFERING_PLUGIN_OPTIONS = "marketplace_offering_plugin_options"
    MARKETPLACE_OFFERING_UUID = "marketplace_offering_uuid"
    MARKETPLACE_PLAN_UUID = "marketplace_plan_uuid"
    MARKETPLACE_RESOURCE_STATE = "marketplace_resource_state"
    MARKETPLACE_RESOURCE_UUID = "marketplace_resource_uuid"
    MODIFIED = "modified"
    NAME = "name"
    PASSWORD = "password"
    PROJECT = "project"
    PROJECT_NAME = "project_name"
    PROJECT_UUID = "project_uuid"
    RESOURCE_GROUP = "resource_group"
    RESOURCE_GROUP_NAME = "resource_group_name"
    RESOURCE_TYPE = "resource_type"
    SERVICE_NAME = "service_name"
    SERVICE_SETTINGS = "service_settings"
    SERVICE_SETTINGS_ERROR_MESSAGE = "service_settings_error_message"
    SERVICE_SETTINGS_STATE = "service_settings_state"
    SERVICE_SETTINGS_UUID = "service_settings_uuid"
    STATE = "state"
    STORAGE_MB = "storage_mb"
    URL = "url"
    USERNAME = "username"
    UUID = "uuid"

    def __str__(self) -> str:
        return str(self.value)
