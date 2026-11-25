from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.feature_rule_matched_user import FeatureRuleMatchedUser


T = TypeVar("T", bound="FeatureRuleMatchedUsersResponse")


@_attrs_define
class FeatureRuleMatchedUsersResponse:
    """
    Attributes:
        count (int): Active users the rule matches, among those checked.
        checked (int): Active users checked.
        complete (bool): False when the check stopped at its limit, so count is a lower bound.
        users (list['FeatureRuleMatchedUser']): The first matched users.
    """

    count: int
    checked: int
    complete: bool
    users: list["FeatureRuleMatchedUser"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        checked = self.checked

        complete = self.complete

        users = []
        for users_item_data in self.users:
            users_item = users_item_data.to_dict()
            users.append(users_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "checked": checked,
                "complete": complete,
                "users": users,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.feature_rule_matched_user import FeatureRuleMatchedUser

        d = dict(src_dict)
        count = d.pop("count")

        checked = d.pop("checked")

        complete = d.pop("complete")

        users = []
        _users = d.pop("users")
        for users_item_data in _users:
            users_item = FeatureRuleMatchedUser.from_dict(users_item_data)

            users.append(users_item)

        feature_rule_matched_users_response = cls(
            count=count,
            checked=checked,
            complete=complete,
            users=users,
        )

        feature_rule_matched_users_response.additional_properties = d
        return feature_rule_matched_users_response

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
