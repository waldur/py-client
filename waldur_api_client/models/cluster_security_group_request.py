from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.rancher_cluster_security_group_rule_request import RancherClusterSecurityGroupRuleRequest


T = TypeVar("T", bound="ClusterSecurityGroupRequest")


@_attrs_define
class ClusterSecurityGroupRequest:
    """
    Attributes:
        rules (list['RancherClusterSecurityGroupRuleRequest']):
    """

    rules: list["RancherClusterSecurityGroupRuleRequest"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rules = []
        for rules_item_data in self.rules:
            rules_item = rules_item_data.to_dict()
            rules.append(rules_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rules": rules,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rancher_cluster_security_group_rule_request import RancherClusterSecurityGroupRuleRequest

        d = dict(src_dict)
        rules = []
        _rules = d.pop("rules")
        for rules_item_data in _rules:
            rules_item = RancherClusterSecurityGroupRuleRequest.from_dict(rules_item_data)

            rules.append(rules_item)

        cluster_security_group_request = cls(
            rules=rules,
        )

        cluster_security_group_request.additional_properties = d
        return cluster_security_group_request

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
