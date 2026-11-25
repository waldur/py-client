from enum import Enum


class K8SEgressRuleProtocolEnum(str, Enum):
    ICMP = "ICMP"
    TCP = "TCP"
    UDP = "UDP"

    def __str__(self) -> str:
        return str(self.value)
