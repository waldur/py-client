from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.offering_thumbnail_request import OfferingThumbnailRequest
from ...models.provider_offering_details import ProviderOfferingDetails
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    *,
    body: Union[
        OfferingThumbnailRequest,
        OfferingThumbnailRequest,
        OfferingThumbnailRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/marketplace-provider-offerings/{uuid}/update_thumbnail/",
    }

    if isinstance(body, OfferingThumbnailRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, OfferingThumbnailRequest):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, OfferingThumbnailRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ProviderOfferingDetails]:
    if response.status_code == 200:
        response_200 = ProviderOfferingDetails.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ProviderOfferingDetails]:
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
    body: Union[
        OfferingThumbnailRequest,
        OfferingThumbnailRequest,
        OfferingThumbnailRequest,
    ],
) -> Response[ProviderOfferingDetails]:
    """Update offering thumbnail.

    Args:
        uuid (UUID):
        body (OfferingThumbnailRequest):
        body (OfferingThumbnailRequest):
        body (OfferingThumbnailRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProviderOfferingDetails]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: Union[
        OfferingThumbnailRequest,
        OfferingThumbnailRequest,
        OfferingThumbnailRequest,
    ],
) -> Optional[ProviderOfferingDetails]:
    """Update offering thumbnail.

    Args:
        uuid (UUID):
        body (OfferingThumbnailRequest):
        body (OfferingThumbnailRequest):
        body (OfferingThumbnailRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProviderOfferingDetails
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: Union[
        OfferingThumbnailRequest,
        OfferingThumbnailRequest,
        OfferingThumbnailRequest,
    ],
) -> Response[ProviderOfferingDetails]:
    """Update offering thumbnail.

    Args:
        uuid (UUID):
        body (OfferingThumbnailRequest):
        body (OfferingThumbnailRequest):
        body (OfferingThumbnailRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProviderOfferingDetails]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: Union[
        OfferingThumbnailRequest,
        OfferingThumbnailRequest,
        OfferingThumbnailRequest,
    ],
) -> Optional[ProviderOfferingDetails]:
    """Update offering thumbnail.

    Args:
        uuid (UUID):
        body (OfferingThumbnailRequest):
        body (OfferingThumbnailRequest):
        body (OfferingThumbnailRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProviderOfferingDetails
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
