import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.component_user_usage import ComponentUserUsage
from ...models.marketplace_component_user_usages_list_field_item import MarketplaceComponentUserUsagesListFieldItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    component_usage_billing_period: Union[Unset, datetime.date] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    date_after: Union[Unset, datetime.date] = UNSET,
    date_before: Union[Unset, datetime.date] = UNSET,
    field: Union[Unset, list[MarketplaceComponentUserUsagesListFieldItem]] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    resource: Union[Unset, str] = UNSET,
    resource_uuid: Union[Unset, UUID] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_component_usage_billing_period: Union[Unset, str] = UNSET
    if not isinstance(component_usage_billing_period, Unset):
        json_component_usage_billing_period = component_usage_billing_period.isoformat()
    params["component_usage__billing_period"] = json_component_usage_billing_period

    json_customer_uuid: Union[Unset, str] = UNSET
    if not isinstance(customer_uuid, Unset):
        json_customer_uuid = str(customer_uuid)
    params["customer_uuid"] = json_customer_uuid

    json_date_after: Union[Unset, str] = UNSET
    if not isinstance(date_after, Unset):
        json_date_after = date_after.isoformat()
    params["date_after"] = json_date_after

    json_date_before: Union[Unset, str] = UNSET
    if not isinstance(date_before, Unset):
        json_date_before = date_before.isoformat()
    params["date_before"] = json_date_before

    json_field: Union[Unset, list[str]] = UNSET
    if not isinstance(field, Unset):
        json_field = []
        for field_item_data in field:
            field_item = field_item_data.value
            json_field.append(field_item)

    params["field"] = json_field

    json_offering_uuid: Union[Unset, str] = UNSET
    if not isinstance(offering_uuid, Unset):
        json_offering_uuid = str(offering_uuid)
    params["offering_uuid"] = json_offering_uuid

    params["page"] = page

    params["page_size"] = page_size

    json_project_uuid: Union[Unset, str] = UNSET
    if not isinstance(project_uuid, Unset):
        json_project_uuid = str(project_uuid)
    params["project_uuid"] = json_project_uuid

    params["resource"] = resource

    json_resource_uuid: Union[Unset, str] = UNSET
    if not isinstance(resource_uuid, Unset):
        json_resource_uuid = str(resource_uuid)
    params["resource_uuid"] = json_resource_uuid

    params["type"] = type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/marketplace-component-user-usages/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["ComponentUserUsage"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_paginated_component_user_usage_list_item_data in _response_200:
            componentsschemas_paginated_component_user_usage_list_item = ComponentUserUsage.from_dict(
                componentsschemas_paginated_component_user_usage_list_item_data
            )

            response_200.append(componentsschemas_paginated_component_user_usage_list_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["ComponentUserUsage"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    component_usage_billing_period: Union[Unset, datetime.date] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    date_after: Union[Unset, datetime.date] = UNSET,
    date_before: Union[Unset, datetime.date] = UNSET,
    field: Union[Unset, list[MarketplaceComponentUserUsagesListFieldItem]] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    resource: Union[Unset, str] = UNSET,
    resource_uuid: Union[Unset, UUID] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> Response[list["ComponentUserUsage"]]:
    """
    Args:
        component_usage_billing_period (Union[Unset, datetime.date]):
        customer_uuid (Union[Unset, UUID]):
        date_after (Union[Unset, datetime.date]):
        date_before (Union[Unset, datetime.date]):
        field (Union[Unset, list[MarketplaceComponentUserUsagesListFieldItem]]):
        offering_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        project_uuid (Union[Unset, UUID]):
        resource (Union[Unset, str]):
        resource_uuid (Union[Unset, UUID]):
        type_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['ComponentUserUsage']]
    """

    kwargs = _get_kwargs(
        component_usage_billing_period=component_usage_billing_period,
        customer_uuid=customer_uuid,
        date_after=date_after,
        date_before=date_before,
        field=field,
        offering_uuid=offering_uuid,
        page=page,
        page_size=page_size,
        project_uuid=project_uuid,
        resource=resource,
        resource_uuid=resource_uuid,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    component_usage_billing_period: Union[Unset, datetime.date] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    date_after: Union[Unset, datetime.date] = UNSET,
    date_before: Union[Unset, datetime.date] = UNSET,
    field: Union[Unset, list[MarketplaceComponentUserUsagesListFieldItem]] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    resource: Union[Unset, str] = UNSET,
    resource_uuid: Union[Unset, UUID] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> Optional[list["ComponentUserUsage"]]:
    """
    Args:
        component_usage_billing_period (Union[Unset, datetime.date]):
        customer_uuid (Union[Unset, UUID]):
        date_after (Union[Unset, datetime.date]):
        date_before (Union[Unset, datetime.date]):
        field (Union[Unset, list[MarketplaceComponentUserUsagesListFieldItem]]):
        offering_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        project_uuid (Union[Unset, UUID]):
        resource (Union[Unset, str]):
        resource_uuid (Union[Unset, UUID]):
        type_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['ComponentUserUsage']
    """

    return sync_detailed(
        client=client,
        component_usage_billing_period=component_usage_billing_period,
        customer_uuid=customer_uuid,
        date_after=date_after,
        date_before=date_before,
        field=field,
        offering_uuid=offering_uuid,
        page=page,
        page_size=page_size,
        project_uuid=project_uuid,
        resource=resource,
        resource_uuid=resource_uuid,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    component_usage_billing_period: Union[Unset, datetime.date] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    date_after: Union[Unset, datetime.date] = UNSET,
    date_before: Union[Unset, datetime.date] = UNSET,
    field: Union[Unset, list[MarketplaceComponentUserUsagesListFieldItem]] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    resource: Union[Unset, str] = UNSET,
    resource_uuid: Union[Unset, UUID] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> Response[list["ComponentUserUsage"]]:
    """
    Args:
        component_usage_billing_period (Union[Unset, datetime.date]):
        customer_uuid (Union[Unset, UUID]):
        date_after (Union[Unset, datetime.date]):
        date_before (Union[Unset, datetime.date]):
        field (Union[Unset, list[MarketplaceComponentUserUsagesListFieldItem]]):
        offering_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        project_uuid (Union[Unset, UUID]):
        resource (Union[Unset, str]):
        resource_uuid (Union[Unset, UUID]):
        type_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['ComponentUserUsage']]
    """

    kwargs = _get_kwargs(
        component_usage_billing_period=component_usage_billing_period,
        customer_uuid=customer_uuid,
        date_after=date_after,
        date_before=date_before,
        field=field,
        offering_uuid=offering_uuid,
        page=page,
        page_size=page_size,
        project_uuid=project_uuid,
        resource=resource,
        resource_uuid=resource_uuid,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    component_usage_billing_period: Union[Unset, datetime.date] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    date_after: Union[Unset, datetime.date] = UNSET,
    date_before: Union[Unset, datetime.date] = UNSET,
    field: Union[Unset, list[MarketplaceComponentUserUsagesListFieldItem]] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    resource: Union[Unset, str] = UNSET,
    resource_uuid: Union[Unset, UUID] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> Optional[list["ComponentUserUsage"]]:
    """
    Args:
        component_usage_billing_period (Union[Unset, datetime.date]):
        customer_uuid (Union[Unset, UUID]):
        date_after (Union[Unset, datetime.date]):
        date_before (Union[Unset, datetime.date]):
        field (Union[Unset, list[MarketplaceComponentUserUsagesListFieldItem]]):
        offering_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        project_uuid (Union[Unset, UUID]):
        resource (Union[Unset, str]):
        resource_uuid (Union[Unset, UUID]):
        type_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['ComponentUserUsage']
    """

    return (
        await asyncio_detailed(
            client=client,
            component_usage_billing_period=component_usage_billing_period,
            customer_uuid=customer_uuid,
            date_after=date_after,
            date_before=date_before,
            field=field,
            offering_uuid=offering_uuid,
            page=page,
            page_size=page_size,
            project_uuid=project_uuid,
            resource=resource,
            resource_uuid=resource_uuid,
            type_=type_,
        )
    ).parsed
