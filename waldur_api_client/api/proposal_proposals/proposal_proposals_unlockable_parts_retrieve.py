from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.unlockable_parts import UnlockableParts
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    step_uuid: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_step_uuid: Union[Unset, str] = UNSET
    if not isinstance(step_uuid, Unset):
        json_step_uuid = str(step_uuid)
    params["step_uuid"] = json_step_uuid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/proposal-proposals/{uuid}/unlockable_parts/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> UnlockableParts:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = UnlockableParts.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[UnlockableParts]:
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
    step_uuid: Union[Unset, UUID] = UNSET,
) -> Response[UnlockableParts]:
    """The parts of the proposal a request for changes may unlock: the Project details fields the call
    collects, and its documents, requested resources, team and compliance answers. At a step of an
    extension request or final report (step_uuid), the run's parts instead: its applicant step's
    answers, and what an extension asks for.

    Args:
        uuid (UUID):
        step_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UnlockableParts]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        step_uuid=step_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    step_uuid: Union[Unset, UUID] = UNSET,
) -> UnlockableParts:
    """The parts of the proposal a request for changes may unlock: the Project details fields the call
    collects, and its documents, requested resources, team and compliance answers. At a step of an
    extension request or final report (step_uuid), the run's parts instead: its applicant step's
    answers, and what an extension asks for.

    Args:
        uuid (UUID):
        step_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UnlockableParts
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        step_uuid=step_uuid,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    step_uuid: Union[Unset, UUID] = UNSET,
) -> Response[UnlockableParts]:
    """The parts of the proposal a request for changes may unlock: the Project details fields the call
    collects, and its documents, requested resources, team and compliance answers. At a step of an
    extension request or final report (step_uuid), the run's parts instead: its applicant step's
    answers, and what an extension asks for.

    Args:
        uuid (UUID):
        step_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UnlockableParts]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        step_uuid=step_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    step_uuid: Union[Unset, UUID] = UNSET,
) -> UnlockableParts:
    """The parts of the proposal a request for changes may unlock: the Project details fields the call
    collects, and its documents, requested resources, team and compliance answers. At a step of an
    extension request or final report (step_uuid), the run's parts instead: its applicant step's
    answers, and what an extension asks for.

    Args:
        uuid (UUID):
        step_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UnlockableParts
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            step_uuid=step_uuid,
        )
    ).parsed
