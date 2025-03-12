from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patched_protected_round_request import PatchedProtectedRoundRequest
from ...models.protected_round import ProtectedRound
from ...types import Response


def _get_kwargs(
    uuid: str,
    obj_uuid: str,
    *,
    body: Union[
        PatchedProtectedRoundRequest,
        PatchedProtectedRoundRequest,
        PatchedProtectedRoundRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/",
    }

    if isinstance(body, PatchedProtectedRoundRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedProtectedRoundRequest):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedProtectedRoundRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ProtectedRound]:
    if response.status_code == 200:
        response_200 = ProtectedRound.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ProtectedRound]:
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
    body: Union[
        PatchedProtectedRoundRequest,
        PatchedProtectedRoundRequest,
        PatchedProtectedRoundRequest,
    ],
) -> Response[ProtectedRound]:
    """
    Args:
        uuid (str):
        obj_uuid (str):
        body (PatchedProtectedRoundRequest):
        body (PatchedProtectedRoundRequest):
        body (PatchedProtectedRoundRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProtectedRound]
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
    body: Union[
        PatchedProtectedRoundRequest,
        PatchedProtectedRoundRequest,
        PatchedProtectedRoundRequest,
    ],
) -> Optional[ProtectedRound]:
    """
    Args:
        uuid (str):
        obj_uuid (str):
        body (PatchedProtectedRoundRequest):
        body (PatchedProtectedRoundRequest):
        body (PatchedProtectedRoundRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProtectedRound
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
    body: Union[
        PatchedProtectedRoundRequest,
        PatchedProtectedRoundRequest,
        PatchedProtectedRoundRequest,
    ],
) -> Response[ProtectedRound]:
    """
    Args:
        uuid (str):
        obj_uuid (str):
        body (PatchedProtectedRoundRequest):
        body (PatchedProtectedRoundRequest):
        body (PatchedProtectedRoundRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProtectedRound]
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
    body: Union[
        PatchedProtectedRoundRequest,
        PatchedProtectedRoundRequest,
        PatchedProtectedRoundRequest,
    ],
) -> Optional[ProtectedRound]:
    """
    Args:
        uuid (str):
        obj_uuid (str):
        body (PatchedProtectedRoundRequest):
        body (PatchedProtectedRoundRequest):
        body (PatchedProtectedRoundRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProtectedRound
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            obj_uuid=obj_uuid,
            client=client,
            body=body,
        )
    ).parsed
