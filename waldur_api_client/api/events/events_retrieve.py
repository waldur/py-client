from http import HTTPStatus
from typing import Any, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.event import Event
from ...models.events_retrieve_field_item import EventsRetrieveFieldItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    field: Union[Unset, list[EventsRetrieveFieldItem]] = UNSET,
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
        "url": f"/api/events/{id}/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Event:
    if response.status_code == 200:
        response_200 = Event.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Event]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    field: Union[Unset, list[EventsRetrieveFieldItem]] = UNSET,
) -> Response[Event]:
    """
    Args:
        id (int):
        field (Union[Unset, list[EventsRetrieveFieldItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Event]
    """

    kwargs = _get_kwargs(
        id=id,
        field=field,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    field: Union[Unset, list[EventsRetrieveFieldItem]] = UNSET,
) -> Event:
    """
    Args:
        id (int):
        field (Union[Unset, list[EventsRetrieveFieldItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Event
    """

    return sync_detailed(
        id=id,
        client=client,
        field=field,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    field: Union[Unset, list[EventsRetrieveFieldItem]] = UNSET,
) -> Response[Event]:
    """
    Args:
        id (int):
        field (Union[Unset, list[EventsRetrieveFieldItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Event]
    """

    kwargs = _get_kwargs(
        id=id,
        field=field,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    field: Union[Unset, list[EventsRetrieveFieldItem]] = UNSET,
) -> Event:
    """
    Args:
        id (int):
        field (Union[Unset, list[EventsRetrieveFieldItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Event
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            field=field,
        )
    ).parsed
