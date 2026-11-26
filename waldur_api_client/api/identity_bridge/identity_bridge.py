from http import HTTPStatus
from typing import Any, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.identity_bridge_request_request import IdentityBridgeRequestRequest
from ...models.identity_bridge_result import IdentityBridgeResult
from ...types import Response


def _get_kwargs(
    *,
    body: IdentityBridgeRequestRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/identity-bridge/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> IdentityBridgeResult:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = IdentityBridgeResult.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[IdentityBridgeResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: IdentityBridgeRequestRequest,
) -> Response[IdentityBridgeResult]:
    """Push user attributes from an ISD

     Allows Identity Service Domains (ISDs) to push user attributes to Waldur. Creates or updates a user
    based on username (CUID). When no user has the username and the push carries a civil_number the
    bridge may set, an existing user with that civil number (ignoring case) is returned unchanged
    instead of a second account being created: no attributes are written, no ISD is added and the pushed
    username is not stored. A caller without staff access is never given a staff, support or identity
    manager account this way. When the civil number does not resolve to exactly one active account it
    may be given, the push is refused with 400 and one generic message; the same answer is given when an
    update would set a civil number another account holds. The endpoint therefore resolves civil numbers
    to account UUIDs for its callers. Requires FEDERATED_IDENTITY_SYNC_ENABLED to be True. Caller must
    be staff or an identity manager with the declared source in managed_isds. Only staff may change
    staff, support or identity manager accounts: anyone else pushing an existing one gets it back
    unchanged (`created` false, no `updated_fields`).

    Args:
        body (IdentityBridgeRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdentityBridgeResult]
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
    body: IdentityBridgeRequestRequest,
) -> IdentityBridgeResult:
    """Push user attributes from an ISD

     Allows Identity Service Domains (ISDs) to push user attributes to Waldur. Creates or updates a user
    based on username (CUID). When no user has the username and the push carries a civil_number the
    bridge may set, an existing user with that civil number (ignoring case) is returned unchanged
    instead of a second account being created: no attributes are written, no ISD is added and the pushed
    username is not stored. A caller without staff access is never given a staff, support or identity
    manager account this way. When the civil number does not resolve to exactly one active account it
    may be given, the push is refused with 400 and one generic message; the same answer is given when an
    update would set a civil number another account holds. The endpoint therefore resolves civil numbers
    to account UUIDs for its callers. Requires FEDERATED_IDENTITY_SYNC_ENABLED to be True. Caller must
    be staff or an identity manager with the declared source in managed_isds. Only staff may change
    staff, support or identity manager accounts: anyone else pushing an existing one gets it back
    unchanged (`created` false, no `updated_fields`).

    Args:
        body (IdentityBridgeRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdentityBridgeResult
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: IdentityBridgeRequestRequest,
) -> Response[IdentityBridgeResult]:
    """Push user attributes from an ISD

     Allows Identity Service Domains (ISDs) to push user attributes to Waldur. Creates or updates a user
    based on username (CUID). When no user has the username and the push carries a civil_number the
    bridge may set, an existing user with that civil number (ignoring case) is returned unchanged
    instead of a second account being created: no attributes are written, no ISD is added and the pushed
    username is not stored. A caller without staff access is never given a staff, support or identity
    manager account this way. When the civil number does not resolve to exactly one active account it
    may be given, the push is refused with 400 and one generic message; the same answer is given when an
    update would set a civil number another account holds. The endpoint therefore resolves civil numbers
    to account UUIDs for its callers. Requires FEDERATED_IDENTITY_SYNC_ENABLED to be True. Caller must
    be staff or an identity manager with the declared source in managed_isds. Only staff may change
    staff, support or identity manager accounts: anyone else pushing an existing one gets it back
    unchanged (`created` false, no `updated_fields`).

    Args:
        body (IdentityBridgeRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdentityBridgeResult]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: IdentityBridgeRequestRequest,
) -> IdentityBridgeResult:
    """Push user attributes from an ISD

     Allows Identity Service Domains (ISDs) to push user attributes to Waldur. Creates or updates a user
    based on username (CUID). When no user has the username and the push carries a civil_number the
    bridge may set, an existing user with that civil number (ignoring case) is returned unchanged
    instead of a second account being created: no attributes are written, no ISD is added and the pushed
    username is not stored. A caller without staff access is never given a staff, support or identity
    manager account this way. When the civil number does not resolve to exactly one active account it
    may be given, the push is refused with 400 and one generic message; the same answer is given when an
    update would set a civil number another account holds. The endpoint therefore resolves civil numbers
    to account UUIDs for its callers. Requires FEDERATED_IDENTITY_SYNC_ENABLED to be True. Caller must
    be staff or an identity manager with the declared source in managed_isds. Only staff may change
    staff, support or identity manager accounts: anyone else pushing an existing one gets it back
    unchanged (`created` false, no `updated_fields`).

    Args:
        body (IdentityBridgeRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdentityBridgeResult
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
