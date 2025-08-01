from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    dst_resource_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    src_resource_uuid: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_dst_resource_uuid: Union[Unset, str] = UNSET
    if not isinstance(dst_resource_uuid, Unset):
        json_dst_resource_uuid = str(dst_resource_uuid)
    params["dst_resource_uuid"] = json_dst_resource_uuid

    params["page"] = page

    params["page_size"] = page_size

    json_src_resource_uuid: Union[Unset, str] = UNSET
    if not isinstance(src_resource_uuid, Unset):
        json_src_resource_uuid = str(src_resource_uuid)
    params["src_resource_uuid"] = json_src_resource_uuid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "head",
        "url": "/api/openstack-migrations/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Any:
    if response.status_code == 200:
        return None
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    dst_resource_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    src_resource_uuid: Union[Unset, UUID] = UNSET,
) -> Response[Any]:
    """Mixin to optimize HEAD requests for DRF views bypassing serializer processing

    Args:
        dst_resource_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        src_resource_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        dst_resource_uuid=dst_resource_uuid,
        page=page,
        page_size=page_size,
        src_resource_uuid=src_resource_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    dst_resource_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    src_resource_uuid: Union[Unset, UUID] = UNSET,
) -> Response[Any]:
    """Mixin to optimize HEAD requests for DRF views bypassing serializer processing

    Args:
        dst_resource_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        src_resource_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        dst_resource_uuid=dst_resource_uuid,
        page=page,
        page_size=page_size,
        src_resource_uuid=src_resource_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
