from enum import Enum


class RuleEnum(str, Enum):
    DWDI_NODE_COMPONENT = "dwdi_node_component"
    DWDI_UNIT_FACTOR_REPORTING = "dwdi_unit_factor_reporting"
    PLAN_COMPONENT_PRICE = "plan_component_price"
    REQUIRED_BACKEND_SETTING = "required_backend_setting"
    SLURM_CLUSTER_NAME = "slurm_cluster_name"
    SLURM_COMPONENT_BILLING_TYPE = "slurm_component_billing_type"
    SLURM_COMPONENT_TRES = "slurm_component_tres"

    def __str__(self) -> str:
        return str(self.value)
