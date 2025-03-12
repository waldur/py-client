from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.marketplace_provider_resources_details_retrieve_field_item import (
    MarketplaceProviderResourcesDetailsRetrieveFieldItem,
)
from ...models.resource import Resource
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    field: Union[Unset, list[MarketplaceProviderResourcesDetailsRetrieveFieldItem]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_field: Union[Unset, list[str]] = UNSET
    if not isinstance(field, Unset):
        json_field = []
        for field_item_data in field:
            field_item = field_item_data.value
            json_field.append(field_item)

    params["field"] = json_field

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/marketplace-provider-resources/{uuid}/details/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Resource]:
    if response.status_code == 200:
        response_200 = Resource.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Resource]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    field: Union[Unset, list[MarketplaceProviderResourcesDetailsRetrieveFieldItem]] = UNSET,
) -> Response[Resource]:
    """
    Args:
        uuid (UUID):
        field (Union[Unset, list[MarketplaceProviderResourcesDetailsRetrieveFieldItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Resource]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        field=field,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    field: Union[Unset, list[MarketplaceProviderResourcesDetailsRetrieveFieldItem]] = UNSET,
) -> Optional[Resource]:
    """
    Args:
        uuid (UUID):
        field (Union[Unset, list[MarketplaceProviderResourcesDetailsRetrieveFieldItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Resource
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        field=field,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    field: Union[Unset, list[MarketplaceProviderResourcesDetailsRetrieveFieldItem]] = UNSET,
) -> Response[Resource]:
    """
    Args:
        uuid (UUID):
        field (Union[Unset, list[MarketplaceProviderResourcesDetailsRetrieveFieldItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Resource]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        field=field,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    field: Union[Unset, list[MarketplaceProviderResourcesDetailsRetrieveFieldItem]] = UNSET,
) -> Optional[Resource]:
    """
    Args:
        uuid (UUID):
        field (Union[Unset, list[MarketplaceProviderResourcesDetailsRetrieveFieldItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Resource
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            field=field,
        )
    ).parsed
