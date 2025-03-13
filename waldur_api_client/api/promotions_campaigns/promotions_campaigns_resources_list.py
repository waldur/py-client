import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.promotions_campaigns_resources_list_o_item import PromotionsCampaignsResourcesListOItem
from ...models.promotions_campaigns_resources_list_state_item import PromotionsCampaignsResourcesListStateItem
from ...models.resource import Resource
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    discount_type: Union[Unset, str] = UNSET,
    end_date: Union[Unset, datetime.date] = UNSET,
    o: Union[Unset, list[PromotionsCampaignsResourcesListOItem]] = UNSET,
    offering: Union[Unset, str] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
    service_provider_uuid: Union[Unset, UUID] = UNSET,
    start_date: Union[Unset, datetime.date] = UNSET,
    state: Union[Unset, list[PromotionsCampaignsResourcesListStateItem]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["discount_type"] = discount_type

    json_end_date: Union[Unset, str] = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat()
    params["end_date"] = json_end_date

    json_o: Union[Unset, list[str]] = UNSET
    if not isinstance(o, Unset):
        json_o = []
        for o_item_data in o:
            o_item = o_item_data.value
            json_o.append(o_item)

    params["o"] = json_o

    params["offering"] = offering

    json_offering_uuid: Union[Unset, str] = UNSET
    if not isinstance(offering_uuid, Unset):
        json_offering_uuid = str(offering_uuid)
    params["offering_uuid"] = json_offering_uuid

    params["page"] = page

    params["page_size"] = page_size

    params["query"] = query

    json_service_provider_uuid: Union[Unset, str] = UNSET
    if not isinstance(service_provider_uuid, Unset):
        json_service_provider_uuid = str(service_provider_uuid)
    params["service_provider_uuid"] = json_service_provider_uuid

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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/promotions-campaigns/{uuid}/resources/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["Resource"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Resource.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["Resource"]]:
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
    discount_type: Union[Unset, str] = UNSET,
    end_date: Union[Unset, datetime.date] = UNSET,
    o: Union[Unset, list[PromotionsCampaignsResourcesListOItem]] = UNSET,
    offering: Union[Unset, str] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
    service_provider_uuid: Union[Unset, UUID] = UNSET,
    start_date: Union[Unset, datetime.date] = UNSET,
    state: Union[Unset, list[PromotionsCampaignsResourcesListStateItem]] = UNSET,
) -> Response[list["Resource"]]:
    """Return a list of resources for which the campaign is applied.

    Args:
        uuid (UUID):
        discount_type (Union[Unset, str]):
        end_date (Union[Unset, datetime.date]):
        o (Union[Unset, list[PromotionsCampaignsResourcesListOItem]]):
        offering (Union[Unset, str]):
        offering_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        query (Union[Unset, str]):
        service_provider_uuid (Union[Unset, UUID]):
        start_date (Union[Unset, datetime.date]):
        state (Union[Unset, list[PromotionsCampaignsResourcesListStateItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['Resource']]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        discount_type=discount_type,
        end_date=end_date,
        o=o,
        offering=offering,
        offering_uuid=offering_uuid,
        page=page,
        page_size=page_size,
        query=query,
        service_provider_uuid=service_provider_uuid,
        start_date=start_date,
        state=state,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    discount_type: Union[Unset, str] = UNSET,
    end_date: Union[Unset, datetime.date] = UNSET,
    o: Union[Unset, list[PromotionsCampaignsResourcesListOItem]] = UNSET,
    offering: Union[Unset, str] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
    service_provider_uuid: Union[Unset, UUID] = UNSET,
    start_date: Union[Unset, datetime.date] = UNSET,
    state: Union[Unset, list[PromotionsCampaignsResourcesListStateItem]] = UNSET,
) -> Optional[list["Resource"]]:
    """Return a list of resources for which the campaign is applied.

    Args:
        uuid (UUID):
        discount_type (Union[Unset, str]):
        end_date (Union[Unset, datetime.date]):
        o (Union[Unset, list[PromotionsCampaignsResourcesListOItem]]):
        offering (Union[Unset, str]):
        offering_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        query (Union[Unset, str]):
        service_provider_uuid (Union[Unset, UUID]):
        start_date (Union[Unset, datetime.date]):
        state (Union[Unset, list[PromotionsCampaignsResourcesListStateItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['Resource']
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        discount_type=discount_type,
        end_date=end_date,
        o=o,
        offering=offering,
        offering_uuid=offering_uuid,
        page=page,
        page_size=page_size,
        query=query,
        service_provider_uuid=service_provider_uuid,
        start_date=start_date,
        state=state,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    discount_type: Union[Unset, str] = UNSET,
    end_date: Union[Unset, datetime.date] = UNSET,
    o: Union[Unset, list[PromotionsCampaignsResourcesListOItem]] = UNSET,
    offering: Union[Unset, str] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
    service_provider_uuid: Union[Unset, UUID] = UNSET,
    start_date: Union[Unset, datetime.date] = UNSET,
    state: Union[Unset, list[PromotionsCampaignsResourcesListStateItem]] = UNSET,
) -> Response[list["Resource"]]:
    """Return a list of resources for which the campaign is applied.

    Args:
        uuid (UUID):
        discount_type (Union[Unset, str]):
        end_date (Union[Unset, datetime.date]):
        o (Union[Unset, list[PromotionsCampaignsResourcesListOItem]]):
        offering (Union[Unset, str]):
        offering_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        query (Union[Unset, str]):
        service_provider_uuid (Union[Unset, UUID]):
        start_date (Union[Unset, datetime.date]):
        state (Union[Unset, list[PromotionsCampaignsResourcesListStateItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['Resource']]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        discount_type=discount_type,
        end_date=end_date,
        o=o,
        offering=offering,
        offering_uuid=offering_uuid,
        page=page,
        page_size=page_size,
        query=query,
        service_provider_uuid=service_provider_uuid,
        start_date=start_date,
        state=state,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    discount_type: Union[Unset, str] = UNSET,
    end_date: Union[Unset, datetime.date] = UNSET,
    o: Union[Unset, list[PromotionsCampaignsResourcesListOItem]] = UNSET,
    offering: Union[Unset, str] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
    service_provider_uuid: Union[Unset, UUID] = UNSET,
    start_date: Union[Unset, datetime.date] = UNSET,
    state: Union[Unset, list[PromotionsCampaignsResourcesListStateItem]] = UNSET,
) -> Optional[list["Resource"]]:
    """Return a list of resources for which the campaign is applied.

    Args:
        uuid (UUID):
        discount_type (Union[Unset, str]):
        end_date (Union[Unset, datetime.date]):
        o (Union[Unset, list[PromotionsCampaignsResourcesListOItem]]):
        offering (Union[Unset, str]):
        offering_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        query (Union[Unset, str]):
        service_provider_uuid (Union[Unset, UUID]):
        start_date (Union[Unset, datetime.date]):
        state (Union[Unset, list[PromotionsCampaignsResourcesListStateItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['Resource']
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            discount_type=discount_type,
            end_date=end_date,
            o=o,
            offering=offering,
            offering_uuid=offering_uuid,
            page=page,
            page_size=page_size,
            query=query,
            service_provider_uuid=service_provider_uuid,
            start_date=start_date,
            state=state,
        )
    ).parsed
