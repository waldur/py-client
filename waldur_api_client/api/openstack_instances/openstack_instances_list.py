from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.open_stack_instance import OpenStackInstance
from ...models.openstack_instances_list_field_item import OpenstackInstancesListFieldItem
from ...models.openstack_instances_list_state_item import OpenstackInstancesListStateItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    attach_volume_uuid: Union[Unset, UUID] = UNSET,
    availability_zone_name: Union[Unset, str] = UNSET,
    backend_id: Union[Unset, str] = UNSET,
    can_manage: Union[Unset, bool] = UNSET,
    customer: Union[Unset, UUID] = UNSET,
    customer_abbreviation: Union[Unset, str] = UNSET,
    customer_name: Union[Unset, str] = UNSET,
    customer_native_name: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    description: Union[Unset, str] = UNSET,
    external_ip: Union[Unset, str] = UNSET,
    field: Union[Unset, list[OpenstackInstancesListFieldItem]] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    project: Union[Unset, UUID] = UNSET,
    project_name: Union[Unset, str] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    runtime_state: Union[Unset, str] = UNSET,
    service_settings_name: Union[Unset, str] = UNSET,
    service_settings_uuid: Union[Unset, UUID] = UNSET,
    state: Union[Unset, list[OpenstackInstancesListStateItem]] = UNSET,
    tenant: Union[Unset, str] = UNSET,
    tenant_uuid: Union[Unset, UUID] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_attach_volume_uuid: Union[Unset, str] = UNSET
    if not isinstance(attach_volume_uuid, Unset):
        json_attach_volume_uuid = str(attach_volume_uuid)
    params["attach_volume_uuid"] = json_attach_volume_uuid

    params["availability_zone_name"] = availability_zone_name

    params["backend_id"] = backend_id

    params["can_manage"] = can_manage

    json_customer: Union[Unset, str] = UNSET
    if not isinstance(customer, Unset):
        json_customer = str(customer)
    params["customer"] = json_customer

    params["customer_abbreviation"] = customer_abbreviation

    params["customer_name"] = customer_name

    params["customer_native_name"] = customer_native_name

    json_customer_uuid: Union[Unset, str] = UNSET
    if not isinstance(customer_uuid, Unset):
        json_customer_uuid = str(customer_uuid)
    params["customer_uuid"] = json_customer_uuid

    params["description"] = description

    params["external_ip"] = external_ip

    json_field: Union[Unset, list[str]] = UNSET
    if not isinstance(field, Unset):
        json_field = []
        for field_item_data in field:
            field_item = field_item_data.value
            json_field.append(field_item)

    params["field"] = json_field

    params["name"] = name

    params["name_exact"] = name_exact

    params["page"] = page

    params["page_size"] = page_size

    json_project: Union[Unset, str] = UNSET
    if not isinstance(project, Unset):
        json_project = str(project)
    params["project"] = json_project

    params["project_name"] = project_name

    json_project_uuid: Union[Unset, str] = UNSET
    if not isinstance(project_uuid, Unset):
        json_project_uuid = str(project_uuid)
    params["project_uuid"] = json_project_uuid

    params["runtime_state"] = runtime_state

    params["service_settings_name"] = service_settings_name

    json_service_settings_uuid: Union[Unset, str] = UNSET
    if not isinstance(service_settings_uuid, Unset):
        json_service_settings_uuid = str(service_settings_uuid)
    params["service_settings_uuid"] = json_service_settings_uuid

    json_state: Union[Unset, list[str]] = UNSET
    if not isinstance(state, Unset):
        json_state = []
        for state_item_data in state:
            state_item = state_item_data.value
            json_state.append(state_item)

    params["state"] = json_state

    params["tenant"] = tenant

    json_tenant_uuid: Union[Unset, str] = UNSET
    if not isinstance(tenant_uuid, Unset):
        json_tenant_uuid = str(tenant_uuid)
    params["tenant_uuid"] = json_tenant_uuid

    json_uuid: Union[Unset, str] = UNSET
    if not isinstance(uuid, Unset):
        json_uuid = str(uuid)
    params["uuid"] = json_uuid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/openstack-instances/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["OpenStackInstance"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = OpenStackInstance.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["OpenStackInstance"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    attach_volume_uuid: Union[Unset, UUID] = UNSET,
    availability_zone_name: Union[Unset, str] = UNSET,
    backend_id: Union[Unset, str] = UNSET,
    can_manage: Union[Unset, bool] = UNSET,
    customer: Union[Unset, UUID] = UNSET,
    customer_abbreviation: Union[Unset, str] = UNSET,
    customer_name: Union[Unset, str] = UNSET,
    customer_native_name: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    description: Union[Unset, str] = UNSET,
    external_ip: Union[Unset, str] = UNSET,
    field: Union[Unset, list[OpenstackInstancesListFieldItem]] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    project: Union[Unset, UUID] = UNSET,
    project_name: Union[Unset, str] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    runtime_state: Union[Unset, str] = UNSET,
    service_settings_name: Union[Unset, str] = UNSET,
    service_settings_uuid: Union[Unset, UUID] = UNSET,
    state: Union[Unset, list[OpenstackInstancesListStateItem]] = UNSET,
    tenant: Union[Unset, str] = UNSET,
    tenant_uuid: Union[Unset, UUID] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
) -> Response[list["OpenStackInstance"]]:
    """
    Args:
        attach_volume_uuid (Union[Unset, UUID]):
        availability_zone_name (Union[Unset, str]):
        backend_id (Union[Unset, str]):
        can_manage (Union[Unset, bool]):
        customer (Union[Unset, UUID]):
        customer_abbreviation (Union[Unset, str]):
        customer_name (Union[Unset, str]):
        customer_native_name (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        description (Union[Unset, str]):
        external_ip (Union[Unset, str]):
        field (Union[Unset, list[OpenstackInstancesListFieldItem]]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        project (Union[Unset, UUID]):
        project_name (Union[Unset, str]):
        project_uuid (Union[Unset, UUID]):
        runtime_state (Union[Unset, str]):
        service_settings_name (Union[Unset, str]):
        service_settings_uuid (Union[Unset, UUID]):
        state (Union[Unset, list[OpenstackInstancesListStateItem]]):
        tenant (Union[Unset, str]):
        tenant_uuid (Union[Unset, UUID]):
        uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['OpenStackInstance']]
    """

    kwargs = _get_kwargs(
        attach_volume_uuid=attach_volume_uuid,
        availability_zone_name=availability_zone_name,
        backend_id=backend_id,
        can_manage=can_manage,
        customer=customer,
        customer_abbreviation=customer_abbreviation,
        customer_name=customer_name,
        customer_native_name=customer_native_name,
        customer_uuid=customer_uuid,
        description=description,
        external_ip=external_ip,
        field=field,
        name=name,
        name_exact=name_exact,
        page=page,
        page_size=page_size,
        project=project,
        project_name=project_name,
        project_uuid=project_uuid,
        runtime_state=runtime_state,
        service_settings_name=service_settings_name,
        service_settings_uuid=service_settings_uuid,
        state=state,
        tenant=tenant,
        tenant_uuid=tenant_uuid,
        uuid=uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    attach_volume_uuid: Union[Unset, UUID] = UNSET,
    availability_zone_name: Union[Unset, str] = UNSET,
    backend_id: Union[Unset, str] = UNSET,
    can_manage: Union[Unset, bool] = UNSET,
    customer: Union[Unset, UUID] = UNSET,
    customer_abbreviation: Union[Unset, str] = UNSET,
    customer_name: Union[Unset, str] = UNSET,
    customer_native_name: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    description: Union[Unset, str] = UNSET,
    external_ip: Union[Unset, str] = UNSET,
    field: Union[Unset, list[OpenstackInstancesListFieldItem]] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    project: Union[Unset, UUID] = UNSET,
    project_name: Union[Unset, str] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    runtime_state: Union[Unset, str] = UNSET,
    service_settings_name: Union[Unset, str] = UNSET,
    service_settings_uuid: Union[Unset, UUID] = UNSET,
    state: Union[Unset, list[OpenstackInstancesListStateItem]] = UNSET,
    tenant: Union[Unset, str] = UNSET,
    tenant_uuid: Union[Unset, UUID] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
) -> Optional[list["OpenStackInstance"]]:
    """
    Args:
        attach_volume_uuid (Union[Unset, UUID]):
        availability_zone_name (Union[Unset, str]):
        backend_id (Union[Unset, str]):
        can_manage (Union[Unset, bool]):
        customer (Union[Unset, UUID]):
        customer_abbreviation (Union[Unset, str]):
        customer_name (Union[Unset, str]):
        customer_native_name (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        description (Union[Unset, str]):
        external_ip (Union[Unset, str]):
        field (Union[Unset, list[OpenstackInstancesListFieldItem]]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        project (Union[Unset, UUID]):
        project_name (Union[Unset, str]):
        project_uuid (Union[Unset, UUID]):
        runtime_state (Union[Unset, str]):
        service_settings_name (Union[Unset, str]):
        service_settings_uuid (Union[Unset, UUID]):
        state (Union[Unset, list[OpenstackInstancesListStateItem]]):
        tenant (Union[Unset, str]):
        tenant_uuid (Union[Unset, UUID]):
        uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['OpenStackInstance']
    """

    return sync_detailed(
        client=client,
        attach_volume_uuid=attach_volume_uuid,
        availability_zone_name=availability_zone_name,
        backend_id=backend_id,
        can_manage=can_manage,
        customer=customer,
        customer_abbreviation=customer_abbreviation,
        customer_name=customer_name,
        customer_native_name=customer_native_name,
        customer_uuid=customer_uuid,
        description=description,
        external_ip=external_ip,
        field=field,
        name=name,
        name_exact=name_exact,
        page=page,
        page_size=page_size,
        project=project,
        project_name=project_name,
        project_uuid=project_uuid,
        runtime_state=runtime_state,
        service_settings_name=service_settings_name,
        service_settings_uuid=service_settings_uuid,
        state=state,
        tenant=tenant,
        tenant_uuid=tenant_uuid,
        uuid=uuid,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    attach_volume_uuid: Union[Unset, UUID] = UNSET,
    availability_zone_name: Union[Unset, str] = UNSET,
    backend_id: Union[Unset, str] = UNSET,
    can_manage: Union[Unset, bool] = UNSET,
    customer: Union[Unset, UUID] = UNSET,
    customer_abbreviation: Union[Unset, str] = UNSET,
    customer_name: Union[Unset, str] = UNSET,
    customer_native_name: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    description: Union[Unset, str] = UNSET,
    external_ip: Union[Unset, str] = UNSET,
    field: Union[Unset, list[OpenstackInstancesListFieldItem]] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    project: Union[Unset, UUID] = UNSET,
    project_name: Union[Unset, str] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    runtime_state: Union[Unset, str] = UNSET,
    service_settings_name: Union[Unset, str] = UNSET,
    service_settings_uuid: Union[Unset, UUID] = UNSET,
    state: Union[Unset, list[OpenstackInstancesListStateItem]] = UNSET,
    tenant: Union[Unset, str] = UNSET,
    tenant_uuid: Union[Unset, UUID] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
) -> Response[list["OpenStackInstance"]]:
    """
    Args:
        attach_volume_uuid (Union[Unset, UUID]):
        availability_zone_name (Union[Unset, str]):
        backend_id (Union[Unset, str]):
        can_manage (Union[Unset, bool]):
        customer (Union[Unset, UUID]):
        customer_abbreviation (Union[Unset, str]):
        customer_name (Union[Unset, str]):
        customer_native_name (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        description (Union[Unset, str]):
        external_ip (Union[Unset, str]):
        field (Union[Unset, list[OpenstackInstancesListFieldItem]]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        project (Union[Unset, UUID]):
        project_name (Union[Unset, str]):
        project_uuid (Union[Unset, UUID]):
        runtime_state (Union[Unset, str]):
        service_settings_name (Union[Unset, str]):
        service_settings_uuid (Union[Unset, UUID]):
        state (Union[Unset, list[OpenstackInstancesListStateItem]]):
        tenant (Union[Unset, str]):
        tenant_uuid (Union[Unset, UUID]):
        uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['OpenStackInstance']]
    """

    kwargs = _get_kwargs(
        attach_volume_uuid=attach_volume_uuid,
        availability_zone_name=availability_zone_name,
        backend_id=backend_id,
        can_manage=can_manage,
        customer=customer,
        customer_abbreviation=customer_abbreviation,
        customer_name=customer_name,
        customer_native_name=customer_native_name,
        customer_uuid=customer_uuid,
        description=description,
        external_ip=external_ip,
        field=field,
        name=name,
        name_exact=name_exact,
        page=page,
        page_size=page_size,
        project=project,
        project_name=project_name,
        project_uuid=project_uuid,
        runtime_state=runtime_state,
        service_settings_name=service_settings_name,
        service_settings_uuid=service_settings_uuid,
        state=state,
        tenant=tenant,
        tenant_uuid=tenant_uuid,
        uuid=uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    attach_volume_uuid: Union[Unset, UUID] = UNSET,
    availability_zone_name: Union[Unset, str] = UNSET,
    backend_id: Union[Unset, str] = UNSET,
    can_manage: Union[Unset, bool] = UNSET,
    customer: Union[Unset, UUID] = UNSET,
    customer_abbreviation: Union[Unset, str] = UNSET,
    customer_name: Union[Unset, str] = UNSET,
    customer_native_name: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    description: Union[Unset, str] = UNSET,
    external_ip: Union[Unset, str] = UNSET,
    field: Union[Unset, list[OpenstackInstancesListFieldItem]] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    project: Union[Unset, UUID] = UNSET,
    project_name: Union[Unset, str] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    runtime_state: Union[Unset, str] = UNSET,
    service_settings_name: Union[Unset, str] = UNSET,
    service_settings_uuid: Union[Unset, UUID] = UNSET,
    state: Union[Unset, list[OpenstackInstancesListStateItem]] = UNSET,
    tenant: Union[Unset, str] = UNSET,
    tenant_uuid: Union[Unset, UUID] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
) -> Optional[list["OpenStackInstance"]]:
    """
    Args:
        attach_volume_uuid (Union[Unset, UUID]):
        availability_zone_name (Union[Unset, str]):
        backend_id (Union[Unset, str]):
        can_manage (Union[Unset, bool]):
        customer (Union[Unset, UUID]):
        customer_abbreviation (Union[Unset, str]):
        customer_name (Union[Unset, str]):
        customer_native_name (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        description (Union[Unset, str]):
        external_ip (Union[Unset, str]):
        field (Union[Unset, list[OpenstackInstancesListFieldItem]]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        project (Union[Unset, UUID]):
        project_name (Union[Unset, str]):
        project_uuid (Union[Unset, UUID]):
        runtime_state (Union[Unset, str]):
        service_settings_name (Union[Unset, str]):
        service_settings_uuid (Union[Unset, UUID]):
        state (Union[Unset, list[OpenstackInstancesListStateItem]]):
        tenant (Union[Unset, str]):
        tenant_uuid (Union[Unset, UUID]):
        uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['OpenStackInstance']
    """

    return (
        await asyncio_detailed(
            client=client,
            attach_volume_uuid=attach_volume_uuid,
            availability_zone_name=availability_zone_name,
            backend_id=backend_id,
            can_manage=can_manage,
            customer=customer,
            customer_abbreviation=customer_abbreviation,
            customer_name=customer_name,
            customer_native_name=customer_native_name,
            customer_uuid=customer_uuid,
            description=description,
            external_ip=external_ip,
            field=field,
            name=name,
            name_exact=name_exact,
            page=page,
            page_size=page_size,
            project=project,
            project_name=project_name,
            project_uuid=project_uuid,
            runtime_state=runtime_state,
            service_settings_name=service_settings_name,
            service_settings_uuid=service_settings_uuid,
            state=state,
            tenant=tenant,
            tenant_uuid=tenant_uuid,
            uuid=uuid,
        )
    ).parsed
