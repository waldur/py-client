from enum import Enum


class K8SSitesTopologyEnum(str, Enum):
    VALUE_0 = "1-datacenter"
    VALUE_1 = "3-datacenter"

    def __str__(self) -> str:
        return str(self.value)
