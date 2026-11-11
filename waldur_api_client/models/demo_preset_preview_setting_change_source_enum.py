from enum import Enum


class DemoPresetPreviewSettingChangeSourceEnum(str, Enum):
    DEFAULT = "default"
    DEPLOYMENT = "deployment"
    OVERLAY = "overlay"
    PRESET = "preset"

    def __str__(self) -> str:
        return str(self.value)
