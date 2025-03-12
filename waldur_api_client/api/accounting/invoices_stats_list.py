import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.invoice_stats_offering import InvoiceStatsOffering
from ...models.invoices_stats_list_o_item import InvoicesStatsListOItem
from ...models.invoices_stats_list_state_item import InvoicesStatsListStateItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    created: Union[Unset, datetime.date] = UNSET,
    customer: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    end_date: Union[Unset, datetime.date] = UNSET,
    max_sum: Union[Unset, float] = UNSET,
    min_sum: Union[Unset, float] = UNSET,
    month: Union[Unset, int] = UNSET,
    o: Union[Unset, list[InvoicesStatsListOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    provider_uuid: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.date] = UNSET,
    state: Union[Unset, list[InvoicesStatsListStateItem]] = UNSET,
    year: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_created: Union[Unset, str] = UNSET
    if not isinstance(created, Unset):
        json_created = created.isoformat()
    params["created"] = json_created

    params["customer"] = customer

    json_customer_uuid: Union[Unset, str] = UNSET
    if not isinstance(customer_uuid, Unset):
        json_customer_uuid = str(customer_uuid)
    params["customer_uuid"] = json_customer_uuid

    json_end_date: Union[Unset, str] = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat()
    params["end_date"] = json_end_date

    params["max_sum"] = max_sum

    params["min_sum"] = min_sum

    params["month"] = month

    json_o: Union[Unset, list[str]] = UNSET
    if not isinstance(o, Unset):
        json_o = []
        for o_item_data in o:
            o_item = o_item_data.value
            json_o.append(o_item)

    params["o"] = json_o

    params["page"] = page

    params["page_size"] = page_size

    params["provider_uuid"] = provider_uuid

    json_start_date: Union[Unset, str] = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["start_date"] = json_start_date

    json_state: Union[Unset, list[str]] = UNSET
    if not isinstance(state, Unset):
        json_state = []
        for state_item_data in state:
            state_item = state_item_data.value
            json_state.append(state_item)

    params["state"] = json_state

    params["year"] = year

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/invoices/{uuid}/stats/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["InvoiceStatsOffering"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_paginated_invoice_stats_offering_list_item_data in _response_200:
            componentsschemas_paginated_invoice_stats_offering_list_item = InvoiceStatsOffering.from_dict(
                componentsschemas_paginated_invoice_stats_offering_list_item_data
            )

            response_200.append(componentsschemas_paginated_invoice_stats_offering_list_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["InvoiceStatsOffering"]]:
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
    created: Union[Unset, datetime.date] = UNSET,
    customer: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    end_date: Union[Unset, datetime.date] = UNSET,
    max_sum: Union[Unset, float] = UNSET,
    min_sum: Union[Unset, float] = UNSET,
    month: Union[Unset, int] = UNSET,
    o: Union[Unset, list[InvoicesStatsListOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    provider_uuid: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.date] = UNSET,
    state: Union[Unset, list[InvoicesStatsListStateItem]] = UNSET,
    year: Union[Unset, int] = UNSET,
) -> Response[list["InvoiceStatsOffering"]]:
    """
    Args:
        uuid (UUID):
        created (Union[Unset, datetime.date]):
        customer (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        end_date (Union[Unset, datetime.date]):
        max_sum (Union[Unset, float]):
        min_sum (Union[Unset, float]):
        month (Union[Unset, int]):
        o (Union[Unset, list[InvoicesStatsListOItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        provider_uuid (Union[Unset, str]):
        start_date (Union[Unset, datetime.date]):
        state (Union[Unset, list[InvoicesStatsListStateItem]]):
        year (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['InvoiceStatsOffering']]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        created=created,
        customer=customer,
        customer_uuid=customer_uuid,
        end_date=end_date,
        max_sum=max_sum,
        min_sum=min_sum,
        month=month,
        o=o,
        page=page,
        page_size=page_size,
        provider_uuid=provider_uuid,
        start_date=start_date,
        state=state,
        year=year,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    created: Union[Unset, datetime.date] = UNSET,
    customer: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    end_date: Union[Unset, datetime.date] = UNSET,
    max_sum: Union[Unset, float] = UNSET,
    min_sum: Union[Unset, float] = UNSET,
    month: Union[Unset, int] = UNSET,
    o: Union[Unset, list[InvoicesStatsListOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    provider_uuid: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.date] = UNSET,
    state: Union[Unset, list[InvoicesStatsListStateItem]] = UNSET,
    year: Union[Unset, int] = UNSET,
) -> Optional[list["InvoiceStatsOffering"]]:
    """
    Args:
        uuid (UUID):
        created (Union[Unset, datetime.date]):
        customer (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        end_date (Union[Unset, datetime.date]):
        max_sum (Union[Unset, float]):
        min_sum (Union[Unset, float]):
        month (Union[Unset, int]):
        o (Union[Unset, list[InvoicesStatsListOItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        provider_uuid (Union[Unset, str]):
        start_date (Union[Unset, datetime.date]):
        state (Union[Unset, list[InvoicesStatsListStateItem]]):
        year (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['InvoiceStatsOffering']
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        created=created,
        customer=customer,
        customer_uuid=customer_uuid,
        end_date=end_date,
        max_sum=max_sum,
        min_sum=min_sum,
        month=month,
        o=o,
        page=page,
        page_size=page_size,
        provider_uuid=provider_uuid,
        start_date=start_date,
        state=state,
        year=year,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    created: Union[Unset, datetime.date] = UNSET,
    customer: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    end_date: Union[Unset, datetime.date] = UNSET,
    max_sum: Union[Unset, float] = UNSET,
    min_sum: Union[Unset, float] = UNSET,
    month: Union[Unset, int] = UNSET,
    o: Union[Unset, list[InvoicesStatsListOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    provider_uuid: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.date] = UNSET,
    state: Union[Unset, list[InvoicesStatsListStateItem]] = UNSET,
    year: Union[Unset, int] = UNSET,
) -> Response[list["InvoiceStatsOffering"]]:
    """
    Args:
        uuid (UUID):
        created (Union[Unset, datetime.date]):
        customer (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        end_date (Union[Unset, datetime.date]):
        max_sum (Union[Unset, float]):
        min_sum (Union[Unset, float]):
        month (Union[Unset, int]):
        o (Union[Unset, list[InvoicesStatsListOItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        provider_uuid (Union[Unset, str]):
        start_date (Union[Unset, datetime.date]):
        state (Union[Unset, list[InvoicesStatsListStateItem]]):
        year (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['InvoiceStatsOffering']]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        created=created,
        customer=customer,
        customer_uuid=customer_uuid,
        end_date=end_date,
        max_sum=max_sum,
        min_sum=min_sum,
        month=month,
        o=o,
        page=page,
        page_size=page_size,
        provider_uuid=provider_uuid,
        start_date=start_date,
        state=state,
        year=year,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    created: Union[Unset, datetime.date] = UNSET,
    customer: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    end_date: Union[Unset, datetime.date] = UNSET,
    max_sum: Union[Unset, float] = UNSET,
    min_sum: Union[Unset, float] = UNSET,
    month: Union[Unset, int] = UNSET,
    o: Union[Unset, list[InvoicesStatsListOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    provider_uuid: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.date] = UNSET,
    state: Union[Unset, list[InvoicesStatsListStateItem]] = UNSET,
    year: Union[Unset, int] = UNSET,
) -> Optional[list["InvoiceStatsOffering"]]:
    """
    Args:
        uuid (UUID):
        created (Union[Unset, datetime.date]):
        customer (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        end_date (Union[Unset, datetime.date]):
        max_sum (Union[Unset, float]):
        min_sum (Union[Unset, float]):
        month (Union[Unset, int]):
        o (Union[Unset, list[InvoicesStatsListOItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        provider_uuid (Union[Unset, str]):
        start_date (Union[Unset, datetime.date]):
        state (Union[Unset, list[InvoicesStatsListStateItem]]):
        year (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['InvoiceStatsOffering']
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            created=created,
            customer=customer,
            customer_uuid=customer_uuid,
            end_date=end_date,
            max_sum=max_sum,
            min_sum=min_sum,
            month=month,
            o=o,
            page=page,
            page_size=page_size,
            provider_uuid=provider_uuid,
            start_date=start_date,
            state=state,
            year=year,
        )
    ).parsed
