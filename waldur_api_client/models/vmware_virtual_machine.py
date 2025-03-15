import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.core_states import CoreStates
from ..models.guest_os_enum import GuestOsEnum
from ..models.guest_power_state_enum import GuestPowerStateEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vmware_nested_disk import VmwareNestedDisk
    from ..models.vmware_nested_port import VmwareNestedPort
    from ..models.vmware_virtual_machine_marketplace_offering_plugin_options import (
        VmwareVirtualMachineMarketplaceOfferingPluginOptions,
    )


T = TypeVar("T", bound="VmwareVirtualMachine")


@_attrs_define
class VmwareVirtualMachine:
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
        guest_os_name (str):
        disk (int): Disk size in MiB
        disks (list['VmwareNestedDisk']):
        runtime_state (str):
        template_name (str):
        cluster_name (str):
        datastore_name (str):
        folder_name (str):
        ports (list['VmwareNestedPort']):
        guest_power_state (GuestPowerStateEnum):
        tools_state (str):
        tools_installed (bool):
        marketplace_offering_uuid (str):
        marketplace_offering_name (str):
        marketplace_offering_plugin_options (VmwareVirtualMachineMarketplaceOfferingPluginOptions):
        marketplace_category_uuid (str):
        marketplace_category_name (str):
        marketplace_resource_uuid (str):
        marketplace_plan_uuid (str):
        marketplace_resource_state (str):
        is_usage_based (bool):
        is_limit_based (bool):
        description (Union[Unset, str]):
        guest_os (Union[GuestOsEnum, None, Unset]):
        cores (Union[Unset, int]): Number of cores in a VM
        cores_per_socket (Union[Unset, int]): Number of cores per socket in a VM
        ram (Union[Unset, int]): Memory size in MiB
        cluster (Union[None, Unset, str]):
        datastore (Union[None, Unset, str]):
        folder (Union[None, Unset, str]):
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
    guest_os_name: str
    disk: int
    disks: list["VmwareNestedDisk"]
    runtime_state: str
    template_name: str
    cluster_name: str
    datastore_name: str
    folder_name: str
    ports: list["VmwareNestedPort"]
    guest_power_state: GuestPowerStateEnum
    tools_state: str
    tools_installed: bool
    marketplace_offering_uuid: str
    marketplace_offering_name: str
    marketplace_offering_plugin_options: "VmwareVirtualMachineMarketplaceOfferingPluginOptions"
    marketplace_category_uuid: str
    marketplace_category_name: str
    marketplace_resource_uuid: str
    marketplace_plan_uuid: str
    marketplace_resource_state: str
    is_usage_based: bool
    is_limit_based: bool
    description: Union[Unset, str] = UNSET
    guest_os: Union[GuestOsEnum, None, Unset] = UNSET
    cores: Union[Unset, int] = UNSET
    cores_per_socket: Union[Unset, int] = UNSET
    ram: Union[Unset, int] = UNSET
    cluster: Union[None, Unset, str] = UNSET
    datastore: Union[None, Unset, str] = UNSET
    folder: Union[None, Unset, str] = UNSET
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

        guest_os_name = self.guest_os_name

        disk = self.disk

        disks = []
        for disks_item_data in self.disks:
            disks_item = disks_item_data.to_dict()
            disks.append(disks_item)

        runtime_state = self.runtime_state

        template_name = self.template_name

        cluster_name = self.cluster_name

        datastore_name = self.datastore_name

        folder_name = self.folder_name

        ports = []
        for ports_item_data in self.ports:
            ports_item = ports_item_data.to_dict()
            ports.append(ports_item)

        guest_power_state = self.guest_power_state.value

        tools_state = self.tools_state

        tools_installed = self.tools_installed

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

        guest_os: Union[None, Unset, str]
        if isinstance(self.guest_os, Unset):
            guest_os = UNSET
        elif isinstance(self.guest_os, GuestOsEnum):
            guest_os = self.guest_os.value
        else:
            guest_os = self.guest_os

        cores = self.cores

        cores_per_socket = self.cores_per_socket

        ram = self.ram

        cluster: Union[None, Unset, str]
        if isinstance(self.cluster, Unset):
            cluster = UNSET
        else:
            cluster = self.cluster

        datastore: Union[None, Unset, str]
        if isinstance(self.datastore, Unset):
            datastore = UNSET
        else:
            datastore = self.datastore

        folder: Union[None, Unset, str]
        if isinstance(self.folder, Unset):
            folder = UNSET
        else:
            folder = self.folder

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
                "guest_os_name": guest_os_name,
                "disk": disk,
                "disks": disks,
                "runtime_state": runtime_state,
                "template_name": template_name,
                "cluster_name": cluster_name,
                "datastore_name": datastore_name,
                "folder_name": folder_name,
                "ports": ports,
                "guest_power_state": guest_power_state,
                "tools_state": tools_state,
                "tools_installed": tools_installed,
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
        if guest_os is not UNSET:
            field_dict["guest_os"] = guest_os
        if cores is not UNSET:
            field_dict["cores"] = cores
        if cores_per_socket is not UNSET:
            field_dict["cores_per_socket"] = cores_per_socket
        if ram is not UNSET:
            field_dict["ram"] = ram
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if datastore is not UNSET:
            field_dict["datastore"] = datastore
        if folder is not UNSET:
            field_dict["folder"] = folder

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vmware_nested_disk import VmwareNestedDisk
        from ..models.vmware_nested_port import VmwareNestedPort
        from ..models.vmware_virtual_machine_marketplace_offering_plugin_options import (
            VmwareVirtualMachineMarketplaceOfferingPluginOptions,
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

        guest_os_name = d.pop("guest_os_name")

        disk = d.pop("disk")

        disks = []
        _disks = d.pop("disks")
        for disks_item_data in _disks:
            disks_item = VmwareNestedDisk.from_dict(disks_item_data)

            disks.append(disks_item)

        runtime_state = d.pop("runtime_state")

        template_name = d.pop("template_name")

        cluster_name = d.pop("cluster_name")

        datastore_name = d.pop("datastore_name")

        folder_name = d.pop("folder_name")

        ports = []
        _ports = d.pop("ports")
        for ports_item_data in _ports:
            ports_item = VmwareNestedPort.from_dict(ports_item_data)

            ports.append(ports_item)

        guest_power_state = GuestPowerStateEnum(d.pop("guest_power_state"))

        tools_state = d.pop("tools_state")

        tools_installed = d.pop("tools_installed")

        marketplace_offering_uuid = d.pop("marketplace_offering_uuid")

        marketplace_offering_name = d.pop("marketplace_offering_name")

        marketplace_offering_plugin_options = VmwareVirtualMachineMarketplaceOfferingPluginOptions.from_dict(
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

        def _parse_guest_os(data: object) -> Union[GuestOsEnum, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                guest_os_type_0 = GuestOsEnum(data)

                return guest_os_type_0
            except:  # noqa: E722
                pass
            return cast(Union[GuestOsEnum, None, Unset], data)

        guest_os = _parse_guest_os(d.pop("guest_os", UNSET))

        cores = d.pop("cores", UNSET)

        cores_per_socket = d.pop("cores_per_socket", UNSET)

        ram = d.pop("ram", UNSET)

        def _parse_cluster(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cluster = _parse_cluster(d.pop("cluster", UNSET))

        def _parse_datastore(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        datastore = _parse_datastore(d.pop("datastore", UNSET))

        def _parse_folder(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        folder = _parse_folder(d.pop("folder", UNSET))

        vmware_virtual_machine = cls(
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
            guest_os_name=guest_os_name,
            disk=disk,
            disks=disks,
            runtime_state=runtime_state,
            template_name=template_name,
            cluster_name=cluster_name,
            datastore_name=datastore_name,
            folder_name=folder_name,
            ports=ports,
            guest_power_state=guest_power_state,
            tools_state=tools_state,
            tools_installed=tools_installed,
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
            guest_os=guest_os,
            cores=cores,
            cores_per_socket=cores_per_socket,
            ram=ram,
            cluster=cluster,
            datastore=datastore,
            folder=folder,
        )

        vmware_virtual_machine.additional_properties = d
        return vmware_virtual_machine

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
