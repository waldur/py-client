from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_settings import ServiceSettings
from ...models.service_settings_list_field_item import ServiceSettingsListFieldItem
from ...models.service_settings_list_state_item import ServiceSettingsListStateItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    customer: Union[Unset, UUID] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    field: Union[Unset, list[ServiceSettingsListFieldItem]] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    o: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    scope_uuid: Union[Unset, UUID] = UNSET,
    shared: Union[Unset, bool] = UNSET,
    state: Union[Unset, list[ServiceSettingsListStateItem]] = UNSET,
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

    json_field: Union[Unset, list[str]] = UNSET
    if not isinstance(field, Unset):
        json_field = []
        for field_item_data in field:
            field_item = field_item_data.value
            json_field.append(field_item)

    params["field"] = json_field

    params["name"] = name

    params["name_exact"] = name_exact

    params["o"] = o

    params["page"] = page

    params["page_size"] = page_size

    json_scope_uuid: Union[Unset, str] = UNSET
    if not isinstance(scope_uuid, Unset):
        json_scope_uuid = str(scope_uuid)
    params["scope_uuid"] = json_scope_uuid

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
        "method": "get",
        "url": "/api/service-settings/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["ServiceSettings"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_paginated_service_settings_list_item_data in _response_200:
            componentsschemas_paginated_service_settings_list_item = ServiceSettings.from_dict(
                componentsschemas_paginated_service_settings_list_item_data
            )

            response_200.append(componentsschemas_paginated_service_settings_list_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["ServiceSettings"]]:
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
    field: Union[Unset, list[ServiceSettingsListFieldItem]] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    o: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    scope_uuid: Union[Unset, UUID] = UNSET,
    shared: Union[Unset, bool] = UNSET,
    state: Union[Unset, list[ServiceSettingsListStateItem]] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> Response[list["ServiceSettings"]]:
    """
    Args:
        customer (Union[Unset, UUID]):
        customer_uuid (Union[Unset, UUID]):
        field (Union[Unset, list[ServiceSettingsListFieldItem]]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        o (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        scope_uuid (Union[Unset, UUID]):
        shared (Union[Unset, bool]):
        state (Union[Unset, list[ServiceSettingsListStateItem]]):
        type_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['ServiceSettings']]
    """

    kwargs = _get_kwargs(
        customer=customer,
        customer_uuid=customer_uuid,
        field=field,
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


def sync(
    *,
    client: AuthenticatedClient,
    customer: Union[Unset, UUID] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    field: Union[Unset, list[ServiceSettingsListFieldItem]] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    o: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    scope_uuid: Union[Unset, UUID] = UNSET,
    shared: Union[Unset, bool] = UNSET,
    state: Union[Unset, list[ServiceSettingsListStateItem]] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> Optional[list["ServiceSettings"]]:
    """
    Args:
        customer (Union[Unset, UUID]):
        customer_uuid (Union[Unset, UUID]):
        field (Union[Unset, list[ServiceSettingsListFieldItem]]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        o (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        scope_uuid (Union[Unset, UUID]):
        shared (Union[Unset, bool]):
        state (Union[Unset, list[ServiceSettingsListStateItem]]):
        type_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['ServiceSettings']
    """

    return sync_detailed(
        client=client,
        customer=customer,
        customer_uuid=customer_uuid,
        field=field,
        name=name,
        name_exact=name_exact,
        o=o,
        page=page,
        page_size=page_size,
        scope_uuid=scope_uuid,
        shared=shared,
        state=state,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    customer: Union[Unset, UUID] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    field: Union[Unset, list[ServiceSettingsListFieldItem]] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    o: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    scope_uuid: Union[Unset, UUID] = UNSET,
    shared: Union[Unset, bool] = UNSET,
    state: Union[Unset, list[ServiceSettingsListStateItem]] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> Response[list["ServiceSettings"]]:
    """
    Args:
        customer (Union[Unset, UUID]):
        customer_uuid (Union[Unset, UUID]):
        field (Union[Unset, list[ServiceSettingsListFieldItem]]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        o (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        scope_uuid (Union[Unset, UUID]):
        shared (Union[Unset, bool]):
        state (Union[Unset, list[ServiceSettingsListStateItem]]):
        type_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['ServiceSettings']]
    """

    kwargs = _get_kwargs(
        customer=customer,
        customer_uuid=customer_uuid,
        field=field,
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


async def asyncio(
    *,
    client: AuthenticatedClient,
    customer: Union[Unset, UUID] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    field: Union[Unset, list[ServiceSettingsListFieldItem]] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    o: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    scope_uuid: Union[Unset, UUID] = UNSET,
    shared: Union[Unset, bool] = UNSET,
    state: Union[Unset, list[ServiceSettingsListStateItem]] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> Optional[list["ServiceSettings"]]:
    """
    Args:
        customer (Union[Unset, UUID]):
        customer_uuid (Union[Unset, UUID]):
        field (Union[Unset, list[ServiceSettingsListFieldItem]]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        o (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        scope_uuid (Union[Unset, UUID]):
        shared (Union[Unset, bool]):
        state (Union[Unset, list[ServiceSettingsListStateItem]]):
        type_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['ServiceSettings']
    """

    return (
        await asyncio_detailed(
            client=client,
            customer=customer,
            customer_uuid=customer_uuid,
            field=field,
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
    ).parsed
