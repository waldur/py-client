from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.invite_suggested_reviewers_response import InviteSuggestedReviewersResponse
from ...models.suggested_reviewers_action_request import SuggestedReviewersActionRequest
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    *,
    body: SuggestedReviewersActionRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/proposal-proposals/{uuid}/invite_suggested_reviewers/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> InviteSuggestedReviewersResponse:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = InviteSuggestedReviewersResponse.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[InviteSuggestedReviewersResponse]:
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
    body: SuggestedReviewersActionRequest,
) -> Response[InviteSuggestedReviewersResponse]:
    """Invite suggested reviewers to the call's reviewer pool, as an invitation by e-mail is sent: the
    call's response window and the invitation e-mail apply. Each suggestion of the person follows the
    invitation. A person already in the pool is linked to their entry instead.

    Args:
        uuid (UUID):
        body (SuggestedReviewersActionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InviteSuggestedReviewersResponse]
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
    body: SuggestedReviewersActionRequest,
) -> InviteSuggestedReviewersResponse:
    """Invite suggested reviewers to the call's reviewer pool, as an invitation by e-mail is sent: the
    call's response window and the invitation e-mail apply. Each suggestion of the person follows the
    invitation. A person already in the pool is linked to their entry instead.

    Args:
        uuid (UUID):
        body (SuggestedReviewersActionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InviteSuggestedReviewersResponse
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
    body: SuggestedReviewersActionRequest,
) -> Response[InviteSuggestedReviewersResponse]:
    """Invite suggested reviewers to the call's reviewer pool, as an invitation by e-mail is sent: the
    call's response window and the invitation e-mail apply. Each suggestion of the person follows the
    invitation. A person already in the pool is linked to their entry instead.

    Args:
        uuid (UUID):
        body (SuggestedReviewersActionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InviteSuggestedReviewersResponse]
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
    body: SuggestedReviewersActionRequest,
) -> InviteSuggestedReviewersResponse:
    """Invite suggested reviewers to the call's reviewer pool, as an invitation by e-mail is sent: the
    call's response window and the invitation e-mail apply. Each suggestion of the person follows the
    invitation. A person already in the pool is linked to their entry instead.

    Args:
        uuid (UUID):
        body (SuggestedReviewersActionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InviteSuggestedReviewersResponse
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
