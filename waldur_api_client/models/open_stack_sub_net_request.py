import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_stack_static_route_request import OpenStackStaticRouteRequest
    from ..models.open_stack_sub_net_allocation_pool_request import OpenStackSubNetAllocationPoolRequest


T = TypeVar("T", bound="OpenStackSubNetRequest")


@_attrs_define
class OpenStackSubNetRequest:
    """
    Attributes:
        name (str):
        description (Union[Unset, str]):
        cidr (Union[Unset, str]):
        gateway_ip (Union[None, Unset, str]):
        disable_gateway (Union[Unset, bool]):
        allocation_pools (Union[Unset, list['OpenStackSubNetAllocationPoolRequest']]):
        dns_nameservers (Union[Unset, list[str]]):
        host_routes (Union[Unset, list['OpenStackStaticRouteRequest']]):
    """

    name: str
    description: Union[Unset, str] = UNSET
    cidr: Union[Unset, str] = UNSET
    gateway_ip: Union[None, Unset, str] = UNSET
    disable_gateway: Union[Unset, bool] = UNSET
    allocation_pools: Union[Unset, list["OpenStackSubNetAllocationPoolRequest"]] = UNSET
    dns_nameservers: Union[Unset, list[str]] = UNSET
    host_routes: Union[Unset, list["OpenStackStaticRouteRequest"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        cidr = self.cidr

        gateway_ip: Union[None, Unset, str]
        if isinstance(self.gateway_ip, Unset):
            gateway_ip = UNSET
        else:
            gateway_ip = self.gateway_ip

        disable_gateway = self.disable_gateway

        allocation_pools: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.allocation_pools, Unset):
            allocation_pools = []
            for allocation_pools_item_data in self.allocation_pools:
                allocation_pools_item = allocation_pools_item_data.to_dict()
                allocation_pools.append(allocation_pools_item)

        dns_nameservers: Union[Unset, list[str]] = UNSET
        if not isinstance(self.dns_nameservers, Unset):
            dns_nameservers = self.dns_nameservers

        host_routes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.host_routes, Unset):
            host_routes = []
            for host_routes_item_data in self.host_routes:
                host_routes_item = host_routes_item_data.to_dict()
                host_routes.append(host_routes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if cidr is not UNSET:
            field_dict["cidr"] = cidr
        if gateway_ip is not UNSET:
            field_dict["gateway_ip"] = gateway_ip
        if disable_gateway is not UNSET:
            field_dict["disable_gateway"] = disable_gateway
        if allocation_pools is not UNSET:
            field_dict["allocation_pools"] = allocation_pools
        if dns_nameservers is not UNSET:
            field_dict["dns_nameservers"] = dns_nameservers
        if host_routes is not UNSET:
            field_dict["host_routes"] = host_routes

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        name = (None, str(self.name).encode(), "text/plain")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        cidr = self.cidr if isinstance(self.cidr, Unset) else (None, str(self.cidr).encode(), "text/plain")

        gateway_ip: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.gateway_ip, Unset):
            gateway_ip = UNSET
        elif isinstance(self.gateway_ip, str):
            gateway_ip = (None, str(self.gateway_ip).encode(), "text/plain")
        else:
            gateway_ip = (None, str(self.gateway_ip).encode(), "text/plain")

        disable_gateway = (
            self.disable_gateway
            if isinstance(self.disable_gateway, Unset)
            else (None, str(self.disable_gateway).encode(), "text/plain")
        )

        allocation_pools: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.allocation_pools, Unset):
            _temp_allocation_pools = []
            for allocation_pools_item_data in self.allocation_pools:
                allocation_pools_item = allocation_pools_item_data.to_dict()
                _temp_allocation_pools.append(allocation_pools_item)
            allocation_pools = (None, json.dumps(_temp_allocation_pools).encode(), "application/json")

        dns_nameservers: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.dns_nameservers, Unset):
            _temp_dns_nameservers = self.dns_nameservers
            dns_nameservers = (None, json.dumps(_temp_dns_nameservers).encode(), "application/json")

        host_routes: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.host_routes, Unset):
            _temp_host_routes = []
            for host_routes_item_data in self.host_routes:
                host_routes_item = host_routes_item_data.to_dict()
                _temp_host_routes.append(host_routes_item)
            host_routes = (None, json.dumps(_temp_host_routes).encode(), "application/json")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if cidr is not UNSET:
            field_dict["cidr"] = cidr
        if gateway_ip is not UNSET:
            field_dict["gateway_ip"] = gateway_ip
        if disable_gateway is not UNSET:
            field_dict["disable_gateway"] = disable_gateway
        if allocation_pools is not UNSET:
            field_dict["allocation_pools"] = allocation_pools
        if dns_nameservers is not UNSET:
            field_dict["dns_nameservers"] = dns_nameservers
        if host_routes is not UNSET:
            field_dict["host_routes"] = host_routes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.open_stack_static_route_request import OpenStackStaticRouteRequest
        from ..models.open_stack_sub_net_allocation_pool_request import OpenStackSubNetAllocationPoolRequest

        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description", UNSET)

        cidr = d.pop("cidr", UNSET)

        def _parse_gateway_ip(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        gateway_ip = _parse_gateway_ip(d.pop("gateway_ip", UNSET))

        disable_gateway = d.pop("disable_gateway", UNSET)

        allocation_pools = []
        _allocation_pools = d.pop("allocation_pools", UNSET)
        for allocation_pools_item_data in _allocation_pools or []:
            allocation_pools_item = OpenStackSubNetAllocationPoolRequest.from_dict(allocation_pools_item_data)

            allocation_pools.append(allocation_pools_item)

        dns_nameservers = cast(list[str], d.pop("dns_nameservers", UNSET))

        host_routes = []
        _host_routes = d.pop("host_routes", UNSET)
        for host_routes_item_data in _host_routes or []:
            host_routes_item = OpenStackStaticRouteRequest.from_dict(host_routes_item_data)

            host_routes.append(host_routes_item)

        open_stack_sub_net_request = cls(
            name=name,
            description=description,
            cidr=cidr,
            gateway_ip=gateway_ip,
            disable_gateway=disable_gateway,
            allocation_pools=allocation_pools,
            dns_nameservers=dns_nameservers,
            host_routes=host_routes,
        )

        open_stack_sub_net_request.additional_properties = d
        return open_stack_sub_net_request

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
