from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.resource_user import ResourceUser
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    resource: Union[Unset, str] = UNSET,
    resource_uuid: Union[Unset, UUID] = UNSET,
    role_name: Union[Unset, str] = UNSET,
    role_uuid: Union[Unset, UUID] = UNSET,
    user_uuid: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["page_size"] = page_size

    params["resource"] = resource

    json_resource_uuid: Union[Unset, str] = UNSET
    if not isinstance(resource_uuid, Unset):
        json_resource_uuid = str(resource_uuid)
    params["resource_uuid"] = json_resource_uuid

    params["role_name"] = role_name

    json_role_uuid: Union[Unset, str] = UNSET
    if not isinstance(role_uuid, Unset):
        json_role_uuid = str(role_uuid)
    params["role_uuid"] = json_role_uuid

    json_user_uuid: Union[Unset, str] = UNSET
    if not isinstance(user_uuid, Unset):
        json_user_uuid = str(user_uuid)
    params["user_uuid"] = json_user_uuid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/marketplace-resource-users/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> list["ResourceUser"]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ResourceUser.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["ResourceUser"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    resource: Union[Unset, str] = UNSET,
    resource_uuid: Union[Unset, UUID] = UNSET,
    role_name: Union[Unset, str] = UNSET,
    role_uuid: Union[Unset, UUID] = UNSET,
    user_uuid: Union[Unset, UUID] = UNSET,
) -> Response[list["ResourceUser"]]:
    """Mixin to optimize HEAD requests for DRF views bypassing serializer processing

    Args:
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        resource (Union[Unset, str]):
        resource_uuid (Union[Unset, UUID]):
        role_name (Union[Unset, str]):
        role_uuid (Union[Unset, UUID]):
        user_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['ResourceUser']]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        resource=resource,
        resource_uuid=resource_uuid,
        role_name=role_name,
        role_uuid=role_uuid,
        user_uuid=user_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    resource: Union[Unset, str] = UNSET,
    resource_uuid: Union[Unset, UUID] = UNSET,
    role_name: Union[Unset, str] = UNSET,
    role_uuid: Union[Unset, UUID] = UNSET,
    user_uuid: Union[Unset, UUID] = UNSET,
) -> list["ResourceUser"]:
    """Mixin to optimize HEAD requests for DRF views bypassing serializer processing

    Args:
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        resource (Union[Unset, str]):
        resource_uuid (Union[Unset, UUID]):
        role_name (Union[Unset, str]):
        role_uuid (Union[Unset, UUID]):
        user_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['ResourceUser']
    """

    return sync_detailed(
        client=client,
        page=page,
        page_size=page_size,
        resource=resource,
        resource_uuid=resource_uuid,
        role_name=role_name,
        role_uuid=role_uuid,
        user_uuid=user_uuid,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    resource: Union[Unset, str] = UNSET,
    resource_uuid: Union[Unset, UUID] = UNSET,
    role_name: Union[Unset, str] = UNSET,
    role_uuid: Union[Unset, UUID] = UNSET,
    user_uuid: Union[Unset, UUID] = UNSET,
) -> Response[list["ResourceUser"]]:
    """Mixin to optimize HEAD requests for DRF views bypassing serializer processing

    Args:
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        resource (Union[Unset, str]):
        resource_uuid (Union[Unset, UUID]):
        role_name (Union[Unset, str]):
        role_uuid (Union[Unset, UUID]):
        user_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['ResourceUser']]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        resource=resource,
        resource_uuid=resource_uuid,
        role_name=role_name,
        role_uuid=role_uuid,
        user_uuid=user_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    resource: Union[Unset, str] = UNSET,
    resource_uuid: Union[Unset, UUID] = UNSET,
    role_name: Union[Unset, str] = UNSET,
    role_uuid: Union[Unset, UUID] = UNSET,
    user_uuid: Union[Unset, UUID] = UNSET,
) -> list["ResourceUser"]:
    """Mixin to optimize HEAD requests for DRF views bypassing serializer processing

    Args:
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        resource (Union[Unset, str]):
        resource_uuid (Union[Unset, UUID]):
        role_name (Union[Unset, str]):
        role_uuid (Union[Unset, UUID]):
        user_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['ResourceUser']
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            page_size=page_size,
            resource=resource,
            resource_uuid=resource_uuid,
            role_name=role_name,
            role_uuid=role_uuid,
            user_uuid=user_uuid,
        )
    ).parsed
