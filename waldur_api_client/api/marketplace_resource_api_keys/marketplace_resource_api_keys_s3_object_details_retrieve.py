from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.s3_object_details import S3ObjectDetails
from ...types import UNSET, Response


def _get_kwargs(
    uuid: UUID,
    *,
    bucket: str,
    key: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["bucket"] = bucket

    params["key"] = key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/marketplace-resource-api-keys/{uuid}/s3/object-details/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> S3ObjectDetails:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = S3ObjectDetails.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[S3ObjectDetails]:
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
    key: str,
) -> Response[S3ObjectDetails]:
    """S3 browser: object details

     One object's content type, storage class, user metadata, encryption, object lock, ACL, tags and
    version count, as the key reads them. Read-only.

    Args:
        uuid (UUID):
        bucket (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[S3ObjectDetails]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        bucket=bucket,
        key=key,
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
    key: str,
) -> S3ObjectDetails:
    """S3 browser: object details

     One object's content type, storage class, user metadata, encryption, object lock, ACL, tags and
    version count, as the key reads them. Read-only.

    Args:
        uuid (UUID):
        bucket (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        S3ObjectDetails
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        bucket=bucket,
        key=key,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    bucket: str,
    key: str,
) -> Response[S3ObjectDetails]:
    """S3 browser: object details

     One object's content type, storage class, user metadata, encryption, object lock, ACL, tags and
    version count, as the key reads them. Read-only.

    Args:
        uuid (UUID):
        bucket (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[S3ObjectDetails]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        bucket=bucket,
        key=key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    bucket: str,
    key: str,
) -> S3ObjectDetails:
    """S3 browser: object details

     One object's content type, storage class, user metadata, encryption, object lock, ACL, tags and
    version count, as the key reads them. Read-only.

    Args:
        uuid (UUID):
        bucket (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        S3ObjectDetails
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            bucket=bucket,
            key=key,
        )
    ).parsed
