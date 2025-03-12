import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.core_states import CoreStates
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.azure_virtual_machine_marketplace_offering_plugin_options import (
        AzureVirtualMachineMarketplaceOfferingPluginOptions,
    )


T = TypeVar("T", bound="AzureVirtualMachine")


@_attrs_define
class AzureVirtualMachine:
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
        start_time (Union[None, datetime.datetime]):
        cores (int): Number of cores in a VM
        ram (int): Memory size in MiB
        disk (int): Disk size in MiB
        min_ram (int): Minimum memory size in MiB
        min_disk (int): Minimum disk size in MiB
        external_ips (list[str]):
        internal_ips (list[str]):
        latitude (Union[None, float]):
        longitude (Union[None, float]):
        key_name (str):
        key_fingerprint (str):
        image_name (str):
        image (str):
        size (str):
        runtime_state (str):
        resource_group (str):
        username (str):
        password (str):
        resource_group_name (str):
        location_name (str):
        size_name (str):
        marketplace_offering_uuid (str):
        marketplace_offering_name (str):
        marketplace_offering_plugin_options (AzureVirtualMachineMarketplaceOfferingPluginOptions):
        marketplace_category_uuid (str):
        marketplace_category_name (str):
        marketplace_resource_uuid (str):
        marketplace_plan_uuid (str):
        marketplace_resource_state (str):
        is_usage_based (bool):
        is_limit_based (bool):
        description (Union[Unset, str]):
        user_data (Union[Unset, str]): Additional data that will be added to instance on provisioning
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
    start_time: Union[None, datetime.datetime]
    cores: int
    ram: int
    disk: int
    min_ram: int
    min_disk: int
    external_ips: list[str]
    internal_ips: list[str]
    latitude: Union[None, float]
    longitude: Union[None, float]
    key_name: str
    key_fingerprint: str
    image_name: str
    image: str
    size: str
    runtime_state: str
    resource_group: str
    username: str
    password: str
    resource_group_name: str
    location_name: str
    size_name: str
    marketplace_offering_uuid: str
    marketplace_offering_name: str
    marketplace_offering_plugin_options: "AzureVirtualMachineMarketplaceOfferingPluginOptions"
    marketplace_category_uuid: str
    marketplace_category_name: str
    marketplace_resource_uuid: str
    marketplace_plan_uuid: str
    marketplace_resource_state: str
    is_usage_based: bool
    is_limit_based: bool
    description: Union[Unset, str] = UNSET
    user_data: Union[Unset, str] = UNSET
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

        start_time: Union[None, str]
        if isinstance(self.start_time, datetime.datetime):
            start_time = self.start_time.isoformat()
        else:
            start_time = self.start_time

        cores = self.cores

        ram = self.ram

        disk = self.disk

        min_ram = self.min_ram

        min_disk = self.min_disk

        external_ips = self.external_ips

        internal_ips = self.internal_ips

        latitude: Union[None, float]
        latitude = self.latitude

        longitude: Union[None, float]
        longitude = self.longitude

        key_name = self.key_name

        key_fingerprint = self.key_fingerprint

        image_name = self.image_name

        image = self.image

        size = self.size

        runtime_state = self.runtime_state

        resource_group = self.resource_group

        username = self.username

        password = self.password

        resource_group_name = self.resource_group_name

        location_name = self.location_name

        size_name = self.size_name

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

        user_data = self.user_data

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
                "start_time": start_time,
                "cores": cores,
                "ram": ram,
                "disk": disk,
                "min_ram": min_ram,
                "min_disk": min_disk,
                "external_ips": external_ips,
                "internal_ips": internal_ips,
                "latitude": latitude,
                "longitude": longitude,
                "key_name": key_name,
                "key_fingerprint": key_fingerprint,
                "image_name": image_name,
                "image": image,
                "size": size,
                "runtime_state": runtime_state,
                "resource_group": resource_group,
                "username": username,
                "password": password,
                "resource_group_name": resource_group_name,
                "location_name": location_name,
                "size_name": size_name,
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
        if user_data is not UNSET:
            field_dict["user_data"] = user_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.azure_virtual_machine_marketplace_offering_plugin_options import (
            AzureVirtualMachineMarketplaceOfferingPluginOptions,
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

        def _parse_start_time(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_time_type_0 = isoparse(data)

                return start_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        start_time = _parse_start_time(d.pop("start_time"))

        cores = d.pop("cores")

        ram = d.pop("ram")

        disk = d.pop("disk")

        min_ram = d.pop("min_ram")

        min_disk = d.pop("min_disk")

        external_ips = cast(list[str], d.pop("external_ips"))

        internal_ips = cast(list[str], d.pop("internal_ips"))

        def _parse_latitude(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        latitude = _parse_latitude(d.pop("latitude"))

        def _parse_longitude(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        longitude = _parse_longitude(d.pop("longitude"))

        key_name = d.pop("key_name")

        key_fingerprint = d.pop("key_fingerprint")

        image_name = d.pop("image_name")

        image = d.pop("image")

        size = d.pop("size")

        runtime_state = d.pop("runtime_state")

        resource_group = d.pop("resource_group")

        username = d.pop("username")

        password = d.pop("password")

        resource_group_name = d.pop("resource_group_name")

        location_name = d.pop("location_name")

        size_name = d.pop("size_name")

        marketplace_offering_uuid = d.pop("marketplace_offering_uuid")

        marketplace_offering_name = d.pop("marketplace_offering_name")

        marketplace_offering_plugin_options = AzureVirtualMachineMarketplaceOfferingPluginOptions.from_dict(
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

        user_data = d.pop("user_data", UNSET)

        azure_virtual_machine = cls(
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
            start_time=start_time,
            cores=cores,
            ram=ram,
            disk=disk,
            min_ram=min_ram,
            min_disk=min_disk,
            external_ips=external_ips,
            internal_ips=internal_ips,
            latitude=latitude,
            longitude=longitude,
            key_name=key_name,
            key_fingerprint=key_fingerprint,
            image_name=image_name,
            image=image,
            size=size,
            runtime_state=runtime_state,
            resource_group=resource_group,
            username=username,
            password=password,
            resource_group_name=resource_group_name,
            location_name=location_name,
            size_name=size_name,
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
            user_data=user_data,
        )

        azure_virtual_machine.additional_properties = d
        return azure_virtual_machine

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
