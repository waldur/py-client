from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.proposal_public_calls_list_field_item import ProposalPublicCallsListFieldItem
from ...models.proposal_public_calls_list_o_item import ProposalPublicCallsListOItem
from ...models.proposal_public_calls_list_state_item import ProposalPublicCallsListStateItem
from ...models.public_call import PublicCall
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    customer: Union[Unset, str] = UNSET,
    customer_keyword: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    field: Union[Unset, list[ProposalPublicCallsListFieldItem]] = UNSET,
    has_active_round: Union[Unset, bool] = UNSET,
    name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[ProposalPublicCallsListOItem]] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    offerings_provider_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    state: Union[Unset, list[ProposalPublicCallsListStateItem]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["customer"] = customer

    params["customer_keyword"] = customer_keyword

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

    params["has_active_round"] = has_active_round

    params["name"] = name

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

    json_offerings_provider_uuid: Union[Unset, str] = UNSET
    if not isinstance(offerings_provider_uuid, Unset):
        json_offerings_provider_uuid = str(offerings_provider_uuid)
    params["offerings_provider_uuid"] = json_offerings_provider_uuid

    params["page"] = page

    params["page_size"] = page_size

    json_state: Union[Unset, list[str]] = UNSET
    if not isinstance(state, Unset):
        json_state = []
        for state_item_data in state:
            state_item = state_item_data.value
            json_state.append(state_item)

    params["state"] = json_state

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/proposal-public-calls/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["PublicCall"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_paginated_public_call_list_item_data in _response_200:
            componentsschemas_paginated_public_call_list_item = PublicCall.from_dict(
                componentsschemas_paginated_public_call_list_item_data
            )

            response_200.append(componentsschemas_paginated_public_call_list_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["PublicCall"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    customer: Union[Unset, str] = UNSET,
    customer_keyword: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    field: Union[Unset, list[ProposalPublicCallsListFieldItem]] = UNSET,
    has_active_round: Union[Unset, bool] = UNSET,
    name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[ProposalPublicCallsListOItem]] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    offerings_provider_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    state: Union[Unset, list[ProposalPublicCallsListStateItem]] = UNSET,
) -> Response[list["PublicCall"]]:
    """
    Args:
        customer (Union[Unset, str]):
        customer_keyword (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        field (Union[Unset, list[ProposalPublicCallsListFieldItem]]):
        has_active_round (Union[Unset, bool]):
        name (Union[Unset, str]):
        o (Union[Unset, list[ProposalPublicCallsListOItem]]):
        offering_uuid (Union[Unset, UUID]):
        offerings_provider_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        state (Union[Unset, list[ProposalPublicCallsListStateItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['PublicCall']]
    """

    kwargs = _get_kwargs(
        customer=customer,
        customer_keyword=customer_keyword,
        customer_uuid=customer_uuid,
        field=field,
        has_active_round=has_active_round,
        name=name,
        o=o,
        offering_uuid=offering_uuid,
        offerings_provider_uuid=offerings_provider_uuid,
        page=page,
        page_size=page_size,
        state=state,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    customer: Union[Unset, str] = UNSET,
    customer_keyword: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    field: Union[Unset, list[ProposalPublicCallsListFieldItem]] = UNSET,
    has_active_round: Union[Unset, bool] = UNSET,
    name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[ProposalPublicCallsListOItem]] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    offerings_provider_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    state: Union[Unset, list[ProposalPublicCallsListStateItem]] = UNSET,
) -> Optional[list["PublicCall"]]:
    """
    Args:
        customer (Union[Unset, str]):
        customer_keyword (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        field (Union[Unset, list[ProposalPublicCallsListFieldItem]]):
        has_active_round (Union[Unset, bool]):
        name (Union[Unset, str]):
        o (Union[Unset, list[ProposalPublicCallsListOItem]]):
        offering_uuid (Union[Unset, UUID]):
        offerings_provider_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        state (Union[Unset, list[ProposalPublicCallsListStateItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['PublicCall']
    """

    return sync_detailed(
        client=client,
        customer=customer,
        customer_keyword=customer_keyword,
        customer_uuid=customer_uuid,
        field=field,
        has_active_round=has_active_round,
        name=name,
        o=o,
        offering_uuid=offering_uuid,
        offerings_provider_uuid=offerings_provider_uuid,
        page=page,
        page_size=page_size,
        state=state,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    customer: Union[Unset, str] = UNSET,
    customer_keyword: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    field: Union[Unset, list[ProposalPublicCallsListFieldItem]] = UNSET,
    has_active_round: Union[Unset, bool] = UNSET,
    name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[ProposalPublicCallsListOItem]] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    offerings_provider_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    state: Union[Unset, list[ProposalPublicCallsListStateItem]] = UNSET,
) -> Response[list["PublicCall"]]:
    """
    Args:
        customer (Union[Unset, str]):
        customer_keyword (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        field (Union[Unset, list[ProposalPublicCallsListFieldItem]]):
        has_active_round (Union[Unset, bool]):
        name (Union[Unset, str]):
        o (Union[Unset, list[ProposalPublicCallsListOItem]]):
        offering_uuid (Union[Unset, UUID]):
        offerings_provider_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        state (Union[Unset, list[ProposalPublicCallsListStateItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['PublicCall']]
    """

    kwargs = _get_kwargs(
        customer=customer,
        customer_keyword=customer_keyword,
        customer_uuid=customer_uuid,
        field=field,
        has_active_round=has_active_round,
        name=name,
        o=o,
        offering_uuid=offering_uuid,
        offerings_provider_uuid=offerings_provider_uuid,
        page=page,
        page_size=page_size,
        state=state,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    customer: Union[Unset, str] = UNSET,
    customer_keyword: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    field: Union[Unset, list[ProposalPublicCallsListFieldItem]] = UNSET,
    has_active_round: Union[Unset, bool] = UNSET,
    name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[ProposalPublicCallsListOItem]] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    offerings_provider_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    state: Union[Unset, list[ProposalPublicCallsListStateItem]] = UNSET,
) -> Optional[list["PublicCall"]]:
    """
    Args:
        customer (Union[Unset, str]):
        customer_keyword (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        field (Union[Unset, list[ProposalPublicCallsListFieldItem]]):
        has_active_round (Union[Unset, bool]):
        name (Union[Unset, str]):
        o (Union[Unset, list[ProposalPublicCallsListOItem]]):
        offering_uuid (Union[Unset, UUID]):
        offerings_provider_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        state (Union[Unset, list[ProposalPublicCallsListStateItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['PublicCall']
    """

    return (
        await asyncio_detailed(
            client=client,
            customer=customer,
            customer_keyword=customer_keyword,
            customer_uuid=customer_uuid,
            field=field,
            has_active_round=has_active_round,
            name=name,
            o=o,
            offering_uuid=offering_uuid,
            offerings_provider_uuid=offerings_provider_uuid,
            page=page,
            page_size=page_size,
            state=state,
        )
    ).parsed
