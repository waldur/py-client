from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.nested_security_group_rule import NestedSecurityGroupRule


T = TypeVar("T", bound="OpenStackNestedSecurityGroup")


@_attrs_define
class OpenStackNestedSecurityGroup:
    """
    Attributes:
        url (str):
        name (str):
        rules (list['NestedSecurityGroupRule']):
        description (str):
        state (str):
    """

    url: str
    name: str
    rules: list["NestedSecurityGroupRule"]
    description: str
    state: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        name = self.name

        rules = []
        for rules_item_data in self.rules:
            rules_item = rules_item_data.to_dict()
            rules.append(rules_item)

        description = self.description

        state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "name": name,
                "rules": rules,
                "description": description,
                "state": state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.nested_security_group_rule import NestedSecurityGroupRule

        d = src_dict.copy()
        url = d.pop("url")

        name = d.pop("name")

        rules = []
        _rules = d.pop("rules")
        for rules_item_data in _rules:
            rules_item = NestedSecurityGroupRule.from_dict(rules_item_data)

            rules.append(rules_item)

        description = d.pop("description")

        state = d.pop("state")

        open_stack_nested_security_group = cls(
            url=url,
            name=name,
            rules=rules,
            description=description,
            state=state,
        )

        open_stack_nested_security_group.additional_properties = d
        return open_stack_nested_security_group

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
