from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dry_run_view_as_result import DryRunViewAsResult
from ...models.proposal_preview_as_request import ProposalPreviewAsRequest
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    *,
    body: ProposalPreviewAsRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/proposal-proposals/{uuid}/preview-as/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> DryRunViewAsResult:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = DryRunViewAsResult.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DryRunViewAsResult]:
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
    body: ProposalPreviewAsRequest,
) -> Response[DryRunViewAsResult]:
    """Preview the proposal as a role of its call

     The proposal page as a role of its call sees it now: the real read endpoints answering a synthetic
    person given the role, in a transaction that is rolled back. No real person is viewed as, nothing is
    saved and no mail is sent. For the same readers as workflow-timeline.

    Args:
        uuid (UUID):
        body (ProposalPreviewAsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DryRunViewAsResult]
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
    body: ProposalPreviewAsRequest,
) -> DryRunViewAsResult:
    """Preview the proposal as a role of its call

     The proposal page as a role of its call sees it now: the real read endpoints answering a synthetic
    person given the role, in a transaction that is rolled back. No real person is viewed as, nothing is
    saved and no mail is sent. For the same readers as workflow-timeline.

    Args:
        uuid (UUID):
        body (ProposalPreviewAsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DryRunViewAsResult
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
    body: ProposalPreviewAsRequest,
) -> Response[DryRunViewAsResult]:
    """Preview the proposal as a role of its call

     The proposal page as a role of its call sees it now: the real read endpoints answering a synthetic
    person given the role, in a transaction that is rolled back. No real person is viewed as, nothing is
    saved and no mail is sent. For the same readers as workflow-timeline.

    Args:
        uuid (UUID):
        body (ProposalPreviewAsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DryRunViewAsResult]
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
    body: ProposalPreviewAsRequest,
) -> DryRunViewAsResult:
    """Preview the proposal as a role of its call

     The proposal page as a role of its call sees it now: the real read endpoints answering a synthetic
    person given the role, in a transaction that is rolled back. No real person is viewed as, nothing is
    saved and no mail is sent. For the same readers as workflow-timeline.

    Args:
        uuid (UUID):
        body (ProposalPreviewAsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DryRunViewAsResult
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
