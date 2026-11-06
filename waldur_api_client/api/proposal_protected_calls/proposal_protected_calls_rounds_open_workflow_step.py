from http import HTTPStatus
from typing import Any, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.lagging_proposals_refusal import LaggingProposalsRefusal
from ...models.open_round_workflow_step_request import OpenRoundWorkflowStepRequest
from ...models.open_round_workflow_step_response import OpenRoundWorkflowStepResponse
from ...types import Response


def _get_kwargs(
    uuid: str,
    obj_uuid: str,
    *,
    body: OpenRoundWorkflowStepRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/open_workflow_step/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[LaggingProposalsRefusal, OpenRoundWorkflowStepResponse]:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = OpenRoundWorkflowStepResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = LaggingProposalsRefusal.from_dict(response.json())

        return response_400
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[LaggingProposalsRefusal, OpenRoundWorkflowStepResponse]]:
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
    body: OpenRoundWorkflowStepRequest,
) -> Response[Union[LaggingProposalsRefusal, OpenRoundWorkflowStepResponse]]:
    """Open a step run once per round (round_scoped) for the round, named by step_uuid or its key. Refused
    while a proposal of the round under evaluation has not reached the step yet, unless forced with a
    reason; that refusal carries lagging_count. The proposals parked on the step before it, waiting to
    be moved on, are moved into it, each committed on its own and listed in advanced, skipped or failed.
    Each contributor of the step gets a round report covering the proposals they hold it for, and one
    mail; the call's managers get one. due_at sets when the step is due in the round. Running it again
    moves in proposals that arrived meanwhile and changes nothing else.

    Args:
        uuid (str):
        obj_uuid (str):
        body (OpenRoundWorkflowStepRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[LaggingProposalsRefusal, OpenRoundWorkflowStepResponse]]
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
    body: OpenRoundWorkflowStepRequest,
) -> Union[LaggingProposalsRefusal, OpenRoundWorkflowStepResponse]:
    """Open a step run once per round (round_scoped) for the round, named by step_uuid or its key. Refused
    while a proposal of the round under evaluation has not reached the step yet, unless forced with a
    reason; that refusal carries lagging_count. The proposals parked on the step before it, waiting to
    be moved on, are moved into it, each committed on its own and listed in advanced, skipped or failed.
    Each contributor of the step gets a round report covering the proposals they hold it for, and one
    mail; the call's managers get one. due_at sets when the step is due in the round. Running it again
    moves in proposals that arrived meanwhile and changes nothing else.

    Args:
        uuid (str):
        obj_uuid (str):
        body (OpenRoundWorkflowStepRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[LaggingProposalsRefusal, OpenRoundWorkflowStepResponse]
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
    body: OpenRoundWorkflowStepRequest,
) -> Response[Union[LaggingProposalsRefusal, OpenRoundWorkflowStepResponse]]:
    """Open a step run once per round (round_scoped) for the round, named by step_uuid or its key. Refused
    while a proposal of the round under evaluation has not reached the step yet, unless forced with a
    reason; that refusal carries lagging_count. The proposals parked on the step before it, waiting to
    be moved on, are moved into it, each committed on its own and listed in advanced, skipped or failed.
    Each contributor of the step gets a round report covering the proposals they hold it for, and one
    mail; the call's managers get one. due_at sets when the step is due in the round. Running it again
    moves in proposals that arrived meanwhile and changes nothing else.

    Args:
        uuid (str):
        obj_uuid (str):
        body (OpenRoundWorkflowStepRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[LaggingProposalsRefusal, OpenRoundWorkflowStepResponse]]
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
    body: OpenRoundWorkflowStepRequest,
) -> Union[LaggingProposalsRefusal, OpenRoundWorkflowStepResponse]:
    """Open a step run once per round (round_scoped) for the round, named by step_uuid or its key. Refused
    while a proposal of the round under evaluation has not reached the step yet, unless forced with a
    reason; that refusal carries lagging_count. The proposals parked on the step before it, waiting to
    be moved on, are moved into it, each committed on its own and listed in advanced, skipped or failed.
    Each contributor of the step gets a round report covering the proposals they hold it for, and one
    mail; the call's managers get one. due_at sets when the step is due in the round. Running it again
    moves in proposals that arrived meanwhile and changes nothing else.

    Args:
        uuid (str):
        obj_uuid (str):
        body (OpenRoundWorkflowStepRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[LaggingProposalsRefusal, OpenRoundWorkflowStepResponse]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            obj_uuid=obj_uuid,
            client=client,
            body=body,
        )
    ).parsed
