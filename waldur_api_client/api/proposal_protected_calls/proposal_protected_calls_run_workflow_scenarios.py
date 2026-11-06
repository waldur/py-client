from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.call_workflow_scenarios import CallWorkflowScenarios
from ...types import Response


def _get_kwargs(
    uuid: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/proposal-protected-calls/{uuid}/run-workflow-scenarios/",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> CallWorkflowScenarios:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 202:
        response_202 = CallWorkflowScenarios.from_dict(response.json())

        return response_202
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CallWorkflowScenarios]:
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
) -> Response[CallWorkflowScenarios]:
    """Run the call's saved scenarios

     Dry-run each scenario of the template the call was created from on the call, at most 20, in the
    background, and keep the results on the call's latest workflow version; a run already on its way is
    not started again. Answers at once with the results so far and status 'running': poll workflow-
    scenarios until its status is 'idle' again. Each run is rolled back: nothing is kept or sent.
    Results are not kept when another dry run of the call got in the way; 'error' then says so. For
    those who configure the call, and staff.

    Args:
        uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CallWorkflowScenarios]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
) -> CallWorkflowScenarios:
    """Run the call's saved scenarios

     Dry-run each scenario of the template the call was created from on the call, at most 20, in the
    background, and keep the results on the call's latest workflow version; a run already on its way is
    not started again. Answers at once with the results so far and status 'running': poll workflow-
    scenarios until its status is 'idle' again. Each run is rolled back: nothing is kept or sent.
    Results are not kept when another dry run of the call got in the way; 'error' then says so. For
    those who configure the call, and staff.

    Args:
        uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CallWorkflowScenarios
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[CallWorkflowScenarios]:
    """Run the call's saved scenarios

     Dry-run each scenario of the template the call was created from on the call, at most 20, in the
    background, and keep the results on the call's latest workflow version; a run already on its way is
    not started again. Answers at once with the results so far and status 'running': poll workflow-
    scenarios until its status is 'idle' again. Each run is rolled back: nothing is kept or sent.
    Results are not kept when another dry run of the call got in the way; 'error' then says so. For
    those who configure the call, and staff.

    Args:
        uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CallWorkflowScenarios]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
) -> CallWorkflowScenarios:
    """Run the call's saved scenarios

     Dry-run each scenario of the template the call was created from on the call, at most 20, in the
    background, and keep the results on the call's latest workflow version; a run already on its way is
    not started again. Answers at once with the results so far and status 'running': poll workflow-
    scenarios until its status is 'idle' again. Each run is rolled back: nothing is kept or sent.
    Results are not kept when another dry run of the call got in the way; 'error' then says so. For
    those who configure the call, and staff.

    Args:
        uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CallWorkflowScenarios
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
        )
    ).parsed
