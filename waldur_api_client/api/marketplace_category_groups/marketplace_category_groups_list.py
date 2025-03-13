from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.category_group import CategoryGroup
from ...models.marketplace_category_groups_list_field_item import MarketplaceCategoryGroupsListFieldItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    field: Union[Unset, list[MarketplaceCategoryGroupsListFieldItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    title: Union[Unset, str] = UNSET,
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

    params["title"] = title

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/marketplace-category-groups/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["CategoryGroup"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CategoryGroup.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["CategoryGroup"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    field: Union[Unset, list[MarketplaceCategoryGroupsListFieldItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> Response[list["CategoryGroup"]]:
    """
    Args:
        field (Union[Unset, list[MarketplaceCategoryGroupsListFieldItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        title (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['CategoryGroup']]
    """

    kwargs = _get_kwargs(
        field=field,
        page=page,
        page_size=page_size,
        title=title,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    field: Union[Unset, list[MarketplaceCategoryGroupsListFieldItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> Optional[list["CategoryGroup"]]:
    """
    Args:
        field (Union[Unset, list[MarketplaceCategoryGroupsListFieldItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        title (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['CategoryGroup']
    """

    return sync_detailed(
        client=client,
        field=field,
        page=page,
        page_size=page_size,
        title=title,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    field: Union[Unset, list[MarketplaceCategoryGroupsListFieldItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> Response[list["CategoryGroup"]]:
    """
    Args:
        field (Union[Unset, list[MarketplaceCategoryGroupsListFieldItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        title (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['CategoryGroup']]
    """

    kwargs = _get_kwargs(
        field=field,
        page=page,
        page_size=page_size,
        title=title,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    field: Union[Unset, list[MarketplaceCategoryGroupsListFieldItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> Optional[list["CategoryGroup"]]:
    """
    Args:
        field (Union[Unset, list[MarketplaceCategoryGroupsListFieldItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        title (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['CategoryGroup']
    """

    return (
        await asyncio_detailed(
            client=client,
            field=field,
            page=page,
            page_size=page_size,
            title=title,
        )
    ).parsed
