from http import HTTPStatus
from typing import Any, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.chat_thread_stats_response import ChatThreadStatsResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/chat-threads/stats/",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> ChatThreadStatsResponse:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = ChatThreadStatsResponse.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ChatThreadStatsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ChatThreadStatsResponse]:
    """Get statistics for visible chat threads

     Summary statistics for the visible chat threads.

    Aggregates over a clean base queryset rather than ``get_queryset`` —
    the per-row token/count annotations there would collide with these
    aggregates. Visibility mirrors the list: staff/support see all, other
    users only their own.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatThreadStatsResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> ChatThreadStatsResponse:
    """Get statistics for visible chat threads

     Summary statistics for the visible chat threads.

    Aggregates over a clean base queryset rather than ``get_queryset`` —
    the per-row token/count annotations there would collide with these
    aggregates. Visibility mirrors the list: staff/support see all, other
    users only their own.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatThreadStatsResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ChatThreadStatsResponse]:
    """Get statistics for visible chat threads

     Summary statistics for the visible chat threads.

    Aggregates over a clean base queryset rather than ``get_queryset`` —
    the per-row token/count annotations there would collide with these
    aggregates. Visibility mirrors the list: staff/support see all, other
    users only their own.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatThreadStatsResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> ChatThreadStatsResponse:
    """Get statistics for visible chat threads

     Summary statistics for the visible chat threads.

    Aggregates over a clean base queryset rather than ``get_queryset`` —
    the per-row token/count annotations there would collide with these
    aggregates. Visibility mirrors the list: staff/support see all, other
    users only their own.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatThreadStatsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
