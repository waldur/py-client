import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.marketplace_provider_resources_plan_periods_list_o_item import (
    MarketplaceProviderResourcesPlanPeriodsListOItem,
)
from ...models.marketplace_provider_resources_plan_periods_list_state_item import (
    MarketplaceProviderResourcesPlanPeriodsListStateItem,
)
from ...models.resource_plan_period import ResourcePlanPeriod
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    backend_id: Union[Unset, str] = UNSET,
    category_uuid: Union[Unset, UUID] = UNSET,
    created: Union[Unset, datetime.date] = UNSET,
    customer: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    downscaled: Union[Unset, bool] = UNSET,
    lexis_links_supported: Union[Unset, bool] = UNSET,
    modified: Union[Unset, datetime.date] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    o: Union[Unset, list[MarketplaceProviderResourcesPlanPeriodsListOItem]] = UNSET,
    offering: Union[Unset, str] = UNSET,
    offering_billable: Union[Unset, UUID] = UNSET,
    offering_type: Union[Unset, str] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    parent_offering_uuid: Union[Unset, UUID] = UNSET,
    paused: Union[Unset, bool] = UNSET,
    project_name: Union[Unset, str] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    provider_uuid: Union[Unset, UUID] = UNSET,
    query: Union[Unset, str] = UNSET,
    restrict_member_access: Union[Unset, bool] = UNSET,
    runtime_state: Union[Unset, str] = UNSET,
    service_manager_uuid: Union[Unset, UUID] = UNSET,
    state: Union[Unset, list[MarketplaceProviderResourcesPlanPeriodsListStateItem]] = UNSET,
    visible_to_username: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["backend_id"] = backend_id

    json_category_uuid: Union[Unset, str] = UNSET
    if not isinstance(category_uuid, Unset):
        json_category_uuid = str(category_uuid)
    params["category_uuid"] = json_category_uuid

    json_created: Union[Unset, str] = UNSET
    if not isinstance(created, Unset):
        json_created = created.isoformat()
    params["created"] = json_created

    params["customer"] = customer

    json_customer_uuid: Union[Unset, str] = UNSET
    if not isinstance(customer_uuid, Unset):
        json_customer_uuid = str(customer_uuid)
    params["customer_uuid"] = json_customer_uuid

    params["downscaled"] = downscaled

    params["lexis_links_supported"] = lexis_links_supported

    json_modified: Union[Unset, str] = UNSET
    if not isinstance(modified, Unset):
        json_modified = modified.isoformat()
    params["modified"] = json_modified

    params["name"] = name

    params["name_exact"] = name_exact

    json_o: Union[Unset, list[str]] = UNSET
    if not isinstance(o, Unset):
        json_o = []
        for o_item_data in o:
            o_item = o_item_data.value
            json_o.append(o_item)

    params["o"] = json_o

    params["offering"] = offering

    json_offering_billable: Union[Unset, str] = UNSET
    if not isinstance(offering_billable, Unset):
        json_offering_billable = str(offering_billable)
    params["offering_billable"] = json_offering_billable

    params["offering_type"] = offering_type

    json_offering_uuid: Union[Unset, str] = UNSET
    if not isinstance(offering_uuid, Unset):
        json_offering_uuid = str(offering_uuid)
    params["offering_uuid"] = json_offering_uuid

    json_parent_offering_uuid: Union[Unset, str] = UNSET
    if not isinstance(parent_offering_uuid, Unset):
        json_parent_offering_uuid = str(parent_offering_uuid)
    params["parent_offering_uuid"] = json_parent_offering_uuid

    params["paused"] = paused

    params["project_name"] = project_name

    json_project_uuid: Union[Unset, str] = UNSET
    if not isinstance(project_uuid, Unset):
        json_project_uuid = str(project_uuid)
    params["project_uuid"] = json_project_uuid

    json_provider_uuid: Union[Unset, str] = UNSET
    if not isinstance(provider_uuid, Unset):
        json_provider_uuid = str(provider_uuid)
    params["provider_uuid"] = json_provider_uuid

    params["query"] = query

    params["restrict_member_access"] = restrict_member_access

    params["runtime_state"] = runtime_state

    json_service_manager_uuid: Union[Unset, str] = UNSET
    if not isinstance(service_manager_uuid, Unset):
        json_service_manager_uuid = str(service_manager_uuid)
    params["service_manager_uuid"] = json_service_manager_uuid

    json_state: Union[Unset, list[str]] = UNSET
    if not isinstance(state, Unset):
        json_state = []
        for state_item_data in state:
            state_item = state_item_data.value
            json_state.append(state_item)

    params["state"] = json_state

    params["visible_to_username"] = visible_to_username

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/marketplace-provider-resources/{uuid}/plan_periods/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["ResourcePlanPeriod"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ResourcePlanPeriod.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["ResourcePlanPeriod"]]:
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
    category_uuid: Union[Unset, UUID] = UNSET,
    created: Union[Unset, datetime.date] = UNSET,
    customer: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    downscaled: Union[Unset, bool] = UNSET,
    lexis_links_supported: Union[Unset, bool] = UNSET,
    modified: Union[Unset, datetime.date] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    o: Union[Unset, list[MarketplaceProviderResourcesPlanPeriodsListOItem]] = UNSET,
    offering: Union[Unset, str] = UNSET,
    offering_billable: Union[Unset, UUID] = UNSET,
    offering_type: Union[Unset, str] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    parent_offering_uuid: Union[Unset, UUID] = UNSET,
    paused: Union[Unset, bool] = UNSET,
    project_name: Union[Unset, str] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    provider_uuid: Union[Unset, UUID] = UNSET,
    query: Union[Unset, str] = UNSET,
    restrict_member_access: Union[Unset, bool] = UNSET,
    runtime_state: Union[Unset, str] = UNSET,
    service_manager_uuid: Union[Unset, UUID] = UNSET,
    state: Union[Unset, list[MarketplaceProviderResourcesPlanPeriodsListStateItem]] = UNSET,
    visible_to_username: Union[Unset, str] = UNSET,
) -> Response[list["ResourcePlanPeriod"]]:
    """
    Args:
        uuid (UUID):
        backend_id (Union[Unset, str]):
        category_uuid (Union[Unset, UUID]):
        created (Union[Unset, datetime.date]):
        customer (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        downscaled (Union[Unset, bool]):
        lexis_links_supported (Union[Unset, bool]):
        modified (Union[Unset, datetime.date]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        o (Union[Unset, list[MarketplaceProviderResourcesPlanPeriodsListOItem]]):
        offering (Union[Unset, str]):
        offering_billable (Union[Unset, UUID]):
        offering_type (Union[Unset, str]):
        offering_uuid (Union[Unset, UUID]):
        parent_offering_uuid (Union[Unset, UUID]):
        paused (Union[Unset, bool]):
        project_name (Union[Unset, str]):
        project_uuid (Union[Unset, UUID]):
        provider_uuid (Union[Unset, UUID]):
        query (Union[Unset, str]):
        restrict_member_access (Union[Unset, bool]):
        runtime_state (Union[Unset, str]):
        service_manager_uuid (Union[Unset, UUID]):
        state (Union[Unset, list[MarketplaceProviderResourcesPlanPeriodsListStateItem]]):
        visible_to_username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['ResourcePlanPeriod']]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        backend_id=backend_id,
        category_uuid=category_uuid,
        created=created,
        customer=customer,
        customer_uuid=customer_uuid,
        downscaled=downscaled,
        lexis_links_supported=lexis_links_supported,
        modified=modified,
        name=name,
        name_exact=name_exact,
        o=o,
        offering=offering,
        offering_billable=offering_billable,
        offering_type=offering_type,
        offering_uuid=offering_uuid,
        parent_offering_uuid=parent_offering_uuid,
        paused=paused,
        project_name=project_name,
        project_uuid=project_uuid,
        provider_uuid=provider_uuid,
        query=query,
        restrict_member_access=restrict_member_access,
        runtime_state=runtime_state,
        service_manager_uuid=service_manager_uuid,
        state=state,
        visible_to_username=visible_to_username,
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
    category_uuid: Union[Unset, UUID] = UNSET,
    created: Union[Unset, datetime.date] = UNSET,
    customer: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    downscaled: Union[Unset, bool] = UNSET,
    lexis_links_supported: Union[Unset, bool] = UNSET,
    modified: Union[Unset, datetime.date] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    o: Union[Unset, list[MarketplaceProviderResourcesPlanPeriodsListOItem]] = UNSET,
    offering: Union[Unset, str] = UNSET,
    offering_billable: Union[Unset, UUID] = UNSET,
    offering_type: Union[Unset, str] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    parent_offering_uuid: Union[Unset, UUID] = UNSET,
    paused: Union[Unset, bool] = UNSET,
    project_name: Union[Unset, str] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    provider_uuid: Union[Unset, UUID] = UNSET,
    query: Union[Unset, str] = UNSET,
    restrict_member_access: Union[Unset, bool] = UNSET,
    runtime_state: Union[Unset, str] = UNSET,
    service_manager_uuid: Union[Unset, UUID] = UNSET,
    state: Union[Unset, list[MarketplaceProviderResourcesPlanPeriodsListStateItem]] = UNSET,
    visible_to_username: Union[Unset, str] = UNSET,
) -> Optional[list["ResourcePlanPeriod"]]:
    """
    Args:
        uuid (UUID):
        backend_id (Union[Unset, str]):
        category_uuid (Union[Unset, UUID]):
        created (Union[Unset, datetime.date]):
        customer (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        downscaled (Union[Unset, bool]):
        lexis_links_supported (Union[Unset, bool]):
        modified (Union[Unset, datetime.date]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        o (Union[Unset, list[MarketplaceProviderResourcesPlanPeriodsListOItem]]):
        offering (Union[Unset, str]):
        offering_billable (Union[Unset, UUID]):
        offering_type (Union[Unset, str]):
        offering_uuid (Union[Unset, UUID]):
        parent_offering_uuid (Union[Unset, UUID]):
        paused (Union[Unset, bool]):
        project_name (Union[Unset, str]):
        project_uuid (Union[Unset, UUID]):
        provider_uuid (Union[Unset, UUID]):
        query (Union[Unset, str]):
        restrict_member_access (Union[Unset, bool]):
        runtime_state (Union[Unset, str]):
        service_manager_uuid (Union[Unset, UUID]):
        state (Union[Unset, list[MarketplaceProviderResourcesPlanPeriodsListStateItem]]):
        visible_to_username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['ResourcePlanPeriod']
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        backend_id=backend_id,
        category_uuid=category_uuid,
        created=created,
        customer=customer,
        customer_uuid=customer_uuid,
        downscaled=downscaled,
        lexis_links_supported=lexis_links_supported,
        modified=modified,
        name=name,
        name_exact=name_exact,
        o=o,
        offering=offering,
        offering_billable=offering_billable,
        offering_type=offering_type,
        offering_uuid=offering_uuid,
        parent_offering_uuid=parent_offering_uuid,
        paused=paused,
        project_name=project_name,
        project_uuid=project_uuid,
        provider_uuid=provider_uuid,
        query=query,
        restrict_member_access=restrict_member_access,
        runtime_state=runtime_state,
        service_manager_uuid=service_manager_uuid,
        state=state,
        visible_to_username=visible_to_username,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    backend_id: Union[Unset, str] = UNSET,
    category_uuid: Union[Unset, UUID] = UNSET,
    created: Union[Unset, datetime.date] = UNSET,
    customer: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    downscaled: Union[Unset, bool] = UNSET,
    lexis_links_supported: Union[Unset, bool] = UNSET,
    modified: Union[Unset, datetime.date] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    o: Union[Unset, list[MarketplaceProviderResourcesPlanPeriodsListOItem]] = UNSET,
    offering: Union[Unset, str] = UNSET,
    offering_billable: Union[Unset, UUID] = UNSET,
    offering_type: Union[Unset, str] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    parent_offering_uuid: Union[Unset, UUID] = UNSET,
    paused: Union[Unset, bool] = UNSET,
    project_name: Union[Unset, str] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    provider_uuid: Union[Unset, UUID] = UNSET,
    query: Union[Unset, str] = UNSET,
    restrict_member_access: Union[Unset, bool] = UNSET,
    runtime_state: Union[Unset, str] = UNSET,
    service_manager_uuid: Union[Unset, UUID] = UNSET,
    state: Union[Unset, list[MarketplaceProviderResourcesPlanPeriodsListStateItem]] = UNSET,
    visible_to_username: Union[Unset, str] = UNSET,
) -> Response[list["ResourcePlanPeriod"]]:
    """
    Args:
        uuid (UUID):
        backend_id (Union[Unset, str]):
        category_uuid (Union[Unset, UUID]):
        created (Union[Unset, datetime.date]):
        customer (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        downscaled (Union[Unset, bool]):
        lexis_links_supported (Union[Unset, bool]):
        modified (Union[Unset, datetime.date]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        o (Union[Unset, list[MarketplaceProviderResourcesPlanPeriodsListOItem]]):
        offering (Union[Unset, str]):
        offering_billable (Union[Unset, UUID]):
        offering_type (Union[Unset, str]):
        offering_uuid (Union[Unset, UUID]):
        parent_offering_uuid (Union[Unset, UUID]):
        paused (Union[Unset, bool]):
        project_name (Union[Unset, str]):
        project_uuid (Union[Unset, UUID]):
        provider_uuid (Union[Unset, UUID]):
        query (Union[Unset, str]):
        restrict_member_access (Union[Unset, bool]):
        runtime_state (Union[Unset, str]):
        service_manager_uuid (Union[Unset, UUID]):
        state (Union[Unset, list[MarketplaceProviderResourcesPlanPeriodsListStateItem]]):
        visible_to_username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['ResourcePlanPeriod']]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        backend_id=backend_id,
        category_uuid=category_uuid,
        created=created,
        customer=customer,
        customer_uuid=customer_uuid,
        downscaled=downscaled,
        lexis_links_supported=lexis_links_supported,
        modified=modified,
        name=name,
        name_exact=name_exact,
        o=o,
        offering=offering,
        offering_billable=offering_billable,
        offering_type=offering_type,
        offering_uuid=offering_uuid,
        parent_offering_uuid=parent_offering_uuid,
        paused=paused,
        project_name=project_name,
        project_uuid=project_uuid,
        provider_uuid=provider_uuid,
        query=query,
        restrict_member_access=restrict_member_access,
        runtime_state=runtime_state,
        service_manager_uuid=service_manager_uuid,
        state=state,
        visible_to_username=visible_to_username,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    backend_id: Union[Unset, str] = UNSET,
    category_uuid: Union[Unset, UUID] = UNSET,
    created: Union[Unset, datetime.date] = UNSET,
    customer: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    downscaled: Union[Unset, bool] = UNSET,
    lexis_links_supported: Union[Unset, bool] = UNSET,
    modified: Union[Unset, datetime.date] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    o: Union[Unset, list[MarketplaceProviderResourcesPlanPeriodsListOItem]] = UNSET,
    offering: Union[Unset, str] = UNSET,
    offering_billable: Union[Unset, UUID] = UNSET,
    offering_type: Union[Unset, str] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    parent_offering_uuid: Union[Unset, UUID] = UNSET,
    paused: Union[Unset, bool] = UNSET,
    project_name: Union[Unset, str] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    provider_uuid: Union[Unset, UUID] = UNSET,
    query: Union[Unset, str] = UNSET,
    restrict_member_access: Union[Unset, bool] = UNSET,
    runtime_state: Union[Unset, str] = UNSET,
    service_manager_uuid: Union[Unset, UUID] = UNSET,
    state: Union[Unset, list[MarketplaceProviderResourcesPlanPeriodsListStateItem]] = UNSET,
    visible_to_username: Union[Unset, str] = UNSET,
) -> Optional[list["ResourcePlanPeriod"]]:
    """
    Args:
        uuid (UUID):
        backend_id (Union[Unset, str]):
        category_uuid (Union[Unset, UUID]):
        created (Union[Unset, datetime.date]):
        customer (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        downscaled (Union[Unset, bool]):
        lexis_links_supported (Union[Unset, bool]):
        modified (Union[Unset, datetime.date]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        o (Union[Unset, list[MarketplaceProviderResourcesPlanPeriodsListOItem]]):
        offering (Union[Unset, str]):
        offering_billable (Union[Unset, UUID]):
        offering_type (Union[Unset, str]):
        offering_uuid (Union[Unset, UUID]):
        parent_offering_uuid (Union[Unset, UUID]):
        paused (Union[Unset, bool]):
        project_name (Union[Unset, str]):
        project_uuid (Union[Unset, UUID]):
        provider_uuid (Union[Unset, UUID]):
        query (Union[Unset, str]):
        restrict_member_access (Union[Unset, bool]):
        runtime_state (Union[Unset, str]):
        service_manager_uuid (Union[Unset, UUID]):
        state (Union[Unset, list[MarketplaceProviderResourcesPlanPeriodsListStateItem]]):
        visible_to_username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['ResourcePlanPeriod']
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            backend_id=backend_id,
            category_uuid=category_uuid,
            created=created,
            customer=customer,
            customer_uuid=customer_uuid,
            downscaled=downscaled,
            lexis_links_supported=lexis_links_supported,
            modified=modified,
            name=name,
            name_exact=name_exact,
            o=o,
            offering=offering,
            offering_billable=offering_billable,
            offering_type=offering_type,
            offering_uuid=offering_uuid,
            parent_offering_uuid=parent_offering_uuid,
            paused=paused,
            project_name=project_name,
            project_uuid=project_uuid,
            provider_uuid=provider_uuid,
            query=query,
            restrict_member_access=restrict_member_access,
            runtime_state=runtime_state,
            service_manager_uuid=service_manager_uuid,
            state=state,
            visible_to_username=visible_to_username,
        )
    ).parsed
