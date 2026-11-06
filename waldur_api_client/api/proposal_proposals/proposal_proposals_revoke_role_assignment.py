from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.proposal_role_assignment import ProposalRoleAssignment
from ...models.proposal_role_assignment_action_request import ProposalRoleAssignmentActionRequest
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    *,
    body: ProposalRoleAssignmentActionRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/proposal-proposals/{uuid}/revoke_role_assignment/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> ProposalRoleAssignment:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = ProposalRoleAssignment.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ProposalRoleAssignment]:
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
    body: ProposalRoleAssignmentActionRequest,
) -> Response[ProposalRoleAssignment]:
    """Take an evaluator role away. The holder loses the access it gave; the assignment is kept as history.
    The completer of an assignment step takes away only their own; the call manager anyone's.

    Args:
        uuid (UUID):
        body (ProposalRoleAssignmentActionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProposalRoleAssignment]
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
    body: ProposalRoleAssignmentActionRequest,
) -> ProposalRoleAssignment:
    """Take an evaluator role away. The holder loses the access it gave; the assignment is kept as history.
    The completer of an assignment step takes away only their own; the call manager anyone's.

    Args:
        uuid (UUID):
        body (ProposalRoleAssignmentActionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProposalRoleAssignment
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
    body: ProposalRoleAssignmentActionRequest,
) -> Response[ProposalRoleAssignment]:
    """Take an evaluator role away. The holder loses the access it gave; the assignment is kept as history.
    The completer of an assignment step takes away only their own; the call manager anyone's.

    Args:
        uuid (UUID):
        body (ProposalRoleAssignmentActionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProposalRoleAssignment]
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
    body: ProposalRoleAssignmentActionRequest,
) -> ProposalRoleAssignment:
    """Take an evaluator role away. The holder loses the access it gave; the assignment is kept as history.
    The completer of an assignment step takes away only their own; the call manager anyone's.

    Args:
        uuid (UUID):
        body (ProposalRoleAssignmentActionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProposalRoleAssignment
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
