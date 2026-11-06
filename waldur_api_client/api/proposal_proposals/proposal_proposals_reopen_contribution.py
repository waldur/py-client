from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.proposal_change_request import ProposalChangeRequest
from ...models.reopen_contribution_request import ReopenContributionRequest
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    *,
    body: ReopenContributionRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/proposal-proposals/{uuid}/reopen_contribution/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> ProposalChangeRequest:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = ProposalChangeRequest.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ProposalChangeRequest]:
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
    body: ReopenContributionRequest,
) -> Response[ProposalChangeRequest]:
    """Reopen a submitted contribution -- one offering's technical assessment, say -- for its contributor
    to revise and submit again. While its step is active, or completed with the proposal waiting to be
    advanced by hand, in which case the step becomes active again. Its answers are kept; its outcome
    counts again once resubmitted. Not for reviews. For the call's managers and organizers, and staff.
    The applicant is not told.

    Args:
        uuid (UUID):
        body (ReopenContributionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProposalChangeRequest]
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
    body: ReopenContributionRequest,
) -> ProposalChangeRequest:
    """Reopen a submitted contribution -- one offering's technical assessment, say -- for its contributor
    to revise and submit again. While its step is active, or completed with the proposal waiting to be
    advanced by hand, in which case the step becomes active again. Its answers are kept; its outcome
    counts again once resubmitted. Not for reviews. For the call's managers and organizers, and staff.
    The applicant is not told.

    Args:
        uuid (UUID):
        body (ReopenContributionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProposalChangeRequest
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
    body: ReopenContributionRequest,
) -> Response[ProposalChangeRequest]:
    """Reopen a submitted contribution -- one offering's technical assessment, say -- for its contributor
    to revise and submit again. While its step is active, or completed with the proposal waiting to be
    advanced by hand, in which case the step becomes active again. Its answers are kept; its outcome
    counts again once resubmitted. Not for reviews. For the call's managers and organizers, and staff.
    The applicant is not told.

    Args:
        uuid (UUID):
        body (ReopenContributionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProposalChangeRequest]
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
    body: ReopenContributionRequest,
) -> ProposalChangeRequest:
    """Reopen a submitted contribution -- one offering's technical assessment, say -- for its contributor
    to revise and submit again. While its step is active, or completed with the proposal waiting to be
    advanced by hand, in which case the step becomes active again. Its answers are kept; its outcome
    counts again once resubmitted. Not for reviews. For the call's managers and organizers, and staff.
    The applicant is not told.

    Args:
        uuid (UUID):
        body (ReopenContributionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProposalChangeRequest
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
