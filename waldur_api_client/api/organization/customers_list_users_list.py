from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.customers_list_users_list_field_item import CustomersListUsersListFieldItem
from ...models.customers_list_users_list_o_item import CustomersListUsersListOItem
from ...models.user_role_details import UserRoleDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    abbreviation: Union[Unset, str] = UNSET,
    agreement_number: Union[Unset, str] = UNSET,
    archived: Union[Unset, bool] = UNSET,
    backend_id: Union[Unset, str] = UNSET,
    contact_details: Union[Unset, str] = UNSET,
    field: Union[Unset, list[CustomersListUsersListFieldItem]] = UNSET,
    full_name: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    native_name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[CustomersListUsersListOItem]] = UNSET,
    organization_group_name: Union[Unset, str] = UNSET,
    organization_group_uuid: Union[Unset, list[UUID]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
    registration_code: Union[Unset, str] = UNSET,
    role: Union[Unset, UUID] = UNSET,
    search_string: Union[Unset, str] = UNSET,
    user: Union[Unset, UUID] = UNSET,
    user_slug: Union[Unset, str] = UNSET,
    user_url: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["abbreviation"] = abbreviation

    params["agreement_number"] = agreement_number

    params["archived"] = archived

    params["backend_id"] = backend_id

    params["contact_details"] = contact_details

    json_field: Union[Unset, list[str]] = UNSET
    if not isinstance(field, Unset):
        json_field = []
        for field_item_data in field:
            field_item = field_item_data.value
            json_field.append(field_item)

    params["field"] = json_field

    params["full_name"] = full_name

    params["name"] = name

    params["name_exact"] = name_exact

    params["native_name"] = native_name

    json_o: Union[Unset, list[str]] = UNSET
    if not isinstance(o, Unset):
        json_o = []
        for o_item_data in o:
            o_item = o_item_data.value
            json_o.append(o_item)

    params["o"] = json_o

    params["organization_group_name"] = organization_group_name

    json_organization_group_uuid: Union[Unset, list[str]] = UNSET
    if not isinstance(organization_group_uuid, Unset):
        json_organization_group_uuid = []
        for organization_group_uuid_item_data in organization_group_uuid:
            organization_group_uuid_item = str(organization_group_uuid_item_data)
            json_organization_group_uuid.append(organization_group_uuid_item)

    params["organization_group_uuid"] = json_organization_group_uuid

    params["page"] = page

    params["page_size"] = page_size

    params["query"] = query

    params["registration_code"] = registration_code

    json_role: Union[Unset, str] = UNSET
    if not isinstance(role, Unset):
        json_role = str(role)
    params["role"] = json_role

    params["search_string"] = search_string

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
        "url": f"/api/customers/{uuid}/list_users/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["UserRoleDetails"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_paginated_user_role_details_list_item_data in _response_200:
            componentsschemas_paginated_user_role_details_list_item = UserRoleDetails.from_dict(
                componentsschemas_paginated_user_role_details_list_item_data
            )

            response_200.append(componentsschemas_paginated_user_role_details_list_item)

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
    abbreviation: Union[Unset, str] = UNSET,
    agreement_number: Union[Unset, str] = UNSET,
    archived: Union[Unset, bool] = UNSET,
    backend_id: Union[Unset, str] = UNSET,
    contact_details: Union[Unset, str] = UNSET,
    field: Union[Unset, list[CustomersListUsersListFieldItem]] = UNSET,
    full_name: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    native_name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[CustomersListUsersListOItem]] = UNSET,
    organization_group_name: Union[Unset, str] = UNSET,
    organization_group_uuid: Union[Unset, list[UUID]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
    registration_code: Union[Unset, str] = UNSET,
    role: Union[Unset, UUID] = UNSET,
    search_string: Union[Unset, str] = UNSET,
    user: Union[Unset, UUID] = UNSET,
    user_slug: Union[Unset, str] = UNSET,
    user_url: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Response[list["UserRoleDetails"]]:
    """
    Args:
        uuid (UUID):
        abbreviation (Union[Unset, str]):
        agreement_number (Union[Unset, str]):
        archived (Union[Unset, bool]):
        backend_id (Union[Unset, str]):
        contact_details (Union[Unset, str]):
        field (Union[Unset, list[CustomersListUsersListFieldItem]]):
        full_name (Union[Unset, str]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        native_name (Union[Unset, str]):
        o (Union[Unset, list[CustomersListUsersListOItem]]):
        organization_group_name (Union[Unset, str]):
        organization_group_uuid (Union[Unset, list[UUID]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        query (Union[Unset, str]):
        registration_code (Union[Unset, str]):
        role (Union[Unset, UUID]):
        search_string (Union[Unset, str]):
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
        abbreviation=abbreviation,
        agreement_number=agreement_number,
        archived=archived,
        backend_id=backend_id,
        contact_details=contact_details,
        field=field,
        full_name=full_name,
        name=name,
        name_exact=name_exact,
        native_name=native_name,
        o=o,
        organization_group_name=organization_group_name,
        organization_group_uuid=organization_group_uuid,
        page=page,
        page_size=page_size,
        query=query,
        registration_code=registration_code,
        role=role,
        search_string=search_string,
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
    abbreviation: Union[Unset, str] = UNSET,
    agreement_number: Union[Unset, str] = UNSET,
    archived: Union[Unset, bool] = UNSET,
    backend_id: Union[Unset, str] = UNSET,
    contact_details: Union[Unset, str] = UNSET,
    field: Union[Unset, list[CustomersListUsersListFieldItem]] = UNSET,
    full_name: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    native_name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[CustomersListUsersListOItem]] = UNSET,
    organization_group_name: Union[Unset, str] = UNSET,
    organization_group_uuid: Union[Unset, list[UUID]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
    registration_code: Union[Unset, str] = UNSET,
    role: Union[Unset, UUID] = UNSET,
    search_string: Union[Unset, str] = UNSET,
    user: Union[Unset, UUID] = UNSET,
    user_slug: Union[Unset, str] = UNSET,
    user_url: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Optional[list["UserRoleDetails"]]:
    """
    Args:
        uuid (UUID):
        abbreviation (Union[Unset, str]):
        agreement_number (Union[Unset, str]):
        archived (Union[Unset, bool]):
        backend_id (Union[Unset, str]):
        contact_details (Union[Unset, str]):
        field (Union[Unset, list[CustomersListUsersListFieldItem]]):
        full_name (Union[Unset, str]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        native_name (Union[Unset, str]):
        o (Union[Unset, list[CustomersListUsersListOItem]]):
        organization_group_name (Union[Unset, str]):
        organization_group_uuid (Union[Unset, list[UUID]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        query (Union[Unset, str]):
        registration_code (Union[Unset, str]):
        role (Union[Unset, UUID]):
        search_string (Union[Unset, str]):
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
        abbreviation=abbreviation,
        agreement_number=agreement_number,
        archived=archived,
        backend_id=backend_id,
        contact_details=contact_details,
        field=field,
        full_name=full_name,
        name=name,
        name_exact=name_exact,
        native_name=native_name,
        o=o,
        organization_group_name=organization_group_name,
        organization_group_uuid=organization_group_uuid,
        page=page,
        page_size=page_size,
        query=query,
        registration_code=registration_code,
        role=role,
        search_string=search_string,
        user=user,
        user_slug=user_slug,
        user_url=user_url,
        username=username,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    abbreviation: Union[Unset, str] = UNSET,
    agreement_number: Union[Unset, str] = UNSET,
    archived: Union[Unset, bool] = UNSET,
    backend_id: Union[Unset, str] = UNSET,
    contact_details: Union[Unset, str] = UNSET,
    field: Union[Unset, list[CustomersListUsersListFieldItem]] = UNSET,
    full_name: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    native_name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[CustomersListUsersListOItem]] = UNSET,
    organization_group_name: Union[Unset, str] = UNSET,
    organization_group_uuid: Union[Unset, list[UUID]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
    registration_code: Union[Unset, str] = UNSET,
    role: Union[Unset, UUID] = UNSET,
    search_string: Union[Unset, str] = UNSET,
    user: Union[Unset, UUID] = UNSET,
    user_slug: Union[Unset, str] = UNSET,
    user_url: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Response[list["UserRoleDetails"]]:
    """
    Args:
        uuid (UUID):
        abbreviation (Union[Unset, str]):
        agreement_number (Union[Unset, str]):
        archived (Union[Unset, bool]):
        backend_id (Union[Unset, str]):
        contact_details (Union[Unset, str]):
        field (Union[Unset, list[CustomersListUsersListFieldItem]]):
        full_name (Union[Unset, str]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        native_name (Union[Unset, str]):
        o (Union[Unset, list[CustomersListUsersListOItem]]):
        organization_group_name (Union[Unset, str]):
        organization_group_uuid (Union[Unset, list[UUID]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        query (Union[Unset, str]):
        registration_code (Union[Unset, str]):
        role (Union[Unset, UUID]):
        search_string (Union[Unset, str]):
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
        abbreviation=abbreviation,
        agreement_number=agreement_number,
        archived=archived,
        backend_id=backend_id,
        contact_details=contact_details,
        field=field,
        full_name=full_name,
        name=name,
        name_exact=name_exact,
        native_name=native_name,
        o=o,
        organization_group_name=organization_group_name,
        organization_group_uuid=organization_group_uuid,
        page=page,
        page_size=page_size,
        query=query,
        registration_code=registration_code,
        role=role,
        search_string=search_string,
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
    abbreviation: Union[Unset, str] = UNSET,
    agreement_number: Union[Unset, str] = UNSET,
    archived: Union[Unset, bool] = UNSET,
    backend_id: Union[Unset, str] = UNSET,
    contact_details: Union[Unset, str] = UNSET,
    field: Union[Unset, list[CustomersListUsersListFieldItem]] = UNSET,
    full_name: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    native_name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[CustomersListUsersListOItem]] = UNSET,
    organization_group_name: Union[Unset, str] = UNSET,
    organization_group_uuid: Union[Unset, list[UUID]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
    registration_code: Union[Unset, str] = UNSET,
    role: Union[Unset, UUID] = UNSET,
    search_string: Union[Unset, str] = UNSET,
    user: Union[Unset, UUID] = UNSET,
    user_slug: Union[Unset, str] = UNSET,
    user_url: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Optional[list["UserRoleDetails"]]:
    """
    Args:
        uuid (UUID):
        abbreviation (Union[Unset, str]):
        agreement_number (Union[Unset, str]):
        archived (Union[Unset, bool]):
        backend_id (Union[Unset, str]):
        contact_details (Union[Unset, str]):
        field (Union[Unset, list[CustomersListUsersListFieldItem]]):
        full_name (Union[Unset, str]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        native_name (Union[Unset, str]):
        o (Union[Unset, list[CustomersListUsersListOItem]]):
        organization_group_name (Union[Unset, str]):
        organization_group_uuid (Union[Unset, list[UUID]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        query (Union[Unset, str]):
        registration_code (Union[Unset, str]):
        role (Union[Unset, UUID]):
        search_string (Union[Unset, str]):
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
            abbreviation=abbreviation,
            agreement_number=agreement_number,
            archived=archived,
            backend_id=backend_id,
            contact_details=contact_details,
            field=field,
            full_name=full_name,
            name=name,
            name_exact=name_exact,
            native_name=native_name,
            o=o,
            organization_group_name=organization_group_name,
            organization_group_uuid=organization_group_uuid,
            page=page,
            page_size=page_size,
            query=query,
            registration_code=registration_code,
            role=role,
            search_string=search_string,
            user=user,
            user_slug=user_slug,
            user_url=user_url,
            username=username,
        )
    ).parsed
