from enum import Enum


class OrderFlowSourceKindEnum(str, Enum):
    CONSTANCE = "constance"
    ENGINE = "engine"
    OFFERING = "offering"
    ORDER = "order"
    ORDERER = "orderer"
    PLUGIN_OPTION = "plugin_option"
    PROJECT = "project"
    ROLE = "role"

    def __str__(self) -> str:
        return str(self.value)
