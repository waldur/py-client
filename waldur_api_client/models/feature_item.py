from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.feature_scope_enum import FeatureScopeEnum

T = TypeVar("T", bound="FeatureItem")


@_attrs_define
class FeatureItem:
    """
    Attributes:
        key (str):
        description (str):
        scope (FeatureScopeEnum):
    """

    key: str
    description: str
    scope: FeatureScopeEnum
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        description = self.description

        scope = self.scope.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "description": description,
                "scope": scope,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        description = d.pop("description")

        scope = FeatureScopeEnum(d.pop("scope"))

        feature_item = cls(
            key=key,
            description=description,
            scope=scope,
        )

        feature_item.additional_properties = d
        return feature_item

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
