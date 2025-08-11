import datetime
from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.marketplace_resources_count_o_item import MarketplaceResourcesCountOItem
from ...models.marketplace_resources_count_state_item import MarketplaceResourcesCountStateItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    backend_id: Union[Unset, str] = UNSET,
    category_uuid: Union[Unset, UUID] = UNSET,
    created: Union[Unset, datetime.datetime] = UNSET,
    customer: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    downscaled: Union[Unset, bool] = UNSET,
    has_terminate_date: Union[Unset, bool] = UNSET,
    lexis_links_supported: Union[Unset, bool] = UNSET,
    modified: Union[Unset, datetime.datetime] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    o: Union[Unset, list[MarketplaceResourcesCountOItem]] = UNSET,
    offering: Union[Unset, str] = UNSET,
    offering_billable: Union[Unset, UUID] = UNSET,
    offering_shared: Union[Unset, bool] = UNSET,
    offering_type: Union[Unset, str] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    parent_offering_uuid: Union[Unset, UUID] = UNSET,
    paused: Union[Unset, bool] = UNSET,
    project_name: Union[Unset, str] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    provider_uuid: Union[Unset, UUID] = UNSET,
    query: Union[Unset, str] = UNSET,
    restrict_member_access: Union[Unset, bool] = UNSET,
    runtime_state: Union[Unset, str] = UNSET,
    service_manager_uuid: Union[Unset, UUID] = UNSET,
    state: Union[Unset, list[MarketplaceResourcesCountStateItem]] = UNSET,
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

    params["has_terminate_date"] = has_terminate_date

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

    params["offering_shared"] = offering_shared

    params["offering_type"] = offering_type

    json_offering_uuid: Union[Unset, str] = UNSET
    if not isinstance(offering_uuid, Unset):
        json_offering_uuid = str(offering_uuid)
    params["offering_uuid"] = json_offering_uuid

    params["page"] = page

    params["page_size"] = page_size

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
        "method": "head",
        "url": "/api/marketplace-resources/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> int:
    if response.status_code == HTTPStatus.OK:
        try:
            return int(response.headers["x-result-count"])
        except KeyError:
            raise errors.UnexpectedStatus(
                response.status_code, b"Expected 'X-Result-Count' header for HEAD request, but it was not found."
            )
        except ValueError:
            count_val = response.headers.get("x-result-count")
            msg = f"Expected 'X-Result-Count' header to be an integer, but got '{count_val}'."
            raise errors.UnexpectedStatus(response.status_code, msg.encode())
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[int]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    backend_id: Union[Unset, str] = UNSET,
    category_uuid: Union[Unset, UUID] = UNSET,
    created: Union[Unset, datetime.datetime] = UNSET,
    customer: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    downscaled: Union[Unset, bool] = UNSET,
    has_terminate_date: Union[Unset, bool] = UNSET,
    lexis_links_supported: Union[Unset, bool] = UNSET,
    modified: Union[Unset, datetime.datetime] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    o: Union[Unset, list[MarketplaceResourcesCountOItem]] = UNSET,
    offering: Union[Unset, str] = UNSET,
    offering_billable: Union[Unset, UUID] = UNSET,
    offering_shared: Union[Unset, bool] = UNSET,
    offering_type: Union[Unset, str] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    parent_offering_uuid: Union[Unset, UUID] = UNSET,
    paused: Union[Unset, bool] = UNSET,
    project_name: Union[Unset, str] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    provider_uuid: Union[Unset, UUID] = UNSET,
    query: Union[Unset, str] = UNSET,
    restrict_member_access: Union[Unset, bool] = UNSET,
    runtime_state: Union[Unset, str] = UNSET,
    service_manager_uuid: Union[Unset, UUID] = UNSET,
    state: Union[Unset, list[MarketplaceResourcesCountStateItem]] = UNSET,
    visible_to_username: Union[Unset, str] = UNSET,
) -> Response[int]:
    """Get number of items in the collection matching the request parameters.

    Args:
        backend_id (Union[Unset, str]):
        category_uuid (Union[Unset, UUID]):
        created (Union[Unset, datetime.datetime]):
        customer (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        downscaled (Union[Unset, bool]):
        has_terminate_date (Union[Unset, bool]):
        lexis_links_supported (Union[Unset, bool]):
        modified (Union[Unset, datetime.datetime]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        o (Union[Unset, list[MarketplaceResourcesCountOItem]]):
        offering (Union[Unset, str]):
        offering_billable (Union[Unset, UUID]):
        offering_shared (Union[Unset, bool]):
        offering_type (Union[Unset, str]):
        offering_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        parent_offering_uuid (Union[Unset, UUID]):
        paused (Union[Unset, bool]):
        project_name (Union[Unset, str]):
        project_uuid (Union[Unset, UUID]):
        provider_uuid (Union[Unset, UUID]):
        query (Union[Unset, str]):
        restrict_member_access (Union[Unset, bool]):
        runtime_state (Union[Unset, str]):
        service_manager_uuid (Union[Unset, UUID]):
        state (Union[Unset, list[MarketplaceResourcesCountStateItem]]):
        visible_to_username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[int]
    """

    kwargs = _get_kwargs(
        backend_id=backend_id,
        category_uuid=category_uuid,
        created=created,
        customer=customer,
        customer_uuid=customer_uuid,
        downscaled=downscaled,
        has_terminate_date=has_terminate_date,
        lexis_links_supported=lexis_links_supported,
        modified=modified,
        name=name,
        name_exact=name_exact,
        o=o,
        offering=offering,
        offering_billable=offering_billable,
        offering_shared=offering_shared,
        offering_type=offering_type,
        offering_uuid=offering_uuid,
        page=page,
        page_size=page_size,
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
    *,
    client: AuthenticatedClient,
    backend_id: Union[Unset, str] = UNSET,
    category_uuid: Union[Unset, UUID] = UNSET,
    created: Union[Unset, datetime.datetime] = UNSET,
    customer: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    downscaled: Union[Unset, bool] = UNSET,
    has_terminate_date: Union[Unset, bool] = UNSET,
    lexis_links_supported: Union[Unset, bool] = UNSET,
    modified: Union[Unset, datetime.datetime] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    o: Union[Unset, list[MarketplaceResourcesCountOItem]] = UNSET,
    offering: Union[Unset, str] = UNSET,
    offering_billable: Union[Unset, UUID] = UNSET,
    offering_shared: Union[Unset, bool] = UNSET,
    offering_type: Union[Unset, str] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    parent_offering_uuid: Union[Unset, UUID] = UNSET,
    paused: Union[Unset, bool] = UNSET,
    project_name: Union[Unset, str] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    provider_uuid: Union[Unset, UUID] = UNSET,
    query: Union[Unset, str] = UNSET,
    restrict_member_access: Union[Unset, bool] = UNSET,
    runtime_state: Union[Unset, str] = UNSET,
    service_manager_uuid: Union[Unset, UUID] = UNSET,
    state: Union[Unset, list[MarketplaceResourcesCountStateItem]] = UNSET,
    visible_to_username: Union[Unset, str] = UNSET,
) -> int:
    """Get number of items in the collection matching the request parameters.

    Args:
        backend_id (Union[Unset, str]):
        category_uuid (Union[Unset, UUID]):
        created (Union[Unset, datetime.datetime]):
        customer (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        downscaled (Union[Unset, bool]):
        has_terminate_date (Union[Unset, bool]):
        lexis_links_supported (Union[Unset, bool]):
        modified (Union[Unset, datetime.datetime]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        o (Union[Unset, list[MarketplaceResourcesCountOItem]]):
        offering (Union[Unset, str]):
        offering_billable (Union[Unset, UUID]):
        offering_shared (Union[Unset, bool]):
        offering_type (Union[Unset, str]):
        offering_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        parent_offering_uuid (Union[Unset, UUID]):
        paused (Union[Unset, bool]):
        project_name (Union[Unset, str]):
        project_uuid (Union[Unset, UUID]):
        provider_uuid (Union[Unset, UUID]):
        query (Union[Unset, str]):
        restrict_member_access (Union[Unset, bool]):
        runtime_state (Union[Unset, str]):
        service_manager_uuid (Union[Unset, UUID]):
        state (Union[Unset, list[MarketplaceResourcesCountStateItem]]):
        visible_to_username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        int
    """

    return sync_detailed(
        client=client,
        backend_id=backend_id,
        category_uuid=category_uuid,
        created=created,
        customer=customer,
        customer_uuid=customer_uuid,
        downscaled=downscaled,
        has_terminate_date=has_terminate_date,
        lexis_links_supported=lexis_links_supported,
        modified=modified,
        name=name,
        name_exact=name_exact,
        o=o,
        offering=offering,
        offering_billable=offering_billable,
        offering_shared=offering_shared,
        offering_type=offering_type,
        offering_uuid=offering_uuid,
        page=page,
        page_size=page_size,
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
    *,
    client: AuthenticatedClient,
    backend_id: Union[Unset, str] = UNSET,
    category_uuid: Union[Unset, UUID] = UNSET,
    created: Union[Unset, datetime.datetime] = UNSET,
    customer: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    downscaled: Union[Unset, bool] = UNSET,
    has_terminate_date: Union[Unset, bool] = UNSET,
    lexis_links_supported: Union[Unset, bool] = UNSET,
    modified: Union[Unset, datetime.datetime] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    o: Union[Unset, list[MarketplaceResourcesCountOItem]] = UNSET,
    offering: Union[Unset, str] = UNSET,
    offering_billable: Union[Unset, UUID] = UNSET,
    offering_shared: Union[Unset, bool] = UNSET,
    offering_type: Union[Unset, str] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    parent_offering_uuid: Union[Unset, UUID] = UNSET,
    paused: Union[Unset, bool] = UNSET,
    project_name: Union[Unset, str] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    provider_uuid: Union[Unset, UUID] = UNSET,
    query: Union[Unset, str] = UNSET,
    restrict_member_access: Union[Unset, bool] = UNSET,
    runtime_state: Union[Unset, str] = UNSET,
    service_manager_uuid: Union[Unset, UUID] = UNSET,
    state: Union[Unset, list[MarketplaceResourcesCountStateItem]] = UNSET,
    visible_to_username: Union[Unset, str] = UNSET,
) -> Response[int]:
    """Get number of items in the collection matching the request parameters.

    Args:
        backend_id (Union[Unset, str]):
        category_uuid (Union[Unset, UUID]):
        created (Union[Unset, datetime.datetime]):
        customer (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        downscaled (Union[Unset, bool]):
        has_terminate_date (Union[Unset, bool]):
        lexis_links_supported (Union[Unset, bool]):
        modified (Union[Unset, datetime.datetime]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        o (Union[Unset, list[MarketplaceResourcesCountOItem]]):
        offering (Union[Unset, str]):
        offering_billable (Union[Unset, UUID]):
        offering_shared (Union[Unset, bool]):
        offering_type (Union[Unset, str]):
        offering_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        parent_offering_uuid (Union[Unset, UUID]):
        paused (Union[Unset, bool]):
        project_name (Union[Unset, str]):
        project_uuid (Union[Unset, UUID]):
        provider_uuid (Union[Unset, UUID]):
        query (Union[Unset, str]):
        restrict_member_access (Union[Unset, bool]):
        runtime_state (Union[Unset, str]):
        service_manager_uuid (Union[Unset, UUID]):
        state (Union[Unset, list[MarketplaceResourcesCountStateItem]]):
        visible_to_username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[int]
    """

    kwargs = _get_kwargs(
        backend_id=backend_id,
        category_uuid=category_uuid,
        created=created,
        customer=customer,
        customer_uuid=customer_uuid,
        downscaled=downscaled,
        has_terminate_date=has_terminate_date,
        lexis_links_supported=lexis_links_supported,
        modified=modified,
        name=name,
        name_exact=name_exact,
        o=o,
        offering=offering,
        offering_billable=offering_billable,
        offering_shared=offering_shared,
        offering_type=offering_type,
        offering_uuid=offering_uuid,
        page=page,
        page_size=page_size,
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
    *,
    client: AuthenticatedClient,
    backend_id: Union[Unset, str] = UNSET,
    category_uuid: Union[Unset, UUID] = UNSET,
    created: Union[Unset, datetime.datetime] = UNSET,
    customer: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    downscaled: Union[Unset, bool] = UNSET,
    has_terminate_date: Union[Unset, bool] = UNSET,
    lexis_links_supported: Union[Unset, bool] = UNSET,
    modified: Union[Unset, datetime.datetime] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    o: Union[Unset, list[MarketplaceResourcesCountOItem]] = UNSET,
    offering: Union[Unset, str] = UNSET,
    offering_billable: Union[Unset, UUID] = UNSET,
    offering_shared: Union[Unset, bool] = UNSET,
    offering_type: Union[Unset, str] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    parent_offering_uuid: Union[Unset, UUID] = UNSET,
    paused: Union[Unset, bool] = UNSET,
    project_name: Union[Unset, str] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    provider_uuid: Union[Unset, UUID] = UNSET,
    query: Union[Unset, str] = UNSET,
    restrict_member_access: Union[Unset, bool] = UNSET,
    runtime_state: Union[Unset, str] = UNSET,
    service_manager_uuid: Union[Unset, UUID] = UNSET,
    state: Union[Unset, list[MarketplaceResourcesCountStateItem]] = UNSET,
    visible_to_username: Union[Unset, str] = UNSET,
) -> int:
    """Get number of items in the collection matching the request parameters.

    Args:
        backend_id (Union[Unset, str]):
        category_uuid (Union[Unset, UUID]):
        created (Union[Unset, datetime.datetime]):
        customer (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        downscaled (Union[Unset, bool]):
        has_terminate_date (Union[Unset, bool]):
        lexis_links_supported (Union[Unset, bool]):
        modified (Union[Unset, datetime.datetime]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        o (Union[Unset, list[MarketplaceResourcesCountOItem]]):
        offering (Union[Unset, str]):
        offering_billable (Union[Unset, UUID]):
        offering_shared (Union[Unset, bool]):
        offering_type (Union[Unset, str]):
        offering_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        parent_offering_uuid (Union[Unset, UUID]):
        paused (Union[Unset, bool]):
        project_name (Union[Unset, str]):
        project_uuid (Union[Unset, UUID]):
        provider_uuid (Union[Unset, UUID]):
        query (Union[Unset, str]):
        restrict_member_access (Union[Unset, bool]):
        runtime_state (Union[Unset, str]):
        service_manager_uuid (Union[Unset, UUID]):
        state (Union[Unset, list[MarketplaceResourcesCountStateItem]]):
        visible_to_username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        int
    """

    return (
        await asyncio_detailed(
            client=client,
            backend_id=backend_id,
            category_uuid=category_uuid,
            created=created,
            customer=customer,
            customer_uuid=customer_uuid,
            downscaled=downscaled,
            has_terminate_date=has_terminate_date,
            lexis_links_supported=lexis_links_supported,
            modified=modified,
            name=name,
            name_exact=name_exact,
            o=o,
            offering=offering,
            offering_billable=offering_billable,
            offering_shared=offering_shared,
            offering_type=offering_type,
            offering_uuid=offering_uuid,
            page=page,
            page_size=page_size,
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
