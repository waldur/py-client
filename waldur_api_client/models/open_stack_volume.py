import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.core_states import CoreStates
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_stack_volume_marketplace_offering_plugin_options import (
        OpenStackVolumeMarketplaceOfferingPluginOptions,
    )


T = TypeVar("T", bound="OpenStackVolume")


@_attrs_define
class OpenStackVolume:
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
        backend_id (Union[None, str]):
        access_url (Union[None, str]):
        source_snapshot (Union[None, str]):
        metadata (Any):
        image_metadata (str):
        image_name (str):
        type_name (str):
        runtime_state (str):
        availability_zone_name (str):
        device (str): Name of volume as instance device e.g. /dev/vdb.
        action (str):
        action_details (Any):
        instance (Union[None, str]):
        instance_name (str):
        instance_marketplace_uuid (UUID):
        tenant (str):
        tenant_uuid (UUID):
        marketplace_offering_uuid (str):
        marketplace_offering_name (str):
        marketplace_offering_plugin_options (OpenStackVolumeMarketplaceOfferingPluginOptions):
        marketplace_category_uuid (str):
        marketplace_category_name (str):
        marketplace_resource_uuid (str):
        marketplace_plan_uuid (str):
        marketplace_resource_state (str):
        is_usage_based (bool):
        is_limit_based (bool):
        description (Union[Unset, str]):
        size (Union[None, Unset, int]): Size in MiB
        bootable (Union[Unset, bool]):
        image (Union[None, Unset, str]):
        type_ (Union[None, Unset, str]):
        availability_zone (Union[None, Unset, str]):
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
    backend_id: Union[None, str]
    access_url: Union[None, str]
    source_snapshot: Union[None, str]
    metadata: Any
    image_metadata: str
    image_name: str
    type_name: str
    runtime_state: str
    availability_zone_name: str
    device: str
    action: str
    action_details: Any
    instance: Union[None, str]
    instance_name: str
    instance_marketplace_uuid: UUID
    tenant: str
    tenant_uuid: UUID
    marketplace_offering_uuid: str
    marketplace_offering_name: str
    marketplace_offering_plugin_options: "OpenStackVolumeMarketplaceOfferingPluginOptions"
    marketplace_category_uuid: str
    marketplace_category_name: str
    marketplace_resource_uuid: str
    marketplace_plan_uuid: str
    marketplace_resource_state: str
    is_usage_based: bool
    is_limit_based: bool
    description: Union[Unset, str] = UNSET
    size: Union[None, Unset, int] = UNSET
    bootable: Union[Unset, bool] = UNSET
    image: Union[None, Unset, str] = UNSET
    type_: Union[None, Unset, str] = UNSET
    availability_zone: Union[None, Unset, str] = UNSET
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

        backend_id: Union[None, str]
        backend_id = self.backend_id

        access_url: Union[None, str]
        access_url = self.access_url

        source_snapshot: Union[None, str]
        source_snapshot = self.source_snapshot

        metadata = self.metadata

        image_metadata = self.image_metadata

        image_name = self.image_name

        type_name = self.type_name

        runtime_state = self.runtime_state

        availability_zone_name = self.availability_zone_name

        device = self.device

        action = self.action

        action_details = self.action_details

        instance: Union[None, str]
        instance = self.instance

        instance_name = self.instance_name

        instance_marketplace_uuid = str(self.instance_marketplace_uuid)

        tenant = self.tenant

        tenant_uuid = str(self.tenant_uuid)

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

        size: Union[None, Unset, int]
        if isinstance(self.size, Unset):
            size = UNSET
        else:
            size = self.size

        bootable = self.bootable

        image: Union[None, Unset, str]
        if isinstance(self.image, Unset):
            image = UNSET
        else:
            image = self.image

        type_: Union[None, Unset, str]
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        availability_zone: Union[None, Unset, str]
        if isinstance(self.availability_zone, Unset):
            availability_zone = UNSET
        else:
            availability_zone = self.availability_zone

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
                "source_snapshot": source_snapshot,
                "metadata": metadata,
                "image_metadata": image_metadata,
                "image_name": image_name,
                "type_name": type_name,
                "runtime_state": runtime_state,
                "availability_zone_name": availability_zone_name,
                "device": device,
                "action": action,
                "action_details": action_details,
                "instance": instance,
                "instance_name": instance_name,
                "instance_marketplace_uuid": instance_marketplace_uuid,
                "tenant": tenant,
                "tenant_uuid": tenant_uuid,
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
        if size is not UNSET:
            field_dict["size"] = size
        if bootable is not UNSET:
            field_dict["bootable"] = bootable
        if image is not UNSET:
            field_dict["image"] = image
        if type_ is not UNSET:
            field_dict["type"] = type_
        if availability_zone is not UNSET:
            field_dict["availability_zone"] = availability_zone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.open_stack_volume_marketplace_offering_plugin_options import (
            OpenStackVolumeMarketplaceOfferingPluginOptions,
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

        def _parse_backend_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        backend_id = _parse_backend_id(d.pop("backend_id"))

        def _parse_access_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        access_url = _parse_access_url(d.pop("access_url"))

        def _parse_source_snapshot(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        source_snapshot = _parse_source_snapshot(d.pop("source_snapshot"))

        metadata = d.pop("metadata")

        image_metadata = d.pop("image_metadata")

        image_name = d.pop("image_name")

        type_name = d.pop("type_name")

        runtime_state = d.pop("runtime_state")

        availability_zone_name = d.pop("availability_zone_name")

        device = d.pop("device")

        action = d.pop("action")

        action_details = d.pop("action_details")

        def _parse_instance(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        instance = _parse_instance(d.pop("instance"))

        instance_name = d.pop("instance_name")

        instance_marketplace_uuid = UUID(d.pop("instance_marketplace_uuid"))

        tenant = d.pop("tenant")

        tenant_uuid = UUID(d.pop("tenant_uuid"))

        marketplace_offering_uuid = d.pop("marketplace_offering_uuid")

        marketplace_offering_name = d.pop("marketplace_offering_name")

        marketplace_offering_plugin_options = OpenStackVolumeMarketplaceOfferingPluginOptions.from_dict(
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

        def _parse_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        size = _parse_size(d.pop("size", UNSET))

        bootable = d.pop("bootable", UNSET)

        def _parse_image(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        image = _parse_image(d.pop("image", UNSET))

        def _parse_type_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_availability_zone(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        availability_zone = _parse_availability_zone(d.pop("availability_zone", UNSET))

        open_stack_volume = cls(
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
            source_snapshot=source_snapshot,
            metadata=metadata,
            image_metadata=image_metadata,
            image_name=image_name,
            type_name=type_name,
            runtime_state=runtime_state,
            availability_zone_name=availability_zone_name,
            device=device,
            action=action,
            action_details=action_details,
            instance=instance,
            instance_name=instance_name,
            instance_marketplace_uuid=instance_marketplace_uuid,
            tenant=tenant,
            tenant_uuid=tenant_uuid,
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
            size=size,
            bootable=bootable,
            image=image,
            type_=type_,
            availability_zone=availability_zone,
        )

        open_stack_volume.additional_properties = d
        return open_stack_volume

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
