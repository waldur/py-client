from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RancherNestedPublicIPRequest")


@_attrs_define
class RancherNestedPublicIPRequest:
    """
    Attributes:
        floating_ip (Union[None, str]):
        cluster (str):
    """

    floating_ip: Union[None, str]
    cluster: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        floating_ip: Union[None, str]
        floating_ip = self.floating_ip

        cluster = self.cluster

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "floating_ip": floating_ip,
                "cluster": cluster,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_floating_ip(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        floating_ip = _parse_floating_ip(d.pop("floating_ip"))

        cluster = d.pop("cluster")

        rancher_nested_public_ip_request = cls(
            floating_ip=floating_ip,
            cluster=cluster,
        )

        rancher_nested_public_ip_request.additional_properties = d
        return rancher_nested_public_ip_request

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
