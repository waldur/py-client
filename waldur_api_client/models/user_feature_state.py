from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.feature_scope_enum import FeatureScopeEnum
from ..models.user_feature_state_source_enum import UserFeatureStateSourceEnum

T = TypeVar("T", bound="UserFeatureState")


@_attrs_define
class UserFeatureState:
    """
    Attributes:
        key (str):
        scope (FeatureScopeEnum):
        enabled (bool):
        source (UserFeatureStateSourceEnum):
        rules (list[UUID]):
    """

    key: str
    scope: FeatureScopeEnum
    enabled: bool
    source: UserFeatureStateSourceEnum
    rules: list[UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        scope = self.scope.value

        enabled = self.enabled

        source = self.source.value

        rules = []
        for rules_item_data in self.rules:
            rules_item = str(rules_item_data)
            rules.append(rules_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "scope": scope,
                "enabled": enabled,
                "source": source,
                "rules": rules,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        scope = FeatureScopeEnum(d.pop("scope"))

        enabled = d.pop("enabled")

        source = UserFeatureStateSourceEnum(d.pop("source"))

        rules = []
        _rules = d.pop("rules")
        for rules_item_data in _rules:
            rules_item = UUID(rules_item_data)

            rules.append(rules_item)

        user_feature_state = cls(
            key=key,
            scope=scope,
            enabled=enabled,
            source=source,
            rules=rules,
        )

        user_feature_state.additional_properties = d
        return user_feature_state

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
