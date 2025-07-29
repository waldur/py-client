import datetime
from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.invoices_head_o_item import InvoicesHeadOItem
from ...models.invoices_head_state_item import InvoicesHeadStateItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    created: Union[Unset, datetime.date] = UNSET,
    customer: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    end_date: Union[Unset, datetime.date] = UNSET,
    month: Union[Unset, int] = UNSET,
    o: Union[Unset, list[InvoicesHeadOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    start_date: Union[Unset, datetime.date] = UNSET,
    state: Union[Unset, list[InvoicesHeadStateItem]] = UNSET,
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
        "method": "head",
        "url": "/api/invoices/",
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
    created: Union[Unset, datetime.date] = UNSET,
    customer: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    end_date: Union[Unset, datetime.date] = UNSET,
    month: Union[Unset, int] = UNSET,
    o: Union[Unset, list[InvoicesHeadOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    start_date: Union[Unset, datetime.date] = UNSET,
    state: Union[Unset, list[InvoicesHeadStateItem]] = UNSET,
    year: Union[Unset, int] = UNSET,
) -> Response[Any]:
    """Mixin to optimize HEAD requests for DRF views bypassing serializer processing

    Args:
        created (Union[Unset, datetime.date]):
        customer (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        end_date (Union[Unset, datetime.date]):
        month (Union[Unset, int]):
        o (Union[Unset, list[InvoicesHeadOItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        start_date (Union[Unset, datetime.date]):
        state (Union[Unset, list[InvoicesHeadStateItem]]):
        year (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        created=created,
        customer=customer,
        customer_uuid=customer_uuid,
        end_date=end_date,
        month=month,
        o=o,
        page=page,
        page_size=page_size,
        start_date=start_date,
        state=state,
        year=year,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    created: Union[Unset, datetime.date] = UNSET,
    customer: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    end_date: Union[Unset, datetime.date] = UNSET,
    month: Union[Unset, int] = UNSET,
    o: Union[Unset, list[InvoicesHeadOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    start_date: Union[Unset, datetime.date] = UNSET,
    state: Union[Unset, list[InvoicesHeadStateItem]] = UNSET,
    year: Union[Unset, int] = UNSET,
) -> Response[Any]:
    """Mixin to optimize HEAD requests for DRF views bypassing serializer processing

    Args:
        created (Union[Unset, datetime.date]):
        customer (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        end_date (Union[Unset, datetime.date]):
        month (Union[Unset, int]):
        o (Union[Unset, list[InvoicesHeadOItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        start_date (Union[Unset, datetime.date]):
        state (Union[Unset, list[InvoicesHeadStateItem]]):
        year (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        created=created,
        customer=customer,
        customer_uuid=customer_uuid,
        end_date=end_date,
        month=month,
        o=o,
        page=page,
        page_size=page_size,
        start_date=start_date,
        state=state,
        year=year,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
