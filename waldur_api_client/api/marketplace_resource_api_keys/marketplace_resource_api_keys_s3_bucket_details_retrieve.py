from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.s3_bucket_details import S3BucketDetails
from ...types import UNSET, Response


def _get_kwargs(
    uuid: UUID,
    *,
    bucket: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["bucket"] = bucket

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/marketplace-resource-api-keys/{uuid}/s3/bucket-details/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> S3BucketDetails:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = S3BucketDetails.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[S3BucketDetails]:
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
) -> Response[S3BucketDetails]:
    """S3 browser: bucket details

     The bucket's size, ACL, policy, public access block, versioning, object lock, lifecycle rules,
    default encryption, CORS rules and tags, as the key reads them. Read-only.

    Args:
        uuid (UUID):
        bucket (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[S3BucketDetails]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        bucket=bucket,
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
) -> S3BucketDetails:
    """S3 browser: bucket details

     The bucket's size, ACL, policy, public access block, versioning, object lock, lifecycle rules,
    default encryption, CORS rules and tags, as the key reads them. Read-only.

    Args:
        uuid (UUID):
        bucket (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        S3BucketDetails
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        bucket=bucket,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    bucket: str,
) -> Response[S3BucketDetails]:
    """S3 browser: bucket details

     The bucket's size, ACL, policy, public access block, versioning, object lock, lifecycle rules,
    default encryption, CORS rules and tags, as the key reads them. Read-only.

    Args:
        uuid (UUID):
        bucket (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[S3BucketDetails]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        bucket=bucket,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    bucket: str,
) -> S3BucketDetails:
    """S3 browser: bucket details

     The bucket's size, ACL, policy, public access block, versioning, object lock, lifecycle rules,
    default encryption, CORS rules and tags, as the key reads them. Read-only.

    Args:
        uuid (UUID):
        bucket (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        S3BucketDetails
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            bucket=bucket,
        )
    ).parsed
