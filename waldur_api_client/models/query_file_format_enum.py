from enum import Enum


class QueryFileFormatEnum(str, Enum):
    CSV = "csv"
    XLSX = "xlsx"

    def __str__(self) -> str:
        return str(self.value)
