from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delegate_team_slots_request import DelegateTeamSlotsRequest
from ...models.delegate_team_slots_result import DelegateTeamSlotsResult
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    *,
    body: DelegateTeamSlotsRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/proposal-requested-offerings/{uuid}/delegate_slots/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> DelegateTeamSlotsResult:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = DelegateTeamSlotsResult.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DelegateTeamSlotsResult]:
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
    body: DelegateTeamSlotsRequest,
) -> Response[DelegateTeamSlotsResult]:
    """Hand several of the team's open slots to one person, or take them back with a null user_uuid. Each
    slot is handed on as delegate_contribution would; one that cannot be is left as it is and listed
    with why.

    Args:
        uuid (UUID):
        body (DelegateTeamSlotsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DelegateTeamSlotsResult]
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
    body: DelegateTeamSlotsRequest,
) -> DelegateTeamSlotsResult:
    """Hand several of the team's open slots to one person, or take them back with a null user_uuid. Each
    slot is handed on as delegate_contribution would; one that cannot be is left as it is and listed
    with why.

    Args:
        uuid (UUID):
        body (DelegateTeamSlotsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DelegateTeamSlotsResult
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
    body: DelegateTeamSlotsRequest,
) -> Response[DelegateTeamSlotsResult]:
    """Hand several of the team's open slots to one person, or take them back with a null user_uuid. Each
    slot is handed on as delegate_contribution would; one that cannot be is left as it is and listed
    with why.

    Args:
        uuid (UUID):
        body (DelegateTeamSlotsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DelegateTeamSlotsResult]
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
    body: DelegateTeamSlotsRequest,
) -> DelegateTeamSlotsResult:
    """Hand several of the team's open slots to one person, or take them back with a null user_uuid. Each
    slot is handed on as delegate_contribution would; one that cannot be is left as it is and listed
    with why.

    Args:
        uuid (UUID):
        body (DelegateTeamSlotsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DelegateTeamSlotsResult
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
