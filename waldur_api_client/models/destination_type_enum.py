from enum import Enum


class DestinationTypeEnum(str, Enum):
    CIDR = "cidr"
    DOMAIN = "domain"

    def __str__(self) -> str:
        return str(self.value)
