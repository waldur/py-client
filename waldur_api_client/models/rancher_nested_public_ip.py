from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RancherNestedPublicIP")


@_attrs_define
class RancherNestedPublicIP:
    """
    Attributes:
        floating_ip (Union[None, Unset, str]):
        cluster (Union[Unset, str]):
        ip_address (Union[Unset, str]):
    """

    floating_ip: Union[None, Unset, str] = UNSET
    cluster: Union[Unset, str] = UNSET
    ip_address: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        floating_ip: Union[None, Unset, str]
        if isinstance(self.floating_ip, Unset):
            floating_ip = UNSET
        else:
            floating_ip = self.floating_ip

        cluster = self.cluster

        ip_address = self.ip_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if floating_ip is not UNSET:
            field_dict["floating_ip"] = floating_ip
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if ip_address is not UNSET:
            field_dict["ip_address"] = ip_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_floating_ip(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        floating_ip = _parse_floating_ip(d.pop("floating_ip", UNSET))

        cluster = d.pop("cluster", UNSET)

        ip_address = d.pop("ip_address", UNSET)

        rancher_nested_public_ip = cls(
            floating_ip=floating_ip,
            cluster=cluster,
            ip_address=ip_address,
        )

        rancher_nested_public_ip.additional_properties = d
        return rancher_nested_public_ip

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
