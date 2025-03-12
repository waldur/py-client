from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.notification import Notification
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    description: Union[Unset, str] = UNSET,
    is_overridden: Union[Unset, bool] = UNSET,
    key: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["description"] = description

    params["is_overridden"] = is_overridden

    params["key"] = key

    params["name"] = name

    params["name_exact"] = name_exact

    params["page"] = page

    params["page_size"] = page_size

    params["query"] = query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/notification-messages/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["Notification"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_paginated_notification_list_item_data in _response_200:
            componentsschemas_paginated_notification_list_item = Notification.from_dict(
                componentsschemas_paginated_notification_list_item_data
            )

            response_200.append(componentsschemas_paginated_notification_list_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["Notification"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    description: Union[Unset, str] = UNSET,
    is_overridden: Union[Unset, bool] = UNSET,
    key: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
) -> Response[list["Notification"]]:
    """
    Args:
        description (Union[Unset, str]):
        is_overridden (Union[Unset, bool]):
        key (Union[Unset, str]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        query (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['Notification']]
    """

    kwargs = _get_kwargs(
        description=description,
        is_overridden=is_overridden,
        key=key,
        name=name,
        name_exact=name_exact,
        page=page,
        page_size=page_size,
        query=query,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    description: Union[Unset, str] = UNSET,
    is_overridden: Union[Unset, bool] = UNSET,
    key: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
) -> Optional[list["Notification"]]:
    """
    Args:
        description (Union[Unset, str]):
        is_overridden (Union[Unset, bool]):
        key (Union[Unset, str]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        query (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['Notification']
    """

    return sync_detailed(
        client=client,
        description=description,
        is_overridden=is_overridden,
        key=key,
        name=name,
        name_exact=name_exact,
        page=page,
        page_size=page_size,
        query=query,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    description: Union[Unset, str] = UNSET,
    is_overridden: Union[Unset, bool] = UNSET,
    key: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
) -> Response[list["Notification"]]:
    """
    Args:
        description (Union[Unset, str]):
        is_overridden (Union[Unset, bool]):
        key (Union[Unset, str]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        query (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['Notification']]
    """

    kwargs = _get_kwargs(
        description=description,
        is_overridden=is_overridden,
        key=key,
        name=name,
        name_exact=name_exact,
        page=page,
        page_size=page_size,
        query=query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    description: Union[Unset, str] = UNSET,
    is_overridden: Union[Unset, bool] = UNSET,
    key: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
) -> Optional[list["Notification"]]:
    """
    Args:
        description (Union[Unset, str]):
        is_overridden (Union[Unset, bool]):
        key (Union[Unset, str]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        query (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['Notification']
    """

    return (
        await asyncio_detailed(
            client=client,
            description=description,
            is_overridden=is_overridden,
            key=key,
            name=name,
            name_exact=name_exact,
            page=page,
            page_size=page_size,
            query=query,
        )
    ).parsed
