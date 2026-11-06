from http import HTTPStatus
from typing import Any, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ranking_import_request import RankingImportRequest
from ...models.ranking_import_response import RankingImportResponse
from ...types import Response


def _get_kwargs(
    *,
    body: RankingImportRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/proposal-rankings/import_csv/",
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> RankingImportResponse:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = RankingImportResponse.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[RankingImportResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RankingImportRequest,
) -> Response[RankingImportResponse]:
    """Create or update the round's ranking from a CSV in the export's format. Rows without a rank are left
    out; rankings not in the file stay as they are. Ranks are checked across the round as it will be
    after the import, so a file can reorder it. All or nothing: an error in any row saves no row.
    Refused for a file over 1 MB, or with more rows than the round has proposals and a few more.

    Args:
        body (RankingImportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RankingImportResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: RankingImportRequest,
) -> RankingImportResponse:
    """Create or update the round's ranking from a CSV in the export's format. Rows without a rank are left
    out; rankings not in the file stay as they are. Ranks are checked across the round as it will be
    after the import, so a file can reorder it. All or nothing: an error in any row saves no row.
    Refused for a file over 1 MB, or with more rows than the round has proposals and a few more.

    Args:
        body (RankingImportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RankingImportResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RankingImportRequest,
) -> Response[RankingImportResponse]:
    """Create or update the round's ranking from a CSV in the export's format. Rows without a rank are left
    out; rankings not in the file stay as they are. Ranks are checked across the round as it will be
    after the import, so a file can reorder it. All or nothing: an error in any row saves no row.
    Refused for a file over 1 MB, or with more rows than the round has proposals and a few more.

    Args:
        body (RankingImportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RankingImportResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RankingImportRequest,
) -> RankingImportResponse:
    """Create or update the round's ranking from a CSV in the export's format. Rows without a rank are left
    out; rankings not in the file stay as they are. Ranks are checked across the round as it will be
    after the import, so a file can reorder it. All or nothing: an error in any row saves no row.
    Refused for a file over 1 MB, or with more rows than the round has proposals and a few more.

    Args:
        body (RankingImportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RankingImportResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
