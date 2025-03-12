from enum import Enum


class MountPointEnum(str, Enum):
    VALUE_0 = "/var/lib/docker"
    VALUE_1 = "/var/lib/etcd"
    VALUE_2 = "/opt/media01"

    def __str__(self) -> str:
        return str(self.value)
