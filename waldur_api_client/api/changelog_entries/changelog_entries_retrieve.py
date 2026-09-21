from http import HTTPStatus
from typing import Any, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.changelog_entry_list import ChangelogEntryList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    highlight: Union[Unset, bool] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    relevant_only: Union[Unset, bool] = UNSET,
    risk: Union[Unset, str] = UNSET,
    scope: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["highlight"] = highlight

    params["page"] = page

    params["page_size"] = page_size

    params["relevant_only"] = relevant_only

    params["risk"] = risk

    params["scope"] = scope

    params["search"] = search

    params["type"] = type_

    params["version"] = version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/changelog-entries/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> ChangelogEntryList:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = ChangelogEntryList.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ChangelogEntryList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    highlight: Union[Unset, bool] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    relevant_only: Union[Unset, bool] = UNSET,
    risk: Union[Unset, str] = UNSET,
    scope: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
) -> Response[ChangelogEntryList]:
    """List changelog entries

     Returns a flat, paginated list of changelog entries for all pending versions. Supports filtering by
    type, risk, scope, version, and text search. Compatible with the standard Waldur table component.

    Args:
        highlight (Union[Unset, bool]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        relevant_only (Union[Unset, bool]):
        risk (Union[Unset, str]):
        scope (Union[Unset, str]):
        search (Union[Unset, str]):
        type_ (Union[Unset, str]):
        version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChangelogEntryList]
    """

    kwargs = _get_kwargs(
        highlight=highlight,
        page=page,
        page_size=page_size,
        relevant_only=relevant_only,
        risk=risk,
        scope=scope,
        search=search,
        type_=type_,
        version=version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    highlight: Union[Unset, bool] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    relevant_only: Union[Unset, bool] = UNSET,
    risk: Union[Unset, str] = UNSET,
    scope: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
) -> ChangelogEntryList:
    """List changelog entries

     Returns a flat, paginated list of changelog entries for all pending versions. Supports filtering by
    type, risk, scope, version, and text search. Compatible with the standard Waldur table component.

    Args:
        highlight (Union[Unset, bool]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        relevant_only (Union[Unset, bool]):
        risk (Union[Unset, str]):
        scope (Union[Unset, str]):
        search (Union[Unset, str]):
        type_ (Union[Unset, str]):
        version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChangelogEntryList
    """

    return sync_detailed(
        client=client,
        highlight=highlight,
        page=page,
        page_size=page_size,
        relevant_only=relevant_only,
        risk=risk,
        scope=scope,
        search=search,
        type_=type_,
        version=version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    highlight: Union[Unset, bool] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    relevant_only: Union[Unset, bool] = UNSET,
    risk: Union[Unset, str] = UNSET,
    scope: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
) -> Response[ChangelogEntryList]:
    """List changelog entries

     Returns a flat, paginated list of changelog entries for all pending versions. Supports filtering by
    type, risk, scope, version, and text search. Compatible with the standard Waldur table component.

    Args:
        highlight (Union[Unset, bool]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        relevant_only (Union[Unset, bool]):
        risk (Union[Unset, str]):
        scope (Union[Unset, str]):
        search (Union[Unset, str]):
        type_ (Union[Unset, str]):
        version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChangelogEntryList]
    """

    kwargs = _get_kwargs(
        highlight=highlight,
        page=page,
        page_size=page_size,
        relevant_only=relevant_only,
        risk=risk,
        scope=scope,
        search=search,
        type_=type_,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    highlight: Union[Unset, bool] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    relevant_only: Union[Unset, bool] = UNSET,
    risk: Union[Unset, str] = UNSET,
    scope: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
) -> ChangelogEntryList:
    """List changelog entries

     Returns a flat, paginated list of changelog entries for all pending versions. Supports filtering by
    type, risk, scope, version, and text search. Compatible with the standard Waldur table component.

    Args:
        highlight (Union[Unset, bool]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        relevant_only (Union[Unset, bool]):
        risk (Union[Unset, str]):
        scope (Union[Unset, str]):
        search (Union[Unset, str]):
        type_ (Union[Unset, str]):
        version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChangelogEntryList
    """

    return (
        await asyncio_detailed(
            client=client,
            highlight=highlight,
            page=page,
            page_size=page_size,
            relevant_only=relevant_only,
            risk=risk,
            scope=scope,
            search=search,
            type_=type_,
            version=version,
        )
    ).parsed
