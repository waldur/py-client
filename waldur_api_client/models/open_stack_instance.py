import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.core_states import CoreStates
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_stack_instance_marketplace_offering_plugin_options import (
        OpenStackInstanceMarketplaceOfferingPluginOptions,
    )
    from ..models.open_stack_nested_floating_ip import OpenStackNestedFloatingIP
    from ..models.open_stack_nested_port import OpenStackNestedPort
    from ..models.open_stack_nested_security_group import OpenStackNestedSecurityGroup
    from ..models.open_stack_nested_server_group import OpenStackNestedServerGroup
    from ..models.open_stack_nested_volume import OpenStackNestedVolume
    from ..models.rancher_cluster_reference import RancherClusterReference


T = TypeVar("T", bound="OpenStackInstance")


@_attrs_define
class OpenStackInstance:
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
        flavor_disk (int): Flavor disk size in MiB
        flavor_name (str):
        volumes (list['OpenStackNestedVolume']):
        ports (list['OpenStackNestedPort']):
        availability_zone_name (str):
        runtime_state (str):
        action (str):
        action_details (Any):
        tenant_uuid (UUID):
        hypervisor_hostname (str):
        tenant (str):
        external_address (list[str]):
        rancher_cluster (RancherClusterReference):
        marketplace_offering_uuid (str):
        marketplace_offering_name (str):
        marketplace_offering_plugin_options (OpenStackInstanceMarketplaceOfferingPluginOptions):
        marketplace_category_uuid (str):
        marketplace_category_name (str):
        marketplace_resource_uuid (str):
        marketplace_plan_uuid (str):
        marketplace_resource_state (str):
        is_usage_based (bool):
        is_limit_based (bool):
        description (Union[Unset, str]):
        user_data (Union[Unset, str]): Additional data that will be added to instance on provisioning
        security_groups (Union[Unset, list['OpenStackNestedSecurityGroup']]):
        server_group (Union[Unset, OpenStackNestedServerGroup]):
        floating_ips (Union[Unset, list['OpenStackNestedFloatingIP']]):
        availability_zone (Union[None, Unset, str]):
        connect_directly_to_external_network (Union[Unset, bool]):
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
    flavor_disk: int
    flavor_name: str
    volumes: list["OpenStackNestedVolume"]
    ports: list["OpenStackNestedPort"]
    availability_zone_name: str
    runtime_state: str
    action: str
    action_details: Any
    tenant_uuid: UUID
    hypervisor_hostname: str
    tenant: str
    external_address: list[str]
    rancher_cluster: "RancherClusterReference"
    marketplace_offering_uuid: str
    marketplace_offering_name: str
    marketplace_offering_plugin_options: "OpenStackInstanceMarketplaceOfferingPluginOptions"
    marketplace_category_uuid: str
    marketplace_category_name: str
    marketplace_resource_uuid: str
    marketplace_plan_uuid: str
    marketplace_resource_state: str
    is_usage_based: bool
    is_limit_based: bool
    description: Union[Unset, str] = UNSET
    user_data: Union[Unset, str] = UNSET
    security_groups: Union[Unset, list["OpenStackNestedSecurityGroup"]] = UNSET
    server_group: Union[Unset, "OpenStackNestedServerGroup"] = UNSET
    floating_ips: Union[Unset, list["OpenStackNestedFloatingIP"]] = UNSET
    availability_zone: Union[None, Unset, str] = UNSET
    connect_directly_to_external_network: Union[Unset, bool] = UNSET
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

        flavor_disk = self.flavor_disk

        flavor_name = self.flavor_name

        volumes = []
        for volumes_item_data in self.volumes:
            volumes_item = volumes_item_data.to_dict()
            volumes.append(volumes_item)

        ports = []
        for ports_item_data in self.ports:
            ports_item = ports_item_data.to_dict()
            ports.append(ports_item)

        availability_zone_name = self.availability_zone_name

        runtime_state = self.runtime_state

        action = self.action

        action_details = self.action_details

        tenant_uuid = str(self.tenant_uuid)

        hypervisor_hostname = self.hypervisor_hostname

        tenant = self.tenant

        external_address = self.external_address

        rancher_cluster = self.rancher_cluster.to_dict()

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

        security_groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.security_groups, Unset):
            security_groups = []
            for security_groups_item_data in self.security_groups:
                security_groups_item = security_groups_item_data.to_dict()
                security_groups.append(security_groups_item)

        server_group: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.server_group, Unset):
            server_group = self.server_group.to_dict()

        floating_ips: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.floating_ips, Unset):
            floating_ips = []
            for floating_ips_item_data in self.floating_ips:
                floating_ips_item = floating_ips_item_data.to_dict()
                floating_ips.append(floating_ips_item)

        availability_zone: Union[None, Unset, str]
        if isinstance(self.availability_zone, Unset):
            availability_zone = UNSET
        else:
            availability_zone = self.availability_zone

        connect_directly_to_external_network = self.connect_directly_to_external_network

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
                "flavor_disk": flavor_disk,
                "flavor_name": flavor_name,
                "volumes": volumes,
                "ports": ports,
                "availability_zone_name": availability_zone_name,
                "runtime_state": runtime_state,
                "action": action,
                "action_details": action_details,
                "tenant_uuid": tenant_uuid,
                "hypervisor_hostname": hypervisor_hostname,
                "tenant": tenant,
                "external_address": external_address,
                "rancher_cluster": rancher_cluster,
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
        if security_groups is not UNSET:
            field_dict["security_groups"] = security_groups
        if server_group is not UNSET:
            field_dict["server_group"] = server_group
        if floating_ips is not UNSET:
            field_dict["floating_ips"] = floating_ips
        if availability_zone is not UNSET:
            field_dict["availability_zone"] = availability_zone
        if connect_directly_to_external_network is not UNSET:
            field_dict["connect_directly_to_external_network"] = connect_directly_to_external_network

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.open_stack_instance_marketplace_offering_plugin_options import (
            OpenStackInstanceMarketplaceOfferingPluginOptions,
        )
        from ..models.open_stack_nested_floating_ip import OpenStackNestedFloatingIP
        from ..models.open_stack_nested_port import OpenStackNestedPort
        from ..models.open_stack_nested_security_group import OpenStackNestedSecurityGroup
        from ..models.open_stack_nested_server_group import OpenStackNestedServerGroup
        from ..models.open_stack_nested_volume import OpenStackNestedVolume
        from ..models.rancher_cluster_reference import RancherClusterReference

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

        flavor_disk = d.pop("flavor_disk")

        flavor_name = d.pop("flavor_name")

        volumes = []
        _volumes = d.pop("volumes")
        for volumes_item_data in _volumes:
            volumes_item = OpenStackNestedVolume.from_dict(volumes_item_data)

            volumes.append(volumes_item)

        ports = []
        _ports = d.pop("ports")
        for ports_item_data in _ports:
            ports_item = OpenStackNestedPort.from_dict(ports_item_data)

            ports.append(ports_item)

        availability_zone_name = d.pop("availability_zone_name")

        runtime_state = d.pop("runtime_state")

        action = d.pop("action")

        action_details = d.pop("action_details")

        tenant_uuid = UUID(d.pop("tenant_uuid"))

        hypervisor_hostname = d.pop("hypervisor_hostname")

        tenant = d.pop("tenant")

        external_address = cast(list[str], d.pop("external_address"))

        rancher_cluster = RancherClusterReference.from_dict(d.pop("rancher_cluster"))

        marketplace_offering_uuid = d.pop("marketplace_offering_uuid")

        marketplace_offering_name = d.pop("marketplace_offering_name")

        marketplace_offering_plugin_options = OpenStackInstanceMarketplaceOfferingPluginOptions.from_dict(
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

        security_groups = []
        _security_groups = d.pop("security_groups", UNSET)
        for security_groups_item_data in _security_groups or []:
            security_groups_item = OpenStackNestedSecurityGroup.from_dict(security_groups_item_data)

            security_groups.append(security_groups_item)

        _server_group = d.pop("server_group", UNSET)
        server_group: Union[Unset, OpenStackNestedServerGroup]
        if isinstance(_server_group, Unset):
            server_group = UNSET
        else:
            server_group = OpenStackNestedServerGroup.from_dict(_server_group)

        floating_ips = []
        _floating_ips = d.pop("floating_ips", UNSET)
        for floating_ips_item_data in _floating_ips or []:
            floating_ips_item = OpenStackNestedFloatingIP.from_dict(floating_ips_item_data)

            floating_ips.append(floating_ips_item)

        def _parse_availability_zone(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        availability_zone = _parse_availability_zone(d.pop("availability_zone", UNSET))

        connect_directly_to_external_network = d.pop("connect_directly_to_external_network", UNSET)

        open_stack_instance = cls(
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
            flavor_disk=flavor_disk,
            flavor_name=flavor_name,
            volumes=volumes,
            ports=ports,
            availability_zone_name=availability_zone_name,
            runtime_state=runtime_state,
            action=action,
            action_details=action_details,
            tenant_uuid=tenant_uuid,
            hypervisor_hostname=hypervisor_hostname,
            tenant=tenant,
            external_address=external_address,
            rancher_cluster=rancher_cluster,
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
            security_groups=security_groups,
            server_group=server_group,
            floating_ips=floating_ips,
            availability_zone=availability_zone,
            connect_directly_to_external_network=connect_directly_to_external_network,
        )

        open_stack_instance.additional_properties = d
        return open_stack_instance

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
