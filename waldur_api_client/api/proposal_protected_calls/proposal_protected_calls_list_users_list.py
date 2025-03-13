from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.proposal_protected_calls_list_users_list_field_item import ProposalProtectedCallsListUsersListFieldItem
from ...models.proposal_protected_calls_list_users_list_o_item import ProposalProtectedCallsListUsersListOItem
from ...models.proposal_protected_calls_list_users_list_state_item import ProposalProtectedCallsListUsersListStateItem
from ...models.user_role_details import UserRoleDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    customer: Union[Unset, str] = UNSET,
    customer_keyword: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    field: Union[Unset, list[ProposalProtectedCallsListUsersListFieldItem]] = UNSET,
    full_name: Union[Unset, str] = UNSET,
    has_active_round: Union[Unset, bool] = UNSET,
    name: Union[Unset, str] = UNSET,
    native_name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[ProposalProtectedCallsListUsersListOItem]] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    offerings_provider_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    role: Union[Unset, UUID] = UNSET,
    search_string: Union[Unset, str] = UNSET,
    state: Union[Unset, list[ProposalProtectedCallsListUsersListStateItem]] = UNSET,
    user: Union[Unset, UUID] = UNSET,
    user_slug: Union[Unset, str] = UNSET,
    user_url: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["customer"] = customer

    params["customer_keyword"] = customer_keyword

    json_customer_uuid: Union[Unset, str] = UNSET
    if not isinstance(customer_uuid, Unset):
        json_customer_uuid = str(customer_uuid)
    params["customer_uuid"] = json_customer_uuid

    json_field: Union[Unset, list[str]] = UNSET
    if not isinstance(field, Unset):
        json_field = []
        for field_item_data in field:
            field_item = field_item_data.value
            json_field.append(field_item)

    params["field"] = json_field

    params["full_name"] = full_name

    params["has_active_round"] = has_active_round

    params["name"] = name

    params["native_name"] = native_name

    json_o: Union[Unset, list[str]] = UNSET
    if not isinstance(o, Unset):
        json_o = []
        for o_item_data in o:
            o_item = o_item_data.value
            json_o.append(o_item)

    params["o"] = json_o

    json_offering_uuid: Union[Unset, str] = UNSET
    if not isinstance(offering_uuid, Unset):
        json_offering_uuid = str(offering_uuid)
    params["offering_uuid"] = json_offering_uuid

    json_offerings_provider_uuid: Union[Unset, str] = UNSET
    if not isinstance(offerings_provider_uuid, Unset):
        json_offerings_provider_uuid = str(offerings_provider_uuid)
    params["offerings_provider_uuid"] = json_offerings_provider_uuid

    params["page"] = page

    params["page_size"] = page_size

    json_role: Union[Unset, str] = UNSET
    if not isinstance(role, Unset):
        json_role = str(role)
    params["role"] = json_role

    params["search_string"] = search_string

    json_state: Union[Unset, list[str]] = UNSET
    if not isinstance(state, Unset):
        json_state = []
        for state_item_data in state:
            state_item = state_item_data.value
            json_state.append(state_item)

    params["state"] = json_state

    json_user: Union[Unset, str] = UNSET
    if not isinstance(user, Unset):
        json_user = str(user)
    params["user"] = json_user

    params["user_slug"] = user_slug

    params["user_url"] = user_url

    params["username"] = username

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/proposal-protected-calls/{uuid}/list_users/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["UserRoleDetails"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = UserRoleDetails.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["UserRoleDetails"]]:
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
    customer: Union[Unset, str] = UNSET,
    customer_keyword: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    field: Union[Unset, list[ProposalProtectedCallsListUsersListFieldItem]] = UNSET,
    full_name: Union[Unset, str] = UNSET,
    has_active_round: Union[Unset, bool] = UNSET,
    name: Union[Unset, str] = UNSET,
    native_name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[ProposalProtectedCallsListUsersListOItem]] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    offerings_provider_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    role: Union[Unset, UUID] = UNSET,
    search_string: Union[Unset, str] = UNSET,
    state: Union[Unset, list[ProposalProtectedCallsListUsersListStateItem]] = UNSET,
    user: Union[Unset, UUID] = UNSET,
    user_slug: Union[Unset, str] = UNSET,
    user_url: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Response[list["UserRoleDetails"]]:
    """
    Args:
        uuid (UUID):
        customer (Union[Unset, str]):
        customer_keyword (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        field (Union[Unset, list[ProposalProtectedCallsListUsersListFieldItem]]):
        full_name (Union[Unset, str]):
        has_active_round (Union[Unset, bool]):
        name (Union[Unset, str]):
        native_name (Union[Unset, str]):
        o (Union[Unset, list[ProposalProtectedCallsListUsersListOItem]]):
        offering_uuid (Union[Unset, UUID]):
        offerings_provider_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        role (Union[Unset, UUID]):
        search_string (Union[Unset, str]):
        state (Union[Unset, list[ProposalProtectedCallsListUsersListStateItem]]):
        user (Union[Unset, UUID]):
        user_slug (Union[Unset, str]):
        user_url (Union[Unset, str]):
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['UserRoleDetails']]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        customer=customer,
        customer_keyword=customer_keyword,
        customer_uuid=customer_uuid,
        field=field,
        full_name=full_name,
        has_active_round=has_active_round,
        name=name,
        native_name=native_name,
        o=o,
        offering_uuid=offering_uuid,
        offerings_provider_uuid=offerings_provider_uuid,
        page=page,
        page_size=page_size,
        role=role,
        search_string=search_string,
        state=state,
        user=user,
        user_slug=user_slug,
        user_url=user_url,
        username=username,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    customer: Union[Unset, str] = UNSET,
    customer_keyword: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    field: Union[Unset, list[ProposalProtectedCallsListUsersListFieldItem]] = UNSET,
    full_name: Union[Unset, str] = UNSET,
    has_active_round: Union[Unset, bool] = UNSET,
    name: Union[Unset, str] = UNSET,
    native_name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[ProposalProtectedCallsListUsersListOItem]] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    offerings_provider_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    role: Union[Unset, UUID] = UNSET,
    search_string: Union[Unset, str] = UNSET,
    state: Union[Unset, list[ProposalProtectedCallsListUsersListStateItem]] = UNSET,
    user: Union[Unset, UUID] = UNSET,
    user_slug: Union[Unset, str] = UNSET,
    user_url: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Optional[list["UserRoleDetails"]]:
    """
    Args:
        uuid (UUID):
        customer (Union[Unset, str]):
        customer_keyword (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        field (Union[Unset, list[ProposalProtectedCallsListUsersListFieldItem]]):
        full_name (Union[Unset, str]):
        has_active_round (Union[Unset, bool]):
        name (Union[Unset, str]):
        native_name (Union[Unset, str]):
        o (Union[Unset, list[ProposalProtectedCallsListUsersListOItem]]):
        offering_uuid (Union[Unset, UUID]):
        offerings_provider_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        role (Union[Unset, UUID]):
        search_string (Union[Unset, str]):
        state (Union[Unset, list[ProposalProtectedCallsListUsersListStateItem]]):
        user (Union[Unset, UUID]):
        user_slug (Union[Unset, str]):
        user_url (Union[Unset, str]):
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['UserRoleDetails']
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        customer=customer,
        customer_keyword=customer_keyword,
        customer_uuid=customer_uuid,
        field=field,
        full_name=full_name,
        has_active_round=has_active_round,
        name=name,
        native_name=native_name,
        o=o,
        offering_uuid=offering_uuid,
        offerings_provider_uuid=offerings_provider_uuid,
        page=page,
        page_size=page_size,
        role=role,
        search_string=search_string,
        state=state,
        user=user,
        user_slug=user_slug,
        user_url=user_url,
        username=username,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    customer: Union[Unset, str] = UNSET,
    customer_keyword: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    field: Union[Unset, list[ProposalProtectedCallsListUsersListFieldItem]] = UNSET,
    full_name: Union[Unset, str] = UNSET,
    has_active_round: Union[Unset, bool] = UNSET,
    name: Union[Unset, str] = UNSET,
    native_name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[ProposalProtectedCallsListUsersListOItem]] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    offerings_provider_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    role: Union[Unset, UUID] = UNSET,
    search_string: Union[Unset, str] = UNSET,
    state: Union[Unset, list[ProposalProtectedCallsListUsersListStateItem]] = UNSET,
    user: Union[Unset, UUID] = UNSET,
    user_slug: Union[Unset, str] = UNSET,
    user_url: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Response[list["UserRoleDetails"]]:
    """
    Args:
        uuid (UUID):
        customer (Union[Unset, str]):
        customer_keyword (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        field (Union[Unset, list[ProposalProtectedCallsListUsersListFieldItem]]):
        full_name (Union[Unset, str]):
        has_active_round (Union[Unset, bool]):
        name (Union[Unset, str]):
        native_name (Union[Unset, str]):
        o (Union[Unset, list[ProposalProtectedCallsListUsersListOItem]]):
        offering_uuid (Union[Unset, UUID]):
        offerings_provider_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        role (Union[Unset, UUID]):
        search_string (Union[Unset, str]):
        state (Union[Unset, list[ProposalProtectedCallsListUsersListStateItem]]):
        user (Union[Unset, UUID]):
        user_slug (Union[Unset, str]):
        user_url (Union[Unset, str]):
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['UserRoleDetails']]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        customer=customer,
        customer_keyword=customer_keyword,
        customer_uuid=customer_uuid,
        field=field,
        full_name=full_name,
        has_active_round=has_active_round,
        name=name,
        native_name=native_name,
        o=o,
        offering_uuid=offering_uuid,
        offerings_provider_uuid=offerings_provider_uuid,
        page=page,
        page_size=page_size,
        role=role,
        search_string=search_string,
        state=state,
        user=user,
        user_slug=user_slug,
        user_url=user_url,
        username=username,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    customer: Union[Unset, str] = UNSET,
    customer_keyword: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    field: Union[Unset, list[ProposalProtectedCallsListUsersListFieldItem]] = UNSET,
    full_name: Union[Unset, str] = UNSET,
    has_active_round: Union[Unset, bool] = UNSET,
    name: Union[Unset, str] = UNSET,
    native_name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[ProposalProtectedCallsListUsersListOItem]] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    offerings_provider_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    role: Union[Unset, UUID] = UNSET,
    search_string: Union[Unset, str] = UNSET,
    state: Union[Unset, list[ProposalProtectedCallsListUsersListStateItem]] = UNSET,
    user: Union[Unset, UUID] = UNSET,
    user_slug: Union[Unset, str] = UNSET,
    user_url: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Optional[list["UserRoleDetails"]]:
    """
    Args:
        uuid (UUID):
        customer (Union[Unset, str]):
        customer_keyword (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        field (Union[Unset, list[ProposalProtectedCallsListUsersListFieldItem]]):
        full_name (Union[Unset, str]):
        has_active_round (Union[Unset, bool]):
        name (Union[Unset, str]):
        native_name (Union[Unset, str]):
        o (Union[Unset, list[ProposalProtectedCallsListUsersListOItem]]):
        offering_uuid (Union[Unset, UUID]):
        offerings_provider_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        role (Union[Unset, UUID]):
        search_string (Union[Unset, str]):
        state (Union[Unset, list[ProposalProtectedCallsListUsersListStateItem]]):
        user (Union[Unset, UUID]):
        user_slug (Union[Unset, str]):
        user_url (Union[Unset, str]):
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['UserRoleDetails']
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            customer=customer,
            customer_keyword=customer_keyword,
            customer_uuid=customer_uuid,
            field=field,
            full_name=full_name,
            has_active_round=has_active_round,
            name=name,
            native_name=native_name,
            o=o,
            offering_uuid=offering_uuid,
            offerings_provider_uuid=offerings_provider_uuid,
            page=page,
            page_size=page_size,
            role=role,
            search_string=search_string,
            state=state,
            user=user,
            user_slug=user_slug,
            user_url=user_url,
            username=username,
        )
    ).parsed
