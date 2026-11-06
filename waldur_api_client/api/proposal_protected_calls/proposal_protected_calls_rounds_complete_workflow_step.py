from http import HTTPStatus
from typing import Any, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.complete_round_workflow_step_request import CompleteRoundWorkflowStepRequest
from ...models.complete_round_workflow_step_response import CompleteRoundWorkflowStepResponse
from ...types import Response


def _get_kwargs(
    uuid: str,
    obj_uuid: str,
    *,
    body: CompleteRoundWorkflowStepRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/complete_workflow_step/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> CompleteRoundWorkflowStepResponse:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = CompleteRoundWorkflowStepResponse.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CompleteRoundWorkflowStepResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: str,
    obj_uuid: str,
    *,
    client: AuthenticatedClient,
    body: CompleteRoundWorkflowStepRequest,
) -> Response[CompleteRoundWorkflowStepResponse]:
    """Complete a call step -- named by step_uuid or its key -- with one outcome for every proposal of the
    round where that step is active, each as if completed on the proposal: same gates, notifications and
    ledger. Each proposal is committed on its own: one whose step cannot be completed, for whatever
    reason, is rolled back alone and listed in failed with the reason, and the rest of the round goes
    on. Proposals not at the step are listed in skipped. Running it again changes nothing for proposals
    already completed. The allocation decision is refused: it is completed on each proposal. Feedback
    per proposal is stored as its outcome reason for the step; on a step whose report is released to the
    applicant it is withheld until then, as when the step is completed on the proposal.

    Args:
        uuid (str):
        obj_uuid (str):
        body (CompleteRoundWorkflowStepRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompleteRoundWorkflowStepResponse]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        obj_uuid=obj_uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: str,
    obj_uuid: str,
    *,
    client: AuthenticatedClient,
    body: CompleteRoundWorkflowStepRequest,
) -> CompleteRoundWorkflowStepResponse:
    """Complete a call step -- named by step_uuid or its key -- with one outcome for every proposal of the
    round where that step is active, each as if completed on the proposal: same gates, notifications and
    ledger. Each proposal is committed on its own: one whose step cannot be completed, for whatever
    reason, is rolled back alone and listed in failed with the reason, and the rest of the round goes
    on. Proposals not at the step are listed in skipped. Running it again changes nothing for proposals
    already completed. The allocation decision is refused: it is completed on each proposal. Feedback
    per proposal is stored as its outcome reason for the step; on a step whose report is released to the
    applicant it is withheld until then, as when the step is completed on the proposal.

    Args:
        uuid (str):
        obj_uuid (str):
        body (CompleteRoundWorkflowStepRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompleteRoundWorkflowStepResponse
    """

    return sync_detailed(
        uuid=uuid,
        obj_uuid=obj_uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    obj_uuid: str,
    *,
    client: AuthenticatedClient,
    body: CompleteRoundWorkflowStepRequest,
) -> Response[CompleteRoundWorkflowStepResponse]:
    """Complete a call step -- named by step_uuid or its key -- with one outcome for every proposal of the
    round where that step is active, each as if completed on the proposal: same gates, notifications and
    ledger. Each proposal is committed on its own: one whose step cannot be completed, for whatever
    reason, is rolled back alone and listed in failed with the reason, and the rest of the round goes
    on. Proposals not at the step are listed in skipped. Running it again changes nothing for proposals
    already completed. The allocation decision is refused: it is completed on each proposal. Feedback
    per proposal is stored as its outcome reason for the step; on a step whose report is released to the
    applicant it is withheld until then, as when the step is completed on the proposal.

    Args:
        uuid (str):
        obj_uuid (str):
        body (CompleteRoundWorkflowStepRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompleteRoundWorkflowStepResponse]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        obj_uuid=obj_uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: str,
    obj_uuid: str,
    *,
    client: AuthenticatedClient,
    body: CompleteRoundWorkflowStepRequest,
) -> CompleteRoundWorkflowStepResponse:
    """Complete a call step -- named by step_uuid or its key -- with one outcome for every proposal of the
    round where that step is active, each as if completed on the proposal: same gates, notifications and
    ledger. Each proposal is committed on its own: one whose step cannot be completed, for whatever
    reason, is rolled back alone and listed in failed with the reason, and the rest of the round goes
    on. Proposals not at the step are listed in skipped. Running it again changes nothing for proposals
    already completed. The allocation decision is refused: it is completed on each proposal. Feedback
    per proposal is stored as its outcome reason for the step; on a step whose report is released to the
    applicant it is withheld until then, as when the step is completed on the proposal.

    Args:
        uuid (str):
        obj_uuid (str):
        body (CompleteRoundWorkflowStepRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompleteRoundWorkflowStepResponse
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            obj_uuid=obj_uuid,
            client=client,
            body=body,
        )
    ).parsed
