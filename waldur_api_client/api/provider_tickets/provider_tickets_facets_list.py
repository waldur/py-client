from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.facet import Facet
from ...models.provider_ticket_o_enum import ProviderTicketOEnum
from ...types import UNSET, Response, Unset
from ...utils import parse_link_header


def _get_kwargs(
    *,
    facet: Union[Unset, str] = UNSET,
    facet_limit: Union[Unset, int] = UNSET,
    facet_q: Union[Unset, str] = UNSET,
    is_escalated: Union[Unset, bool] = UNSET,
    o: Union[Unset, list[ProviderTicketOEnum]] = UNSET,
    priority: Union[Unset, str] = UNSET,
    provider_assignee: Union[Unset, UUID] = UNSET,
    provider_helpdesk_uuid: Union[Unset, UUID] = UNSET,
    sla_breached: Union[Unset, bool] = UNSET,
    status: Union[Unset, str] = UNSET,
    summary: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["facet"] = facet

    params["facet_limit"] = facet_limit

    params["facet_q"] = facet_q

    params["is_escalated"] = is_escalated

    json_o: Union[Unset, list[str]] = UNSET
    if not isinstance(o, Unset):
        json_o = []
        for o_item_data in o:
            o_item = o_item_data.value
            json_o.append(o_item)

    params["o"] = json_o

    params["priority"] = priority

    json_provider_assignee: Union[Unset, str] = UNSET
    if not isinstance(provider_assignee, Unset):
        json_provider_assignee = str(provider_assignee)
    params["provider_assignee"] = json_provider_assignee

    json_provider_helpdesk_uuid: Union[Unset, str] = UNSET
    if not isinstance(provider_helpdesk_uuid, Unset):
        json_provider_helpdesk_uuid = str(provider_helpdesk_uuid)
    params["provider_helpdesk_uuid"] = json_provider_helpdesk_uuid

    params["sla_breached"] = sla_breached

    params["status"] = status

    params["summary"] = summary

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/provider-tickets/facets/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> list["Facet"]:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Facet.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[list["Facet"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    facet: Union[Unset, str] = UNSET,
    facet_limit: Union[Unset, int] = UNSET,
    facet_q: Union[Unset, str] = UNSET,
    is_escalated: Union[Unset, bool] = UNSET,
    o: Union[Unset, list[ProviderTicketOEnum]] = UNSET,
    priority: Union[Unset, str] = UNSET,
    provider_assignee: Union[Unset, UUID] = UNSET,
    provider_helpdesk_uuid: Union[Unset, UUID] = UNSET,
    sla_breached: Union[Unset, bool] = UNSET,
    status: Union[Unset, str] = UNSET,
    summary: Union[Unset, str] = UNSET,
) -> Response[list["Facet"]]:
    """Count the values each filter can still take

     Accepts the same filters as the list. Each facet is counted under every filter except its own, so
    its values are those that still have rows given the other selections and search.

    Args:
        facet (Union[Unset, str]):
        facet_limit (Union[Unset, int]):
        facet_q (Union[Unset, str]):
        is_escalated (Union[Unset, bool]):
        o (Union[Unset, list[ProviderTicketOEnum]]):
        priority (Union[Unset, str]):
        provider_assignee (Union[Unset, UUID]):
        provider_helpdesk_uuid (Union[Unset, UUID]):
        sla_breached (Union[Unset, bool]):
        status (Union[Unset, str]):
        summary (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['Facet']]
    """

    kwargs = _get_kwargs(
        facet=facet,
        facet_limit=facet_limit,
        facet_q=facet_q,
        is_escalated=is_escalated,
        o=o,
        priority=priority,
        provider_assignee=provider_assignee,
        provider_helpdesk_uuid=provider_helpdesk_uuid,
        sla_breached=sla_breached,
        status=status,
        summary=summary,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    facet: Union[Unset, str] = UNSET,
    facet_limit: Union[Unset, int] = UNSET,
    facet_q: Union[Unset, str] = UNSET,
    is_escalated: Union[Unset, bool] = UNSET,
    o: Union[Unset, list[ProviderTicketOEnum]] = UNSET,
    priority: Union[Unset, str] = UNSET,
    provider_assignee: Union[Unset, UUID] = UNSET,
    provider_helpdesk_uuid: Union[Unset, UUID] = UNSET,
    sla_breached: Union[Unset, bool] = UNSET,
    status: Union[Unset, str] = UNSET,
    summary: Union[Unset, str] = UNSET,
) -> list["Facet"]:
    """Count the values each filter can still take

     Accepts the same filters as the list. Each facet is counted under every filter except its own, so
    its values are those that still have rows given the other selections and search.

    Args:
        facet (Union[Unset, str]):
        facet_limit (Union[Unset, int]):
        facet_q (Union[Unset, str]):
        is_escalated (Union[Unset, bool]):
        o (Union[Unset, list[ProviderTicketOEnum]]):
        priority (Union[Unset, str]):
        provider_assignee (Union[Unset, UUID]):
        provider_helpdesk_uuid (Union[Unset, UUID]):
        sla_breached (Union[Unset, bool]):
        status (Union[Unset, str]):
        summary (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['Facet']
    """

    return sync_detailed(
        client=client,
        facet=facet,
        facet_limit=facet_limit,
        facet_q=facet_q,
        is_escalated=is_escalated,
        o=o,
        priority=priority,
        provider_assignee=provider_assignee,
        provider_helpdesk_uuid=provider_helpdesk_uuid,
        sla_breached=sla_breached,
        status=status,
        summary=summary,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    facet: Union[Unset, str] = UNSET,
    facet_limit: Union[Unset, int] = UNSET,
    facet_q: Union[Unset, str] = UNSET,
    is_escalated: Union[Unset, bool] = UNSET,
    o: Union[Unset, list[ProviderTicketOEnum]] = UNSET,
    priority: Union[Unset, str] = UNSET,
    provider_assignee: Union[Unset, UUID] = UNSET,
    provider_helpdesk_uuid: Union[Unset, UUID] = UNSET,
    sla_breached: Union[Unset, bool] = UNSET,
    status: Union[Unset, str] = UNSET,
    summary: Union[Unset, str] = UNSET,
) -> Response[list["Facet"]]:
    """Count the values each filter can still take

     Accepts the same filters as the list. Each facet is counted under every filter except its own, so
    its values are those that still have rows given the other selections and search.

    Args:
        facet (Union[Unset, str]):
        facet_limit (Union[Unset, int]):
        facet_q (Union[Unset, str]):
        is_escalated (Union[Unset, bool]):
        o (Union[Unset, list[ProviderTicketOEnum]]):
        priority (Union[Unset, str]):
        provider_assignee (Union[Unset, UUID]):
        provider_helpdesk_uuid (Union[Unset, UUID]):
        sla_breached (Union[Unset, bool]):
        status (Union[Unset, str]):
        summary (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['Facet']]
    """

    kwargs = _get_kwargs(
        facet=facet,
        facet_limit=facet_limit,
        facet_q=facet_q,
        is_escalated=is_escalated,
        o=o,
        priority=priority,
        provider_assignee=provider_assignee,
        provider_helpdesk_uuid=provider_helpdesk_uuid,
        sla_breached=sla_breached,
        status=status,
        summary=summary,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    facet: Union[Unset, str] = UNSET,
    facet_limit: Union[Unset, int] = UNSET,
    facet_q: Union[Unset, str] = UNSET,
    is_escalated: Union[Unset, bool] = UNSET,
    o: Union[Unset, list[ProviderTicketOEnum]] = UNSET,
    priority: Union[Unset, str] = UNSET,
    provider_assignee: Union[Unset, UUID] = UNSET,
    provider_helpdesk_uuid: Union[Unset, UUID] = UNSET,
    sla_breached: Union[Unset, bool] = UNSET,
    status: Union[Unset, str] = UNSET,
    summary: Union[Unset, str] = UNSET,
) -> list["Facet"]:
    """Count the values each filter can still take

     Accepts the same filters as the list. Each facet is counted under every filter except its own, so
    its values are those that still have rows given the other selections and search.

    Args:
        facet (Union[Unset, str]):
        facet_limit (Union[Unset, int]):
        facet_q (Union[Unset, str]):
        is_escalated (Union[Unset, bool]):
        o (Union[Unset, list[ProviderTicketOEnum]]):
        priority (Union[Unset, str]):
        provider_assignee (Union[Unset, UUID]):
        provider_helpdesk_uuid (Union[Unset, UUID]):
        sla_breached (Union[Unset, bool]):
        status (Union[Unset, str]):
        summary (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['Facet']
    """

    return (
        await asyncio_detailed(
            client=client,
            facet=facet,
            facet_limit=facet_limit,
            facet_q=facet_q,
            is_escalated=is_escalated,
            o=o,
            priority=priority,
            provider_assignee=provider_assignee,
            provider_helpdesk_uuid=provider_helpdesk_uuid,
            sla_breached=sla_breached,
            status=status,
            summary=summary,
        )
    ).parsed


def sync_all(
    *,
    client: AuthenticatedClient,
    facet: Union[Unset, str] = UNSET,
    facet_limit: Union[Unset, int] = UNSET,
    facet_q: Union[Unset, str] = UNSET,
    is_escalated: Union[Unset, bool] = UNSET,
    o: Union[Unset, list[ProviderTicketOEnum]] = UNSET,
    priority: Union[Unset, str] = UNSET,
    provider_assignee: Union[Unset, UUID] = UNSET,
    provider_helpdesk_uuid: Union[Unset, UUID] = UNSET,
    sla_breached: Union[Unset, bool] = UNSET,
    status: Union[Unset, str] = UNSET,
    summary: Union[Unset, str] = UNSET,
) -> list["Facet"]:
    """Get All Pages

     Fetch all pages of paginated results. This function automatically handles pagination
     by following the 'next' link in the Link header until all results are retrieved.

     Note: page_size will be set to 100 (the maximum allowed) automatically.

    Args:
        facet (Union[Unset, str]):
        facet_limit (Union[Unset, int]):
        facet_q (Union[Unset, str]):
        is_escalated (Union[Unset, bool]):
        o (Union[Unset, list[ProviderTicketOEnum]]):
        priority (Union[Unset, str]):
        provider_assignee (Union[Unset, UUID]):
        provider_helpdesk_uuid (Union[Unset, UUID]):
        sla_breached (Union[Unset, bool]):
        status (Union[Unset, str]):
        summary (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['Facet']: Combined results from all pages
    """
    from urllib.parse import parse_qs, urlparse

    all_results: list[Facet] = []

    # Get initial request kwargs
    kwargs = _get_kwargs(
        facet=facet,
        facet_limit=facet_limit,
        facet_q=facet_q,
        is_escalated=is_escalated,
        o=o,
        priority=priority,
        provider_assignee=provider_assignee,
        provider_helpdesk_uuid=provider_helpdesk_uuid,
        sla_breached=sla_breached,
        status=status,
        summary=summary,
    )

    # Set page_size to maximum
    if "params" not in kwargs:
        kwargs["params"] = {}
    kwargs["params"]["page_size"] = 100

    # Make initial request
    response = client.get_httpx_client().request(**kwargs)
    parsed_response = _parse_response(client=client, response=response)

    if parsed_response:
        all_results.extend(parsed_response)

    # Follow pagination links
    while True:
        link_header = response.headers.get("Link", "")
        links = parse_link_header(link_header)

        if "next" not in links:
            break

        # Extract page number from next URL
        next_url = links["next"]
        parsed_url = urlparse(next_url)
        next_params = parse_qs(parsed_url.query)

        if "page" not in next_params:
            break

        # Update only the page parameter, keep all other params
        page_number = next_params["page"][0]
        kwargs["params"]["page"] = page_number

        # Fetch next page
        response = client.get_httpx_client().request(**kwargs)
        parsed_response = _parse_response(client=client, response=response)

        if parsed_response:
            all_results.extend(parsed_response)

    return all_results


async def asyncio_all(
    *,
    client: AuthenticatedClient,
    facet: Union[Unset, str] = UNSET,
    facet_limit: Union[Unset, int] = UNSET,
    facet_q: Union[Unset, str] = UNSET,
    is_escalated: Union[Unset, bool] = UNSET,
    o: Union[Unset, list[ProviderTicketOEnum]] = UNSET,
    priority: Union[Unset, str] = UNSET,
    provider_assignee: Union[Unset, UUID] = UNSET,
    provider_helpdesk_uuid: Union[Unset, UUID] = UNSET,
    sla_breached: Union[Unset, bool] = UNSET,
    status: Union[Unset, str] = UNSET,
    summary: Union[Unset, str] = UNSET,
) -> list["Facet"]:
    """Get All Pages (Async)

     Fetch all pages of paginated results asynchronously. This function automatically handles pagination
     by following the 'next' link in the Link header until all results are retrieved.

     Note: page_size will be set to 100 (the maximum allowed) automatically.

    Args:
        facet (Union[Unset, str]):
        facet_limit (Union[Unset, int]):
        facet_q (Union[Unset, str]):
        is_escalated (Union[Unset, bool]):
        o (Union[Unset, list[ProviderTicketOEnum]]):
        priority (Union[Unset, str]):
        provider_assignee (Union[Unset, UUID]):
        provider_helpdesk_uuid (Union[Unset, UUID]):
        sla_breached (Union[Unset, bool]):
        status (Union[Unset, str]):
        summary (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['Facet']: Combined results from all pages
    """
    from urllib.parse import parse_qs, urlparse

    all_results: list[Facet] = []

    # Get initial request kwargs
    kwargs = _get_kwargs(
        facet=facet,
        facet_limit=facet_limit,
        facet_q=facet_q,
        is_escalated=is_escalated,
        o=o,
        priority=priority,
        provider_assignee=provider_assignee,
        provider_helpdesk_uuid=provider_helpdesk_uuid,
        sla_breached=sla_breached,
        status=status,
        summary=summary,
    )

    # Set page_size to maximum
    if "params" not in kwargs:
        kwargs["params"] = {}
    kwargs["params"]["page_size"] = 100

    # Make initial request
    response = await client.get_async_httpx_client().request(**kwargs)
    parsed_response = _parse_response(client=client, response=response)

    if parsed_response:
        all_results.extend(parsed_response)

    # Follow pagination links
    while True:
        link_header = response.headers.get("Link", "")
        links = parse_link_header(link_header)

        if "next" not in links:
            break

        # Extract page number from next URL
        next_url = links["next"]
        parsed_url = urlparse(next_url)
        next_params = parse_qs(parsed_url.query)

        if "page" not in next_params:
            break

        # Update only the page parameter, keep all other params
        page_number = next_params["page"][0]
        kwargs["params"]["page"] = page_number

        # Fetch next page
        response = await client.get_async_httpx_client().request(**kwargs)
        parsed_response = _parse_response(client=client, response=response)

        if parsed_response:
            all_results.extend(parsed_response)

    return all_results
