from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.workflow_paths import WorkflowPaths
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    round_: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_round_: Union[Unset, str] = UNSET
    if not isinstance(round_, Unset):
        json_round_ = str(round_)
    params["round"] = json_round_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/proposal-protected-calls/{uuid}/workflow-paths/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> WorkflowPaths:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = WorkflowPaths.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[WorkflowPaths]:
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
    round_: Union[Unset, UUID] = UNSET,
) -> Response[WorkflowPaths]:
    """Paths the call's proposals took through its workflow

     Each distinct sequence of steps and outcomes the proposals took, with how many took it and whether a
    saved scenario covers it. For those who configure the call, staff and support.

    Args:
        uuid (UUID):
        round_ (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WorkflowPaths]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        round_=round_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    round_: Union[Unset, UUID] = UNSET,
) -> WorkflowPaths:
    """Paths the call's proposals took through its workflow

     Each distinct sequence of steps and outcomes the proposals took, with how many took it and whether a
    saved scenario covers it. For those who configure the call, staff and support.

    Args:
        uuid (UUID):
        round_ (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WorkflowPaths
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        round_=round_,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    round_: Union[Unset, UUID] = UNSET,
) -> Response[WorkflowPaths]:
    """Paths the call's proposals took through its workflow

     Each distinct sequence of steps and outcomes the proposals took, with how many took it and whether a
    saved scenario covers it. For those who configure the call, staff and support.

    Args:
        uuid (UUID):
        round_ (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WorkflowPaths]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        round_=round_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    round_: Union[Unset, UUID] = UNSET,
) -> WorkflowPaths:
    """Paths the call's proposals took through its workflow

     Each distinct sequence of steps and outcomes the proposals took, with how many took it and whether a
    saved scenario covers it. For those who configure the call, staff and support.

    Args:
        uuid (UUID):
        round_ (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WorkflowPaths
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            round_=round_,
        )
    ).parsed
