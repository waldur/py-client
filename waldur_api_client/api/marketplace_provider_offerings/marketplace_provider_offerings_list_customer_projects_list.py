from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.marketplace_provider_offerings_list_customer_projects_list_field_item import (
    MarketplaceProviderOfferingsListCustomerProjectsListFieldItem,
)
from ...models.project import Project
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    field: Union[Unset, list[MarketplaceProviderOfferingsListCustomerProjectsListFieldItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_field: Union[Unset, list[str]] = UNSET
    if not isinstance(field, Unset):
        json_field = []
        for field_item_data in field:
            field_item = field_item_data.value
            json_field.append(field_item)

    params["field"] = json_field

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/marketplace-provider-offerings/{uuid}/list_customer_projects/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> list["Project"]:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Project.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["Project"]]:
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
    field: Union[Unset, list[MarketplaceProviderOfferingsListCustomerProjectsListFieldItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[list["Project"]]:
    """
    Args:
        uuid (UUID):
        field (Union[Unset, list[MarketplaceProviderOfferingsListCustomerProjectsListFieldItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['Project']]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        field=field,
        page=page,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    field: Union[Unset, list[MarketplaceProviderOfferingsListCustomerProjectsListFieldItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> list["Project"]:
    """
    Args:
        uuid (UUID):
        field (Union[Unset, list[MarketplaceProviderOfferingsListCustomerProjectsListFieldItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['Project']
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        field=field,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    field: Union[Unset, list[MarketplaceProviderOfferingsListCustomerProjectsListFieldItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[list["Project"]]:
    """
    Args:
        uuid (UUID):
        field (Union[Unset, list[MarketplaceProviderOfferingsListCustomerProjectsListFieldItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['Project']]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        field=field,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    field: Union[Unset, list[MarketplaceProviderOfferingsListCustomerProjectsListFieldItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> list["Project"]:
    """
    Args:
        uuid (UUID):
        field (Union[Unset, list[MarketplaceProviderOfferingsListCustomerProjectsListFieldItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['Project']
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            field=field,
            page=page,
            page_size=page_size,
        )
    ).parsed
