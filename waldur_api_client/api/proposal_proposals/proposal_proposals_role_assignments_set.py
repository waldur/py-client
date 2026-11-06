from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.proposal_role_assign_request import ProposalRoleAssignRequest
from ...models.proposal_role_assignment import ProposalRoleAssignment
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    *,
    body: ProposalRoleAssignRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/proposal-proposals/{uuid}/role_assignments/",
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
    body: ProposalRoleAssignRequest,
) -> Response[ProposalRoleAssignment]:
    """Assign an evaluator role on the proposal. Call managers at any time, the completer of an assignment
    step for the role while it runs -- who may make someone the lead only while the role has none, or
    when they are its lead handing it over. Refused for an ineligible user, a recorded conflict of
    interest, a member of the applicant team, or one holder too many.

    Args:
        uuid (UUID):
        body (ProposalRoleAssignRequest):

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
    body: ProposalRoleAssignRequest,
) -> ProposalRoleAssignment:
    """Assign an evaluator role on the proposal. Call managers at any time, the completer of an assignment
    step for the role while it runs -- who may make someone the lead only while the role has none, or
    when they are its lead handing it over. Refused for an ineligible user, a recorded conflict of
    interest, a member of the applicant team, or one holder too many.

    Args:
        uuid (UUID):
        body (ProposalRoleAssignRequest):

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
    body: ProposalRoleAssignRequest,
) -> Response[ProposalRoleAssignment]:
    """Assign an evaluator role on the proposal. Call managers at any time, the completer of an assignment
    step for the role while it runs -- who may make someone the lead only while the role has none, or
    when they are its lead handing it over. Refused for an ineligible user, a recorded conflict of
    interest, a member of the applicant team, or one holder too many.

    Args:
        uuid (UUID):
        body (ProposalRoleAssignRequest):

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
    body: ProposalRoleAssignRequest,
) -> ProposalRoleAssignment:
    """Assign an evaluator role on the proposal. Call managers at any time, the completer of an assignment
    step for the role while it runs -- who may make someone the lead only while the role has none, or
    when they are its lead handing it over. Refused for an ineligible user, a recorded conflict of
    interest, a member of the applicant team, or one holder too many.

    Args:
        uuid (UUID):
        body (ProposalRoleAssignRequest):

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
