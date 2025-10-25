from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.offering_software_catalog_request import OfferingSoftwareCatalogRequest
from ...models.software_catalog_uuid import SoftwareCatalogUUID
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    *,
    body: OfferingSoftwareCatalogRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/marketplace-provider-offerings/{uuid}/add_software_catalog/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> SoftwareCatalogUUID:
    if response.status_code == 201:
        response_201 = SoftwareCatalogUUID.from_dict(response.json())

        return response_201
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SoftwareCatalogUUID]:
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
    body: OfferingSoftwareCatalogRequest,
) -> Response[SoftwareCatalogUUID]:
    """Add software catalog to offering.

    Args:
        uuid (UUID):
        body (OfferingSoftwareCatalogRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SoftwareCatalogUUID]
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
    body: OfferingSoftwareCatalogRequest,
) -> SoftwareCatalogUUID:
    """Add software catalog to offering.

    Args:
        uuid (UUID):
        body (OfferingSoftwareCatalogRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SoftwareCatalogUUID
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
    body: OfferingSoftwareCatalogRequest,
) -> Response[SoftwareCatalogUUID]:
    """Add software catalog to offering.

    Args:
        uuid (UUID):
        body (OfferingSoftwareCatalogRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SoftwareCatalogUUID]
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
    body: OfferingSoftwareCatalogRequest,
) -> SoftwareCatalogUUID:
    """Add software catalog to offering.

    Args:
        uuid (UUID):
        body (OfferingSoftwareCatalogRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SoftwareCatalogUUID
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
