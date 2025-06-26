from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.keycloak_user_group_membership import KeycloakUserGroupMembership
from ...models.patched_keycloak_user_group_membership_request import PatchedKeycloakUserGroupMembershipRequest
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    *,
    body: PatchedKeycloakUserGroupMembershipRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/api/keycloak-user-group-memberships/{uuid}/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> KeycloakUserGroupMembership:
    if response.status_code == 200:
        response_200 = KeycloakUserGroupMembership.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[KeycloakUserGroupMembership]:
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
    body: PatchedKeycloakUserGroupMembershipRequest,
) -> Response[KeycloakUserGroupMembership]:
    """
    Args:
        uuid (UUID):
        body (PatchedKeycloakUserGroupMembershipRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KeycloakUserGroupMembership]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchedKeycloakUserGroupMembershipRequest,
) -> KeycloakUserGroupMembership:
    """
    Args:
        uuid (UUID):
        body (PatchedKeycloakUserGroupMembershipRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KeycloakUserGroupMembership
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchedKeycloakUserGroupMembershipRequest,
) -> Response[KeycloakUserGroupMembership]:
    """
    Args:
        uuid (UUID):
        body (PatchedKeycloakUserGroupMembershipRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KeycloakUserGroupMembership]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchedKeycloakUserGroupMembershipRequest,
) -> KeycloakUserGroupMembership:
    """
    Args:
        uuid (UUID):
        body (PatchedKeycloakUserGroupMembershipRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KeycloakUserGroupMembership
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
