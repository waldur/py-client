from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.provider_invoice_items_head_o_item import ProviderInvoiceItemsHeadOItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    customer_uuid: Union[Unset, UUID] = UNSET,
    invoice_month: Union[Unset, int] = UNSET,
    invoice_year: Union[Unset, int] = UNSET,
    o: Union[Unset, list[ProviderInvoiceItemsHeadOItem]] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_customer_uuid: Union[Unset, str] = UNSET
    if not isinstance(customer_uuid, Unset):
        json_customer_uuid = str(customer_uuid)
    params["customer_uuid"] = json_customer_uuid

    params["invoice_month"] = invoice_month

    params["invoice_year"] = invoice_year

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

    params["page"] = page

    params["page_size"] = page_size

    json_project_uuid: Union[Unset, str] = UNSET
    if not isinstance(project_uuid, Unset):
        json_project_uuid = str(project_uuid)
    params["project_uuid"] = json_project_uuid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "head",
        "url": "/api/provider-invoice-items/",
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
    customer_uuid: Union[Unset, UUID] = UNSET,
    invoice_month: Union[Unset, int] = UNSET,
    invoice_year: Union[Unset, int] = UNSET,
    o: Union[Unset, list[ProviderInvoiceItemsHeadOItem]] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
) -> Response[Any]:
    """Mixin to optimize HEAD requests for DRF views bypassing serializer processing

    Args:
        customer_uuid (Union[Unset, UUID]):
        invoice_month (Union[Unset, int]):
        invoice_year (Union[Unset, int]):
        o (Union[Unset, list[ProviderInvoiceItemsHeadOItem]]):
        offering_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        project_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        customer_uuid=customer_uuid,
        invoice_month=invoice_month,
        invoice_year=invoice_year,
        o=o,
        offering_uuid=offering_uuid,
        page=page,
        page_size=page_size,
        project_uuid=project_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    customer_uuid: Union[Unset, UUID] = UNSET,
    invoice_month: Union[Unset, int] = UNSET,
    invoice_year: Union[Unset, int] = UNSET,
    o: Union[Unset, list[ProviderInvoiceItemsHeadOItem]] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
) -> Response[Any]:
    """Mixin to optimize HEAD requests for DRF views bypassing serializer processing

    Args:
        customer_uuid (Union[Unset, UUID]):
        invoice_month (Union[Unset, int]):
        invoice_year (Union[Unset, int]):
        o (Union[Unset, list[ProviderInvoiceItemsHeadOItem]]):
        offering_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        project_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        customer_uuid=customer_uuid,
        invoice_month=invoice_month,
        invoice_year=invoice_year,
        o=o,
        offering_uuid=offering_uuid,
        page=page,
        page_size=page_size,
        project_uuid=project_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
