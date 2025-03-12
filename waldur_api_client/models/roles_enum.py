from enum import Enum


class RolesEnum(str, Enum):
    CONTROLPLANE = "controlplane"
    ETCD = "etcd"
    WORKER = "worker"

    def __str__(self) -> str:
        return str(self.value)
