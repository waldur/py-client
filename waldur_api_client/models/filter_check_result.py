from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FilterCheckResult")


@_attrs_define
class FilterCheckResult:
    """
    Attributes:
        name (str):
        configured (bool):
        matched (bool):
        reason (str):
        user_value (Union[Unset, Any]):
        rule_value (Union[Unset, Any]):
    """

    name: str
    configured: bool
    matched: bool
    reason: str
    user_value: Union[Unset, Any] = UNSET
    rule_value: Union[Unset, Any] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        configured = self.configured

        matched = self.matched

        reason = self.reason

        user_value = self.user_value

        rule_value = self.rule_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "configured": configured,
                "matched": matched,
                "reason": reason,
            }
        )
        if user_value is not UNSET:
            field_dict["user_value"] = user_value
        if rule_value is not UNSET:
            field_dict["rule_value"] = rule_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        configured = d.pop("configured")

        matched = d.pop("matched")

        reason = d.pop("reason")

        user_value = d.pop("user_value", UNSET)

        rule_value = d.pop("rule_value", UNSET)

        filter_check_result = cls(
            name=name,
            configured=configured,
            matched=matched,
            reason=reason,
            user_value=user_value,
            rule_value=rule_value,
        )

        filter_check_result.additional_properties = d
        return filter_check_result

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
