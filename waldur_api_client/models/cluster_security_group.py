from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rancher_cluster_security_group_rule import RancherClusterSecurityGroupRule


T = TypeVar("T", bound="ClusterSecurityGroup")


@_attrs_define
class ClusterSecurityGroup:
    """
    Attributes:
        uuid (UUID):
        name (str):
        rules (list['RancherClusterSecurityGroupRule']):
        description (Union[Unset, str]):
    """

    uuid: UUID
    name: str
    rules: list["RancherClusterSecurityGroupRule"]
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        name = self.name

        rules = []
        for rules_item_data in self.rules:
            rules_item = rules_item_data.to_dict()
            rules.append(rules_item)

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "name": name,
                "rules": rules,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.rancher_cluster_security_group_rule import RancherClusterSecurityGroupRule

        d = src_dict.copy()
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        rules = []
        _rules = d.pop("rules")
        for rules_item_data in _rules:
            rules_item = RancherClusterSecurityGroupRule.from_dict(rules_item_data)

            rules.append(rules_item)

        description = d.pop("description", UNSET)

        cluster_security_group = cls(
            uuid=uuid,
            name=name,
            rules=rules,
            description=description,
        )

        cluster_security_group.additional_properties = d
        return cluster_security_group

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
