from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.awarded_resource import AwardedResource
from ...models.provision_awarded_item_request import ProvisionAwardedItemRequest
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    *,
    body: ProvisionAwardedItemRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/proposal-proposals/{uuid}/provision_awarded_item/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> AwardedResource:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = AwardedResource.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AwardedResource]:
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
    body: ProvisionAwardedItemRequest,
) -> Response[AwardedResource]:
    """Order an item of an allocated proposal's award again: one that allocation could not order (see its
    provision_error) or whose order the provider refused. Call managers and staff, once the provider's
    offering takes orders again.

    Args:
        uuid (UUID):
        body (ProvisionAwardedItemRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AwardedResource]
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
    body: ProvisionAwardedItemRequest,
) -> AwardedResource:
    """Order an item of an allocated proposal's award again: one that allocation could not order (see its
    provision_error) or whose order the provider refused. Call managers and staff, once the provider's
    offering takes orders again.

    Args:
        uuid (UUID):
        body (ProvisionAwardedItemRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AwardedResource
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
    body: ProvisionAwardedItemRequest,
) -> Response[AwardedResource]:
    """Order an item of an allocated proposal's award again: one that allocation could not order (see its
    provision_error) or whose order the provider refused. Call managers and staff, once the provider's
    offering takes orders again.

    Args:
        uuid (UUID):
        body (ProvisionAwardedItemRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AwardedResource]
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
    body: ProvisionAwardedItemRequest,
) -> AwardedResource:
    """Order an item of an allocated proposal's award again: one that allocation could not order (see its
    provision_error) or whose order the provider refused. Call managers and staff, once the provider's
    offering takes orders again.

    Args:
        uuid (UUID):
        body (ProvisionAwardedItemRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AwardedResource
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
