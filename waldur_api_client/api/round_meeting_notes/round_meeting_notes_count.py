from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    call_step_uuid: Union[Unset, UUID] = UNSET,
    call_uuid: Union[Unset, UUID] = UNSET,
    is_report: Union[Unset, bool] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    round_uuid: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_call_step_uuid: Union[Unset, str] = UNSET
    if not isinstance(call_step_uuid, Unset):
        json_call_step_uuid = str(call_step_uuid)
    params["call_step_uuid"] = json_call_step_uuid

    json_call_uuid: Union[Unset, str] = UNSET
    if not isinstance(call_uuid, Unset):
        json_call_uuid = str(call_uuid)
    params["call_uuid"] = json_call_uuid

    params["is_report"] = is_report

    params["page"] = page

    params["page_size"] = page_size

    json_round_uuid: Union[Unset, str] = UNSET
    if not isinstance(round_uuid, Unset):
        json_round_uuid = str(round_uuid)
    params["round_uuid"] = json_round_uuid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "head",
        "url": "/api/round-meeting-notes/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> int:
    if response.status_code == HTTPStatus.OK:
        try:
            return int(response.headers["x-result-count"])
        except KeyError:
            raise errors.UnexpectedStatus(
                response.status_code,
                b"Expected 'X-Result-Count' header for HEAD request, but it was not found.",
                response.url,
            )
        except ValueError:
            count_val = response.headers.get("x-result-count")
            msg = f"Expected 'X-Result-Count' header to be an integer, but got '{count_val}'."
            raise errors.UnexpectedStatus(response.status_code, msg.encode(), response.url)
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[int]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    call_step_uuid: Union[Unset, UUID] = UNSET,
    call_uuid: Union[Unset, UUID] = UNSET,
    is_report: Union[Unset, bool] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    round_uuid: Union[Unset, UUID] = UNSET,
) -> Response[int]:
    """Get number of items in the collection matching the request parameters.

    Args:
        call_step_uuid (Union[Unset, UUID]):
        call_uuid (Union[Unset, UUID]):
        is_report (Union[Unset, bool]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        round_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[int]
    """

    kwargs = _get_kwargs(
        call_step_uuid=call_step_uuid,
        call_uuid=call_uuid,
        is_report=is_report,
        page=page,
        page_size=page_size,
        round_uuid=round_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    call_step_uuid: Union[Unset, UUID] = UNSET,
    call_uuid: Union[Unset, UUID] = UNSET,
    is_report: Union[Unset, bool] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    round_uuid: Union[Unset, UUID] = UNSET,
) -> int:
    """Get number of items in the collection matching the request parameters.

    Args:
        call_step_uuid (Union[Unset, UUID]):
        call_uuid (Union[Unset, UUID]):
        is_report (Union[Unset, bool]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        round_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        int
    """

    return sync_detailed(
        client=client,
        call_step_uuid=call_step_uuid,
        call_uuid=call_uuid,
        is_report=is_report,
        page=page,
        page_size=page_size,
        round_uuid=round_uuid,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    call_step_uuid: Union[Unset, UUID] = UNSET,
    call_uuid: Union[Unset, UUID] = UNSET,
    is_report: Union[Unset, bool] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    round_uuid: Union[Unset, UUID] = UNSET,
) -> Response[int]:
    """Get number of items in the collection matching the request parameters.

    Args:
        call_step_uuid (Union[Unset, UUID]):
        call_uuid (Union[Unset, UUID]):
        is_report (Union[Unset, bool]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        round_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[int]
    """

    kwargs = _get_kwargs(
        call_step_uuid=call_step_uuid,
        call_uuid=call_uuid,
        is_report=is_report,
        page=page,
        page_size=page_size,
        round_uuid=round_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    call_step_uuid: Union[Unset, UUID] = UNSET,
    call_uuid: Union[Unset, UUID] = UNSET,
    is_report: Union[Unset, bool] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    round_uuid: Union[Unset, UUID] = UNSET,
) -> int:
    """Get number of items in the collection matching the request parameters.

    Args:
        call_step_uuid (Union[Unset, UUID]):
        call_uuid (Union[Unset, UUID]):
        is_report (Union[Unset, bool]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        round_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        int
    """

    return (
        await asyncio_detailed(
            client=client,
            call_step_uuid=call_step_uuid,
            call_uuid=call_uuid,
            is_report=is_report,
            page=page,
            page_size=page_size,
            round_uuid=round_uuid,
        )
    ).parsed
