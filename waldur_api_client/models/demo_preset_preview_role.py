from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DemoPresetPreviewRole")


@_attrs_define
class DemoPresetPreviewRole:
    """
    Attributes:
        role (str): Role name, such as CUSTOMER.OWNER.
        scope_type (str): Type of the role's scope, such as structure.customer.
        scope_name (str): Name of the role's scope in the preset.
    """

    role: str
    scope_type: str
    scope_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role = self.role

        scope_type = self.scope_type

        scope_name = self.scope_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
                "scope_type": scope_type,
                "scope_name": scope_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        role = d.pop("role")

        scope_type = d.pop("scope_type")

        scope_name = d.pop("scope_name")

        demo_preset_preview_role = cls(
            role=role,
            scope_type=scope_type,
            scope_name=scope_name,
        )

        demo_preset_preview_role.additional_properties = d
        return demo_preset_preview_role

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
