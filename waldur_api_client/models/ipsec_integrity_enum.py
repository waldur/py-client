from enum import Enum


class IpsecIntegrityEnum(str, Enum):
    SHA1 = "sha1"
    SHA256 = "sha256"
    SHA384 = "sha384"
    SHA512 = "sha512"

    def __str__(self) -> str:
        return str(self.value)
