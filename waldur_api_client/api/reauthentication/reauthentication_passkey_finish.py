from http import HTTPStatus
from typing import Any, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.passkey_reauthentication_finish_request import PasskeyReauthenticationFinishRequest
from ...models.reauthentication_grant import ReauthenticationGrant
from ...models.reauthentication_throttled import ReauthenticationThrottled
from ...types import Response


def _get_kwargs(
    *,
    body: PasskeyReauthenticationFinishRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/reauthentication/passkey/finish/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[ReauthenticationGrant, ReauthenticationThrottled]:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 201:
        response_201 = ReauthenticationGrant.from_dict(response.json())

        return response_201
    if response.status_code == 429:
        response_429 = ReauthenticationThrottled.from_dict(response.json())

        return response_429
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ReauthenticationGrant, ReauthenticationThrottled]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PasskeyReauthenticationFinishRequest,
) -> Response[Union[ReauthenticationGrant, ReauthenticationThrottled]]:
    """Finish re-authentication with a passkey

     Returns a single-use grant for one change that requires re-authentication, to send in the
    X-Reauthentication-Grant header.

    Args:
        body (PasskeyReauthenticationFinishRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ReauthenticationGrant, ReauthenticationThrottled]]
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
    body: PasskeyReauthenticationFinishRequest,
) -> Union[ReauthenticationGrant, ReauthenticationThrottled]:
    """Finish re-authentication with a passkey

     Returns a single-use grant for one change that requires re-authentication, to send in the
    X-Reauthentication-Grant header.

    Args:
        body (PasskeyReauthenticationFinishRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ReauthenticationGrant, ReauthenticationThrottled]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PasskeyReauthenticationFinishRequest,
) -> Response[Union[ReauthenticationGrant, ReauthenticationThrottled]]:
    """Finish re-authentication with a passkey

     Returns a single-use grant for one change that requires re-authentication, to send in the
    X-Reauthentication-Grant header.

    Args:
        body (PasskeyReauthenticationFinishRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ReauthenticationGrant, ReauthenticationThrottled]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PasskeyReauthenticationFinishRequest,
) -> Union[ReauthenticationGrant, ReauthenticationThrottled]:
    """Finish re-authentication with a passkey

     Returns a single-use grant for one change that requires re-authentication, to send in the
    X-Reauthentication-Grant header.

    Args:
        body (PasskeyReauthenticationFinishRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ReauthenticationGrant, ReauthenticationThrottled]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
