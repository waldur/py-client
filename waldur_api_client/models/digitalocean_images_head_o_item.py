from enum import Enum


class DigitaloceanImagesHeadOItem(str, Enum):
    DISTRIBUTION = "distribution"
    TYPE = "type"
    VALUE_0 = "-distribution"
    VALUE_1 = "-type"

    def __str__(self) -> str:
        return str(self.value)
