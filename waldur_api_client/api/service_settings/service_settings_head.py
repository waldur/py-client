from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_settings_head_state_item import ServiceSettingsHeadStateItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    customer: Union[Unset, UUID] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    o: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    scope_uuid: Union[Unset, str] = UNSET,
    shared: Union[Unset, bool] = UNSET,
    state: Union[Unset, list[ServiceSettingsHeadStateItem]] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_customer: Union[Unset, str] = UNSET
    if not isinstance(customer, Unset):
        json_customer = str(customer)
    params["customer"] = json_customer

    json_customer_uuid: Union[Unset, str] = UNSET
    if not isinstance(customer_uuid, Unset):
        json_customer_uuid = str(customer_uuid)
    params["customer_uuid"] = json_customer_uuid

    params["name"] = name

    params["name_exact"] = name_exact

    params["o"] = o

    params["page"] = page

    params["page_size"] = page_size

    params["scope_uuid"] = scope_uuid

    params["shared"] = shared

    json_state: Union[Unset, list[str]] = UNSET
    if not isinstance(state, Unset):
        json_state = []
        for state_item_data in state:
            state_item = state_item_data.value
            json_state.append(state_item)

    params["state"] = json_state

    params["type"] = type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "head",
        "url": "/api/service-settings/",
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
    customer: Union[Unset, UUID] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    o: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    scope_uuid: Union[Unset, str] = UNSET,
    shared: Union[Unset, bool] = UNSET,
    state: Union[Unset, list[ServiceSettingsHeadStateItem]] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Mixin to optimize HEAD requests for DRF views bypassing serializer processing

    Args:
        customer (Union[Unset, UUID]):
        customer_uuid (Union[Unset, UUID]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        o (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        scope_uuid (Union[Unset, str]):
        shared (Union[Unset, bool]):
        state (Union[Unset, list[ServiceSettingsHeadStateItem]]):
        type_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        customer=customer,
        customer_uuid=customer_uuid,
        name=name,
        name_exact=name_exact,
        o=o,
        page=page,
        page_size=page_size,
        scope_uuid=scope_uuid,
        shared=shared,
        state=state,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    customer: Union[Unset, UUID] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    o: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    scope_uuid: Union[Unset, str] = UNSET,
    shared: Union[Unset, bool] = UNSET,
    state: Union[Unset, list[ServiceSettingsHeadStateItem]] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Mixin to optimize HEAD requests for DRF views bypassing serializer processing

    Args:
        customer (Union[Unset, UUID]):
        customer_uuid (Union[Unset, UUID]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        o (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        scope_uuid (Union[Unset, str]):
        shared (Union[Unset, bool]):
        state (Union[Unset, list[ServiceSettingsHeadStateItem]]):
        type_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        customer=customer,
        customer_uuid=customer_uuid,
        name=name,
        name_exact=name_exact,
        o=o,
        page=page,
        page_size=page_size,
        scope_uuid=scope_uuid,
        shared=shared,
        state=state,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
