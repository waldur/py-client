from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bulk_step_decision import BulkStepDecision
from ...models.decide_workflow_steps_request import DecideWorkflowStepsRequest
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    *,
    body: DecideWorkflowStepsRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/proposal-protected-calls/{uuid}/decide_workflow_steps/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> BulkStepDecision:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = BulkStepDecision.from_dict(response.json())

        return response_200
    if response.status_code == 202:
        response_202 = BulkStepDecision.from_dict(response.json())

        return response_202
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[BulkStepDecision]:
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
    body: DecideWorkflowStepsRequest,
) -> Response[BulkStepDecision]:
    """Decide one decision step for many proposals of the call at once, with one outcome and reason. Each
    proposal is decided as complete_workflow_step decides it on its page -- it must stand on the step,
    the caller must be allowed to act on it, and the step's gates must let the outcome through -- each
    in its own transaction, so one refused does not undo the others. Each comes back decided, or refused
    with the reason, in the order named; of a proposal the caller may not act on only its id and the
    reason are told. Refused with 403, recording nothing, when the caller may act on none of the
    selected proposals standing on the step, and with 400 when none stands on it. With dry_run nothing
    is decided: every proposal is checked as the run would check it. A selection of up to 25 proposals
    is decided, or previewed, within the request (200; a preview is not recorded); a larger one is
    recorded and run in the background (202, state pending): read its progress and results from
    proposal-bulk-step-decisions. A real run is recorded with one event on the call. Only a decision
    step that is neither the allocation decision nor completed once per round is decided this way.

    Args:
        uuid (UUID):
        body (DecideWorkflowStepsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkStepDecision]
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
    body: DecideWorkflowStepsRequest,
) -> BulkStepDecision:
    """Decide one decision step for many proposals of the call at once, with one outcome and reason. Each
    proposal is decided as complete_workflow_step decides it on its page -- it must stand on the step,
    the caller must be allowed to act on it, and the step's gates must let the outcome through -- each
    in its own transaction, so one refused does not undo the others. Each comes back decided, or refused
    with the reason, in the order named; of a proposal the caller may not act on only its id and the
    reason are told. Refused with 403, recording nothing, when the caller may act on none of the
    selected proposals standing on the step, and with 400 when none stands on it. With dry_run nothing
    is decided: every proposal is checked as the run would check it. A selection of up to 25 proposals
    is decided, or previewed, within the request (200; a preview is not recorded); a larger one is
    recorded and run in the background (202, state pending): read its progress and results from
    proposal-bulk-step-decisions. A real run is recorded with one event on the call. Only a decision
    step that is neither the allocation decision nor completed once per round is decided this way.

    Args:
        uuid (UUID):
        body (DecideWorkflowStepsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkStepDecision
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
    body: DecideWorkflowStepsRequest,
) -> Response[BulkStepDecision]:
    """Decide one decision step for many proposals of the call at once, with one outcome and reason. Each
    proposal is decided as complete_workflow_step decides it on its page -- it must stand on the step,
    the caller must be allowed to act on it, and the step's gates must let the outcome through -- each
    in its own transaction, so one refused does not undo the others. Each comes back decided, or refused
    with the reason, in the order named; of a proposal the caller may not act on only its id and the
    reason are told. Refused with 403, recording nothing, when the caller may act on none of the
    selected proposals standing on the step, and with 400 when none stands on it. With dry_run nothing
    is decided: every proposal is checked as the run would check it. A selection of up to 25 proposals
    is decided, or previewed, within the request (200; a preview is not recorded); a larger one is
    recorded and run in the background (202, state pending): read its progress and results from
    proposal-bulk-step-decisions. A real run is recorded with one event on the call. Only a decision
    step that is neither the allocation decision nor completed once per round is decided this way.

    Args:
        uuid (UUID):
        body (DecideWorkflowStepsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkStepDecision]
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
    body: DecideWorkflowStepsRequest,
) -> BulkStepDecision:
    """Decide one decision step for many proposals of the call at once, with one outcome and reason. Each
    proposal is decided as complete_workflow_step decides it on its page -- it must stand on the step,
    the caller must be allowed to act on it, and the step's gates must let the outcome through -- each
    in its own transaction, so one refused does not undo the others. Each comes back decided, or refused
    with the reason, in the order named; of a proposal the caller may not act on only its id and the
    reason are told. Refused with 403, recording nothing, when the caller may act on none of the
    selected proposals standing on the step, and with 400 when none stands on it. With dry_run nothing
    is decided: every proposal is checked as the run would check it. A selection of up to 25 proposals
    is decided, or previewed, within the request (200; a preview is not recorded); a larger one is
    recorded and run in the background (202, state pending): read its progress and results from
    proposal-bulk-step-decisions. A real run is recorded with one event on the call. Only a decision
    step that is neither the allocation decision nor completed once per round is decided this way.

    Args:
        uuid (UUID):
        body (DecideWorkflowStepsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkStepDecision
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
