import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.core_states import CoreStates
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_stack_nested_sub_net import OpenStackNestedSubNet
    from ..models.open_stack_network_marketplace_offering_plugin_options import (
        OpenStackNetworkMarketplaceOfferingPluginOptions,
    )


T = TypeVar("T", bound="OpenStackNetwork")


@_attrs_define
class OpenStackNetwork:
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
        tenant_uuid (UUID):
        is_external (bool):
        type_ (str):
        subnets (list['OpenStackNestedSubNet']):
        mtu (Union[None, int]): The maximum transmission unit (MTU) value to address fragmentation.
        marketplace_offering_uuid (str):
        marketplace_offering_name (str):
        marketplace_offering_plugin_options (OpenStackNetworkMarketplaceOfferingPluginOptions):
        marketplace_category_uuid (str):
        marketplace_category_name (str):
        marketplace_resource_uuid (str):
        marketplace_plan_uuid (str):
        marketplace_resource_state (str):
        is_usage_based (bool):
        is_limit_based (bool):
        description (Union[Unset, str]):
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
    tenant_uuid: UUID
    is_external: bool
    type_: str
    subnets: list["OpenStackNestedSubNet"]
    mtu: Union[None, int]
    marketplace_offering_uuid: str
    marketplace_offering_name: str
    marketplace_offering_plugin_options: "OpenStackNetworkMarketplaceOfferingPluginOptions"
    marketplace_category_uuid: str
    marketplace_category_name: str
    marketplace_resource_uuid: str
    marketplace_plan_uuid: str
    marketplace_resource_state: str
    is_usage_based: bool
    is_limit_based: bool
    description: Union[Unset, str] = UNSET
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

        tenant_uuid = str(self.tenant_uuid)

        is_external = self.is_external

        type_ = self.type_

        subnets = []
        for subnets_item_data in self.subnets:
            subnets_item = subnets_item_data.to_dict()
            subnets.append(subnets_item)

        mtu: Union[None, int]
        mtu = self.mtu

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
                "tenant_uuid": tenant_uuid,
                "is_external": is_external,
                "type": type_,
                "subnets": subnets,
                "mtu": mtu,
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.open_stack_nested_sub_net import OpenStackNestedSubNet
        from ..models.open_stack_network_marketplace_offering_plugin_options import (
            OpenStackNetworkMarketplaceOfferingPluginOptions,
        )

        d = src_dict.copy()
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

        tenant_uuid = UUID(d.pop("tenant_uuid"))

        is_external = d.pop("is_external")

        type_ = d.pop("type")

        subnets = []
        _subnets = d.pop("subnets")
        for subnets_item_data in _subnets:
            subnets_item = OpenStackNestedSubNet.from_dict(subnets_item_data)

            subnets.append(subnets_item)

        def _parse_mtu(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        mtu = _parse_mtu(d.pop("mtu"))

        marketplace_offering_uuid = d.pop("marketplace_offering_uuid")

        marketplace_offering_name = d.pop("marketplace_offering_name")

        marketplace_offering_plugin_options = OpenStackNetworkMarketplaceOfferingPluginOptions.from_dict(
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

        open_stack_network = cls(
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
            tenant_uuid=tenant_uuid,
            is_external=is_external,
            type_=type_,
            subnets=subnets,
            mtu=mtu,
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
        )

        open_stack_network.additional_properties = d
        return open_stack_network

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
