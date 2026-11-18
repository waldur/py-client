from enum import Enum


class S3BrowserFlavorEnum(str, Enum):
    CEPH = "ceph"
    GARAGE = "garage"
    GENERIC = "generic"
    MINIO = "minio"

    def __str__(self) -> str:
        return str(self.value)
