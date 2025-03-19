import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.projects_list_users_list_field_item import ProjectsListUsersListFieldItem
from ...models.projects_list_users_list_o_item import ProjectsListUsersListOItem
from ...models.user_role_details import UserRoleDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    backend_id: Union[Unset, str] = UNSET,
    can_admin: Union[Unset, bool] = UNSET,
    can_manage: Union[Unset, bool] = UNSET,
    conceal_ended_projects: Union[Unset, bool] = UNSET,
    created: Union[Unset, datetime.datetime] = UNSET,
    customer: Union[Unset, list[UUID]] = UNSET,
    customer_abbreviation: Union[Unset, str] = UNSET,
    customer_name: Union[Unset, str] = UNSET,
    customer_native_name: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    field: Union[Unset, list[ProjectsListUsersListFieldItem]] = UNSET,
    full_name: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    native_name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[ProjectsListUsersListOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
    role: Union[Unset, UUID] = UNSET,
    search_string: Union[Unset, str] = UNSET,
    user: Union[Unset, UUID] = UNSET,
    user_slug: Union[Unset, str] = UNSET,
    user_url: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["backend_id"] = backend_id

    params["can_admin"] = can_admin

    params["can_manage"] = can_manage

    params["conceal_ended_projects"] = conceal_ended_projects

    json_created: Union[Unset, str] = UNSET
    if not isinstance(created, Unset):
        json_created = created.isoformat()
    params["created"] = json_created

    json_customer: Union[Unset, list[str]] = UNSET
    if not isinstance(customer, Unset):
        json_customer = []
        for customer_item_data in customer:
            customer_item = str(customer_item_data)
            json_customer.append(customer_item)

    params["customer"] = json_customer

    params["customer_abbreviation"] = customer_abbreviation

    params["customer_name"] = customer_name

    params["customer_native_name"] = customer_native_name

    params["description"] = description

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

    params["page"] = page

    params["page_size"] = page_size

    params["query"] = query

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
        "url": f"/api/projects/{uuid}/list_users/",
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
    backend_id: Union[Unset, str] = UNSET,
    can_admin: Union[Unset, bool] = UNSET,
    can_manage: Union[Unset, bool] = UNSET,
    conceal_ended_projects: Union[Unset, bool] = UNSET,
    created: Union[Unset, datetime.datetime] = UNSET,
    customer: Union[Unset, list[UUID]] = UNSET,
    customer_abbreviation: Union[Unset, str] = UNSET,
    customer_name: Union[Unset, str] = UNSET,
    customer_native_name: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    field: Union[Unset, list[ProjectsListUsersListFieldItem]] = UNSET,
    full_name: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    native_name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[ProjectsListUsersListOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
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
        backend_id (Union[Unset, str]):
        can_admin (Union[Unset, bool]):
        can_manage (Union[Unset, bool]):
        conceal_ended_projects (Union[Unset, bool]):
        created (Union[Unset, datetime.datetime]):
        customer (Union[Unset, list[UUID]]):
        customer_abbreviation (Union[Unset, str]):
        customer_name (Union[Unset, str]):
        customer_native_name (Union[Unset, str]):
        description (Union[Unset, str]):
        field (Union[Unset, list[ProjectsListUsersListFieldItem]]):
        full_name (Union[Unset, str]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        native_name (Union[Unset, str]):
        o (Union[Unset, list[ProjectsListUsersListOItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        query (Union[Unset, str]):
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
        backend_id=backend_id,
        can_admin=can_admin,
        can_manage=can_manage,
        conceal_ended_projects=conceal_ended_projects,
        created=created,
        customer=customer,
        customer_abbreviation=customer_abbreviation,
        customer_name=customer_name,
        customer_native_name=customer_native_name,
        description=description,
        field=field,
        full_name=full_name,
        name=name,
        name_exact=name_exact,
        native_name=native_name,
        o=o,
        page=page,
        page_size=page_size,
        query=query,
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
    backend_id: Union[Unset, str] = UNSET,
    can_admin: Union[Unset, bool] = UNSET,
    can_manage: Union[Unset, bool] = UNSET,
    conceal_ended_projects: Union[Unset, bool] = UNSET,
    created: Union[Unset, datetime.datetime] = UNSET,
    customer: Union[Unset, list[UUID]] = UNSET,
    customer_abbreviation: Union[Unset, str] = UNSET,
    customer_name: Union[Unset, str] = UNSET,
    customer_native_name: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    field: Union[Unset, list[ProjectsListUsersListFieldItem]] = UNSET,
    full_name: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    native_name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[ProjectsListUsersListOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
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
        backend_id (Union[Unset, str]):
        can_admin (Union[Unset, bool]):
        can_manage (Union[Unset, bool]):
        conceal_ended_projects (Union[Unset, bool]):
        created (Union[Unset, datetime.datetime]):
        customer (Union[Unset, list[UUID]]):
        customer_abbreviation (Union[Unset, str]):
        customer_name (Union[Unset, str]):
        customer_native_name (Union[Unset, str]):
        description (Union[Unset, str]):
        field (Union[Unset, list[ProjectsListUsersListFieldItem]]):
        full_name (Union[Unset, str]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        native_name (Union[Unset, str]):
        o (Union[Unset, list[ProjectsListUsersListOItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        query (Union[Unset, str]):
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
        backend_id=backend_id,
        can_admin=can_admin,
        can_manage=can_manage,
        conceal_ended_projects=conceal_ended_projects,
        created=created,
        customer=customer,
        customer_abbreviation=customer_abbreviation,
        customer_name=customer_name,
        customer_native_name=customer_native_name,
        description=description,
        field=field,
        full_name=full_name,
        name=name,
        name_exact=name_exact,
        native_name=native_name,
        o=o,
        page=page,
        page_size=page_size,
        query=query,
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
    backend_id: Union[Unset, str] = UNSET,
    can_admin: Union[Unset, bool] = UNSET,
    can_manage: Union[Unset, bool] = UNSET,
    conceal_ended_projects: Union[Unset, bool] = UNSET,
    created: Union[Unset, datetime.datetime] = UNSET,
    customer: Union[Unset, list[UUID]] = UNSET,
    customer_abbreviation: Union[Unset, str] = UNSET,
    customer_name: Union[Unset, str] = UNSET,
    customer_native_name: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    field: Union[Unset, list[ProjectsListUsersListFieldItem]] = UNSET,
    full_name: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    native_name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[ProjectsListUsersListOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
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
        backend_id (Union[Unset, str]):
        can_admin (Union[Unset, bool]):
        can_manage (Union[Unset, bool]):
        conceal_ended_projects (Union[Unset, bool]):
        created (Union[Unset, datetime.datetime]):
        customer (Union[Unset, list[UUID]]):
        customer_abbreviation (Union[Unset, str]):
        customer_name (Union[Unset, str]):
        customer_native_name (Union[Unset, str]):
        description (Union[Unset, str]):
        field (Union[Unset, list[ProjectsListUsersListFieldItem]]):
        full_name (Union[Unset, str]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        native_name (Union[Unset, str]):
        o (Union[Unset, list[ProjectsListUsersListOItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        query (Union[Unset, str]):
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
        backend_id=backend_id,
        can_admin=can_admin,
        can_manage=can_manage,
        conceal_ended_projects=conceal_ended_projects,
        created=created,
        customer=customer,
        customer_abbreviation=customer_abbreviation,
        customer_name=customer_name,
        customer_native_name=customer_native_name,
        description=description,
        field=field,
        full_name=full_name,
        name=name,
        name_exact=name_exact,
        native_name=native_name,
        o=o,
        page=page,
        page_size=page_size,
        query=query,
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
    backend_id: Union[Unset, str] = UNSET,
    can_admin: Union[Unset, bool] = UNSET,
    can_manage: Union[Unset, bool] = UNSET,
    conceal_ended_projects: Union[Unset, bool] = UNSET,
    created: Union[Unset, datetime.datetime] = UNSET,
    customer: Union[Unset, list[UUID]] = UNSET,
    customer_abbreviation: Union[Unset, str] = UNSET,
    customer_name: Union[Unset, str] = UNSET,
    customer_native_name: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    field: Union[Unset, list[ProjectsListUsersListFieldItem]] = UNSET,
    full_name: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    native_name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[ProjectsListUsersListOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
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
        backend_id (Union[Unset, str]):
        can_admin (Union[Unset, bool]):
        can_manage (Union[Unset, bool]):
        conceal_ended_projects (Union[Unset, bool]):
        created (Union[Unset, datetime.datetime]):
        customer (Union[Unset, list[UUID]]):
        customer_abbreviation (Union[Unset, str]):
        customer_name (Union[Unset, str]):
        customer_native_name (Union[Unset, str]):
        description (Union[Unset, str]):
        field (Union[Unset, list[ProjectsListUsersListFieldItem]]):
        full_name (Union[Unset, str]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        native_name (Union[Unset, str]):
        o (Union[Unset, list[ProjectsListUsersListOItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        query (Union[Unset, str]):
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
            backend_id=backend_id,
            can_admin=can_admin,
            can_manage=can_manage,
            conceal_ended_projects=conceal_ended_projects,
            created=created,
            customer=customer,
            customer_abbreviation=customer_abbreviation,
            customer_name=customer_name,
            customer_native_name=customer_native_name,
            description=description,
            field=field,
            full_name=full_name,
            name=name,
            name_exact=name_exact,
            native_name=native_name,
            o=o,
            page=page,
            page_size=page_size,
            query=query,
            role=role,
            search_string=search_string,
            user=user,
            user_slug=user_slug,
            user_url=user_url,
            username=username,
        )
    ).parsed
