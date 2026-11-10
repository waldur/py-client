from http import HTTPStatus
from typing import Any, Union, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.order_period_usage import OrderPeriodUsage
from ...types import Response


def _get_kwargs(
    uuid: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/marketplace-resources/{uuid}/order_period_usage/",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[list["OrderPeriodUsage"], str]:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = OrderPeriodUsage.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = cast(str, response.json())
        return response_400
    if response.status_code == 403:
        response_403 = cast(str, response.json())
        return response_403
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[list["OrderPeriodUsage"], str]]:
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
) -> Response[Union[list["OrderPeriodUsage"], str]]:
    """Get usage for the whole order period

     Returns the usage of each limit-based, non-prepaid component with a monthly limit period, summed
    since the resource was created, counting each billing period with its highest reported usage.
    Available when the offering has show_order_period_totals enabled. Not shown to users who see the
    resource only through a ResourceProject role.

    Args:
        uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[list['OrderPeriodUsage'], str]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
) -> Union[list["OrderPeriodUsage"], str]:
    """Get usage for the whole order period

     Returns the usage of each limit-based, non-prepaid component with a monthly limit period, summed
    since the resource was created, counting each billing period with its highest reported usage.
    Available when the offering has show_order_period_totals enabled. Not shown to users who see the
    resource only through a ResourceProject role.

    Args:
        uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[list['OrderPeriodUsage'], str]
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Union[list["OrderPeriodUsage"], str]]:
    """Get usage for the whole order period

     Returns the usage of each limit-based, non-prepaid component with a monthly limit period, summed
    since the resource was created, counting each billing period with its highest reported usage.
    Available when the offering has show_order_period_totals enabled. Not shown to users who see the
    resource only through a ResourceProject role.

    Args:
        uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[list['OrderPeriodUsage'], str]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
) -> Union[list["OrderPeriodUsage"], str]:
    """Get usage for the whole order period

     Returns the usage of each limit-based, non-prepaid component with a monthly limit period, summed
    since the resource was created, counting each billing period with its highest reported usage.
    Available when the offering has show_order_period_totals enabled. Not shown to users who see the
    resource only through a ResourceProject role.

    Args:
        uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[list['OrderPeriodUsage'], str]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
        )
    ).parsed
