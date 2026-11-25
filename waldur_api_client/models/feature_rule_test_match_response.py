from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.feature_rule_check import FeatureRuleCheck


T = TypeVar("T", bound="FeatureRuleTestMatchResponse")


@_attrs_define
class FeatureRuleTestMatchResponse:
    """
    Attributes:
        matched (bool): Whether the rule matches the user, active or not.
        is_active (bool):
        enabled_globally (bool): Whether the feature is already on for everyone, so the rule changes nothing.
        user_uuid (UUID):
        user_username (str):
        filters (list['FeatureRuleCheck']):
    """

    matched: bool
    is_active: bool
    enabled_globally: bool
    user_uuid: UUID
    user_username: str
    filters: list["FeatureRuleCheck"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        matched = self.matched

        is_active = self.is_active

        enabled_globally = self.enabled_globally

        user_uuid = str(self.user_uuid)

        user_username = self.user_username

        filters = []
        for filters_item_data in self.filters:
            filters_item = filters_item_data.to_dict()
            filters.append(filters_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "matched": matched,
                "is_active": is_active,
                "enabled_globally": enabled_globally,
                "user_uuid": user_uuid,
                "user_username": user_username,
                "filters": filters,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.feature_rule_check import FeatureRuleCheck

        d = dict(src_dict)
        matched = d.pop("matched")

        is_active = d.pop("is_active")

        enabled_globally = d.pop("enabled_globally")

        user_uuid = UUID(d.pop("user_uuid"))

        user_username = d.pop("user_username")

        filters = []
        _filters = d.pop("filters")
        for filters_item_data in _filters:
            filters_item = FeatureRuleCheck.from_dict(filters_item_data)

            filters.append(filters_item)

        feature_rule_test_match_response = cls(
            matched=matched,
            is_active=is_active,
            enabled_globally=enabled_globally,
            user_uuid=user_uuid,
            user_username=user_username,
            filters=filters,
        )

        feature_rule_test_match_response.additional_properties = d
        return feature_rule_test_match_response

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
