from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.workflow_dry_run import WorkflowDryRun
from ...models.workflow_dry_run_parameters_request import WorkflowDryRunParametersRequest
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    *,
    body: WorkflowDryRunParametersRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/proposal-protected-calls/{uuid}/workflow-dry-run/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> WorkflowDryRun:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = WorkflowDryRun.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[WorkflowDryRun]:
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
    body: WorkflowDryRunParametersRequest,
) -> Response[WorkflowDryRun]:
    """Dry-run the call's workflow

     Replay a path through the call's workflow on a synthetic proposal and return the state of every
    step, the log, every mail the path would send rendered with the real templates, and the outcomes
    tried. Stateless: each request replays its whole list of actions, and rewinding is a shorter list.
    Nothing is sent or kept: the run is rolled back. With view_as, the proposal as a role of the
    workflow description would read it, through the real read endpoints, as a synthetic holder of that
    role. For those who configure the call, and staff; one run per call at a time.

    Args:
        uuid (UUID):
        body (WorkflowDryRunParametersRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WorkflowDryRun]
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
    body: WorkflowDryRunParametersRequest,
) -> WorkflowDryRun:
    """Dry-run the call's workflow

     Replay a path through the call's workflow on a synthetic proposal and return the state of every
    step, the log, every mail the path would send rendered with the real templates, and the outcomes
    tried. Stateless: each request replays its whole list of actions, and rewinding is a shorter list.
    Nothing is sent or kept: the run is rolled back. With view_as, the proposal as a role of the
    workflow description would read it, through the real read endpoints, as a synthetic holder of that
    role. For those who configure the call, and staff; one run per call at a time.

    Args:
        uuid (UUID):
        body (WorkflowDryRunParametersRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WorkflowDryRun
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
    body: WorkflowDryRunParametersRequest,
) -> Response[WorkflowDryRun]:
    """Dry-run the call's workflow

     Replay a path through the call's workflow on a synthetic proposal and return the state of every
    step, the log, every mail the path would send rendered with the real templates, and the outcomes
    tried. Stateless: each request replays its whole list of actions, and rewinding is a shorter list.
    Nothing is sent or kept: the run is rolled back. With view_as, the proposal as a role of the
    workflow description would read it, through the real read endpoints, as a synthetic holder of that
    role. For those who configure the call, and staff; one run per call at a time.

    Args:
        uuid (UUID):
        body (WorkflowDryRunParametersRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WorkflowDryRun]
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
    body: WorkflowDryRunParametersRequest,
) -> WorkflowDryRun:
    """Dry-run the call's workflow

     Replay a path through the call's workflow on a synthetic proposal and return the state of every
    step, the log, every mail the path would send rendered with the real templates, and the outcomes
    tried. Stateless: each request replays its whole list of actions, and rewinding is a shorter list.
    Nothing is sent or kept: the run is rolled back. With view_as, the proposal as a role of the
    workflow description would read it, through the real read endpoints, as a synthetic holder of that
    role. For those who configure the call, and staff; one run per call at a time.

    Args:
        uuid (UUID):
        body (WorkflowDryRunParametersRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WorkflowDryRun
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
