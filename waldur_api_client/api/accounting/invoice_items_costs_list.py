from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.invoice_cost import InvoiceCost
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    credit_uuid: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, str] = UNSET,
    month: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    project_uuid: Union[Unset, str] = UNSET,
    resource_uuid: Union[Unset, str] = UNSET,
    year: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["credit_uuid"] = credit_uuid

    params["customer_uuid"] = customer_uuid

    params["month"] = month

    params["page"] = page

    params["page_size"] = page_size

    params["project_uuid"] = project_uuid

    params["resource_uuid"] = resource_uuid

    params["year"] = year

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/invoice-items/costs/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["InvoiceCost"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_paginated_invoice_cost_list_item_data in _response_200:
            componentsschemas_paginated_invoice_cost_list_item = InvoiceCost.from_dict(
                componentsschemas_paginated_invoice_cost_list_item_data
            )

            response_200.append(componentsschemas_paginated_invoice_cost_list_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["InvoiceCost"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    credit_uuid: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, str] = UNSET,
    month: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    project_uuid: Union[Unset, str] = UNSET,
    resource_uuid: Union[Unset, str] = UNSET,
    year: Union[Unset, int] = UNSET,
) -> Response[list["InvoiceCost"]]:
    """
    Args:
        credit_uuid (Union[Unset, str]):
        customer_uuid (Union[Unset, str]):
        month (Union[Unset, int]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        project_uuid (Union[Unset, str]):
        resource_uuid (Union[Unset, str]):
        year (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['InvoiceCost']]
    """

    kwargs = _get_kwargs(
        credit_uuid=credit_uuid,
        customer_uuid=customer_uuid,
        month=month,
        page=page,
        page_size=page_size,
        project_uuid=project_uuid,
        resource_uuid=resource_uuid,
        year=year,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    credit_uuid: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, str] = UNSET,
    month: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    project_uuid: Union[Unset, str] = UNSET,
    resource_uuid: Union[Unset, str] = UNSET,
    year: Union[Unset, int] = UNSET,
) -> Optional[list["InvoiceCost"]]:
    """
    Args:
        credit_uuid (Union[Unset, str]):
        customer_uuid (Union[Unset, str]):
        month (Union[Unset, int]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        project_uuid (Union[Unset, str]):
        resource_uuid (Union[Unset, str]):
        year (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['InvoiceCost']
    """

    return sync_detailed(
        client=client,
        credit_uuid=credit_uuid,
        customer_uuid=customer_uuid,
        month=month,
        page=page,
        page_size=page_size,
        project_uuid=project_uuid,
        resource_uuid=resource_uuid,
        year=year,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    credit_uuid: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, str] = UNSET,
    month: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    project_uuid: Union[Unset, str] = UNSET,
    resource_uuid: Union[Unset, str] = UNSET,
    year: Union[Unset, int] = UNSET,
) -> Response[list["InvoiceCost"]]:
    """
    Args:
        credit_uuid (Union[Unset, str]):
        customer_uuid (Union[Unset, str]):
        month (Union[Unset, int]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        project_uuid (Union[Unset, str]):
        resource_uuid (Union[Unset, str]):
        year (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['InvoiceCost']]
    """

    kwargs = _get_kwargs(
        credit_uuid=credit_uuid,
        customer_uuid=customer_uuid,
        month=month,
        page=page,
        page_size=page_size,
        project_uuid=project_uuid,
        resource_uuid=resource_uuid,
        year=year,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    credit_uuid: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, str] = UNSET,
    month: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    project_uuid: Union[Unset, str] = UNSET,
    resource_uuid: Union[Unset, str] = UNSET,
    year: Union[Unset, int] = UNSET,
) -> Optional[list["InvoiceCost"]]:
    """
    Args:
        credit_uuid (Union[Unset, str]):
        customer_uuid (Union[Unset, str]):
        month (Union[Unset, int]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        project_uuid (Union[Unset, str]):
        resource_uuid (Union[Unset, str]):
        year (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['InvoiceCost']
    """

    return (
        await asyncio_detailed(
            client=client,
            credit_uuid=credit_uuid,
            customer_uuid=customer_uuid,
            month=month,
            page=page,
            page_size=page_size,
            project_uuid=project_uuid,
            resource_uuid=resource_uuid,
            year=year,
        )
    ).parsed
