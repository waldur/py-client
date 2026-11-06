from http import HTTPStatus
from typing import Any, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patched_proposal_run_update_request import PatchedProposalRunUpdateRequest
from ...models.proposal_run import ProposalRun
from ...types import Response


def _get_kwargs(
    uuid: str,
    obj_uuid: str,
    *,
    body: PatchedProposalRunUpdateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/api/proposal-proposals/{uuid}/runs/{obj_uuid}/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> ProposalRun:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = ProposalRun.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[ProposalRun]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: str,
    obj_uuid: str,
    *,
    client: AuthenticatedClient,
    body: PatchedProposalRunUpdateRequest,
) -> Response[ProposalRun]:
    """Read an extension request or final report, or change what an open extension asks for -- the
    proposal's team, while its request step runs -- or grants: whoever completes its decision, while
    that runs.

    Args:
        uuid (str):
        obj_uuid (str):
        body (PatchedProposalRunUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProposalRun]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        obj_uuid=obj_uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: str,
    obj_uuid: str,
    *,
    client: AuthenticatedClient,
    body: PatchedProposalRunUpdateRequest,
) -> ProposalRun:
    """Read an extension request or final report, or change what an open extension asks for -- the
    proposal's team, while its request step runs -- or grants: whoever completes its decision, while
    that runs.

    Args:
        uuid (str):
        obj_uuid (str):
        body (PatchedProposalRunUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProposalRun
    """

    return sync_detailed(
        uuid=uuid,
        obj_uuid=obj_uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    obj_uuid: str,
    *,
    client: AuthenticatedClient,
    body: PatchedProposalRunUpdateRequest,
) -> Response[ProposalRun]:
    """Read an extension request or final report, or change what an open extension asks for -- the
    proposal's team, while its request step runs -- or grants: whoever completes its decision, while
    that runs.

    Args:
        uuid (str):
        obj_uuid (str):
        body (PatchedProposalRunUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProposalRun]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        obj_uuid=obj_uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: str,
    obj_uuid: str,
    *,
    client: AuthenticatedClient,
    body: PatchedProposalRunUpdateRequest,
) -> ProposalRun:
    """Read an extension request or final report, or change what an open extension asks for -- the
    proposal's team, while its request step runs -- or grants: whoever completes its decision, while
    that runs.

    Args:
        uuid (str):
        obj_uuid (str):
        body (PatchedProposalRunUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProposalRun
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            obj_uuid=obj_uuid,
            client=client,
            body=body,
        )
    ).parsed
