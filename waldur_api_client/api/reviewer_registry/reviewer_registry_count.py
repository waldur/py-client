from http import HTTPStatus
from typing import Any, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.reviewer_registry_o_enum import ReviewerRegistryOEnum
from ...models.reviewer_standing_enum import ReviewerStandingEnum
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    o: Union[Unset, list[ReviewerRegistryOEnum]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    publication_pending: Union[Unset, bool] = UNSET,
    query: Union[Unset, str] = UNSET,
    standing: Union[Unset, list[ReviewerStandingEnum]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_o: Union[Unset, list[str]] = UNSET
    if not isinstance(o, Unset):
        json_o = []
        for o_item_data in o:
            o_item = o_item_data.value
            json_o.append(o_item)

    params["o"] = json_o

    params["page"] = page

    params["page_size"] = page_size

    params["publication_pending"] = publication_pending

    params["query"] = query

    json_standing: Union[Unset, list[str]] = UNSET
    if not isinstance(standing, Unset):
        json_standing = []
        for standing_item_data in standing:
            standing_item = standing_item_data.value
            json_standing.append(standing_item)

    params["standing"] = json_standing

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "head",
        "url": "/api/reviewer-registry/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> int:
    if response.status_code == HTTPStatus.OK:
        try:
            return int(response.headers["x-result-count"])
        except KeyError:
            raise errors.UnexpectedStatus(
                response.status_code,
                b"Expected 'X-Result-Count' header for HEAD request, but it was not found.",
                response.url,
            )
        except ValueError:
            count_val = response.headers.get("x-result-count")
            msg = f"Expected 'X-Result-Count' header to be an integer, but got '{count_val}'."
            raise errors.UnexpectedStatus(response.status_code, msg.encode(), response.url)
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


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
    o: Union[Unset, list[ReviewerRegistryOEnum]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    publication_pending: Union[Unset, bool] = UNSET,
    query: Union[Unset, str] = UNSET,
    standing: Union[Unset, list[ReviewerStandingEnum]] = UNSET,
) -> Response[int]:
    """Get number of items in the collection matching the request parameters.

    Args:
        o (Union[Unset, list[ReviewerRegistryOEnum]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        publication_pending (Union[Unset, bool]):
        query (Union[Unset, str]):
        standing (Union[Unset, list[ReviewerStandingEnum]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[int]
    """

    kwargs = _get_kwargs(
        o=o,
        page=page,
        page_size=page_size,
        publication_pending=publication_pending,
        query=query,
        standing=standing,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    o: Union[Unset, list[ReviewerRegistryOEnum]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    publication_pending: Union[Unset, bool] = UNSET,
    query: Union[Unset, str] = UNSET,
    standing: Union[Unset, list[ReviewerStandingEnum]] = UNSET,
) -> int:
    """Get number of items in the collection matching the request parameters.

    Args:
        o (Union[Unset, list[ReviewerRegistryOEnum]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        publication_pending (Union[Unset, bool]):
        query (Union[Unset, str]):
        standing (Union[Unset, list[ReviewerStandingEnum]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        int
    """

    return sync_detailed(
        client=client,
        o=o,
        page=page,
        page_size=page_size,
        publication_pending=publication_pending,
        query=query,
        standing=standing,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    o: Union[Unset, list[ReviewerRegistryOEnum]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    publication_pending: Union[Unset, bool] = UNSET,
    query: Union[Unset, str] = UNSET,
    standing: Union[Unset, list[ReviewerStandingEnum]] = UNSET,
) -> Response[int]:
    """Get number of items in the collection matching the request parameters.

    Args:
        o (Union[Unset, list[ReviewerRegistryOEnum]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        publication_pending (Union[Unset, bool]):
        query (Union[Unset, str]):
        standing (Union[Unset, list[ReviewerStandingEnum]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[int]
    """

    kwargs = _get_kwargs(
        o=o,
        page=page,
        page_size=page_size,
        publication_pending=publication_pending,
        query=query,
        standing=standing,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    o: Union[Unset, list[ReviewerRegistryOEnum]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    publication_pending: Union[Unset, bool] = UNSET,
    query: Union[Unset, str] = UNSET,
    standing: Union[Unset, list[ReviewerStandingEnum]] = UNSET,
) -> int:
    """Get number of items in the collection matching the request parameters.

    Args:
        o (Union[Unset, list[ReviewerRegistryOEnum]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        publication_pending (Union[Unset, bool]):
        query (Union[Unset, str]):
        standing (Union[Unset, list[ReviewerStandingEnum]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        int
    """

    return (
        await asyncio_detailed(
            client=client,
            o=o,
            page=page,
            page_size=page_size,
            publication_pending=publication_pending,
            query=query,
            standing=standing,
        )
    ).parsed
