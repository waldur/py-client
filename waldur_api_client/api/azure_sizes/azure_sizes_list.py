from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.azure_size import AzureSize
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    location: Union[Unset, str] = UNSET,
    location_uuid: Union[Unset, UUID] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    settings: Union[Unset, str] = UNSET,
    settings_uuid: Union[Unset, UUID] = UNSET,
    zone: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["location"] = location

    json_location_uuid: Union[Unset, str] = UNSET
    if not isinstance(location_uuid, Unset):
        json_location_uuid = str(location_uuid)
    params["location_uuid"] = json_location_uuid

    params["name"] = name

    params["name_exact"] = name_exact

    params["page"] = page

    params["page_size"] = page_size

    params["settings"] = settings

    json_settings_uuid: Union[Unset, str] = UNSET
    if not isinstance(settings_uuid, Unset):
        json_settings_uuid = str(settings_uuid)
    params["settings_uuid"] = json_settings_uuid

    params["zone"] = zone

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/azure-sizes/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> list["AzureSize"]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AzureSize.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["AzureSize"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    location: Union[Unset, str] = UNSET,
    location_uuid: Union[Unset, UUID] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    settings: Union[Unset, str] = UNSET,
    settings_uuid: Union[Unset, UUID] = UNSET,
    zone: Union[Unset, int] = UNSET,
) -> Response[list["AzureSize"]]:
    """Mixin to optimize HEAD requests for DRF views bypassing serializer processing

    Args:
        location (Union[Unset, str]):
        location_uuid (Union[Unset, UUID]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        settings (Union[Unset, str]):
        settings_uuid (Union[Unset, UUID]):
        zone (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['AzureSize']]
    """

    kwargs = _get_kwargs(
        location=location,
        location_uuid=location_uuid,
        name=name,
        name_exact=name_exact,
        page=page,
        page_size=page_size,
        settings=settings,
        settings_uuid=settings_uuid,
        zone=zone,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    location: Union[Unset, str] = UNSET,
    location_uuid: Union[Unset, UUID] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    settings: Union[Unset, str] = UNSET,
    settings_uuid: Union[Unset, UUID] = UNSET,
    zone: Union[Unset, int] = UNSET,
) -> list["AzureSize"]:
    """Mixin to optimize HEAD requests for DRF views bypassing serializer processing

    Args:
        location (Union[Unset, str]):
        location_uuid (Union[Unset, UUID]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        settings (Union[Unset, str]):
        settings_uuid (Union[Unset, UUID]):
        zone (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['AzureSize']
    """

    return sync_detailed(
        client=client,
        location=location,
        location_uuid=location_uuid,
        name=name,
        name_exact=name_exact,
        page=page,
        page_size=page_size,
        settings=settings,
        settings_uuid=settings_uuid,
        zone=zone,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    location: Union[Unset, str] = UNSET,
    location_uuid: Union[Unset, UUID] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    settings: Union[Unset, str] = UNSET,
    settings_uuid: Union[Unset, UUID] = UNSET,
    zone: Union[Unset, int] = UNSET,
) -> Response[list["AzureSize"]]:
    """Mixin to optimize HEAD requests for DRF views bypassing serializer processing

    Args:
        location (Union[Unset, str]):
        location_uuid (Union[Unset, UUID]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        settings (Union[Unset, str]):
        settings_uuid (Union[Unset, UUID]):
        zone (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['AzureSize']]
    """

    kwargs = _get_kwargs(
        location=location,
        location_uuid=location_uuid,
        name=name,
        name_exact=name_exact,
        page=page,
        page_size=page_size,
        settings=settings,
        settings_uuid=settings_uuid,
        zone=zone,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    location: Union[Unset, str] = UNSET,
    location_uuid: Union[Unset, UUID] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    settings: Union[Unset, str] = UNSET,
    settings_uuid: Union[Unset, UUID] = UNSET,
    zone: Union[Unset, int] = UNSET,
) -> list["AzureSize"]:
    """Mixin to optimize HEAD requests for DRF views bypassing serializer processing

    Args:
        location (Union[Unset, str]):
        location_uuid (Union[Unset, UUID]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        settings (Union[Unset, str]):
        settings_uuid (Union[Unset, UUID]):
        zone (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['AzureSize']
    """

    return (
        await asyncio_detailed(
            client=client,
            location=location,
            location_uuid=location_uuid,
            name=name,
            name_exact=name_exact,
            page=page,
            page_size=page_size,
            settings=settings,
            settings_uuid=settings_uuid,
            zone=zone,
        )
    ).parsed
