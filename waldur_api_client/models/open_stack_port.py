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
    from ..models.open_stack_allowed_address_pair import OpenStackAllowedAddressPair
    from ..models.open_stack_fixed_ip import OpenStackFixedIp
    from ..models.open_stack_port_marketplace_offering_plugin_options import (
        OpenStackPortMarketplaceOfferingPluginOptions,
    )
    from ..models.open_stack_port_nested_security_group import OpenStackPortNestedSecurityGroup


T = TypeVar("T", bound="OpenStackPort")


@_attrs_define
class OpenStackPort:
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
        allowed_address_pairs (list['OpenStackAllowedAddressPair']):
        tenant (str):
        tenant_name (str):
        tenant_uuid (UUID):
        network_name (str):
        network_uuid (UUID):
        floating_ips (list[str]):
        device_id (Union[None, str]):
        device_owner (Union[None, str]):
        port_security_enabled (bool):
        security_groups (list['OpenStackPortNestedSecurityGroup']):
        marketplace_offering_uuid (str):
        marketplace_offering_name (str):
        marketplace_offering_plugin_options (OpenStackPortMarketplaceOfferingPluginOptions):
        marketplace_category_uuid (str):
        marketplace_category_name (str):
        marketplace_resource_uuid (str):
        marketplace_plan_uuid (str):
        marketplace_resource_state (str):
        is_usage_based (bool):
        is_limit_based (bool):
        description (Union[Unset, str]):
        fixed_ips (Union[Unset, list['OpenStackFixedIp']]):
        mac_address (Union[Unset, str]):
        network (Union[None, Unset, str]):
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
    allowed_address_pairs: list["OpenStackAllowedAddressPair"]
    tenant: str
    tenant_name: str
    tenant_uuid: UUID
    network_name: str
    network_uuid: UUID
    floating_ips: list[str]
    device_id: Union[None, str]
    device_owner: Union[None, str]
    port_security_enabled: bool
    security_groups: list["OpenStackPortNestedSecurityGroup"]
    marketplace_offering_uuid: str
    marketplace_offering_name: str
    marketplace_offering_plugin_options: "OpenStackPortMarketplaceOfferingPluginOptions"
    marketplace_category_uuid: str
    marketplace_category_name: str
    marketplace_resource_uuid: str
    marketplace_plan_uuid: str
    marketplace_resource_state: str
    is_usage_based: bool
    is_limit_based: bool
    description: Union[Unset, str] = UNSET
    fixed_ips: Union[Unset, list["OpenStackFixedIp"]] = UNSET
    mac_address: Union[Unset, str] = UNSET
    network: Union[None, Unset, str] = UNSET
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

        allowed_address_pairs = []
        for allowed_address_pairs_item_data in self.allowed_address_pairs:
            allowed_address_pairs_item = allowed_address_pairs_item_data.to_dict()
            allowed_address_pairs.append(allowed_address_pairs_item)

        tenant = self.tenant

        tenant_name = self.tenant_name

        tenant_uuid = str(self.tenant_uuid)

        network_name = self.network_name

        network_uuid = str(self.network_uuid)

        floating_ips = self.floating_ips

        device_id: Union[None, str]
        device_id = self.device_id

        device_owner: Union[None, str]
        device_owner = self.device_owner

        port_security_enabled = self.port_security_enabled

        security_groups = []
        for security_groups_item_data in self.security_groups:
            security_groups_item = security_groups_item_data.to_dict()
            security_groups.append(security_groups_item)

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

        fixed_ips: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fixed_ips, Unset):
            fixed_ips = []
            for fixed_ips_item_data in self.fixed_ips:
                fixed_ips_item = fixed_ips_item_data.to_dict()
                fixed_ips.append(fixed_ips_item)

        mac_address = self.mac_address

        network: Union[None, Unset, str]
        if isinstance(self.network, Unset):
            network = UNSET
        else:
            network = self.network

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
                "allowed_address_pairs": allowed_address_pairs,
                "tenant": tenant,
                "tenant_name": tenant_name,
                "tenant_uuid": tenant_uuid,
                "network_name": network_name,
                "network_uuid": network_uuid,
                "floating_ips": floating_ips,
                "device_id": device_id,
                "device_owner": device_owner,
                "port_security_enabled": port_security_enabled,
                "security_groups": security_groups,
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
        if fixed_ips is not UNSET:
            field_dict["fixed_ips"] = fixed_ips
        if mac_address is not UNSET:
            field_dict["mac_address"] = mac_address
        if network is not UNSET:
            field_dict["network"] = network

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.open_stack_allowed_address_pair import OpenStackAllowedAddressPair
        from ..models.open_stack_fixed_ip import OpenStackFixedIp
        from ..models.open_stack_port_marketplace_offering_plugin_options import (
            OpenStackPortMarketplaceOfferingPluginOptions,
        )
        from ..models.open_stack_port_nested_security_group import OpenStackPortNestedSecurityGroup

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

        allowed_address_pairs = []
        _allowed_address_pairs = d.pop("allowed_address_pairs")
        for allowed_address_pairs_item_data in _allowed_address_pairs:
            allowed_address_pairs_item = OpenStackAllowedAddressPair.from_dict(allowed_address_pairs_item_data)

            allowed_address_pairs.append(allowed_address_pairs_item)

        tenant = d.pop("tenant")

        tenant_name = d.pop("tenant_name")

        tenant_uuid = UUID(d.pop("tenant_uuid"))

        network_name = d.pop("network_name")

        network_uuid = UUID(d.pop("network_uuid"))

        floating_ips = cast(list[str], d.pop("floating_ips"))

        def _parse_device_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        device_id = _parse_device_id(d.pop("device_id"))

        def _parse_device_owner(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        device_owner = _parse_device_owner(d.pop("device_owner"))

        port_security_enabled = d.pop("port_security_enabled")

        security_groups = []
        _security_groups = d.pop("security_groups")
        for security_groups_item_data in _security_groups:
            security_groups_item = OpenStackPortNestedSecurityGroup.from_dict(security_groups_item_data)

            security_groups.append(security_groups_item)

        marketplace_offering_uuid = d.pop("marketplace_offering_uuid")

        marketplace_offering_name = d.pop("marketplace_offering_name")

        marketplace_offering_plugin_options = OpenStackPortMarketplaceOfferingPluginOptions.from_dict(
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

        fixed_ips = []
        _fixed_ips = d.pop("fixed_ips", UNSET)
        for fixed_ips_item_data in _fixed_ips or []:
            fixed_ips_item = OpenStackFixedIp.from_dict(fixed_ips_item_data)

            fixed_ips.append(fixed_ips_item)

        mac_address = d.pop("mac_address", UNSET)

        def _parse_network(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        network = _parse_network(d.pop("network", UNSET))

        open_stack_port = cls(
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
            allowed_address_pairs=allowed_address_pairs,
            tenant=tenant,
            tenant_name=tenant_name,
            tenant_uuid=tenant_uuid,
            network_name=network_name,
            network_uuid=network_uuid,
            floating_ips=floating_ips,
            device_id=device_id,
            device_owner=device_owner,
            port_security_enabled=port_security_enabled,
            security_groups=security_groups,
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
            fixed_ips=fixed_ips,
            mac_address=mac_address,
            network=network,
        )

        open_stack_port.additional_properties = d
        return open_stack_port

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
