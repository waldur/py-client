from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_stack_sub_net_allocation_pool import OpenStackSubNetAllocationPool


T = TypeVar("T", bound="OpenStackNestedSubNet")


@_attrs_define
class OpenStackNestedSubNet:
    """
    Attributes:
        name (str):
        allocation_pools (list['OpenStackSubNetAllocationPool']):
        description (Union[Unset, str]):
        cidr (Union[Unset, str]):
        gateway_ip (Union[None, Unset, str]):
        ip_version (Union[Unset, int]):
        enable_dhcp (Union[Unset, bool]):
    """

    name: str
    allocation_pools: list["OpenStackSubNetAllocationPool"]
    description: Union[Unset, str] = UNSET
    cidr: Union[Unset, str] = UNSET
    gateway_ip: Union[None, Unset, str] = UNSET
    ip_version: Union[Unset, int] = UNSET
    enable_dhcp: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        allocation_pools = []
        for allocation_pools_item_data in self.allocation_pools:
            allocation_pools_item = allocation_pools_item_data.to_dict()
            allocation_pools.append(allocation_pools_item)

        description = self.description

        cidr = self.cidr

        gateway_ip: Union[None, Unset, str]
        if isinstance(self.gateway_ip, Unset):
            gateway_ip = UNSET
        else:
            gateway_ip = self.gateway_ip

        ip_version = self.ip_version

        enable_dhcp = self.enable_dhcp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "allocation_pools": allocation_pools,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if cidr is not UNSET:
            field_dict["cidr"] = cidr
        if gateway_ip is not UNSET:
            field_dict["gateway_ip"] = gateway_ip
        if ip_version is not UNSET:
            field_dict["ip_version"] = ip_version
        if enable_dhcp is not UNSET:
            field_dict["enable_dhcp"] = enable_dhcp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.open_stack_sub_net_allocation_pool import OpenStackSubNetAllocationPool

        d = src_dict.copy()
        name = d.pop("name")

        allocation_pools = []
        _allocation_pools = d.pop("allocation_pools")
        for allocation_pools_item_data in _allocation_pools:
            allocation_pools_item = OpenStackSubNetAllocationPool.from_dict(allocation_pools_item_data)

            allocation_pools.append(allocation_pools_item)

        description = d.pop("description", UNSET)

        cidr = d.pop("cidr", UNSET)

        def _parse_gateway_ip(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        gateway_ip = _parse_gateway_ip(d.pop("gateway_ip", UNSET))

        ip_version = d.pop("ip_version", UNSET)

        enable_dhcp = d.pop("enable_dhcp", UNSET)

        open_stack_nested_sub_net = cls(
            name=name,
            allocation_pools=allocation_pools,
            description=description,
            cidr=cidr,
            gateway_ip=gateway_ip,
            ip_version=ip_version,
            enable_dhcp=enable_dhcp,
        )

        open_stack_nested_sub_net.additional_properties = d
        return open_stack_nested_sub_net

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
