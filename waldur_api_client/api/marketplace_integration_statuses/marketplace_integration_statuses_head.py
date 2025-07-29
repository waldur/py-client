from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.marketplace_integration_statuses_head_o_item import MarketplaceIntegrationStatusesHeadOItem
from ...models.marketplace_integration_statuses_head_status_item import MarketplaceIntegrationStatusesHeadStatusItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    agent_type: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, str] = UNSET,
    o: Union[Unset, list[MarketplaceIntegrationStatusesHeadOItem]] = UNSET,
    offering: Union[Unset, str] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    parent_offering_uuid: Union[Unset, UUID] = UNSET,
    status: Union[Unset, list[MarketplaceIntegrationStatusesHeadStatusItem]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["agent_type"] = agent_type

    params["customer_uuid"] = customer_uuid

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

    json_parent_offering_uuid: Union[Unset, str] = UNSET
    if not isinstance(parent_offering_uuid, Unset):
        json_parent_offering_uuid = str(parent_offering_uuid)
    params["parent_offering_uuid"] = json_parent_offering_uuid

    json_status: Union[Unset, list[str]] = UNSET
    if not isinstance(status, Unset):
        json_status = []
        for status_item_data in status:
            status_item = status_item_data.value
            json_status.append(status_item)

    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "head",
        "url": "/api/marketplace-integration-statuses/",
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
    agent_type: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, str] = UNSET,
    o: Union[Unset, list[MarketplaceIntegrationStatusesHeadOItem]] = UNSET,
    offering: Union[Unset, str] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    parent_offering_uuid: Union[Unset, UUID] = UNSET,
    status: Union[Unset, list[MarketplaceIntegrationStatusesHeadStatusItem]] = UNSET,
) -> Response[Any]:
    """Mixin to optimize HEAD requests for DRF views bypassing serializer processing

    Args:
        agent_type (Union[Unset, str]):
        customer_uuid (Union[Unset, str]):
        o (Union[Unset, list[MarketplaceIntegrationStatusesHeadOItem]]):
        offering (Union[Unset, str]):
        offering_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        parent_offering_uuid (Union[Unset, UUID]):
        status (Union[Unset, list[MarketplaceIntegrationStatusesHeadStatusItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        agent_type=agent_type,
        customer_uuid=customer_uuid,
        o=o,
        offering=offering,
        offering_uuid=offering_uuid,
        page=page,
        page_size=page_size,
        parent_offering_uuid=parent_offering_uuid,
        status=status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    agent_type: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, str] = UNSET,
    o: Union[Unset, list[MarketplaceIntegrationStatusesHeadOItem]] = UNSET,
    offering: Union[Unset, str] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    parent_offering_uuid: Union[Unset, UUID] = UNSET,
    status: Union[Unset, list[MarketplaceIntegrationStatusesHeadStatusItem]] = UNSET,
) -> Response[Any]:
    """Mixin to optimize HEAD requests for DRF views bypassing serializer processing

    Args:
        agent_type (Union[Unset, str]):
        customer_uuid (Union[Unset, str]):
        o (Union[Unset, list[MarketplaceIntegrationStatusesHeadOItem]]):
        offering (Union[Unset, str]):
        offering_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        parent_offering_uuid (Union[Unset, UUID]):
        status (Union[Unset, list[MarketplaceIntegrationStatusesHeadStatusItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        agent_type=agent_type,
        customer_uuid=customer_uuid,
        o=o,
        offering=offering,
        offering_uuid=offering_uuid,
        page=page,
        page_size=page_size,
        parent_offering_uuid=parent_offering_uuid,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
