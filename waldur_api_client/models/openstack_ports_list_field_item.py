from enum import Enum


class OpenstackPortsListFieldItem(str, Enum):
    ACCESS_URL = "access_url"
    ALLOWED_ADDRESS_PAIRS = "allowed_address_pairs"
    BACKEND_ID = "backend_id"
    CREATED = "created"
    CUSTOMER = "customer"
    CUSTOMER_ABBREVIATION = "customer_abbreviation"
    CUSTOMER_NAME = "customer_name"
    CUSTOMER_NATIVE_NAME = "customer_native_name"
    DESCRIPTION = "description"
    DEVICE_ID = "device_id"
    DEVICE_OWNER = "device_owner"
    ERROR_MESSAGE = "error_message"
    ERROR_TRACEBACK = "error_traceback"
    FIXED_IPS = "fixed_ips"
    FLOATING_IPS = "floating_ips"
    IS_LIMIT_BASED = "is_limit_based"
    IS_USAGE_BASED = "is_usage_based"
    MAC_ADDRESS = "mac_address"
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
    NETWORK = "network"
    NETWORK_NAME = "network_name"
    NETWORK_UUID = "network_uuid"
    PORT_SECURITY_ENABLED = "port_security_enabled"
    PROJECT = "project"
    PROJECT_NAME = "project_name"
    PROJECT_UUID = "project_uuid"
    RESOURCE_TYPE = "resource_type"
    SECURITY_GROUPS = "security_groups"
    SERVICE_NAME = "service_name"
    SERVICE_SETTINGS = "service_settings"
    SERVICE_SETTINGS_ERROR_MESSAGE = "service_settings_error_message"
    SERVICE_SETTINGS_STATE = "service_settings_state"
    SERVICE_SETTINGS_UUID = "service_settings_uuid"
    STATE = "state"
    TENANT = "tenant"
    TENANT_NAME = "tenant_name"
    TENANT_UUID = "tenant_uuid"
    URL = "url"
    UUID = "uuid"

    def __str__(self) -> str:
        return str(self.value)
