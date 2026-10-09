from enum import Enum


class MatrixCryptoLeaseRequestKindEnum(str, Enum):
    BOOTSTRAP = "bootstrap"
    RESET = "reset"

    def __str__(self) -> str:
        return str(self.value)
