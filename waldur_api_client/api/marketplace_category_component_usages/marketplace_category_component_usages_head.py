import datetime
from http import HTTPStatus
from typing import Any, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    date_after: Union[Unset, datetime.date] = UNSET,
    date_before: Union[Unset, datetime.date] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_date_after: Union[Unset, str] = UNSET
    if not isinstance(date_after, Unset):
        json_date_after = date_after.isoformat()
    params["date_after"] = json_date_after

    json_date_before: Union[Unset, str] = UNSET
    if not isinstance(date_before, Unset):
        json_date_before = date_before.isoformat()
    params["date_before"] = json_date_before

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "head",
        "url": "/api/marketplace-category-component-usages/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> int:
    if response.status_code == HTTPStatus.OK:
        try:
            return int(response.headers["x-result-count"])
        except KeyError:
            raise errors.UnexpectedStatus(
                response.status_code, b"Expected 'X-Result-Count' header for HEAD request, but it was not found."
            )
        except ValueError:
            count_val = response.headers.get("x-result-count")
            msg = f"Expected 'X-Result-Count' header to be an integer, but got '{count_val}'."
            raise errors.UnexpectedStatus(response.status_code, msg.encode())
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[int]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    date_after: Union[Unset, datetime.date] = UNSET,
    date_before: Union[Unset, datetime.date] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[int]:
    """Get number of items in the collection matching the request parameters.

    Args:
        date_after (Union[Unset, datetime.date]):
        date_before (Union[Unset, datetime.date]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[int]
    """

    kwargs = _get_kwargs(
        date_after=date_after,
        date_before=date_before,
        page=page,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    date_after: Union[Unset, datetime.date] = UNSET,
    date_before: Union[Unset, datetime.date] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> int:
    """Get number of items in the collection matching the request parameters.

    Args:
        date_after (Union[Unset, datetime.date]):
        date_before (Union[Unset, datetime.date]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        int
    """

    return sync_detailed(
        client=client,
        date_after=date_after,
        date_before=date_before,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    date_after: Union[Unset, datetime.date] = UNSET,
    date_before: Union[Unset, datetime.date] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[int]:
    """Get number of items in the collection matching the request parameters.

    Args:
        date_after (Union[Unset, datetime.date]):
        date_before (Union[Unset, datetime.date]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[int]
    """

    kwargs = _get_kwargs(
        date_after=date_after,
        date_before=date_before,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    date_after: Union[Unset, datetime.date] = UNSET,
    date_before: Union[Unset, datetime.date] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> int:
    """Get number of items in the collection matching the request parameters.

    Args:
        date_after (Union[Unset, datetime.date]):
        date_before (Union[Unset, datetime.date]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        int
    """

    return (
        await asyncio_detailed(
            client=client,
            date_after=date_after,
            date_before=date_before,
            page=page,
            page_size=page_size,
        )
    ).parsed
