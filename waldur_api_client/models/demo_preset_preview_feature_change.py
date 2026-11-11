from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.demo_preset_preview_feature_change_source_enum import DemoPresetPreviewFeatureChangeSourceEnum

T = TypeVar("T", bound="DemoPresetPreviewFeatureChange")


@_attrs_define
class DemoPresetPreviewFeatureChange:
    """
    Attributes:
        key (str):
        current_value (bool):
        new_value (bool):
        source (DemoPresetPreviewFeatureChangeSourceEnum):
        changed (bool):
    """

    key: str
    current_value: bool
    new_value: bool
    source: DemoPresetPreviewFeatureChangeSourceEnum
    changed: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        current_value = self.current_value

        new_value = self.new_value

        source = self.source.value

        changed = self.changed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "current_value": current_value,
                "new_value": new_value,
                "source": source,
                "changed": changed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        current_value = d.pop("current_value")

        new_value = d.pop("new_value")

        source = DemoPresetPreviewFeatureChangeSourceEnum(d.pop("source"))

        changed = d.pop("changed")

        demo_preset_preview_feature_change = cls(
            key=key,
            current_value=current_value,
            new_value=new_value,
            source=source,
            changed=changed,
        )

        demo_preset_preview_feature_change.additional_properties = d
        return demo_preset_preview_feature_change

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
