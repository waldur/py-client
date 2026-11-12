from http import HTTPStatus
from typing import Any, Union, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.reauthentication_challenge import ReauthenticationChallenge
from ...models.user_email_change_request import UserEmailChangeRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    body: UserEmailChangeRequest,
    x_reauthentication_grant: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_reauthentication_grant, Unset):
        headers["X-Reauthentication-Grant"] = x_reauthentication_grant

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/users/{uuid}/change_email/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[Any, ReauthenticationChallenge]:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 401:
        response_401 = ReauthenticationChallenge.from_dict(response.json())

        return response_401
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ReauthenticationChallenge]]:
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
    body: UserEmailChangeRequest,
    x_reauthentication_grant: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ReauthenticationChallenge]]:
    """Request email change

     Allows to change email for user. Requires a re-authentication grant for change_email, except for a
    user changing their own email who has no method to re-authenticate with. Refused when the user's
    identity provider supplies the email.

    Args:
        uuid (UUID):
        x_reauthentication_grant (Union[Unset, str]):
        body (UserEmailChangeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ReauthenticationChallenge]]
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
    body: UserEmailChangeRequest,
    x_reauthentication_grant: Union[Unset, str] = UNSET,
) -> Union[Any, ReauthenticationChallenge]:
    """Request email change

     Allows to change email for user. Requires a re-authentication grant for change_email, except for a
    user changing their own email who has no method to re-authenticate with. Refused when the user's
    identity provider supplies the email.

    Args:
        uuid (UUID):
        x_reauthentication_grant (Union[Unset, str]):
        body (UserEmailChangeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ReauthenticationChallenge]
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
    body: UserEmailChangeRequest,
    x_reauthentication_grant: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ReauthenticationChallenge]]:
    """Request email change

     Allows to change email for user. Requires a re-authentication grant for change_email, except for a
    user changing their own email who has no method to re-authenticate with. Refused when the user's
    identity provider supplies the email.

    Args:
        uuid (UUID):
        x_reauthentication_grant (Union[Unset, str]):
        body (UserEmailChangeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ReauthenticationChallenge]]
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
    body: UserEmailChangeRequest,
    x_reauthentication_grant: Union[Unset, str] = UNSET,
) -> Union[Any, ReauthenticationChallenge]:
    """Request email change

     Allows to change email for user. Requires a re-authentication grant for change_email, except for a
    user changing their own email who has no method to re-authenticate with. Refused when the user's
    identity provider supplies the email.

    Args:
        uuid (UUID):
        x_reauthentication_grant (Union[Unset, str]):
        body (UserEmailChangeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ReauthenticationChallenge]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
            x_reauthentication_grant=x_reauthentication_grant,
        )
    ).parsed
