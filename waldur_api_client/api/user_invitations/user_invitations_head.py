from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.user_invitations_head_o_item import UserInvitationsHeadOItem
from ...models.user_invitations_head_state_item import UserInvitationsHeadStateItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    civil_number: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    email: Union[Unset, str] = UNSET,
    o: Union[Unset, list[UserInvitationsHeadOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    role_name: Union[Unset, str] = UNSET,
    role_uuid: Union[Unset, UUID] = UNSET,
    scope_type: Union[Unset, str] = UNSET,
    state: Union[Unset, list[UserInvitationsHeadStateItem]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["civil_number"] = civil_number

    json_customer_uuid: Union[Unset, str] = UNSET
    if not isinstance(customer_uuid, Unset):
        json_customer_uuid = str(customer_uuid)
    params["customer_uuid"] = json_customer_uuid

    params["email"] = email

    json_o: Union[Unset, list[str]] = UNSET
    if not isinstance(o, Unset):
        json_o = []
        for o_item_data in o:
            o_item = o_item_data.value
            json_o.append(o_item)

    params["o"] = json_o

    params["page"] = page

    params["page_size"] = page_size

    params["role_name"] = role_name

    json_role_uuid: Union[Unset, str] = UNSET
    if not isinstance(role_uuid, Unset):
        json_role_uuid = str(role_uuid)
    params["role_uuid"] = json_role_uuid

    params["scope_type"] = scope_type

    json_state: Union[Unset, list[str]] = UNSET
    if not isinstance(state, Unset):
        json_state = []
        for state_item_data in state:
            state_item = state_item_data.value
            json_state.append(state_item)

    params["state"] = json_state

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "head",
        "url": "/api/user-invitations/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Any:
    if response.status_code == 200:
        return None
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    civil_number: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    email: Union[Unset, str] = UNSET,
    o: Union[Unset, list[UserInvitationsHeadOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    role_name: Union[Unset, str] = UNSET,
    role_uuid: Union[Unset, UUID] = UNSET,
    scope_type: Union[Unset, str] = UNSET,
    state: Union[Unset, list[UserInvitationsHeadStateItem]] = UNSET,
) -> Response[Any]:
    """Mixin to optimize HEAD requests for DRF views bypassing serializer processing

    Args:
        civil_number (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        email (Union[Unset, str]):
        o (Union[Unset, list[UserInvitationsHeadOItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        role_name (Union[Unset, str]):
        role_uuid (Union[Unset, UUID]):
        scope_type (Union[Unset, str]):
        state (Union[Unset, list[UserInvitationsHeadStateItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        civil_number=civil_number,
        customer_uuid=customer_uuid,
        email=email,
        o=o,
        page=page,
        page_size=page_size,
        role_name=role_name,
        role_uuid=role_uuid,
        scope_type=scope_type,
        state=state,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    civil_number: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    email: Union[Unset, str] = UNSET,
    o: Union[Unset, list[UserInvitationsHeadOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    role_name: Union[Unset, str] = UNSET,
    role_uuid: Union[Unset, UUID] = UNSET,
    scope_type: Union[Unset, str] = UNSET,
    state: Union[Unset, list[UserInvitationsHeadStateItem]] = UNSET,
) -> Response[Any]:
    """Mixin to optimize HEAD requests for DRF views bypassing serializer processing

    Args:
        civil_number (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        email (Union[Unset, str]):
        o (Union[Unset, list[UserInvitationsHeadOItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        role_name (Union[Unset, str]):
        role_uuid (Union[Unset, UUID]):
        scope_type (Union[Unset, str]):
        state (Union[Unset, list[UserInvitationsHeadStateItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        civil_number=civil_number,
        customer_uuid=customer_uuid,
        email=email,
        o=o,
        page=page,
        page_size=page_size,
        role_name=role_name,
        role_uuid=role_uuid,
        scope_type=scope_type,
        state=state,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
