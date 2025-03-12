from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.open_stack_port import OpenStackPort
from ...models.openstack_ports_list_field_item import OpenstackPortsListFieldItem
from ...models.openstack_ports_list_o_item import OpenstackPortsListOItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    field: Union[Unset, list[OpenstackPortsListFieldItem]] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    o: Union[Unset, list[OpenstackPortsListOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    tenant: Union[Unset, str] = UNSET,
    tenant_uuid: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_field: Union[Unset, list[str]] = UNSET
    if not isinstance(field, Unset):
        json_field = []
        for field_item_data in field:
            field_item = field_item_data.value
            json_field.append(field_item)

    params["field"] = json_field

    params["name"] = name

    params["name_exact"] = name_exact

    json_o: Union[Unset, list[str]] = UNSET
    if not isinstance(o, Unset):
        json_o = []
        for o_item_data in o:
            o_item = o_item_data.value
            json_o.append(o_item)

    params["o"] = json_o

    params["page"] = page

    params["page_size"] = page_size

    params["tenant"] = tenant

    json_tenant_uuid: Union[Unset, str] = UNSET
    if not isinstance(tenant_uuid, Unset):
        json_tenant_uuid = str(tenant_uuid)
    params["tenant_uuid"] = json_tenant_uuid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/openstack-ports/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["OpenStackPort"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_paginated_open_stack_port_list_item_data in _response_200:
            componentsschemas_paginated_open_stack_port_list_item = OpenStackPort.from_dict(
                componentsschemas_paginated_open_stack_port_list_item_data
            )

            response_200.append(componentsschemas_paginated_open_stack_port_list_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["OpenStackPort"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    field: Union[Unset, list[OpenstackPortsListFieldItem]] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    o: Union[Unset, list[OpenstackPortsListOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    tenant: Union[Unset, str] = UNSET,
    tenant_uuid: Union[Unset, UUID] = UNSET,
) -> Response[list["OpenStackPort"]]:
    """
    Args:
        field (Union[Unset, list[OpenstackPortsListFieldItem]]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        o (Union[Unset, list[OpenstackPortsListOItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        tenant (Union[Unset, str]):
        tenant_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['OpenStackPort']]
    """

    kwargs = _get_kwargs(
        field=field,
        name=name,
        name_exact=name_exact,
        o=o,
        page=page,
        page_size=page_size,
        tenant=tenant,
        tenant_uuid=tenant_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    field: Union[Unset, list[OpenstackPortsListFieldItem]] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    o: Union[Unset, list[OpenstackPortsListOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    tenant: Union[Unset, str] = UNSET,
    tenant_uuid: Union[Unset, UUID] = UNSET,
) -> Optional[list["OpenStackPort"]]:
    """
    Args:
        field (Union[Unset, list[OpenstackPortsListFieldItem]]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        o (Union[Unset, list[OpenstackPortsListOItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        tenant (Union[Unset, str]):
        tenant_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['OpenStackPort']
    """

    return sync_detailed(
        client=client,
        field=field,
        name=name,
        name_exact=name_exact,
        o=o,
        page=page,
        page_size=page_size,
        tenant=tenant,
        tenant_uuid=tenant_uuid,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    field: Union[Unset, list[OpenstackPortsListFieldItem]] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    o: Union[Unset, list[OpenstackPortsListOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    tenant: Union[Unset, str] = UNSET,
    tenant_uuid: Union[Unset, UUID] = UNSET,
) -> Response[list["OpenStackPort"]]:
    """
    Args:
        field (Union[Unset, list[OpenstackPortsListFieldItem]]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        o (Union[Unset, list[OpenstackPortsListOItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        tenant (Union[Unset, str]):
        tenant_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['OpenStackPort']]
    """

    kwargs = _get_kwargs(
        field=field,
        name=name,
        name_exact=name_exact,
        o=o,
        page=page,
        page_size=page_size,
        tenant=tenant,
        tenant_uuid=tenant_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    field: Union[Unset, list[OpenstackPortsListFieldItem]] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    o: Union[Unset, list[OpenstackPortsListOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    tenant: Union[Unset, str] = UNSET,
    tenant_uuid: Union[Unset, UUID] = UNSET,
) -> Optional[list["OpenStackPort"]]:
    """
    Args:
        field (Union[Unset, list[OpenstackPortsListFieldItem]]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        o (Union[Unset, list[OpenstackPortsListOItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        tenant (Union[Unset, str]):
        tenant_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['OpenStackPort']
    """

    return (
        await asyncio_detailed(
            client=client,
            field=field,
            name=name,
            name_exact=name_exact,
            o=o,
            page=page,
            page_size=page_size,
            tenant=tenant,
            tenant_uuid=tenant_uuid,
        )
    ).parsed
