from http import HTTPStatus
from typing import Any, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.passkey_ceremony_options import PasskeyCeremonyOptions
from ...models.reauthentication_challenge import ReauthenticationChallenge
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    x_reauthentication_grant: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_reauthentication_grant, Unset):
        headers["X-Reauthentication-Grant"] = x_reauthentication_grant

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/passkeys/registration/begin/",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[PasskeyCeremonyOptions, ReauthenticationChallenge]:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = PasskeyCeremonyOptions.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = ReauthenticationChallenge.from_dict(response.json())

        return response_401
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[PasskeyCeremonyOptions, ReauthenticationChallenge]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    x_reauthentication_grant: Union[Unset, str] = UNSET,
) -> Response[Union[PasskeyCeremonyOptions, ReauthenticationChallenge]]:
    """Begin passkey registration

    Args:
        x_reauthentication_grant (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PasskeyCeremonyOptions, ReauthenticationChallenge]]
    """

    kwargs = _get_kwargs(
        x_reauthentication_grant=x_reauthentication_grant,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    x_reauthentication_grant: Union[Unset, str] = UNSET,
) -> Union[PasskeyCeremonyOptions, ReauthenticationChallenge]:
    """Begin passkey registration

    Args:
        x_reauthentication_grant (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PasskeyCeremonyOptions, ReauthenticationChallenge]
    """

    return sync_detailed(
        client=client,
        x_reauthentication_grant=x_reauthentication_grant,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    x_reauthentication_grant: Union[Unset, str] = UNSET,
) -> Response[Union[PasskeyCeremonyOptions, ReauthenticationChallenge]]:
    """Begin passkey registration

    Args:
        x_reauthentication_grant (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PasskeyCeremonyOptions, ReauthenticationChallenge]]
    """

    kwargs = _get_kwargs(
        x_reauthentication_grant=x_reauthentication_grant,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    x_reauthentication_grant: Union[Unset, str] = UNSET,
) -> Union[PasskeyCeremonyOptions, ReauthenticationChallenge]:
    """Begin passkey registration

    Args:
        x_reauthentication_grant (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PasskeyCeremonyOptions, ReauthenticationChallenge]
    """

    return (
        await asyncio_detailed(
            client=client,
            x_reauthentication_grant=x_reauthentication_grant,
        )
    ).parsed
