from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.marketplace_provider_offerings_list_users_list_field_item import (
    MarketplaceProviderOfferingsListUsersListFieldItem,
)
from ...models.marketplace_provider_offerings_list_users_list_o_item import (
    MarketplaceProviderOfferingsListUsersListOItem,
)
from ...models.marketplace_provider_offerings_list_users_list_state_item import (
    MarketplaceProviderOfferingsListUsersListStateItem,
)
from ...models.user_role_details import UserRoleDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    accessible_via_calls: Union[Unset, bool] = UNSET,
    allowed_customer_uuid: Union[Unset, UUID] = UNSET,
    attributes: Union[Unset, str] = UNSET,
    billable: Union[Unset, bool] = UNSET,
    category_group_uuid: Union[Unset, UUID] = UNSET,
    category_uuid: Union[Unset, UUID] = UNSET,
    customer: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    description: Union[Unset, str] = UNSET,
    field: Union[Unset, list[MarketplaceProviderOfferingsListUsersListFieldItem]] = UNSET,
    full_name: Union[Unset, str] = UNSET,
    keyword: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    native_name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[MarketplaceProviderOfferingsListUsersListOItem]] = UNSET,
    organization_group_uuid: Union[Unset, list[UUID]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    parent_uuid: Union[Unset, UUID] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    role: Union[Unset, UUID] = UNSET,
    scope_uuid: Union[Unset, UUID] = UNSET,
    search_string: Union[Unset, str] = UNSET,
    service_manager_uuid: Union[Unset, UUID] = UNSET,
    shared: Union[Unset, bool] = UNSET,
    state: Union[Unset, list[MarketplaceProviderOfferingsListUsersListStateItem]] = UNSET,
    type_: Union[Unset, list[str]] = UNSET,
    user: Union[Unset, UUID] = UNSET,
    user_slug: Union[Unset, str] = UNSET,
    user_url: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["accessible_via_calls"] = accessible_via_calls

    json_allowed_customer_uuid: Union[Unset, str] = UNSET
    if not isinstance(allowed_customer_uuid, Unset):
        json_allowed_customer_uuid = str(allowed_customer_uuid)
    params["allowed_customer_uuid"] = json_allowed_customer_uuid

    params["attributes"] = attributes

    params["billable"] = billable

    json_category_group_uuid: Union[Unset, str] = UNSET
    if not isinstance(category_group_uuid, Unset):
        json_category_group_uuid = str(category_group_uuid)
    params["category_group_uuid"] = json_category_group_uuid

    json_category_uuid: Union[Unset, str] = UNSET
    if not isinstance(category_uuid, Unset):
        json_category_uuid = str(category_uuid)
    params["category_uuid"] = json_category_uuid

    params["customer"] = customer

    json_customer_uuid: Union[Unset, str] = UNSET
    if not isinstance(customer_uuid, Unset):
        json_customer_uuid = str(customer_uuid)
    params["customer_uuid"] = json_customer_uuid

    params["description"] = description

    json_field: Union[Unset, list[str]] = UNSET
    if not isinstance(field, Unset):
        json_field = []
        for field_item_data in field:
            field_item = field_item_data.value
            json_field.append(field_item)

    params["field"] = json_field

    params["full_name"] = full_name

    params["keyword"] = keyword

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

    json_organization_group_uuid: Union[Unset, list[str]] = UNSET
    if not isinstance(organization_group_uuid, Unset):
        json_organization_group_uuid = []
        for organization_group_uuid_item_data in organization_group_uuid:
            organization_group_uuid_item = str(organization_group_uuid_item_data)
            json_organization_group_uuid.append(organization_group_uuid_item)

    params["organization_group_uuid"] = json_organization_group_uuid

    params["page"] = page

    params["page_size"] = page_size

    json_parent_uuid: Union[Unset, str] = UNSET
    if not isinstance(parent_uuid, Unset):
        json_parent_uuid = str(parent_uuid)
    params["parent_uuid"] = json_parent_uuid

    json_project_uuid: Union[Unset, str] = UNSET
    if not isinstance(project_uuid, Unset):
        json_project_uuid = str(project_uuid)
    params["project_uuid"] = json_project_uuid

    json_role: Union[Unset, str] = UNSET
    if not isinstance(role, Unset):
        json_role = str(role)
    params["role"] = json_role

    json_scope_uuid: Union[Unset, str] = UNSET
    if not isinstance(scope_uuid, Unset):
        json_scope_uuid = str(scope_uuid)
    params["scope_uuid"] = json_scope_uuid

    params["search_string"] = search_string

    json_service_manager_uuid: Union[Unset, str] = UNSET
    if not isinstance(service_manager_uuid, Unset):
        json_service_manager_uuid = str(service_manager_uuid)
    params["service_manager_uuid"] = json_service_manager_uuid

    params["shared"] = shared

    json_state: Union[Unset, list[str]] = UNSET
    if not isinstance(state, Unset):
        json_state = []
        for state_item_data in state:
            state_item = state_item_data.value
            json_state.append(state_item)

    params["state"] = json_state

    json_type_: Union[Unset, list[str]] = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_

    params["type"] = json_type_

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
        "url": f"/api/marketplace-provider-offerings/{uuid}/list_users/",
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
    accessible_via_calls: Union[Unset, bool] = UNSET,
    allowed_customer_uuid: Union[Unset, UUID] = UNSET,
    attributes: Union[Unset, str] = UNSET,
    billable: Union[Unset, bool] = UNSET,
    category_group_uuid: Union[Unset, UUID] = UNSET,
    category_uuid: Union[Unset, UUID] = UNSET,
    customer: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    description: Union[Unset, str] = UNSET,
    field: Union[Unset, list[MarketplaceProviderOfferingsListUsersListFieldItem]] = UNSET,
    full_name: Union[Unset, str] = UNSET,
    keyword: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    native_name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[MarketplaceProviderOfferingsListUsersListOItem]] = UNSET,
    organization_group_uuid: Union[Unset, list[UUID]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    parent_uuid: Union[Unset, UUID] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    role: Union[Unset, UUID] = UNSET,
    scope_uuid: Union[Unset, UUID] = UNSET,
    search_string: Union[Unset, str] = UNSET,
    service_manager_uuid: Union[Unset, UUID] = UNSET,
    shared: Union[Unset, bool] = UNSET,
    state: Union[Unset, list[MarketplaceProviderOfferingsListUsersListStateItem]] = UNSET,
    type_: Union[Unset, list[str]] = UNSET,
    user: Union[Unset, UUID] = UNSET,
    user_slug: Union[Unset, str] = UNSET,
    user_url: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Response[list["UserRoleDetails"]]:
    """
    Args:
        uuid (UUID):
        accessible_via_calls (Union[Unset, bool]):
        allowed_customer_uuid (Union[Unset, UUID]):
        attributes (Union[Unset, str]):
        billable (Union[Unset, bool]):
        category_group_uuid (Union[Unset, UUID]):
        category_uuid (Union[Unset, UUID]):
        customer (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        description (Union[Unset, str]):
        field (Union[Unset, list[MarketplaceProviderOfferingsListUsersListFieldItem]]):
        full_name (Union[Unset, str]):
        keyword (Union[Unset, str]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        native_name (Union[Unset, str]):
        o (Union[Unset, list[MarketplaceProviderOfferingsListUsersListOItem]]):
        organization_group_uuid (Union[Unset, list[UUID]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        parent_uuid (Union[Unset, UUID]):
        project_uuid (Union[Unset, UUID]):
        role (Union[Unset, UUID]):
        scope_uuid (Union[Unset, UUID]):
        search_string (Union[Unset, str]):
        service_manager_uuid (Union[Unset, UUID]):
        shared (Union[Unset, bool]):
        state (Union[Unset, list[MarketplaceProviderOfferingsListUsersListStateItem]]):
        type_ (Union[Unset, list[str]]):
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
        accessible_via_calls=accessible_via_calls,
        allowed_customer_uuid=allowed_customer_uuid,
        attributes=attributes,
        billable=billable,
        category_group_uuid=category_group_uuid,
        category_uuid=category_uuid,
        customer=customer,
        customer_uuid=customer_uuid,
        description=description,
        field=field,
        full_name=full_name,
        keyword=keyword,
        name=name,
        name_exact=name_exact,
        native_name=native_name,
        o=o,
        organization_group_uuid=organization_group_uuid,
        page=page,
        page_size=page_size,
        parent_uuid=parent_uuid,
        project_uuid=project_uuid,
        role=role,
        scope_uuid=scope_uuid,
        search_string=search_string,
        service_manager_uuid=service_manager_uuid,
        shared=shared,
        state=state,
        type_=type_,
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
    accessible_via_calls: Union[Unset, bool] = UNSET,
    allowed_customer_uuid: Union[Unset, UUID] = UNSET,
    attributes: Union[Unset, str] = UNSET,
    billable: Union[Unset, bool] = UNSET,
    category_group_uuid: Union[Unset, UUID] = UNSET,
    category_uuid: Union[Unset, UUID] = UNSET,
    customer: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    description: Union[Unset, str] = UNSET,
    field: Union[Unset, list[MarketplaceProviderOfferingsListUsersListFieldItem]] = UNSET,
    full_name: Union[Unset, str] = UNSET,
    keyword: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    native_name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[MarketplaceProviderOfferingsListUsersListOItem]] = UNSET,
    organization_group_uuid: Union[Unset, list[UUID]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    parent_uuid: Union[Unset, UUID] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    role: Union[Unset, UUID] = UNSET,
    scope_uuid: Union[Unset, UUID] = UNSET,
    search_string: Union[Unset, str] = UNSET,
    service_manager_uuid: Union[Unset, UUID] = UNSET,
    shared: Union[Unset, bool] = UNSET,
    state: Union[Unset, list[MarketplaceProviderOfferingsListUsersListStateItem]] = UNSET,
    type_: Union[Unset, list[str]] = UNSET,
    user: Union[Unset, UUID] = UNSET,
    user_slug: Union[Unset, str] = UNSET,
    user_url: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Optional[list["UserRoleDetails"]]:
    """
    Args:
        uuid (UUID):
        accessible_via_calls (Union[Unset, bool]):
        allowed_customer_uuid (Union[Unset, UUID]):
        attributes (Union[Unset, str]):
        billable (Union[Unset, bool]):
        category_group_uuid (Union[Unset, UUID]):
        category_uuid (Union[Unset, UUID]):
        customer (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        description (Union[Unset, str]):
        field (Union[Unset, list[MarketplaceProviderOfferingsListUsersListFieldItem]]):
        full_name (Union[Unset, str]):
        keyword (Union[Unset, str]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        native_name (Union[Unset, str]):
        o (Union[Unset, list[MarketplaceProviderOfferingsListUsersListOItem]]):
        organization_group_uuid (Union[Unset, list[UUID]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        parent_uuid (Union[Unset, UUID]):
        project_uuid (Union[Unset, UUID]):
        role (Union[Unset, UUID]):
        scope_uuid (Union[Unset, UUID]):
        search_string (Union[Unset, str]):
        service_manager_uuid (Union[Unset, UUID]):
        shared (Union[Unset, bool]):
        state (Union[Unset, list[MarketplaceProviderOfferingsListUsersListStateItem]]):
        type_ (Union[Unset, list[str]]):
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
        accessible_via_calls=accessible_via_calls,
        allowed_customer_uuid=allowed_customer_uuid,
        attributes=attributes,
        billable=billable,
        category_group_uuid=category_group_uuid,
        category_uuid=category_uuid,
        customer=customer,
        customer_uuid=customer_uuid,
        description=description,
        field=field,
        full_name=full_name,
        keyword=keyword,
        name=name,
        name_exact=name_exact,
        native_name=native_name,
        o=o,
        organization_group_uuid=organization_group_uuid,
        page=page,
        page_size=page_size,
        parent_uuid=parent_uuid,
        project_uuid=project_uuid,
        role=role,
        scope_uuid=scope_uuid,
        search_string=search_string,
        service_manager_uuid=service_manager_uuid,
        shared=shared,
        state=state,
        type_=type_,
        user=user,
        user_slug=user_slug,
        user_url=user_url,
        username=username,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    accessible_via_calls: Union[Unset, bool] = UNSET,
    allowed_customer_uuid: Union[Unset, UUID] = UNSET,
    attributes: Union[Unset, str] = UNSET,
    billable: Union[Unset, bool] = UNSET,
    category_group_uuid: Union[Unset, UUID] = UNSET,
    category_uuid: Union[Unset, UUID] = UNSET,
    customer: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    description: Union[Unset, str] = UNSET,
    field: Union[Unset, list[MarketplaceProviderOfferingsListUsersListFieldItem]] = UNSET,
    full_name: Union[Unset, str] = UNSET,
    keyword: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    native_name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[MarketplaceProviderOfferingsListUsersListOItem]] = UNSET,
    organization_group_uuid: Union[Unset, list[UUID]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    parent_uuid: Union[Unset, UUID] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    role: Union[Unset, UUID] = UNSET,
    scope_uuid: Union[Unset, UUID] = UNSET,
    search_string: Union[Unset, str] = UNSET,
    service_manager_uuid: Union[Unset, UUID] = UNSET,
    shared: Union[Unset, bool] = UNSET,
    state: Union[Unset, list[MarketplaceProviderOfferingsListUsersListStateItem]] = UNSET,
    type_: Union[Unset, list[str]] = UNSET,
    user: Union[Unset, UUID] = UNSET,
    user_slug: Union[Unset, str] = UNSET,
    user_url: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Response[list["UserRoleDetails"]]:
    """
    Args:
        uuid (UUID):
        accessible_via_calls (Union[Unset, bool]):
        allowed_customer_uuid (Union[Unset, UUID]):
        attributes (Union[Unset, str]):
        billable (Union[Unset, bool]):
        category_group_uuid (Union[Unset, UUID]):
        category_uuid (Union[Unset, UUID]):
        customer (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        description (Union[Unset, str]):
        field (Union[Unset, list[MarketplaceProviderOfferingsListUsersListFieldItem]]):
        full_name (Union[Unset, str]):
        keyword (Union[Unset, str]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        native_name (Union[Unset, str]):
        o (Union[Unset, list[MarketplaceProviderOfferingsListUsersListOItem]]):
        organization_group_uuid (Union[Unset, list[UUID]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        parent_uuid (Union[Unset, UUID]):
        project_uuid (Union[Unset, UUID]):
        role (Union[Unset, UUID]):
        scope_uuid (Union[Unset, UUID]):
        search_string (Union[Unset, str]):
        service_manager_uuid (Union[Unset, UUID]):
        shared (Union[Unset, bool]):
        state (Union[Unset, list[MarketplaceProviderOfferingsListUsersListStateItem]]):
        type_ (Union[Unset, list[str]]):
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
        accessible_via_calls=accessible_via_calls,
        allowed_customer_uuid=allowed_customer_uuid,
        attributes=attributes,
        billable=billable,
        category_group_uuid=category_group_uuid,
        category_uuid=category_uuid,
        customer=customer,
        customer_uuid=customer_uuid,
        description=description,
        field=field,
        full_name=full_name,
        keyword=keyword,
        name=name,
        name_exact=name_exact,
        native_name=native_name,
        o=o,
        organization_group_uuid=organization_group_uuid,
        page=page,
        page_size=page_size,
        parent_uuid=parent_uuid,
        project_uuid=project_uuid,
        role=role,
        scope_uuid=scope_uuid,
        search_string=search_string,
        service_manager_uuid=service_manager_uuid,
        shared=shared,
        state=state,
        type_=type_,
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
    accessible_via_calls: Union[Unset, bool] = UNSET,
    allowed_customer_uuid: Union[Unset, UUID] = UNSET,
    attributes: Union[Unset, str] = UNSET,
    billable: Union[Unset, bool] = UNSET,
    category_group_uuid: Union[Unset, UUID] = UNSET,
    category_uuid: Union[Unset, UUID] = UNSET,
    customer: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    description: Union[Unset, str] = UNSET,
    field: Union[Unset, list[MarketplaceProviderOfferingsListUsersListFieldItem]] = UNSET,
    full_name: Union[Unset, str] = UNSET,
    keyword: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    native_name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[MarketplaceProviderOfferingsListUsersListOItem]] = UNSET,
    organization_group_uuid: Union[Unset, list[UUID]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    parent_uuid: Union[Unset, UUID] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    role: Union[Unset, UUID] = UNSET,
    scope_uuid: Union[Unset, UUID] = UNSET,
    search_string: Union[Unset, str] = UNSET,
    service_manager_uuid: Union[Unset, UUID] = UNSET,
    shared: Union[Unset, bool] = UNSET,
    state: Union[Unset, list[MarketplaceProviderOfferingsListUsersListStateItem]] = UNSET,
    type_: Union[Unset, list[str]] = UNSET,
    user: Union[Unset, UUID] = UNSET,
    user_slug: Union[Unset, str] = UNSET,
    user_url: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Optional[list["UserRoleDetails"]]:
    """
    Args:
        uuid (UUID):
        accessible_via_calls (Union[Unset, bool]):
        allowed_customer_uuid (Union[Unset, UUID]):
        attributes (Union[Unset, str]):
        billable (Union[Unset, bool]):
        category_group_uuid (Union[Unset, UUID]):
        category_uuid (Union[Unset, UUID]):
        customer (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        description (Union[Unset, str]):
        field (Union[Unset, list[MarketplaceProviderOfferingsListUsersListFieldItem]]):
        full_name (Union[Unset, str]):
        keyword (Union[Unset, str]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        native_name (Union[Unset, str]):
        o (Union[Unset, list[MarketplaceProviderOfferingsListUsersListOItem]]):
        organization_group_uuid (Union[Unset, list[UUID]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        parent_uuid (Union[Unset, UUID]):
        project_uuid (Union[Unset, UUID]):
        role (Union[Unset, UUID]):
        scope_uuid (Union[Unset, UUID]):
        search_string (Union[Unset, str]):
        service_manager_uuid (Union[Unset, UUID]):
        shared (Union[Unset, bool]):
        state (Union[Unset, list[MarketplaceProviderOfferingsListUsersListStateItem]]):
        type_ (Union[Unset, list[str]]):
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
            accessible_via_calls=accessible_via_calls,
            allowed_customer_uuid=allowed_customer_uuid,
            attributes=attributes,
            billable=billable,
            category_group_uuid=category_group_uuid,
            category_uuid=category_uuid,
            customer=customer,
            customer_uuid=customer_uuid,
            description=description,
            field=field,
            full_name=full_name,
            keyword=keyword,
            name=name,
            name_exact=name_exact,
            native_name=native_name,
            o=o,
            organization_group_uuid=organization_group_uuid,
            page=page,
            page_size=page_size,
            parent_uuid=parent_uuid,
            project_uuid=project_uuid,
            role=role,
            scope_uuid=scope_uuid,
            search_string=search_string,
            service_manager_uuid=service_manager_uuid,
            shared=shared,
            state=state,
            type_=type_,
            user=user,
            user_slug=user_slug,
            user_url=user_url,
            username=username,
        )
    ).parsed
