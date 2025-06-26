from http import HTTPStatus
from typing import Any, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.open_stack_flavor import OpenStackFlavor
from ...models.openstack_flavors_usage_stats_retrieve_field_item import OpenstackFlavorsUsageStatsRetrieveFieldItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    field: Union[Unset, list[OpenstackFlavorsUsageStatsRetrieveFieldItem]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_field: Union[Unset, list[str]] = UNSET
    if not isinstance(field, Unset):
        json_field = []
        for field_item_data in field:
            field_item = field_item_data.value
            json_field.append(field_item)

    params["field"] = json_field

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/openstack-flavors/usage_stats/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> OpenStackFlavor:
    if response.status_code == 200:
        response_200 = OpenStackFlavor.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OpenStackFlavor]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    field: Union[Unset, list[OpenstackFlavorsUsageStatsRetrieveFieldItem]] = UNSET,
) -> Response[OpenStackFlavor]:
    """
    Args:
        field (Union[Unset, list[OpenstackFlavorsUsageStatsRetrieveFieldItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OpenStackFlavor]
    """

    kwargs = _get_kwargs(
        field=field,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    field: Union[Unset, list[OpenstackFlavorsUsageStatsRetrieveFieldItem]] = UNSET,
) -> OpenStackFlavor:
    """
    Args:
        field (Union[Unset, list[OpenstackFlavorsUsageStatsRetrieveFieldItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OpenStackFlavor
    """

    return sync_detailed(
        client=client,
        field=field,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    field: Union[Unset, list[OpenstackFlavorsUsageStatsRetrieveFieldItem]] = UNSET,
) -> Response[OpenStackFlavor]:
    """
    Args:
        field (Union[Unset, list[OpenstackFlavorsUsageStatsRetrieveFieldItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OpenStackFlavor]
    """

    kwargs = _get_kwargs(
        field=field,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    field: Union[Unset, list[OpenstackFlavorsUsageStatsRetrieveFieldItem]] = UNSET,
) -> OpenStackFlavor:
    """
    Args:
        field (Union[Unset, list[OpenstackFlavorsUsageStatsRetrieveFieldItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OpenStackFlavor
    """

    return (
        await asyncio_detailed(
            client=client,
            field=field,
        )
    ).parsed
