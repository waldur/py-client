from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.assignment_import_request import AssignmentImportRequest
from ...models.assignment_import_response import AssignmentImportResponse
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    *,
    body: AssignmentImportRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/proposal-protected-calls/{uuid}/import-assignments/",
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> AssignmentImportResponse:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = AssignmentImportResponse.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AssignmentImportResponse]:
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
    body: AssignmentImportRequest,
) -> Response[AssignmentImportResponse]:
    """Assign proposals of a round to reviewers from a CSV file with a header row: reviewer_email, and
    proposal_slug or proposal_uuid. Rows are grouped by reviewer and assigned as create-manual-
    assignment does, in the reviewer's draft manual batch: already assigned proposals are skipped,
    conflicts of interest give conflict-blocked items, and the workload limit applies unless overridden.
    Every row is reported with a status (ready, created, coi_blocked, skipped, error) and a reason. A
    dry run, the default, changes nothing; otherwise the valid rows are applied in one transaction.
    Nothing is sent to reviewers: send the draft batches when they are ready. Refused for a file over 1
    MB, not UTF-8, without the required columns, or with more rows than the round's proposals times the
    call's reviewers.

    Args:
        uuid (UUID):
        body (AssignmentImportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssignmentImportResponse]
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
    body: AssignmentImportRequest,
) -> AssignmentImportResponse:
    """Assign proposals of a round to reviewers from a CSV file with a header row: reviewer_email, and
    proposal_slug or proposal_uuid. Rows are grouped by reviewer and assigned as create-manual-
    assignment does, in the reviewer's draft manual batch: already assigned proposals are skipped,
    conflicts of interest give conflict-blocked items, and the workload limit applies unless overridden.
    Every row is reported with a status (ready, created, coi_blocked, skipped, error) and a reason. A
    dry run, the default, changes nothing; otherwise the valid rows are applied in one transaction.
    Nothing is sent to reviewers: send the draft batches when they are ready. Refused for a file over 1
    MB, not UTF-8, without the required columns, or with more rows than the round's proposals times the
    call's reviewers.

    Args:
        uuid (UUID):
        body (AssignmentImportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssignmentImportResponse
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
    body: AssignmentImportRequest,
) -> Response[AssignmentImportResponse]:
    """Assign proposals of a round to reviewers from a CSV file with a header row: reviewer_email, and
    proposal_slug or proposal_uuid. Rows are grouped by reviewer and assigned as create-manual-
    assignment does, in the reviewer's draft manual batch: already assigned proposals are skipped,
    conflicts of interest give conflict-blocked items, and the workload limit applies unless overridden.
    Every row is reported with a status (ready, created, coi_blocked, skipped, error) and a reason. A
    dry run, the default, changes nothing; otherwise the valid rows are applied in one transaction.
    Nothing is sent to reviewers: send the draft batches when they are ready. Refused for a file over 1
    MB, not UTF-8, without the required columns, or with more rows than the round's proposals times the
    call's reviewers.

    Args:
        uuid (UUID):
        body (AssignmentImportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssignmentImportResponse]
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
    body: AssignmentImportRequest,
) -> AssignmentImportResponse:
    """Assign proposals of a round to reviewers from a CSV file with a header row: reviewer_email, and
    proposal_slug or proposal_uuid. Rows are grouped by reviewer and assigned as create-manual-
    assignment does, in the reviewer's draft manual batch: already assigned proposals are skipped,
    conflicts of interest give conflict-blocked items, and the workload limit applies unless overridden.
    Every row is reported with a status (ready, created, coi_blocked, skipped, error) and a reason. A
    dry run, the default, changes nothing; otherwise the valid rows are applied in one transaction.
    Nothing is sent to reviewers: send the draft batches when they are ready. Refused for a file over 1
    MB, not UTF-8, without the required columns, or with more rows than the round's proposals times the
    call's reviewers.

    Args:
        uuid (UUID):
        body (AssignmentImportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssignmentImportResponse
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
