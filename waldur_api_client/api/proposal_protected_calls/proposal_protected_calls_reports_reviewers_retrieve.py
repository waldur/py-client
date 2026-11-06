import datetime
from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.reviewer_report import ReviewerReport
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    round_uuid: Union[Unset, UUID] = UNSET,
    submitted_from: Union[Unset, datetime.date] = UNSET,
    submitted_to: Union[Unset, datetime.date] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_round_uuid: Union[Unset, str] = UNSET
    if not isinstance(round_uuid, Unset):
        json_round_uuid = str(round_uuid)
    params["round_uuid"] = json_round_uuid

    json_submitted_from: Union[Unset, str] = UNSET
    if not isinstance(submitted_from, Unset):
        json_submitted_from = submitted_from.isoformat()
    params["submitted_from"] = json_submitted_from

    json_submitted_to: Union[Unset, str] = UNSET
    if not isinstance(submitted_to, Unset):
        json_submitted_to = submitted_to.isoformat()
    params["submitted_to"] = json_submitted_to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/proposal-protected-calls/{uuid}/reports/reviewers/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> ReviewerReport:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = ReviewerReport.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ReviewerReport]:
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
    round_uuid: Union[Unset, UUID] = UNSET,
    submitted_from: Union[Unset, datetime.date] = UNSET,
    submitted_to: Union[Unset, datetime.date] = UNSET,
) -> Response[ReviewerReport]:
    """Per reviewer of the proposals: assignments sent and how they were answered, reviews by state and
    overdue, the median days to answer and to review, and the mean score given. Deactivated reviewers
    are listed too. Over the call alone, for its managers, staff and support.

    Args:
        uuid (UUID):
        round_uuid (Union[Unset, UUID]):
        submitted_from (Union[Unset, datetime.date]):
        submitted_to (Union[Unset, datetime.date]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReviewerReport]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        round_uuid=round_uuid,
        submitted_from=submitted_from,
        submitted_to=submitted_to,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    round_uuid: Union[Unset, UUID] = UNSET,
    submitted_from: Union[Unset, datetime.date] = UNSET,
    submitted_to: Union[Unset, datetime.date] = UNSET,
) -> ReviewerReport:
    """Per reviewer of the proposals: assignments sent and how they were answered, reviews by state and
    overdue, the median days to answer and to review, and the mean score given. Deactivated reviewers
    are listed too. Over the call alone, for its managers, staff and support.

    Args:
        uuid (UUID):
        round_uuid (Union[Unset, UUID]):
        submitted_from (Union[Unset, datetime.date]):
        submitted_to (Union[Unset, datetime.date]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReviewerReport
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        round_uuid=round_uuid,
        submitted_from=submitted_from,
        submitted_to=submitted_to,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    round_uuid: Union[Unset, UUID] = UNSET,
    submitted_from: Union[Unset, datetime.date] = UNSET,
    submitted_to: Union[Unset, datetime.date] = UNSET,
) -> Response[ReviewerReport]:
    """Per reviewer of the proposals: assignments sent and how they were answered, reviews by state and
    overdue, the median days to answer and to review, and the mean score given. Deactivated reviewers
    are listed too. Over the call alone, for its managers, staff and support.

    Args:
        uuid (UUID):
        round_uuid (Union[Unset, UUID]):
        submitted_from (Union[Unset, datetime.date]):
        submitted_to (Union[Unset, datetime.date]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReviewerReport]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        round_uuid=round_uuid,
        submitted_from=submitted_from,
        submitted_to=submitted_to,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    round_uuid: Union[Unset, UUID] = UNSET,
    submitted_from: Union[Unset, datetime.date] = UNSET,
    submitted_to: Union[Unset, datetime.date] = UNSET,
) -> ReviewerReport:
    """Per reviewer of the proposals: assignments sent and how they were answered, reviews by state and
    overdue, the median days to answer and to review, and the mean score given. Deactivated reviewers
    are listed too. Over the call alone, for its managers, staff and support.

    Args:
        uuid (UUID):
        round_uuid (Union[Unset, UUID]):
        submitted_from (Union[Unset, datetime.date]):
        submitted_to (Union[Unset, datetime.date]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReviewerReport
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            round_uuid=round_uuid,
            submitted_from=submitted_from,
            submitted_to=submitted_to,
        )
    ).parsed
