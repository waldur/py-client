from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.customer_estimated_cost_policy import CustomerEstimatedCostPolicy
from ...models.customer_estimated_cost_policy_request import CustomerEstimatedCostPolicyRequest
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    *,
    body: CustomerEstimatedCostPolicyRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/marketplace-customer-estimated-cost-policies/{uuid}/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> CustomerEstimatedCostPolicy:
    if response.status_code == 200:
        response_200 = CustomerEstimatedCostPolicy.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CustomerEstimatedCostPolicy]:
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
    body: CustomerEstimatedCostPolicyRequest,
) -> Response[CustomerEstimatedCostPolicy]:
    """
    Args:
        uuid (UUID):
        body (CustomerEstimatedCostPolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomerEstimatedCostPolicy]
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
    body: CustomerEstimatedCostPolicyRequest,
) -> CustomerEstimatedCostPolicy:
    """
    Args:
        uuid (UUID):
        body (CustomerEstimatedCostPolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomerEstimatedCostPolicy
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
    body: CustomerEstimatedCostPolicyRequest,
) -> Response[CustomerEstimatedCostPolicy]:
    """
    Args:
        uuid (UUID):
        body (CustomerEstimatedCostPolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomerEstimatedCostPolicy]
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
    body: CustomerEstimatedCostPolicyRequest,
) -> CustomerEstimatedCostPolicy:
    """
    Args:
        uuid (UUID):
        body (CustomerEstimatedCostPolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomerEstimatedCostPolicy
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
