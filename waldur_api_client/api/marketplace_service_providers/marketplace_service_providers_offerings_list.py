from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.marketplace_service_providers_offerings_list_o import MarketplaceServiceProvidersOfferingsListO
from ...models.marketplace_service_providers_offerings_list_state_item import (
    MarketplaceServiceProvidersOfferingsListStateItem,
)
from ...models.provider_offering import ProviderOffering
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
    customer_keyword: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    description: Union[Unset, str] = UNSET,
    keyword: Union[Unset, str] = UNSET,
    o: Union[Unset, MarketplaceServiceProvidersOfferingsListO] = UNSET,
    organization_group_uuid: Union[Unset, list[UUID]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    parent_uuid: Union[Unset, UUID] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    scope_uuid: Union[Unset, UUID] = UNSET,
    service_manager_uuid: Union[Unset, UUID] = UNSET,
    shared: Union[Unset, bool] = UNSET,
    state: Union[Unset, list[MarketplaceServiceProvidersOfferingsListStateItem]] = UNSET,
    type_: Union[Unset, list[str]] = UNSET,
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

    params["customer_keyword"] = customer_keyword

    json_customer_uuid: Union[Unset, str] = UNSET
    if not isinstance(customer_uuid, Unset):
        json_customer_uuid = str(customer_uuid)
    params["customer_uuid"] = json_customer_uuid

    params["description"] = description

    params["keyword"] = keyword

    json_o: Union[Unset, str] = UNSET
    if not isinstance(o, Unset):
        json_o = o.value

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

    json_scope_uuid: Union[Unset, str] = UNSET
    if not isinstance(scope_uuid, Unset):
        json_scope_uuid = str(scope_uuid)
    params["scope_uuid"] = json_scope_uuid

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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/marketplace-service-providers/{uuid}/offerings/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["ProviderOffering"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ProviderOffering.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["ProviderOffering"]]:
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
    customer_keyword: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    description: Union[Unset, str] = UNSET,
    keyword: Union[Unset, str] = UNSET,
    o: Union[Unset, MarketplaceServiceProvidersOfferingsListO] = UNSET,
    organization_group_uuid: Union[Unset, list[UUID]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    parent_uuid: Union[Unset, UUID] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    scope_uuid: Union[Unset, UUID] = UNSET,
    service_manager_uuid: Union[Unset, UUID] = UNSET,
    shared: Union[Unset, bool] = UNSET,
    state: Union[Unset, list[MarketplaceServiceProvidersOfferingsListStateItem]] = UNSET,
    type_: Union[Unset, list[str]] = UNSET,
) -> Response[list["ProviderOffering"]]:
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
        customer_keyword (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        description (Union[Unset, str]):
        keyword (Union[Unset, str]):
        o (Union[Unset, MarketplaceServiceProvidersOfferingsListO]):
        organization_group_uuid (Union[Unset, list[UUID]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        parent_uuid (Union[Unset, UUID]):
        project_uuid (Union[Unset, UUID]):
        scope_uuid (Union[Unset, UUID]):
        service_manager_uuid (Union[Unset, UUID]):
        shared (Union[Unset, bool]):
        state (Union[Unset, list[MarketplaceServiceProvidersOfferingsListStateItem]]):
        type_ (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['ProviderOffering']]
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
        customer_keyword=customer_keyword,
        customer_uuid=customer_uuid,
        description=description,
        keyword=keyword,
        o=o,
        organization_group_uuid=organization_group_uuid,
        page=page,
        page_size=page_size,
        parent_uuid=parent_uuid,
        project_uuid=project_uuid,
        scope_uuid=scope_uuid,
        service_manager_uuid=service_manager_uuid,
        shared=shared,
        state=state,
        type_=type_,
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
    customer_keyword: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    description: Union[Unset, str] = UNSET,
    keyword: Union[Unset, str] = UNSET,
    o: Union[Unset, MarketplaceServiceProvidersOfferingsListO] = UNSET,
    organization_group_uuid: Union[Unset, list[UUID]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    parent_uuid: Union[Unset, UUID] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    scope_uuid: Union[Unset, UUID] = UNSET,
    service_manager_uuid: Union[Unset, UUID] = UNSET,
    shared: Union[Unset, bool] = UNSET,
    state: Union[Unset, list[MarketplaceServiceProvidersOfferingsListStateItem]] = UNSET,
    type_: Union[Unset, list[str]] = UNSET,
) -> Optional[list["ProviderOffering"]]:
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
        customer_keyword (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        description (Union[Unset, str]):
        keyword (Union[Unset, str]):
        o (Union[Unset, MarketplaceServiceProvidersOfferingsListO]):
        organization_group_uuid (Union[Unset, list[UUID]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        parent_uuid (Union[Unset, UUID]):
        project_uuid (Union[Unset, UUID]):
        scope_uuid (Union[Unset, UUID]):
        service_manager_uuid (Union[Unset, UUID]):
        shared (Union[Unset, bool]):
        state (Union[Unset, list[MarketplaceServiceProvidersOfferingsListStateItem]]):
        type_ (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['ProviderOffering']
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
        customer_keyword=customer_keyword,
        customer_uuid=customer_uuid,
        description=description,
        keyword=keyword,
        o=o,
        organization_group_uuid=organization_group_uuid,
        page=page,
        page_size=page_size,
        parent_uuid=parent_uuid,
        project_uuid=project_uuid,
        scope_uuid=scope_uuid,
        service_manager_uuid=service_manager_uuid,
        shared=shared,
        state=state,
        type_=type_,
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
    customer_keyword: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    description: Union[Unset, str] = UNSET,
    keyword: Union[Unset, str] = UNSET,
    o: Union[Unset, MarketplaceServiceProvidersOfferingsListO] = UNSET,
    organization_group_uuid: Union[Unset, list[UUID]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    parent_uuid: Union[Unset, UUID] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    scope_uuid: Union[Unset, UUID] = UNSET,
    service_manager_uuid: Union[Unset, UUID] = UNSET,
    shared: Union[Unset, bool] = UNSET,
    state: Union[Unset, list[MarketplaceServiceProvidersOfferingsListStateItem]] = UNSET,
    type_: Union[Unset, list[str]] = UNSET,
) -> Response[list["ProviderOffering"]]:
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
        customer_keyword (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        description (Union[Unset, str]):
        keyword (Union[Unset, str]):
        o (Union[Unset, MarketplaceServiceProvidersOfferingsListO]):
        organization_group_uuid (Union[Unset, list[UUID]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        parent_uuid (Union[Unset, UUID]):
        project_uuid (Union[Unset, UUID]):
        scope_uuid (Union[Unset, UUID]):
        service_manager_uuid (Union[Unset, UUID]):
        shared (Union[Unset, bool]):
        state (Union[Unset, list[MarketplaceServiceProvidersOfferingsListStateItem]]):
        type_ (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['ProviderOffering']]
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
        customer_keyword=customer_keyword,
        customer_uuid=customer_uuid,
        description=description,
        keyword=keyword,
        o=o,
        organization_group_uuid=organization_group_uuid,
        page=page,
        page_size=page_size,
        parent_uuid=parent_uuid,
        project_uuid=project_uuid,
        scope_uuid=scope_uuid,
        service_manager_uuid=service_manager_uuid,
        shared=shared,
        state=state,
        type_=type_,
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
    customer_keyword: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    description: Union[Unset, str] = UNSET,
    keyword: Union[Unset, str] = UNSET,
    o: Union[Unset, MarketplaceServiceProvidersOfferingsListO] = UNSET,
    organization_group_uuid: Union[Unset, list[UUID]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    parent_uuid: Union[Unset, UUID] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    scope_uuid: Union[Unset, UUID] = UNSET,
    service_manager_uuid: Union[Unset, UUID] = UNSET,
    shared: Union[Unset, bool] = UNSET,
    state: Union[Unset, list[MarketplaceServiceProvidersOfferingsListStateItem]] = UNSET,
    type_: Union[Unset, list[str]] = UNSET,
) -> Optional[list["ProviderOffering"]]:
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
        customer_keyword (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        description (Union[Unset, str]):
        keyword (Union[Unset, str]):
        o (Union[Unset, MarketplaceServiceProvidersOfferingsListO]):
        organization_group_uuid (Union[Unset, list[UUID]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        parent_uuid (Union[Unset, UUID]):
        project_uuid (Union[Unset, UUID]):
        scope_uuid (Union[Unset, UUID]):
        service_manager_uuid (Union[Unset, UUID]):
        shared (Union[Unset, bool]):
        state (Union[Unset, list[MarketplaceServiceProvidersOfferingsListStateItem]]):
        type_ (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['ProviderOffering']
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
            customer_keyword=customer_keyword,
            customer_uuid=customer_uuid,
            description=description,
            keyword=keyword,
            o=o,
            organization_group_uuid=organization_group_uuid,
            page=page,
            page_size=page_size,
            parent_uuid=parent_uuid,
            project_uuid=project_uuid,
            scope_uuid=scope_uuid,
            service_manager_uuid=service_manager_uuid,
            shared=shared,
            state=state,
            type_=type_,
        )
    ).parsed
