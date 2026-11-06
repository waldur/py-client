from http import HTTPStatus
from typing import Any, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    meeting_note_uuid: Union[Unset, str] = UNSET,
    round_uuid: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["meeting_note_uuid"] = meeting_note_uuid

    params["round_uuid"] = round_uuid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/proposal-rankings/export_csv/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> str:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = response.text
        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    meeting_note_uuid: Union[Unset, str] = UNSET,
    round_uuid: str,
) -> Response[str]:
    """The round's ranking as CSV: one row per ranked proposal, with a recommended:<requested offering
    uuid>:<component type> column per offering component of the call. For the call's managers, the
    proposals of the round not ranked yet follow with empty values, so the file can be filled in and
    imported.

    Args:
        meeting_note_uuid (Union[Unset, str]):
        round_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        meeting_note_uuid=meeting_note_uuid,
        round_uuid=round_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    meeting_note_uuid: Union[Unset, str] = UNSET,
    round_uuid: str,
) -> str:
    """The round's ranking as CSV: one row per ranked proposal, with a recommended:<requested offering
    uuid>:<component type> column per offering component of the call. For the call's managers, the
    proposals of the round not ranked yet follow with empty values, so the file can be filled in and
    imported.

    Args:
        meeting_note_uuid (Union[Unset, str]):
        round_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return sync_detailed(
        client=client,
        meeting_note_uuid=meeting_note_uuid,
        round_uuid=round_uuid,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    meeting_note_uuid: Union[Unset, str] = UNSET,
    round_uuid: str,
) -> Response[str]:
    """The round's ranking as CSV: one row per ranked proposal, with a recommended:<requested offering
    uuid>:<component type> column per offering component of the call. For the call's managers, the
    proposals of the round not ranked yet follow with empty values, so the file can be filled in and
    imported.

    Args:
        meeting_note_uuid (Union[Unset, str]):
        round_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        meeting_note_uuid=meeting_note_uuid,
        round_uuid=round_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    meeting_note_uuid: Union[Unset, str] = UNSET,
    round_uuid: str,
) -> str:
    """The round's ranking as CSV: one row per ranked proposal, with a recommended:<requested offering
    uuid>:<component type> column per offering component of the call. For the call's managers, the
    proposals of the round not ranked yet follow with empty values, so the file can be filled in and
    imported.

    Args:
        meeting_note_uuid (Union[Unset, str]):
        round_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return (
        await asyncio_detailed(
            client=client,
            meeting_note_uuid=meeting_note_uuid,
            round_uuid=round_uuid,
        )
    ).parsed
