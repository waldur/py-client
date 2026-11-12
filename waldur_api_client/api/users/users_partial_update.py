from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patched_user_request import PatchedUserRequest
from ...models.patched_user_request_form import PatchedUserRequestForm
from ...models.patched_user_request_multipart import PatchedUserRequestMultipart
from ...models.reauthentication_challenge import ReauthenticationChallenge
from ...models.user import User
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    body: Union[
        PatchedUserRequest,
        PatchedUserRequestForm,
        PatchedUserRequestMultipart,
    ],
    x_reauthentication_grant: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_reauthentication_grant, Unset):
        headers["X-Reauthentication-Grant"] = x_reauthentication_grant

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/api/users/{uuid}/",
    }

    if isinstance(body, PatchedUserRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedUserRequestForm):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedUserRequestMultipart):
        _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[ReauthenticationChallenge, User]:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = User.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = ReauthenticationChallenge.from_dict(response.json())

        return response_401
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ReauthenticationChallenge, User]]:
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
    body: Union[
        PatchedUserRequest,
        PatchedUserRequestForm,
        PatchedUserRequestMultipart,
    ],
    x_reauthentication_grant: Union[Unset, str] = UNSET,
) -> Response[Union[ReauthenticationChallenge, User]]:
    """
    Args:
        uuid (UUID):
        x_reauthentication_grant (Union[Unset, str]):
        body (PatchedUserRequest):
        body (PatchedUserRequestForm):
        body (PatchedUserRequestMultipart):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ReauthenticationChallenge, User]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
        x_reauthentication_grant=x_reauthentication_grant,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: Union[
        PatchedUserRequest,
        PatchedUserRequestForm,
        PatchedUserRequestMultipart,
    ],
    x_reauthentication_grant: Union[Unset, str] = UNSET,
) -> Union[ReauthenticationChallenge, User]:
    """
    Args:
        uuid (UUID):
        x_reauthentication_grant (Union[Unset, str]):
        body (PatchedUserRequest):
        body (PatchedUserRequestForm):
        body (PatchedUserRequestMultipart):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ReauthenticationChallenge, User]
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        body=body,
        x_reauthentication_grant=x_reauthentication_grant,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: Union[
        PatchedUserRequest,
        PatchedUserRequestForm,
        PatchedUserRequestMultipart,
    ],
    x_reauthentication_grant: Union[Unset, str] = UNSET,
) -> Response[Union[ReauthenticationChallenge, User]]:
    """
    Args:
        uuid (UUID):
        x_reauthentication_grant (Union[Unset, str]):
        body (PatchedUserRequest):
        body (PatchedUserRequestForm):
        body (PatchedUserRequestMultipart):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ReauthenticationChallenge, User]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
        x_reauthentication_grant=x_reauthentication_grant,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: Union[
        PatchedUserRequest,
        PatchedUserRequestForm,
        PatchedUserRequestMultipart,
    ],
    x_reauthentication_grant: Union[Unset, str] = UNSET,
) -> Union[ReauthenticationChallenge, User]:
    """
    Args:
        uuid (UUID):
        x_reauthentication_grant (Union[Unset, str]):
        body (PatchedUserRequest):
        body (PatchedUserRequestForm):
        body (PatchedUserRequestMultipart):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ReauthenticationChallenge, User]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
            x_reauthentication_grant=x_reauthentication_grant,
        )
    ).parsed
