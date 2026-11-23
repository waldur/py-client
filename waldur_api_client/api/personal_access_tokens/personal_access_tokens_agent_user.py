from http import HTTPStatus
from typing import Any, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dedicated_user_token_create_request import DedicatedUserTokenCreateRequest
from ...models.dedicated_user_token_created import DedicatedUserTokenCreated
from ...models.reauthentication_challenge import ReauthenticationChallenge
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: DedicatedUserTokenCreateRequest,
    x_reauthentication_grant: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_reauthentication_grant, Unset):
        headers["X-Reauthentication-Grant"] = x_reauthentication_grant

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/personal-access-tokens/agent_user/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[DedicatedUserTokenCreated, ReauthenticationChallenge]:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 201:
        response_201 = DedicatedUserTokenCreated.from_dict(response.json())

        return response_201
    if response.status_code == 401:
        response_401 = ReauthenticationChallenge.from_dict(response.json())

        return response_401
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[DedicatedUserTokenCreated, ReauthenticationChallenge]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: DedicatedUserTokenCreateRequest,
    x_reauthentication_grant: Union[Unset, str] = UNSET,
) -> Response[Union[DedicatedUserTokenCreated, ReauthenticationChallenge]]:
    """Create a dedicated user and its token for a template target

     Staff: create a user that only holds the template's role on the
    target (an offering's manager, for a site agent), and a token for it
    with the template's scopes, restricted to the target.

    Unlike a staff user's own token, which works there only with
    STAFF.ACCESS and then reaches everything, this one reaches the target
    alone. The user has no usable password; it exists for the token.

    Args:
        x_reauthentication_grant (Union[Unset, str]):
        body (DedicatedUserTokenCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DedicatedUserTokenCreated, ReauthenticationChallenge]]
    """

    kwargs = _get_kwargs(
        body=body,
        x_reauthentication_grant=x_reauthentication_grant,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: DedicatedUserTokenCreateRequest,
    x_reauthentication_grant: Union[Unset, str] = UNSET,
) -> Union[DedicatedUserTokenCreated, ReauthenticationChallenge]:
    """Create a dedicated user and its token for a template target

     Staff: create a user that only holds the template's role on the
    target (an offering's manager, for a site agent), and a token for it
    with the template's scopes, restricted to the target.

    Unlike a staff user's own token, which works there only with
    STAFF.ACCESS and then reaches everything, this one reaches the target
    alone. The user has no usable password; it exists for the token.

    Args:
        x_reauthentication_grant (Union[Unset, str]):
        body (DedicatedUserTokenCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DedicatedUserTokenCreated, ReauthenticationChallenge]
    """

    return sync_detailed(
        client=client,
        body=body,
        x_reauthentication_grant=x_reauthentication_grant,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: DedicatedUserTokenCreateRequest,
    x_reauthentication_grant: Union[Unset, str] = UNSET,
) -> Response[Union[DedicatedUserTokenCreated, ReauthenticationChallenge]]:
    """Create a dedicated user and its token for a template target

     Staff: create a user that only holds the template's role on the
    target (an offering's manager, for a site agent), and a token for it
    with the template's scopes, restricted to the target.

    Unlike a staff user's own token, which works there only with
    STAFF.ACCESS and then reaches everything, this one reaches the target
    alone. The user has no usable password; it exists for the token.

    Args:
        x_reauthentication_grant (Union[Unset, str]):
        body (DedicatedUserTokenCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DedicatedUserTokenCreated, ReauthenticationChallenge]]
    """

    kwargs = _get_kwargs(
        body=body,
        x_reauthentication_grant=x_reauthentication_grant,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: DedicatedUserTokenCreateRequest,
    x_reauthentication_grant: Union[Unset, str] = UNSET,
) -> Union[DedicatedUserTokenCreated, ReauthenticationChallenge]:
    """Create a dedicated user and its token for a template target

     Staff: create a user that only holds the template's role on the
    target (an offering's manager, for a site agent), and a token for it
    with the template's scopes, restricted to the target.

    Unlike a staff user's own token, which works there only with
    STAFF.ACCESS and then reaches everything, this one reaches the target
    alone. The user has no usable password; it exists for the token.

    Args:
        x_reauthentication_grant (Union[Unset, str]):
        body (DedicatedUserTokenCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DedicatedUserTokenCreated, ReauthenticationChallenge]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_reauthentication_grant=x_reauthentication_grant,
        )
    ).parsed
