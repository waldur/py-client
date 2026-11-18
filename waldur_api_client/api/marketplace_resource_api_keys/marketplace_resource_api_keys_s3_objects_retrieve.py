from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.s3_object_list import S3ObjectList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    bucket: str,
    continuation_token: Union[Unset, str] = "",
    page_size: Union[Unset, int] = UNSET,
    prefix: Union[Unset, str] = "",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["bucket"] = bucket

    params["continuation_token"] = continuation_token

    params["page_size"] = page_size

    params["prefix"] = prefix

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/marketplace-resource-api-keys/{uuid}/s3/objects/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> S3ObjectList:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = S3ObjectList.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[S3ObjectList]:
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
    bucket: str,
    continuation_token: Union[Unset, str] = "",
    page_size: Union[Unset, int] = UNSET,
    prefix: Union[Unset, str] = "",
) -> Response[S3ObjectList]:
    """S3 browser: list objects

     One page of a bucket listing under a prefix, with common prefixes as folders. Follow
    next_continuation_token for the next page.

    Args:
        uuid (UUID):
        bucket (str):
        continuation_token (Union[Unset, str]):  Default: ''.
        page_size (Union[Unset, int]):
        prefix (Union[Unset, str]):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[S3ObjectList]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        bucket=bucket,
        continuation_token=continuation_token,
        page_size=page_size,
        prefix=prefix,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    bucket: str,
    continuation_token: Union[Unset, str] = "",
    page_size: Union[Unset, int] = UNSET,
    prefix: Union[Unset, str] = "",
) -> S3ObjectList:
    """S3 browser: list objects

     One page of a bucket listing under a prefix, with common prefixes as folders. Follow
    next_continuation_token for the next page.

    Args:
        uuid (UUID):
        bucket (str):
        continuation_token (Union[Unset, str]):  Default: ''.
        page_size (Union[Unset, int]):
        prefix (Union[Unset, str]):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        S3ObjectList
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        bucket=bucket,
        continuation_token=continuation_token,
        page_size=page_size,
        prefix=prefix,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    bucket: str,
    continuation_token: Union[Unset, str] = "",
    page_size: Union[Unset, int] = UNSET,
    prefix: Union[Unset, str] = "",
) -> Response[S3ObjectList]:
    """S3 browser: list objects

     One page of a bucket listing under a prefix, with common prefixes as folders. Follow
    next_continuation_token for the next page.

    Args:
        uuid (UUID):
        bucket (str):
        continuation_token (Union[Unset, str]):  Default: ''.
        page_size (Union[Unset, int]):
        prefix (Union[Unset, str]):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[S3ObjectList]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        bucket=bucket,
        continuation_token=continuation_token,
        page_size=page_size,
        prefix=prefix,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    bucket: str,
    continuation_token: Union[Unset, str] = "",
    page_size: Union[Unset, int] = UNSET,
    prefix: Union[Unset, str] = "",
) -> S3ObjectList:
    """S3 browser: list objects

     One page of a bucket listing under a prefix, with common prefixes as folders. Follow
    next_continuation_token for the next page.

    Args:
        uuid (UUID):
        bucket (str):
        continuation_token (Union[Unset, str]):  Default: ''.
        page_size (Union[Unset, int]):
        prefix (Union[Unset, str]):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        S3ObjectList
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            bucket=bucket,
            continuation_token=continuation_token,
            page_size=page_size,
            prefix=prefix,
        )
    ).parsed
