from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.set_resource_spending_limits import SetResourceSpendingLimits
from ...models.set_resource_spending_limits_request import SetResourceSpendingLimitsRequest
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    *,
    body: SetResourceSpendingLimitsRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/marketplace-resources/{uuid}/set_spending_limits/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> SetResourceSpendingLimits:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = SetResourceSpendingLimits.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SetResourceSpendingLimits]:
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
    body: SetResourceSpendingLimitsRequest,
) -> Response[SetResourceSpendingLimits]:
    """Set resource spending limits

     Replaces the spending limits of the resource's usage-based components at once, with no order or
    provider approval. Each value must be within the provider's maximum. The usage-limit restriction is
    re-evaluated immediately.

    Args:
        uuid (UUID):
        body (SetResourceSpendingLimitsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SetResourceSpendingLimits]
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
    body: SetResourceSpendingLimitsRequest,
) -> SetResourceSpendingLimits:
    """Set resource spending limits

     Replaces the spending limits of the resource's usage-based components at once, with no order or
    provider approval. Each value must be within the provider's maximum. The usage-limit restriction is
    re-evaluated immediately.

    Args:
        uuid (UUID):
        body (SetResourceSpendingLimitsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SetResourceSpendingLimits
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
    body: SetResourceSpendingLimitsRequest,
) -> Response[SetResourceSpendingLimits]:
    """Set resource spending limits

     Replaces the spending limits of the resource's usage-based components at once, with no order or
    provider approval. Each value must be within the provider's maximum. The usage-limit restriction is
    re-evaluated immediately.

    Args:
        uuid (UUID):
        body (SetResourceSpendingLimitsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SetResourceSpendingLimits]
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
    body: SetResourceSpendingLimitsRequest,
) -> SetResourceSpendingLimits:
    """Set resource spending limits

     Replaces the spending limits of the resource's usage-based components at once, with no order or
    provider approval. Each value must be within the provider's maximum. The usage-limit restriction is
    re-evaluated immediately.

    Args:
        uuid (UUID):
        body (SetResourceSpendingLimitsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SetResourceSpendingLimits
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
