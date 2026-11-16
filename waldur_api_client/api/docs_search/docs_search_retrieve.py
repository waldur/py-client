from http import HTTPStatus
from typing import Any, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.docs_search_disabled import DocsSearchDisabled
from ...models.docs_search_response import DocsSearchResponse
from ...models.docs_search_unavailable import DocsSearchUnavailable
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Union[Unset, int] = 5,
    query: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["query"] = query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/docs-search/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[DocsSearchDisabled, DocsSearchResponse, DocsSearchUnavailable]:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = DocsSearchResponse.from_dict(response.json())

        return response_200
    if response.status_code == 424:
        response_424 = DocsSearchDisabled.from_dict(response.json())

        return response_424
    if response.status_code == 503:
        response_503 = DocsSearchUnavailable.from_dict(response.json())

        return response_503
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[DocsSearchDisabled, DocsSearchResponse, DocsSearchUnavailable]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = 5,
    query: str,
) -> Response[Union[DocsSearchDisabled, DocsSearchResponse, DocsSearchUnavailable]]:
    """Search the documentation of this release.

    End users get only the sections for their role whose features are
    switched on here. Staff and support also get sections for switched-off
    features, marked ``enabled_here: false``. Answers 424 while
    DOCS_SEARCH_ENABLED is off and 503 when no documentation corpus
    is loaded.

    Args:
        limit (Union[Unset, int]):  Default: 5.
        query (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DocsSearchDisabled, DocsSearchResponse, DocsSearchUnavailable]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        query=query,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = 5,
    query: str,
) -> Union[DocsSearchDisabled, DocsSearchResponse, DocsSearchUnavailable]:
    """Search the documentation of this release.

    End users get only the sections for their role whose features are
    switched on here. Staff and support also get sections for switched-off
    features, marked ``enabled_here: false``. Answers 424 while
    DOCS_SEARCH_ENABLED is off and 503 when no documentation corpus
    is loaded.

    Args:
        limit (Union[Unset, int]):  Default: 5.
        query (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DocsSearchDisabled, DocsSearchResponse, DocsSearchUnavailable]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        query=query,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = 5,
    query: str,
) -> Response[Union[DocsSearchDisabled, DocsSearchResponse, DocsSearchUnavailable]]:
    """Search the documentation of this release.

    End users get only the sections for their role whose features are
    switched on here. Staff and support also get sections for switched-off
    features, marked ``enabled_here: false``. Answers 424 while
    DOCS_SEARCH_ENABLED is off and 503 when no documentation corpus
    is loaded.

    Args:
        limit (Union[Unset, int]):  Default: 5.
        query (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DocsSearchDisabled, DocsSearchResponse, DocsSearchUnavailable]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        query=query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = 5,
    query: str,
) -> Union[DocsSearchDisabled, DocsSearchResponse, DocsSearchUnavailable]:
    """Search the documentation of this release.

    End users get only the sections for their role whose features are
    switched on here. Staff and support also get sections for switched-off
    features, marked ``enabled_here: false``. Answers 424 while
    DOCS_SEARCH_ENABLED is off and 503 when no documentation corpus
    is loaded.

    Args:
        limit (Union[Unset, int]):  Default: 5.
        query (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DocsSearchDisabled, DocsSearchResponse, DocsSearchUnavailable]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            query=query,
        )
    ).parsed
