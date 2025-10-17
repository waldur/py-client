from http import HTTPStatus
from typing import Any, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.customer_component_usage_policy import CustomerComponentUsagePolicy
from ...models.customer_component_usage_policy_request import CustomerComponentUsagePolicyRequest
from ...types import Response


def _get_kwargs(
    *,
    body: CustomerComponentUsagePolicyRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/marketplace-customer-component-usage-policies/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> CustomerComponentUsagePolicy:
    if response.status_code == 201:
        response_201 = CustomerComponentUsagePolicy.from_dict(response.json())

        return response_201
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CustomerComponentUsagePolicy]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CustomerComponentUsagePolicyRequest,
) -> Response[CustomerComponentUsagePolicy]:
    """
    Args:
        body (CustomerComponentUsagePolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomerComponentUsagePolicy]
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
    body: CustomerComponentUsagePolicyRequest,
) -> CustomerComponentUsagePolicy:
    """
    Args:
        body (CustomerComponentUsagePolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomerComponentUsagePolicy
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CustomerComponentUsagePolicyRequest,
) -> Response[CustomerComponentUsagePolicy]:
    """
    Args:
        body (CustomerComponentUsagePolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomerComponentUsagePolicy]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CustomerComponentUsagePolicyRequest,
) -> CustomerComponentUsagePolicy:
    """
    Args:
        body (CustomerComponentUsagePolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomerComponentUsagePolicy
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
