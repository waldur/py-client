from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.personal_access_token import PersonalAccessToken
from ...models.personal_access_token_network_acl_request import PersonalAccessTokenNetworkAclRequest
from ...models.reauthentication_challenge import ReauthenticationChallenge
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    body: PersonalAccessTokenNetworkAclRequest,
    x_reauthentication_grant: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_reauthentication_grant, Unset):
        headers["X-Reauthentication-Grant"] = x_reauthentication_grant

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/personal-access-tokens/{uuid}/set_network_acl/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[PersonalAccessToken, ReauthenticationChallenge]:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = PersonalAccessToken.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = ReauthenticationChallenge.from_dict(response.json())

        return response_401
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[PersonalAccessToken, ReauthenticationChallenge]]:
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
    body: PersonalAccessTokenNetworkAclRequest,
    x_reauthentication_grant: Union[Unset, str] = UNSET,
) -> Response[Union[PersonalAccessToken, ReauthenticationChallenge]]:
    """Replace the network ACL of a personal access token

     Replace the token's source-network allowlist.

    Narrowing the list needs nothing more: every new network lies inside
    a current one of the same address family, or the token was
    unrestricted, or the list is unchanged. Anything else lets the token
    work from an address it could not before, and needs a
    re-authentication grant, as creating a token does. That includes an
    empty list, which means from anywhere.

    A dedicated action rather than PATCH: update/partial_update stay
    disabled on this viewset, and the change gets its own audit event.

    Args:
        uuid (UUID):
        x_reauthentication_grant (Union[Unset, str]):
        body (PersonalAccessTokenNetworkAclRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PersonalAccessToken, ReauthenticationChallenge]]
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
    body: PersonalAccessTokenNetworkAclRequest,
    x_reauthentication_grant: Union[Unset, str] = UNSET,
) -> Union[PersonalAccessToken, ReauthenticationChallenge]:
    """Replace the network ACL of a personal access token

     Replace the token's source-network allowlist.

    Narrowing the list needs nothing more: every new network lies inside
    a current one of the same address family, or the token was
    unrestricted, or the list is unchanged. Anything else lets the token
    work from an address it could not before, and needs a
    re-authentication grant, as creating a token does. That includes an
    empty list, which means from anywhere.

    A dedicated action rather than PATCH: update/partial_update stay
    disabled on this viewset, and the change gets its own audit event.

    Args:
        uuid (UUID):
        x_reauthentication_grant (Union[Unset, str]):
        body (PersonalAccessTokenNetworkAclRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PersonalAccessToken, ReauthenticationChallenge]
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
    body: PersonalAccessTokenNetworkAclRequest,
    x_reauthentication_grant: Union[Unset, str] = UNSET,
) -> Response[Union[PersonalAccessToken, ReauthenticationChallenge]]:
    """Replace the network ACL of a personal access token

     Replace the token's source-network allowlist.

    Narrowing the list needs nothing more: every new network lies inside
    a current one of the same address family, or the token was
    unrestricted, or the list is unchanged. Anything else lets the token
    work from an address it could not before, and needs a
    re-authentication grant, as creating a token does. That includes an
    empty list, which means from anywhere.

    A dedicated action rather than PATCH: update/partial_update stay
    disabled on this viewset, and the change gets its own audit event.

    Args:
        uuid (UUID):
        x_reauthentication_grant (Union[Unset, str]):
        body (PersonalAccessTokenNetworkAclRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PersonalAccessToken, ReauthenticationChallenge]]
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
    body: PersonalAccessTokenNetworkAclRequest,
    x_reauthentication_grant: Union[Unset, str] = UNSET,
) -> Union[PersonalAccessToken, ReauthenticationChallenge]:
    """Replace the network ACL of a personal access token

     Replace the token's source-network allowlist.

    Narrowing the list needs nothing more: every new network lies inside
    a current one of the same address family, or the token was
    unrestricted, or the list is unchanged. Anything else lets the token
    work from an address it could not before, and needs a
    re-authentication grant, as creating a token does. That includes an
    empty list, which means from anywhere.

    A dedicated action rather than PATCH: update/partial_update stay
    disabled on this viewset, and the change gets its own audit event.

    Args:
        uuid (UUID):
        x_reauthentication_grant (Union[Unset, str]):
        body (PersonalAccessTokenNetworkAclRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PersonalAccessToken, ReauthenticationChallenge]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
            x_reauthentication_grant=x_reauthentication_grant,
        )
    ).parsed
