from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.remote_eduteams_request_request import RemoteEduteamsRequestRequest
from ...models.remote_eduteams_uuid import RemoteEduteamsUUID
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        RemoteEduteamsRequestRequest,
        RemoteEduteamsRequestRequest,
        RemoteEduteamsRequestRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/remote-eduteams/",
    }

    if isinstance(body, RemoteEduteamsRequestRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, RemoteEduteamsRequestRequest):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, RemoteEduteamsRequestRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[RemoteEduteamsUUID]:
    if response.status_code == 200:
        response_200 = RemoteEduteamsUUID.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[RemoteEduteamsUUID]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        RemoteEduteamsRequestRequest,
        RemoteEduteamsRequestRequest,
        RemoteEduteamsRequestRequest,
    ],
) -> Response[RemoteEduteamsUUID]:
    """Allows to pull user details from remote eduTEAMS instance.

    Args:
        body (RemoteEduteamsRequestRequest):
        body (RemoteEduteamsRequestRequest):
        body (RemoteEduteamsRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemoteEduteamsUUID]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: Union[
        RemoteEduteamsRequestRequest,
        RemoteEduteamsRequestRequest,
        RemoteEduteamsRequestRequest,
    ],
) -> Optional[RemoteEduteamsUUID]:
    """Allows to pull user details from remote eduTEAMS instance.

    Args:
        body (RemoteEduteamsRequestRequest):
        body (RemoteEduteamsRequestRequest):
        body (RemoteEduteamsRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemoteEduteamsUUID
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        RemoteEduteamsRequestRequest,
        RemoteEduteamsRequestRequest,
        RemoteEduteamsRequestRequest,
    ],
) -> Response[RemoteEduteamsUUID]:
    """Allows to pull user details from remote eduTEAMS instance.

    Args:
        body (RemoteEduteamsRequestRequest):
        body (RemoteEduteamsRequestRequest):
        body (RemoteEduteamsRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemoteEduteamsUUID]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Union[
        RemoteEduteamsRequestRequest,
        RemoteEduteamsRequestRequest,
        RemoteEduteamsRequestRequest,
    ],
) -> Optional[RemoteEduteamsUUID]:
    """Allows to pull user details from remote eduTEAMS instance.

    Args:
        body (RemoteEduteamsRequestRequest):
        body (RemoteEduteamsRequestRequest):
        body (RemoteEduteamsRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemoteEduteamsUUID
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
