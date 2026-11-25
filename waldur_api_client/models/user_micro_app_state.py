from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.micro_app_mode_enum import MicroAppModeEnum

T = TypeVar("T", bound="UserMicroAppState")


@_attrs_define
class UserMicroAppState:
    """
    Attributes:
        name (str):
        mode (MicroAppModeEnum):
        enabled (bool):
        rules (list[UUID]):
    """

    name: str
    mode: MicroAppModeEnum
    enabled: bool
    rules: list[UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        mode = self.mode.value

        enabled = self.enabled

        rules = []
        for rules_item_data in self.rules:
            rules_item = str(rules_item_data)
            rules.append(rules_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "mode": mode,
                "enabled": enabled,
                "rules": rules,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        mode = MicroAppModeEnum(d.pop("mode"))

        enabled = d.pop("enabled")

        rules = []
        _rules = d.pop("rules")
        for rules_item_data in _rules:
            rules_item = UUID(rules_item_data)

            rules.append(rules_item)

        user_micro_app_state = cls(
            name=name,
            mode=mode,
            enabled=enabled,
            rules=rules,
        )

        user_micro_app_state.additional_properties = d
        return user_micro_app_state

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
