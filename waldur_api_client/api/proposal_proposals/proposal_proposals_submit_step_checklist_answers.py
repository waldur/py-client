from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.answer_submit_request import AnswerSubmitRequest
from ...models.proposal_checklist_answer_submit_response import ProposalChecklistAnswerSubmitResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    body: list["AnswerSubmitRequest"],
    contribution_uuid: Union[Unset, UUID] = UNSET,
    step: Union[Unset, str] = UNSET,
    step_uuid: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_contribution_uuid: Union[Unset, str] = UNSET
    if not isinstance(contribution_uuid, Unset):
        json_contribution_uuid = str(contribution_uuid)
    params["contribution_uuid"] = json_contribution_uuid

    params["step"] = step

    json_step_uuid: Union[Unset, str] = UNSET
    if not isinstance(step_uuid, Unset):
        json_step_uuid = str(step_uuid)
    params["step_uuid"] = json_step_uuid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/proposal-proposals/{uuid}/submit-step-checklist-answers/",
        "params": params,
    }

    _kwargs["json"] = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _kwargs["json"].append(body_item)

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[Any, ProposalChecklistAnswerSubmitResponse]:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = ProposalChecklistAnswerSubmitResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = response.json()
        return response_400
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ProposalChecklistAnswerSubmitResponse]]:
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
    body: list["AnswerSubmitRequest"],
    contribution_uuid: Union[Unset, UUID] = UNSET,
    step: Union[Unset, str] = UNSET,
    step_uuid: Union[Unset, UUID] = UNSET,
) -> Response[Union[Any, ProposalChecklistAnswerSubmitResponse]]:
    """Submit answers to a workflow step's checklist.

    Args:
        uuid (UUID):
        contribution_uuid (Union[Unset, UUID]):
        step (Union[Unset, str]):
        step_uuid (Union[Unset, UUID]):
        body (list['AnswerSubmitRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProposalChecklistAnswerSubmitResponse]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
        contribution_uuid=contribution_uuid,
        step=step,
        step_uuid=step_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: list["AnswerSubmitRequest"],
    contribution_uuid: Union[Unset, UUID] = UNSET,
    step: Union[Unset, str] = UNSET,
    step_uuid: Union[Unset, UUID] = UNSET,
) -> Union[Any, ProposalChecklistAnswerSubmitResponse]:
    """Submit answers to a workflow step's checklist.

    Args:
        uuid (UUID):
        contribution_uuid (Union[Unset, UUID]):
        step (Union[Unset, str]):
        step_uuid (Union[Unset, UUID]):
        body (list['AnswerSubmitRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProposalChecklistAnswerSubmitResponse]
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        body=body,
        contribution_uuid=contribution_uuid,
        step=step,
        step_uuid=step_uuid,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: list["AnswerSubmitRequest"],
    contribution_uuid: Union[Unset, UUID] = UNSET,
    step: Union[Unset, str] = UNSET,
    step_uuid: Union[Unset, UUID] = UNSET,
) -> Response[Union[Any, ProposalChecklistAnswerSubmitResponse]]:
    """Submit answers to a workflow step's checklist.

    Args:
        uuid (UUID):
        contribution_uuid (Union[Unset, UUID]):
        step (Union[Unset, str]):
        step_uuid (Union[Unset, UUID]):
        body (list['AnswerSubmitRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProposalChecklistAnswerSubmitResponse]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
        contribution_uuid=contribution_uuid,
        step=step,
        step_uuid=step_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: list["AnswerSubmitRequest"],
    contribution_uuid: Union[Unset, UUID] = UNSET,
    step: Union[Unset, str] = UNSET,
    step_uuid: Union[Unset, UUID] = UNSET,
) -> Union[Any, ProposalChecklistAnswerSubmitResponse]:
    """Submit answers to a workflow step's checklist.

    Args:
        uuid (UUID):
        contribution_uuid (Union[Unset, UUID]):
        step (Union[Unset, str]):
        step_uuid (Union[Unset, UUID]):
        body (list['AnswerSubmitRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProposalChecklistAnswerSubmitResponse]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
            contribution_uuid=contribution_uuid,
            step=step,
            step_uuid=step_uuid,
        )
    ).parsed
