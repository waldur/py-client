from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rancher_role_templates_list_o_item import RancherRoleTemplatesListOItem
from ...models.role_template import RoleTemplate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[RancherRoleTemplatesListOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    scope_type: Union[Unset, str] = UNSET,
    settings_uuid: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["name"] = name

    json_o: Union[Unset, list[str]] = UNSET
    if not isinstance(o, Unset):
        json_o = []
        for o_item_data in o:
            o_item = o_item_data.value
            json_o.append(o_item)

    params["o"] = json_o

    params["page"] = page

    params["page_size"] = page_size

    params["scope_type"] = scope_type

    json_settings_uuid: Union[Unset, str] = UNSET
    if not isinstance(settings_uuid, Unset):
        json_settings_uuid = str(settings_uuid)
    params["settings_uuid"] = json_settings_uuid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/rancher-role-templates/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> list["RoleTemplate"]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RoleTemplate.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["RoleTemplate"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[RancherRoleTemplatesListOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    scope_type: Union[Unset, str] = UNSET,
    settings_uuid: Union[Unset, UUID] = UNSET,
) -> Response[list["RoleTemplate"]]:
    """
    Args:
        name (Union[Unset, str]):
        o (Union[Unset, list[RancherRoleTemplatesListOItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        scope_type (Union[Unset, str]):
        settings_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['RoleTemplate']]
    """

    kwargs = _get_kwargs(
        name=name,
        o=o,
        page=page,
        page_size=page_size,
        scope_type=scope_type,
        settings_uuid=settings_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[RancherRoleTemplatesListOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    scope_type: Union[Unset, str] = UNSET,
    settings_uuid: Union[Unset, UUID] = UNSET,
) -> list["RoleTemplate"]:
    """
    Args:
        name (Union[Unset, str]):
        o (Union[Unset, list[RancherRoleTemplatesListOItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        scope_type (Union[Unset, str]):
        settings_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['RoleTemplate']
    """

    return sync_detailed(
        client=client,
        name=name,
        o=o,
        page=page,
        page_size=page_size,
        scope_type=scope_type,
        settings_uuid=settings_uuid,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[RancherRoleTemplatesListOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    scope_type: Union[Unset, str] = UNSET,
    settings_uuid: Union[Unset, UUID] = UNSET,
) -> Response[list["RoleTemplate"]]:
    """
    Args:
        name (Union[Unset, str]):
        o (Union[Unset, list[RancherRoleTemplatesListOItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        scope_type (Union[Unset, str]):
        settings_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['RoleTemplate']]
    """

    kwargs = _get_kwargs(
        name=name,
        o=o,
        page=page,
        page_size=page_size,
        scope_type=scope_type,
        settings_uuid=settings_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[RancherRoleTemplatesListOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    scope_type: Union[Unset, str] = UNSET,
    settings_uuid: Union[Unset, UUID] = UNSET,
) -> list["RoleTemplate"]:
    """
    Args:
        name (Union[Unset, str]):
        o (Union[Unset, list[RancherRoleTemplatesListOItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        scope_type (Union[Unset, str]):
        settings_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['RoleTemplate']
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            o=o,
            page=page,
            page_size=page_size,
            scope_type=scope_type,
            settings_uuid=settings_uuid,
        )
    ).parsed
