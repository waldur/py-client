import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.payment import Payment
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    date_of_payment: Union[Unset, datetime.date] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    profile: Union[Unset, str] = UNSET,
    profile_uuid: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_date_of_payment: Union[Unset, str] = UNSET
    if not isinstance(date_of_payment, Unset):
        json_date_of_payment = date_of_payment.isoformat()
    params["date_of_payment"] = json_date_of_payment

    params["page"] = page

    params["page_size"] = page_size

    params["profile"] = profile

    json_profile_uuid: Union[Unset, str] = UNSET
    if not isinstance(profile_uuid, Unset):
        json_profile_uuid = str(profile_uuid)
    params["profile_uuid"] = json_profile_uuid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/payments/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["Payment"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_paginated_payment_list_item_data in _response_200:
            componentsschemas_paginated_payment_list_item = Payment.from_dict(
                componentsschemas_paginated_payment_list_item_data
            )

            response_200.append(componentsschemas_paginated_payment_list_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["Payment"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    date_of_payment: Union[Unset, datetime.date] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    profile: Union[Unset, str] = UNSET,
    profile_uuid: Union[Unset, UUID] = UNSET,
) -> Response[list["Payment"]]:
    """
    Args:
        date_of_payment (Union[Unset, datetime.date]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        profile (Union[Unset, str]):
        profile_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['Payment']]
    """

    kwargs = _get_kwargs(
        date_of_payment=date_of_payment,
        page=page,
        page_size=page_size,
        profile=profile,
        profile_uuid=profile_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    date_of_payment: Union[Unset, datetime.date] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    profile: Union[Unset, str] = UNSET,
    profile_uuid: Union[Unset, UUID] = UNSET,
) -> Optional[list["Payment"]]:
    """
    Args:
        date_of_payment (Union[Unset, datetime.date]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        profile (Union[Unset, str]):
        profile_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['Payment']
    """

    return sync_detailed(
        client=client,
        date_of_payment=date_of_payment,
        page=page,
        page_size=page_size,
        profile=profile,
        profile_uuid=profile_uuid,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    date_of_payment: Union[Unset, datetime.date] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    profile: Union[Unset, str] = UNSET,
    profile_uuid: Union[Unset, UUID] = UNSET,
) -> Response[list["Payment"]]:
    """
    Args:
        date_of_payment (Union[Unset, datetime.date]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        profile (Union[Unset, str]):
        profile_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['Payment']]
    """

    kwargs = _get_kwargs(
        date_of_payment=date_of_payment,
        page=page,
        page_size=page_size,
        profile=profile,
        profile_uuid=profile_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    date_of_payment: Union[Unset, datetime.date] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    profile: Union[Unset, str] = UNSET,
    profile_uuid: Union[Unset, UUID] = UNSET,
) -> Optional[list["Payment"]]:
    """
    Args:
        date_of_payment (Union[Unset, datetime.date]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        profile (Union[Unset, str]):
        profile_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['Payment']
    """

    return (
        await asyncio_detailed(
            client=client,
            date_of_payment=date_of_payment,
            page=page,
            page_size=page_size,
            profile=profile,
            profile_uuid=profile_uuid,
        )
    ).parsed
