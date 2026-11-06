from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.proposal_change_request import ProposalChangeRequest
from ...models.request_changes_request import RequestChangesRequest
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    *,
    body: RequestChangesRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/proposal-proposals/{uuid}/request_changes/",
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
    body: RequestChangesRequest,
) -> Response[ProposalChangeRequest]:
    """Send a proposal in review back to its applicant to change the parts named, at a step that allows it.
    The proposal stays in review on the step; the parts become editable for the applicant until the
    changes are submitted, and the step does not lapse meanwhile. For whoever acts on the step -- the
    call's managers and organizers, its completer -- and staff; never the applicant team. Changes may be
    requested again after each submission.

    Args:
        uuid (UUID):
        body (RequestChangesRequest):

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
    body: RequestChangesRequest,
) -> ProposalChangeRequest:
    """Send a proposal in review back to its applicant to change the parts named, at a step that allows it.
    The proposal stays in review on the step; the parts become editable for the applicant until the
    changes are submitted, and the step does not lapse meanwhile. For whoever acts on the step -- the
    call's managers and organizers, its completer -- and staff; never the applicant team. Changes may be
    requested again after each submission.

    Args:
        uuid (UUID):
        body (RequestChangesRequest):

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
    body: RequestChangesRequest,
) -> Response[ProposalChangeRequest]:
    """Send a proposal in review back to its applicant to change the parts named, at a step that allows it.
    The proposal stays in review on the step; the parts become editable for the applicant until the
    changes are submitted, and the step does not lapse meanwhile. For whoever acts on the step -- the
    call's managers and organizers, its completer -- and staff; never the applicant team. Changes may be
    requested again after each submission.

    Args:
        uuid (UUID):
        body (RequestChangesRequest):

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
    body: RequestChangesRequest,
) -> ProposalChangeRequest:
    """Send a proposal in review back to its applicant to change the parts named, at a step that allows it.
    The proposal stays in review on the step; the parts become editable for the applicant until the
    changes are submitted, and the step does not lapse meanwhile. For whoever acts on the step -- the
    call's managers and organizers, its completer -- and staff; never the applicant team. Changes may be
    requested again after each submission.

    Args:
        uuid (UUID):
        body (RequestChangesRequest):

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
