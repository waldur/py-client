from enum import Enum


class OptionFieldTypeEnum(str, Enum):
    BOOLEAN = "boolean"
    CIDR = "cidr"
    COMPONENT_FORMULA = "component_formula"
    COMPONENT_MULTIPLIER = "component_multiplier"
    COMPONENT_SUM = "component_sum"
    CONDITIONAL_CASCADE = "conditional_cascade"
    DATE = "date"
    HTML_TEXT = "html_text"
    INTEGER = "integer"
    IPSEC_VPN_CONFIG = "ipsec_vpn_config"
    K8S_CLUSTER_CONFIG = "k8s_cluster_config"
    K8S_EGRESS_RULES = "k8s_egress_rules"
    MONEY = "money"
    SECRET = "secret"
    SELECT_MULTIPLE_OPENSTACK_INSTANCES = "select_multiple_openstack_instances"
    SELECT_MULTIPLE_OPENSTACK_TENANTS = "select_multiple_openstack_tenants"
    SELECT_OPENSTACK_INSTANCE = "select_openstack_instance"
    SELECT_OPENSTACK_TENANT = "select_openstack_tenant"
    SELECT_STRING = "select_string"
    SELECT_STRING_MULTI = "select_string_multi"
    STORAGE_FOLDER_MANAGER = "storage_folder_manager"
    STRING = "string"
    TEXT = "text"
    TIME = "time"

    def __str__(self) -> str:
        return str(self.value)
