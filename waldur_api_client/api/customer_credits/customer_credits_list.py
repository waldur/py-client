from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.customer_credit import CustomerCredit
from ...models.customer_credits_list_o_item import CustomerCreditsListOItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    customer_name: Union[Unset, str] = UNSET,
    customer_slug: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    o: Union[Unset, list[CustomerCreditsListOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["customer_name"] = customer_name

    params["customer_slug"] = customer_slug

    json_customer_uuid: Union[Unset, str] = UNSET
    if not isinstance(customer_uuid, Unset):
        json_customer_uuid = str(customer_uuid)
    params["customer_uuid"] = json_customer_uuid

    json_o: Union[Unset, list[str]] = UNSET
    if not isinstance(o, Unset):
        json_o = []
        for o_item_data in o:
            o_item = o_item_data.value
            json_o.append(o_item)

    params["o"] = json_o

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/customer-credits/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> list["CustomerCredit"]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CustomerCredit.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["CustomerCredit"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    customer_name: Union[Unset, str] = UNSET,
    customer_slug: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    o: Union[Unset, list[CustomerCreditsListOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[list["CustomerCredit"]]:
    """Mixin to optimize HEAD requests for DRF views bypassing serializer processing

    Args:
        customer_name (Union[Unset, str]):
        customer_slug (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        o (Union[Unset, list[CustomerCreditsListOItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['CustomerCredit']]
    """

    kwargs = _get_kwargs(
        customer_name=customer_name,
        customer_slug=customer_slug,
        customer_uuid=customer_uuid,
        o=o,
        page=page,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    customer_name: Union[Unset, str] = UNSET,
    customer_slug: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    o: Union[Unset, list[CustomerCreditsListOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> list["CustomerCredit"]:
    """Mixin to optimize HEAD requests for DRF views bypassing serializer processing

    Args:
        customer_name (Union[Unset, str]):
        customer_slug (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        o (Union[Unset, list[CustomerCreditsListOItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['CustomerCredit']
    """

    return sync_detailed(
        client=client,
        customer_name=customer_name,
        customer_slug=customer_slug,
        customer_uuid=customer_uuid,
        o=o,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    customer_name: Union[Unset, str] = UNSET,
    customer_slug: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    o: Union[Unset, list[CustomerCreditsListOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[list["CustomerCredit"]]:
    """Mixin to optimize HEAD requests for DRF views bypassing serializer processing

    Args:
        customer_name (Union[Unset, str]):
        customer_slug (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        o (Union[Unset, list[CustomerCreditsListOItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['CustomerCredit']]
    """

    kwargs = _get_kwargs(
        customer_name=customer_name,
        customer_slug=customer_slug,
        customer_uuid=customer_uuid,
        o=o,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    customer_name: Union[Unset, str] = UNSET,
    customer_slug: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    o: Union[Unset, list[CustomerCreditsListOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> list["CustomerCredit"]:
    """Mixin to optimize HEAD requests for DRF views bypassing serializer processing

    Args:
        customer_name (Union[Unset, str]):
        customer_slug (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        o (Union[Unset, list[CustomerCreditsListOItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['CustomerCredit']
    """

    return (
        await asyncio_detailed(
            client=client,
            customer_name=customer_name,
            customer_slug=customer_slug,
            customer_uuid=customer_uuid,
            o=o,
            page=page,
            page_size=page_size,
        )
    ).parsed
