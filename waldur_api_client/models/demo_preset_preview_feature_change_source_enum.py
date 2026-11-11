from enum import Enum


class DemoPresetPreviewFeatureChangeSourceEnum(str, Enum):
    DEFAULT = "default"
    OVERLAY = "overlay"
    PRESET = "preset"

    def __str__(self) -> str:
        return str(self.value)
