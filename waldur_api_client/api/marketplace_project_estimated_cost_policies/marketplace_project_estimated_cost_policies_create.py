from http import HTTPStatus
from typing import Any, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.project_estimated_cost_policy import ProjectEstimatedCostPolicy
from ...models.project_estimated_cost_policy_request import ProjectEstimatedCostPolicyRequest
from ...types import Response


def _get_kwargs(
    *,
    body: ProjectEstimatedCostPolicyRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/marketplace-project-estimated-cost-policies/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> ProjectEstimatedCostPolicy:
    if response.status_code == 201:
        response_201 = ProjectEstimatedCostPolicy.from_dict(response.json())

        return response_201
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ProjectEstimatedCostPolicy]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ProjectEstimatedCostPolicyRequest,
) -> Response[ProjectEstimatedCostPolicy]:
    """
    Args:
        body (ProjectEstimatedCostPolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProjectEstimatedCostPolicy]
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
    body: ProjectEstimatedCostPolicyRequest,
) -> ProjectEstimatedCostPolicy:
    """
    Args:
        body (ProjectEstimatedCostPolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProjectEstimatedCostPolicy
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ProjectEstimatedCostPolicyRequest,
) -> Response[ProjectEstimatedCostPolicy]:
    """
    Args:
        body (ProjectEstimatedCostPolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProjectEstimatedCostPolicy]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ProjectEstimatedCostPolicyRequest,
) -> ProjectEstimatedCostPolicy:
    """
    Args:
        body (ProjectEstimatedCostPolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProjectEstimatedCostPolicy
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
