from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.policy_enum import PolicyEnum

T = TypeVar("T", bound="OpenStackNestedServerGroup")


@_attrs_define
class OpenStackNestedServerGroup:
    """
    Attributes:
        url (str):
        name (str):
        policy (PolicyEnum):
        state (str):
    """

    url: str
    name: str
    policy: PolicyEnum
    state: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        name = self.name

        policy = self.policy.value

        state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "name": name,
                "policy": policy,
                "state": state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        name = d.pop("name")

        policy = PolicyEnum(d.pop("policy"))

        state = d.pop("state")

        open_stack_nested_server_group = cls(
            url=url,
            name=name,
            policy=policy,
            state=state,
        )

        open_stack_nested_server_group.additional_properties = d
        return open_stack_nested_server_group

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
