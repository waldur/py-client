import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.core_states import CoreStates
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_stack_static_route import OpenStackStaticRoute
    from ..models.open_stack_sub_net_allocation_pool import OpenStackSubNetAllocationPool
    from ..models.open_stack_sub_net_marketplace_offering_plugin_options import (
        OpenStackSubNetMarketplaceOfferingPluginOptions,
    )


T = TypeVar("T", bound="OpenStackSubNet")


@_attrs_define
class OpenStackSubNet:
    """
    Attributes:
        url (str):
        uuid (UUID):
        name (str):
        service_name (str):
        service_settings (str):
        service_settings_uuid (UUID):
        service_settings_state (str):
        service_settings_error_message (str):
        project (str):
        project_name (str):
        project_uuid (UUID):
        customer (str):
        customer_name (str):
        customer_native_name (str):
        customer_abbreviation (str):
        error_message (str):
        error_traceback (str):
        resource_type (str):
        state (CoreStates):
        created (datetime.datetime):
        modified (datetime.datetime):
        backend_id (str):
        access_url (Union[None, str]):
        tenant (str):
        tenant_name (str):
        network (str):
        network_name (str):
        allocation_pools (list['OpenStackSubNetAllocationPool']):
        ip_version (int):
        enable_dhcp (bool):
        is_connected (bool): Is subnet connected to the default tenant router.
        marketplace_offering_uuid (str):
        marketplace_offering_name (str):
        marketplace_offering_plugin_options (OpenStackSubNetMarketplaceOfferingPluginOptions):
        marketplace_category_uuid (str):
        marketplace_category_name (str):
        marketplace_resource_uuid (str):
        marketplace_plan_uuid (str):
        marketplace_resource_state (str):
        is_usage_based (bool):
        is_limit_based (bool):
        description (Union[Unset, str]):
        cidr (Union[Unset, str]):
        gateway_ip (Union[None, Unset, str]):
        disable_gateway (Union[Unset, bool]):
        dns_nameservers (Union[Unset, list[str]]):
        host_routes (Union[Unset, list['OpenStackStaticRoute']]):
    """

    url: str
    uuid: UUID
    name: str
    service_name: str
    service_settings: str
    service_settings_uuid: UUID
    service_settings_state: str
    service_settings_error_message: str
    project: str
    project_name: str
    project_uuid: UUID
    customer: str
    customer_name: str
    customer_native_name: str
    customer_abbreviation: str
    error_message: str
    error_traceback: str
    resource_type: str
    state: CoreStates
    created: datetime.datetime
    modified: datetime.datetime
    backend_id: str
    access_url: Union[None, str]
    tenant: str
    tenant_name: str
    network: str
    network_name: str
    allocation_pools: list["OpenStackSubNetAllocationPool"]
    ip_version: int
    enable_dhcp: bool
    is_connected: bool
    marketplace_offering_uuid: str
    marketplace_offering_name: str
    marketplace_offering_plugin_options: "OpenStackSubNetMarketplaceOfferingPluginOptions"
    marketplace_category_uuid: str
    marketplace_category_name: str
    marketplace_resource_uuid: str
    marketplace_plan_uuid: str
    marketplace_resource_state: str
    is_usage_based: bool
    is_limit_based: bool
    description: Union[Unset, str] = UNSET
    cidr: Union[Unset, str] = UNSET
    gateway_ip: Union[None, Unset, str] = UNSET
    disable_gateway: Union[Unset, bool] = UNSET
    dns_nameservers: Union[Unset, list[str]] = UNSET
    host_routes: Union[Unset, list["OpenStackStaticRoute"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        uuid = str(self.uuid)

        name = self.name

        service_name = self.service_name

        service_settings = self.service_settings

        service_settings_uuid = str(self.service_settings_uuid)

        service_settings_state = self.service_settings_state

        service_settings_error_message = self.service_settings_error_message

        project = self.project

        project_name = self.project_name

        project_uuid = str(self.project_uuid)

        customer = self.customer

        customer_name = self.customer_name

        customer_native_name = self.customer_native_name

        customer_abbreviation = self.customer_abbreviation

        error_message = self.error_message

        error_traceback = self.error_traceback

        resource_type = self.resource_type

        state = self.state.value

        created = self.created.isoformat()

        modified = self.modified.isoformat()

        backend_id = self.backend_id

        access_url: Union[None, str]
        access_url = self.access_url

        tenant = self.tenant

        tenant_name = self.tenant_name

        network = self.network

        network_name = self.network_name

        allocation_pools = []
        for allocation_pools_item_data in self.allocation_pools:
            allocation_pools_item = allocation_pools_item_data.to_dict()
            allocation_pools.append(allocation_pools_item)

        ip_version = self.ip_version

        enable_dhcp = self.enable_dhcp

        is_connected = self.is_connected

        marketplace_offering_uuid = self.marketplace_offering_uuid

        marketplace_offering_name = self.marketplace_offering_name

        marketplace_offering_plugin_options = self.marketplace_offering_plugin_options.to_dict()

        marketplace_category_uuid = self.marketplace_category_uuid

        marketplace_category_name = self.marketplace_category_name

        marketplace_resource_uuid = self.marketplace_resource_uuid

        marketplace_plan_uuid = self.marketplace_plan_uuid

        marketplace_resource_state = self.marketplace_resource_state

        is_usage_based = self.is_usage_based

        is_limit_based = self.is_limit_based

        description = self.description

        cidr = self.cidr

        gateway_ip: Union[None, Unset, str]
        if isinstance(self.gateway_ip, Unset):
            gateway_ip = UNSET
        else:
            gateway_ip = self.gateway_ip

        disable_gateway = self.disable_gateway

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
                "url": url,
                "uuid": uuid,
                "name": name,
                "service_name": service_name,
                "service_settings": service_settings,
                "service_settings_uuid": service_settings_uuid,
                "service_settings_state": service_settings_state,
                "service_settings_error_message": service_settings_error_message,
                "project": project,
                "project_name": project_name,
                "project_uuid": project_uuid,
                "customer": customer,
                "customer_name": customer_name,
                "customer_native_name": customer_native_name,
                "customer_abbreviation": customer_abbreviation,
                "error_message": error_message,
                "error_traceback": error_traceback,
                "resource_type": resource_type,
                "state": state,
                "created": created,
                "modified": modified,
                "backend_id": backend_id,
                "access_url": access_url,
                "tenant": tenant,
                "tenant_name": tenant_name,
                "network": network,
                "network_name": network_name,
                "allocation_pools": allocation_pools,
                "ip_version": ip_version,
                "enable_dhcp": enable_dhcp,
                "is_connected": is_connected,
                "marketplace_offering_uuid": marketplace_offering_uuid,
                "marketplace_offering_name": marketplace_offering_name,
                "marketplace_offering_plugin_options": marketplace_offering_plugin_options,
                "marketplace_category_uuid": marketplace_category_uuid,
                "marketplace_category_name": marketplace_category_name,
                "marketplace_resource_uuid": marketplace_resource_uuid,
                "marketplace_plan_uuid": marketplace_plan_uuid,
                "marketplace_resource_state": marketplace_resource_state,
                "is_usage_based": is_usage_based,
                "is_limit_based": is_limit_based,
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
        if dns_nameservers is not UNSET:
            field_dict["dns_nameservers"] = dns_nameservers
        if host_routes is not UNSET:
            field_dict["host_routes"] = host_routes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.open_stack_static_route import OpenStackStaticRoute
        from ..models.open_stack_sub_net_allocation_pool import OpenStackSubNetAllocationPool
        from ..models.open_stack_sub_net_marketplace_offering_plugin_options import (
            OpenStackSubNetMarketplaceOfferingPluginOptions,
        )

        d = dict(src_dict)
        url = d.pop("url")

        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        service_name = d.pop("service_name")

        service_settings = d.pop("service_settings")

        service_settings_uuid = UUID(d.pop("service_settings_uuid"))

        service_settings_state = d.pop("service_settings_state")

        service_settings_error_message = d.pop("service_settings_error_message")

        project = d.pop("project")

        project_name = d.pop("project_name")

        project_uuid = UUID(d.pop("project_uuid"))

        customer = d.pop("customer")

        customer_name = d.pop("customer_name")

        customer_native_name = d.pop("customer_native_name")

        customer_abbreviation = d.pop("customer_abbreviation")

        error_message = d.pop("error_message")

        error_traceback = d.pop("error_traceback")

        resource_type = d.pop("resource_type")

        state = CoreStates(d.pop("state"))

        created = isoparse(d.pop("created"))

        modified = isoparse(d.pop("modified"))

        backend_id = d.pop("backend_id")

        def _parse_access_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        access_url = _parse_access_url(d.pop("access_url"))

        tenant = d.pop("tenant")

        tenant_name = d.pop("tenant_name")

        network = d.pop("network")

        network_name = d.pop("network_name")

        allocation_pools = []
        _allocation_pools = d.pop("allocation_pools")
        for allocation_pools_item_data in _allocation_pools:
            allocation_pools_item = OpenStackSubNetAllocationPool.from_dict(allocation_pools_item_data)

            allocation_pools.append(allocation_pools_item)

        ip_version = d.pop("ip_version")

        enable_dhcp = d.pop("enable_dhcp")

        is_connected = d.pop("is_connected")

        marketplace_offering_uuid = d.pop("marketplace_offering_uuid")

        marketplace_offering_name = d.pop("marketplace_offering_name")

        marketplace_offering_plugin_options = OpenStackSubNetMarketplaceOfferingPluginOptions.from_dict(
            d.pop("marketplace_offering_plugin_options")
        )

        marketplace_category_uuid = d.pop("marketplace_category_uuid")

        marketplace_category_name = d.pop("marketplace_category_name")

        marketplace_resource_uuid = d.pop("marketplace_resource_uuid")

        marketplace_plan_uuid = d.pop("marketplace_plan_uuid")

        marketplace_resource_state = d.pop("marketplace_resource_state")

        is_usage_based = d.pop("is_usage_based")

        is_limit_based = d.pop("is_limit_based")

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

        dns_nameservers = cast(list[str], d.pop("dns_nameservers", UNSET))

        host_routes = []
        _host_routes = d.pop("host_routes", UNSET)
        for host_routes_item_data in _host_routes or []:
            host_routes_item = OpenStackStaticRoute.from_dict(host_routes_item_data)

            host_routes.append(host_routes_item)

        open_stack_sub_net = cls(
            url=url,
            uuid=uuid,
            name=name,
            service_name=service_name,
            service_settings=service_settings,
            service_settings_uuid=service_settings_uuid,
            service_settings_state=service_settings_state,
            service_settings_error_message=service_settings_error_message,
            project=project,
            project_name=project_name,
            project_uuid=project_uuid,
            customer=customer,
            customer_name=customer_name,
            customer_native_name=customer_native_name,
            customer_abbreviation=customer_abbreviation,
            error_message=error_message,
            error_traceback=error_traceback,
            resource_type=resource_type,
            state=state,
            created=created,
            modified=modified,
            backend_id=backend_id,
            access_url=access_url,
            tenant=tenant,
            tenant_name=tenant_name,
            network=network,
            network_name=network_name,
            allocation_pools=allocation_pools,
            ip_version=ip_version,
            enable_dhcp=enable_dhcp,
            is_connected=is_connected,
            marketplace_offering_uuid=marketplace_offering_uuid,
            marketplace_offering_name=marketplace_offering_name,
            marketplace_offering_plugin_options=marketplace_offering_plugin_options,
            marketplace_category_uuid=marketplace_category_uuid,
            marketplace_category_name=marketplace_category_name,
            marketplace_resource_uuid=marketplace_resource_uuid,
            marketplace_plan_uuid=marketplace_plan_uuid,
            marketplace_resource_state=marketplace_resource_state,
            is_usage_based=is_usage_based,
            is_limit_based=is_limit_based,
            description=description,
            cidr=cidr,
            gateway_ip=gateway_ip,
            disable_gateway=disable_gateway,
            dns_nameservers=dns_nameservers,
            host_routes=host_routes,
        )

        open_stack_sub_net.additional_properties = d
        return open_stack_sub_net

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
