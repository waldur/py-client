from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.demo_preset_preview_setting_change_source_enum import DemoPresetPreviewSettingChangeSourceEnum

if TYPE_CHECKING:
    from ..models.demo_preset_preview_setting_change_current_value_type_0 import (
        DemoPresetPreviewSettingChangeCurrentValueType0,
    )
    from ..models.demo_preset_preview_setting_change_new_value_type_0 import DemoPresetPreviewSettingChangeNewValueType0


T = TypeVar("T", bound="DemoPresetPreviewSettingChange")


@_attrs_define
class DemoPresetPreviewSettingChange:
    """
    Attributes:
        key (str):
        current_value (Union['DemoPresetPreviewSettingChangeCurrentValueType0', None]): Null for a secret.
        new_value (Union['DemoPresetPreviewSettingChangeNewValueType0', None]): Value after the load. Null for a secret.
        source (DemoPresetPreviewSettingChangeSourceEnum):
        changed (bool): Whether the load changes the value.
        skipped (bool): The preset sets a setting the deployment owns; it keeps its value.
        secret (bool): Values of secrets are never shown.
    """

    key: str
    current_value: Union["DemoPresetPreviewSettingChangeCurrentValueType0", None]
    new_value: Union["DemoPresetPreviewSettingChangeNewValueType0", None]
    source: DemoPresetPreviewSettingChangeSourceEnum
    changed: bool
    skipped: bool
    secret: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.demo_preset_preview_setting_change_current_value_type_0 import (
            DemoPresetPreviewSettingChangeCurrentValueType0,
        )
        from ..models.demo_preset_preview_setting_change_new_value_type_0 import (
            DemoPresetPreviewSettingChangeNewValueType0,
        )

        key = self.key

        current_value: Union[None, dict[str, Any]]
        if isinstance(self.current_value, DemoPresetPreviewSettingChangeCurrentValueType0):
            current_value = self.current_value.to_dict()
        else:
            current_value = self.current_value

        new_value: Union[None, dict[str, Any]]
        if isinstance(self.new_value, DemoPresetPreviewSettingChangeNewValueType0):
            new_value = self.new_value.to_dict()
        else:
            new_value = self.new_value

        source = self.source.value

        changed = self.changed

        skipped = self.skipped

        secret = self.secret

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "current_value": current_value,
                "new_value": new_value,
                "source": source,
                "changed": changed,
                "skipped": skipped,
                "secret": secret,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.demo_preset_preview_setting_change_current_value_type_0 import (
            DemoPresetPreviewSettingChangeCurrentValueType0,
        )
        from ..models.demo_preset_preview_setting_change_new_value_type_0 import (
            DemoPresetPreviewSettingChangeNewValueType0,
        )

        d = dict(src_dict)
        key = d.pop("key")

        def _parse_current_value(data: object) -> Union["DemoPresetPreviewSettingChangeCurrentValueType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                current_value_type_0 = DemoPresetPreviewSettingChangeCurrentValueType0.from_dict(data)

                return current_value_type_0
            except:  # noqa: E722
                pass
            return cast(Union["DemoPresetPreviewSettingChangeCurrentValueType0", None], data)

        current_value = _parse_current_value(d.pop("current_value"))

        def _parse_new_value(data: object) -> Union["DemoPresetPreviewSettingChangeNewValueType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                new_value_type_0 = DemoPresetPreviewSettingChangeNewValueType0.from_dict(data)

                return new_value_type_0
            except:  # noqa: E722
                pass
            return cast(Union["DemoPresetPreviewSettingChangeNewValueType0", None], data)

        new_value = _parse_new_value(d.pop("new_value"))

        source = DemoPresetPreviewSettingChangeSourceEnum(d.pop("source"))

        changed = d.pop("changed")

        skipped = d.pop("skipped")

        secret = d.pop("secret")

        demo_preset_preview_setting_change = cls(
            key=key,
            current_value=current_value,
            new_value=new_value,
            source=source,
            changed=changed,
            skipped=skipped,
            secret=secret,
        )

        demo_preset_preview_setting_change.additional_properties = d
        return demo_preset_preview_setting_change

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
