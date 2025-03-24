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
    from ..models.rancher_cluster_marketplace_offering_plugin_options import (
        RancherClusterMarketplaceOfferingPluginOptions,
    )
    from ..models.rancher_nested_node import RancherNestedNode


T = TypeVar("T", bound="RancherCluster")


@_attrs_define
class RancherCluster:
    """
    Attributes:
        url (Union[Unset, str]):
        uuid (Union[Unset, UUID]):
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        service_name (Union[Unset, str]):
        service_settings (Union[Unset, str]):
        service_settings_uuid (Union[Unset, UUID]):
        service_settings_state (Union[Unset, str]):
        service_settings_error_message (Union[Unset, str]):
        project (Union[Unset, str]):
        project_name (Union[Unset, str]):
        project_uuid (Union[Unset, UUID]):
        customer (Union[Unset, str]):
        customer_name (Union[Unset, str]):
        customer_native_name (Union[Unset, str]):
        customer_abbreviation (Union[Unset, str]):
        error_message (Union[Unset, str]):
        error_traceback (Union[Unset, str]):
        resource_type (Union[Unset, str]):
        state (Union[Unset, CoreStates]):
        created (Union[Unset, datetime.datetime]):
        modified (Union[Unset, datetime.datetime]):
        backend_id (Union[Unset, str]):
        access_url (Union[None, Unset, str]):
        node_command (Union[Unset, str]): Rancher generated node installation command base.
        nodes (Union[Unset, list['RancherNestedNode']]):
        tenant (Union[Unset, str]):
        tenant_uuid (Union[Unset, UUID]):
        runtime_state (Union[Unset, str]):
        install_longhorn (Union[Unset, bool]): Longhorn is a distributed block storage deployed on top of Kubernetes
            cluster Default: False.
        management_security_group (Union[Unset, str]):
        marketplace_offering_uuid (Union[Unset, str]):
        marketplace_offering_name (Union[Unset, str]):
        marketplace_offering_plugin_options (Union[Unset, RancherClusterMarketplaceOfferingPluginOptions]):
        marketplace_category_uuid (Union[Unset, str]):
        marketplace_category_name (Union[Unset, str]):
        marketplace_resource_uuid (Union[Unset, str]):
        marketplace_plan_uuid (Union[Unset, str]):
        marketplace_resource_state (Union[Unset, str]):
        is_usage_based (Union[Unset, bool]):
        is_limit_based (Union[Unset, bool]):
    """

    url: Union[Unset, str] = UNSET
    uuid: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    service_name: Union[Unset, str] = UNSET
    service_settings: Union[Unset, str] = UNSET
    service_settings_uuid: Union[Unset, UUID] = UNSET
    service_settings_state: Union[Unset, str] = UNSET
    service_settings_error_message: Union[Unset, str] = UNSET
    project: Union[Unset, str] = UNSET
    project_name: Union[Unset, str] = UNSET
    project_uuid: Union[Unset, UUID] = UNSET
    customer: Union[Unset, str] = UNSET
    customer_name: Union[Unset, str] = UNSET
    customer_native_name: Union[Unset, str] = UNSET
    customer_abbreviation: Union[Unset, str] = UNSET
    error_message: Union[Unset, str] = UNSET
    error_traceback: Union[Unset, str] = UNSET
    resource_type: Union[Unset, str] = UNSET
    state: Union[Unset, CoreStates] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    modified: Union[Unset, datetime.datetime] = UNSET
    backend_id: Union[Unset, str] = UNSET
    access_url: Union[None, Unset, str] = UNSET
    node_command: Union[Unset, str] = UNSET
    nodes: Union[Unset, list["RancherNestedNode"]] = UNSET
    tenant: Union[Unset, str] = UNSET
    tenant_uuid: Union[Unset, UUID] = UNSET
    runtime_state: Union[Unset, str] = UNSET
    install_longhorn: Union[Unset, bool] = False
    management_security_group: Union[Unset, str] = UNSET
    marketplace_offering_uuid: Union[Unset, str] = UNSET
    marketplace_offering_name: Union[Unset, str] = UNSET
    marketplace_offering_plugin_options: Union[Unset, "RancherClusterMarketplaceOfferingPluginOptions"] = UNSET
    marketplace_category_uuid: Union[Unset, str] = UNSET
    marketplace_category_name: Union[Unset, str] = UNSET
    marketplace_resource_uuid: Union[Unset, str] = UNSET
    marketplace_plan_uuid: Union[Unset, str] = UNSET
    marketplace_resource_state: Union[Unset, str] = UNSET
    is_usage_based: Union[Unset, bool] = UNSET
    is_limit_based: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        uuid: Union[Unset, str] = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        name = self.name

        description = self.description

        service_name = self.service_name

        service_settings = self.service_settings

        service_settings_uuid: Union[Unset, str] = UNSET
        if not isinstance(self.service_settings_uuid, Unset):
            service_settings_uuid = str(self.service_settings_uuid)

        service_settings_state = self.service_settings_state

        service_settings_error_message = self.service_settings_error_message

        project = self.project

        project_name = self.project_name

        project_uuid: Union[Unset, str] = UNSET
        if not isinstance(self.project_uuid, Unset):
            project_uuid = str(self.project_uuid)

        customer = self.customer

        customer_name = self.customer_name

        customer_native_name = self.customer_native_name

        customer_abbreviation = self.customer_abbreviation

        error_message = self.error_message

        error_traceback = self.error_traceback

        resource_type = self.resource_type

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        modified: Union[Unset, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat()

        backend_id = self.backend_id

        access_url: Union[None, Unset, str]
        if isinstance(self.access_url, Unset):
            access_url = UNSET
        else:
            access_url = self.access_url

        node_command = self.node_command

        nodes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.nodes, Unset):
            nodes = []
            for nodes_item_data in self.nodes:
                nodes_item = nodes_item_data.to_dict()
                nodes.append(nodes_item)

        tenant = self.tenant

        tenant_uuid: Union[Unset, str] = UNSET
        if not isinstance(self.tenant_uuid, Unset):
            tenant_uuid = str(self.tenant_uuid)

        runtime_state = self.runtime_state

        install_longhorn = self.install_longhorn

        management_security_group = self.management_security_group

        marketplace_offering_uuid = self.marketplace_offering_uuid

        marketplace_offering_name = self.marketplace_offering_name

        marketplace_offering_plugin_options: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.marketplace_offering_plugin_options, Unset):
            marketplace_offering_plugin_options = self.marketplace_offering_plugin_options.to_dict()

        marketplace_category_uuid = self.marketplace_category_uuid

        marketplace_category_name = self.marketplace_category_name

        marketplace_resource_uuid = self.marketplace_resource_uuid

        marketplace_plan_uuid = self.marketplace_plan_uuid

        marketplace_resource_state = self.marketplace_resource_state

        is_usage_based = self.is_usage_based

        is_limit_based = self.is_limit_based

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if service_name is not UNSET:
            field_dict["service_name"] = service_name
        if service_settings is not UNSET:
            field_dict["service_settings"] = service_settings
        if service_settings_uuid is not UNSET:
            field_dict["service_settings_uuid"] = service_settings_uuid
        if service_settings_state is not UNSET:
            field_dict["service_settings_state"] = service_settings_state
        if service_settings_error_message is not UNSET:
            field_dict["service_settings_error_message"] = service_settings_error_message
        if project is not UNSET:
            field_dict["project"] = project
        if project_name is not UNSET:
            field_dict["project_name"] = project_name
        if project_uuid is not UNSET:
            field_dict["project_uuid"] = project_uuid
        if customer is not UNSET:
            field_dict["customer"] = customer
        if customer_name is not UNSET:
            field_dict["customer_name"] = customer_name
        if customer_native_name is not UNSET:
            field_dict["customer_native_name"] = customer_native_name
        if customer_abbreviation is not UNSET:
            field_dict["customer_abbreviation"] = customer_abbreviation
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if error_traceback is not UNSET:
            field_dict["error_traceback"] = error_traceback
        if resource_type is not UNSET:
            field_dict["resource_type"] = resource_type
        if state is not UNSET:
            field_dict["state"] = state
        if created is not UNSET:
            field_dict["created"] = created
        if modified is not UNSET:
            field_dict["modified"] = modified
        if backend_id is not UNSET:
            field_dict["backend_id"] = backend_id
        if access_url is not UNSET:
            field_dict["access_url"] = access_url
        if node_command is not UNSET:
            field_dict["node_command"] = node_command
        if nodes is not UNSET:
            field_dict["nodes"] = nodes
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if tenant_uuid is not UNSET:
            field_dict["tenant_uuid"] = tenant_uuid
        if runtime_state is not UNSET:
            field_dict["runtime_state"] = runtime_state
        if install_longhorn is not UNSET:
            field_dict["install_longhorn"] = install_longhorn
        if management_security_group is not UNSET:
            field_dict["management_security_group"] = management_security_group
        if marketplace_offering_uuid is not UNSET:
            field_dict["marketplace_offering_uuid"] = marketplace_offering_uuid
        if marketplace_offering_name is not UNSET:
            field_dict["marketplace_offering_name"] = marketplace_offering_name
        if marketplace_offering_plugin_options is not UNSET:
            field_dict["marketplace_offering_plugin_options"] = marketplace_offering_plugin_options
        if marketplace_category_uuid is not UNSET:
            field_dict["marketplace_category_uuid"] = marketplace_category_uuid
        if marketplace_category_name is not UNSET:
            field_dict["marketplace_category_name"] = marketplace_category_name
        if marketplace_resource_uuid is not UNSET:
            field_dict["marketplace_resource_uuid"] = marketplace_resource_uuid
        if marketplace_plan_uuid is not UNSET:
            field_dict["marketplace_plan_uuid"] = marketplace_plan_uuid
        if marketplace_resource_state is not UNSET:
            field_dict["marketplace_resource_state"] = marketplace_resource_state
        if is_usage_based is not UNSET:
            field_dict["is_usage_based"] = is_usage_based
        if is_limit_based is not UNSET:
            field_dict["is_limit_based"] = is_limit_based

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rancher_cluster_marketplace_offering_plugin_options import (
            RancherClusterMarketplaceOfferingPluginOptions,
        )
        from ..models.rancher_nested_node import RancherNestedNode

        d = dict(src_dict)
        url = d.pop("url", UNSET)

        _uuid = d.pop("uuid", UNSET)
        uuid: Union[Unset, UUID]
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        service_name = d.pop("service_name", UNSET)

        service_settings = d.pop("service_settings", UNSET)

        _service_settings_uuid = d.pop("service_settings_uuid", UNSET)
        service_settings_uuid: Union[Unset, UUID]
        if isinstance(_service_settings_uuid, Unset):
            service_settings_uuid = UNSET
        else:
            service_settings_uuid = UUID(_service_settings_uuid)

        service_settings_state = d.pop("service_settings_state", UNSET)

        service_settings_error_message = d.pop("service_settings_error_message", UNSET)

        project = d.pop("project", UNSET)

        project_name = d.pop("project_name", UNSET)

        _project_uuid = d.pop("project_uuid", UNSET)
        project_uuid: Union[Unset, UUID]
        if isinstance(_project_uuid, Unset):
            project_uuid = UNSET
        else:
            project_uuid = UUID(_project_uuid)

        customer = d.pop("customer", UNSET)

        customer_name = d.pop("customer_name", UNSET)

        customer_native_name = d.pop("customer_native_name", UNSET)

        customer_abbreviation = d.pop("customer_abbreviation", UNSET)

        error_message = d.pop("error_message", UNSET)

        error_traceback = d.pop("error_traceback", UNSET)

        resource_type = d.pop("resource_type", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, CoreStates]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = CoreStates(_state)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _modified = d.pop("modified", UNSET)
        modified: Union[Unset, datetime.datetime]
        if isinstance(_modified, Unset):
            modified = UNSET
        else:
            modified = isoparse(_modified)

        backend_id = d.pop("backend_id", UNSET)

        def _parse_access_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        access_url = _parse_access_url(d.pop("access_url", UNSET))

        node_command = d.pop("node_command", UNSET)

        nodes = []
        _nodes = d.pop("nodes", UNSET)
        for nodes_item_data in _nodes or []:
            nodes_item = RancherNestedNode.from_dict(nodes_item_data)

            nodes.append(nodes_item)

        tenant = d.pop("tenant", UNSET)

        _tenant_uuid = d.pop("tenant_uuid", UNSET)
        tenant_uuid: Union[Unset, UUID]
        if isinstance(_tenant_uuid, Unset):
            tenant_uuid = UNSET
        else:
            tenant_uuid = UUID(_tenant_uuid)

        runtime_state = d.pop("runtime_state", UNSET)

        install_longhorn = d.pop("install_longhorn", UNSET)

        management_security_group = d.pop("management_security_group", UNSET)

        marketplace_offering_uuid = d.pop("marketplace_offering_uuid", UNSET)

        marketplace_offering_name = d.pop("marketplace_offering_name", UNSET)

        _marketplace_offering_plugin_options = d.pop("marketplace_offering_plugin_options", UNSET)
        marketplace_offering_plugin_options: Union[Unset, RancherClusterMarketplaceOfferingPluginOptions]
        if isinstance(_marketplace_offering_plugin_options, Unset):
            marketplace_offering_plugin_options = UNSET
        else:
            marketplace_offering_plugin_options = RancherClusterMarketplaceOfferingPluginOptions.from_dict(
                _marketplace_offering_plugin_options
            )

        marketplace_category_uuid = d.pop("marketplace_category_uuid", UNSET)

        marketplace_category_name = d.pop("marketplace_category_name", UNSET)

        marketplace_resource_uuid = d.pop("marketplace_resource_uuid", UNSET)

        marketplace_plan_uuid = d.pop("marketplace_plan_uuid", UNSET)

        marketplace_resource_state = d.pop("marketplace_resource_state", UNSET)

        is_usage_based = d.pop("is_usage_based", UNSET)

        is_limit_based = d.pop("is_limit_based", UNSET)

        rancher_cluster = cls(
            url=url,
            uuid=uuid,
            name=name,
            description=description,
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
            node_command=node_command,
            nodes=nodes,
            tenant=tenant,
            tenant_uuid=tenant_uuid,
            runtime_state=runtime_state,
            install_longhorn=install_longhorn,
            management_security_group=management_security_group,
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
        )

        rancher_cluster.additional_properties = d
        return rancher_cluster

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
