import datetime
from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.remote_project_usage_report import RemoteProjectUsageReport
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    end: Union[Unset, datetime.date] = UNSET,
    start: Union[Unset, datetime.date] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_end: Union[Unset, str] = UNSET
    if not isinstance(end, Unset):
        json_end = end.isoformat()
    params["end"] = json_end

    json_start: Union[Unset, str] = UNSET
    if not isinstance(start, Unset):
        json_start = start.isoformat()
    params["start"] = json_start

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/openportal-remote-projects/{uuid}/usage-report/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> RemoteProjectUsageReport:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = RemoteProjectUsageReport.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[RemoteProjectUsageReport]:
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
    end: Union[Unset, datetime.date] = UNSET,
    start: Union[Unset, datetime.date] = UNSET,
) -> Response[RemoteProjectUsageReport]:
    """Usage of the award over a date range, across every project it has been attached to. Each project's
    usage counts only for the days the award was attached there; on the day the award moved, the project
    it moved to claims the whole day. A window on a project the caller cannot see is listed without its
    project, but with its start and end dates, and still counts in full; its per-user usage is folded
    into unattributed usage, so that its users' usernames and usage are not shown. Unless staff or
    support, the caller sees per-user usage only for windows on projects they can see. The report is
    labeled with the award's identifier (with none, the local identifier of the latest project it was
    attached to): its project, and the project part of every user identifier in it, are rewritten to
    that, so user identifiers read <user>.<award identifier>, which is a remote portal's identifier and
    matches no local user. Match users by their local username (the values of the report's users
    mapping, and the keys of each day's usage) instead.

    Args:
        uuid (UUID):
        end (Union[Unset, datetime.date]):
        start (Union[Unset, datetime.date]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemoteProjectUsageReport]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        end=end,
        start=start,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    end: Union[Unset, datetime.date] = UNSET,
    start: Union[Unset, datetime.date] = UNSET,
) -> RemoteProjectUsageReport:
    """Usage of the award over a date range, across every project it has been attached to. Each project's
    usage counts only for the days the award was attached there; on the day the award moved, the project
    it moved to claims the whole day. A window on a project the caller cannot see is listed without its
    project, but with its start and end dates, and still counts in full; its per-user usage is folded
    into unattributed usage, so that its users' usernames and usage are not shown. Unless staff or
    support, the caller sees per-user usage only for windows on projects they can see. The report is
    labeled with the award's identifier (with none, the local identifier of the latest project it was
    attached to): its project, and the project part of every user identifier in it, are rewritten to
    that, so user identifiers read <user>.<award identifier>, which is a remote portal's identifier and
    matches no local user. Match users by their local username (the values of the report's users
    mapping, and the keys of each day's usage) instead.

    Args:
        uuid (UUID):
        end (Union[Unset, datetime.date]):
        start (Union[Unset, datetime.date]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemoteProjectUsageReport
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        end=end,
        start=start,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    end: Union[Unset, datetime.date] = UNSET,
    start: Union[Unset, datetime.date] = UNSET,
) -> Response[RemoteProjectUsageReport]:
    """Usage of the award over a date range, across every project it has been attached to. Each project's
    usage counts only for the days the award was attached there; on the day the award moved, the project
    it moved to claims the whole day. A window on a project the caller cannot see is listed without its
    project, but with its start and end dates, and still counts in full; its per-user usage is folded
    into unattributed usage, so that its users' usernames and usage are not shown. Unless staff or
    support, the caller sees per-user usage only for windows on projects they can see. The report is
    labeled with the award's identifier (with none, the local identifier of the latest project it was
    attached to): its project, and the project part of every user identifier in it, are rewritten to
    that, so user identifiers read <user>.<award identifier>, which is a remote portal's identifier and
    matches no local user. Match users by their local username (the values of the report's users
    mapping, and the keys of each day's usage) instead.

    Args:
        uuid (UUID):
        end (Union[Unset, datetime.date]):
        start (Union[Unset, datetime.date]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemoteProjectUsageReport]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        end=end,
        start=start,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    end: Union[Unset, datetime.date] = UNSET,
    start: Union[Unset, datetime.date] = UNSET,
) -> RemoteProjectUsageReport:
    """Usage of the award over a date range, across every project it has been attached to. Each project's
    usage counts only for the days the award was attached there; on the day the award moved, the project
    it moved to claims the whole day. A window on a project the caller cannot see is listed without its
    project, but with its start and end dates, and still counts in full; its per-user usage is folded
    into unattributed usage, so that its users' usernames and usage are not shown. Unless staff or
    support, the caller sees per-user usage only for windows on projects they can see. The report is
    labeled with the award's identifier (with none, the local identifier of the latest project it was
    attached to): its project, and the project part of every user identifier in it, are rewritten to
    that, so user identifiers read <user>.<award identifier>, which is a remote portal's identifier and
    matches no local user. Match users by their local username (the values of the report's users
    mapping, and the keys of each day's usage) instead.

    Args:
        uuid (UUID):
        end (Union[Unset, datetime.date]):
        start (Union[Unset, datetime.date]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemoteProjectUsageReport
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            end=end,
            start=start,
        )
    ).parsed
