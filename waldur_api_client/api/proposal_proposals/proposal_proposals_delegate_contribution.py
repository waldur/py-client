from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delegate_step_contribution_request import DelegateStepContributionRequest
from ...models.step_contribution import StepContribution
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    *,
    body: DelegateStepContributionRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/proposal-proposals/{uuid}/delegate_contribution/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> StepContribution:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = StepContribution.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[StepContribution]:
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
    body: DelegateStepContributionRequest,
) -> Response[StepContribution]:
    """Hand a contribution slot to someone the step's delegable_to allows -- an offering manager of the
    slot's offering, or a holder of an evaluator role on the proposal -- or take it back with a null
    user_uuid. Its holders and the call's managers may; the person it is handed to accepts or declines
    it.

    Args:
        uuid (UUID):
        body (DelegateStepContributionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StepContribution]
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
    body: DelegateStepContributionRequest,
) -> StepContribution:
    """Hand a contribution slot to someone the step's delegable_to allows -- an offering manager of the
    slot's offering, or a holder of an evaluator role on the proposal -- or take it back with a null
    user_uuid. Its holders and the call's managers may; the person it is handed to accepts or declines
    it.

    Args:
        uuid (UUID):
        body (DelegateStepContributionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StepContribution
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
    body: DelegateStepContributionRequest,
) -> Response[StepContribution]:
    """Hand a contribution slot to someone the step's delegable_to allows -- an offering manager of the
    slot's offering, or a holder of an evaluator role on the proposal -- or take it back with a null
    user_uuid. Its holders and the call's managers may; the person it is handed to accepts or declines
    it.

    Args:
        uuid (UUID):
        body (DelegateStepContributionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StepContribution]
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
    body: DelegateStepContributionRequest,
) -> StepContribution:
    """Hand a contribution slot to someone the step's delegable_to allows -- an offering manager of the
    slot's offering, or a holder of an evaluator role on the proposal -- or take it back with a null
    user_uuid. Its holders and the call's managers may; the person it is handed to accepts or declines
    it.

    Args:
        uuid (UUID):
        body (DelegateStepContributionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StepContribution
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
