from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.proposal_requested_offerings_count_o_item import ProposalRequestedOfferingsCountOItem
from ...models.proposal_requested_offerings_count_state_item import ProposalRequestedOfferingsCountStateItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    call: Union[Unset, str] = UNSET,
    call_uuid: Union[Unset, UUID] = UNSET,
    o: Union[Unset, list[ProposalRequestedOfferingsCountOItem]] = UNSET,
    offering: Union[Unset, str] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    organization_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    provider_uuid: Union[Unset, UUID] = UNSET,
    state: Union[Unset, list[ProposalRequestedOfferingsCountStateItem]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["call"] = call

    json_call_uuid: Union[Unset, str] = UNSET
    if not isinstance(call_uuid, Unset):
        json_call_uuid = str(call_uuid)
    params["call_uuid"] = json_call_uuid

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

    json_organization_uuid: Union[Unset, str] = UNSET
    if not isinstance(organization_uuid, Unset):
        json_organization_uuid = str(organization_uuid)
    params["organization_uuid"] = json_organization_uuid

    params["page"] = page

    params["page_size"] = page_size

    json_provider_uuid: Union[Unset, str] = UNSET
    if not isinstance(provider_uuid, Unset):
        json_provider_uuid = str(provider_uuid)
    params["provider_uuid"] = json_provider_uuid

    json_state: Union[Unset, list[str]] = UNSET
    if not isinstance(state, Unset):
        json_state = []
        for state_item_data in state:
            state_item = state_item_data.value
            json_state.append(state_item)

    params["state"] = json_state

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "head",
        "url": "/api/proposal-requested-offerings/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> int:
    if response.status_code == HTTPStatus.OK:
        try:
            return int(response.headers["x-result-count"])
        except KeyError:
            raise errors.UnexpectedStatus(
                response.status_code, b"Expected 'X-Result-Count' header for HEAD request, but it was not found."
            )
        except ValueError:
            count_val = response.headers.get("x-result-count")
            msg = f"Expected 'X-Result-Count' header to be an integer, but got '{count_val}'."
            raise errors.UnexpectedStatus(response.status_code, msg.encode())
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[int]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    call: Union[Unset, str] = UNSET,
    call_uuid: Union[Unset, UUID] = UNSET,
    o: Union[Unset, list[ProposalRequestedOfferingsCountOItem]] = UNSET,
    offering: Union[Unset, str] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    organization_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    provider_uuid: Union[Unset, UUID] = UNSET,
    state: Union[Unset, list[ProposalRequestedOfferingsCountStateItem]] = UNSET,
) -> Response[int]:
    """Get number of items in the collection matching the request parameters.

    Args:
        call (Union[Unset, str]):
        call_uuid (Union[Unset, UUID]):
        o (Union[Unset, list[ProposalRequestedOfferingsCountOItem]]):
        offering (Union[Unset, str]):
        offering_uuid (Union[Unset, UUID]):
        organization_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        provider_uuid (Union[Unset, UUID]):
        state (Union[Unset, list[ProposalRequestedOfferingsCountStateItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[int]
    """

    kwargs = _get_kwargs(
        call=call,
        call_uuid=call_uuid,
        o=o,
        offering=offering,
        offering_uuid=offering_uuid,
        organization_uuid=organization_uuid,
        page=page,
        page_size=page_size,
        provider_uuid=provider_uuid,
        state=state,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    call: Union[Unset, str] = UNSET,
    call_uuid: Union[Unset, UUID] = UNSET,
    o: Union[Unset, list[ProposalRequestedOfferingsCountOItem]] = UNSET,
    offering: Union[Unset, str] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    organization_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    provider_uuid: Union[Unset, UUID] = UNSET,
    state: Union[Unset, list[ProposalRequestedOfferingsCountStateItem]] = UNSET,
) -> int:
    """Get number of items in the collection matching the request parameters.

    Args:
        call (Union[Unset, str]):
        call_uuid (Union[Unset, UUID]):
        o (Union[Unset, list[ProposalRequestedOfferingsCountOItem]]):
        offering (Union[Unset, str]):
        offering_uuid (Union[Unset, UUID]):
        organization_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        provider_uuid (Union[Unset, UUID]):
        state (Union[Unset, list[ProposalRequestedOfferingsCountStateItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        int
    """

    return sync_detailed(
        client=client,
        call=call,
        call_uuid=call_uuid,
        o=o,
        offering=offering,
        offering_uuid=offering_uuid,
        organization_uuid=organization_uuid,
        page=page,
        page_size=page_size,
        provider_uuid=provider_uuid,
        state=state,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    call: Union[Unset, str] = UNSET,
    call_uuid: Union[Unset, UUID] = UNSET,
    o: Union[Unset, list[ProposalRequestedOfferingsCountOItem]] = UNSET,
    offering: Union[Unset, str] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    organization_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    provider_uuid: Union[Unset, UUID] = UNSET,
    state: Union[Unset, list[ProposalRequestedOfferingsCountStateItem]] = UNSET,
) -> Response[int]:
    """Get number of items in the collection matching the request parameters.

    Args:
        call (Union[Unset, str]):
        call_uuid (Union[Unset, UUID]):
        o (Union[Unset, list[ProposalRequestedOfferingsCountOItem]]):
        offering (Union[Unset, str]):
        offering_uuid (Union[Unset, UUID]):
        organization_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        provider_uuid (Union[Unset, UUID]):
        state (Union[Unset, list[ProposalRequestedOfferingsCountStateItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[int]
    """

    kwargs = _get_kwargs(
        call=call,
        call_uuid=call_uuid,
        o=o,
        offering=offering,
        offering_uuid=offering_uuid,
        organization_uuid=organization_uuid,
        page=page,
        page_size=page_size,
        provider_uuid=provider_uuid,
        state=state,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    call: Union[Unset, str] = UNSET,
    call_uuid: Union[Unset, UUID] = UNSET,
    o: Union[Unset, list[ProposalRequestedOfferingsCountOItem]] = UNSET,
    offering: Union[Unset, str] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    organization_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    provider_uuid: Union[Unset, UUID] = UNSET,
    state: Union[Unset, list[ProposalRequestedOfferingsCountStateItem]] = UNSET,
) -> int:
    """Get number of items in the collection matching the request parameters.

    Args:
        call (Union[Unset, str]):
        call_uuid (Union[Unset, UUID]):
        o (Union[Unset, list[ProposalRequestedOfferingsCountOItem]]):
        offering (Union[Unset, str]):
        offering_uuid (Union[Unset, UUID]):
        organization_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        provider_uuid (Union[Unset, UUID]):
        state (Union[Unset, list[ProposalRequestedOfferingsCountStateItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        int
    """

    return (
        await asyncio_detailed(
            client=client,
            call=call,
            call_uuid=call_uuid,
            o=o,
            offering=offering,
            offering_uuid=offering_uuid,
            organization_uuid=organization_uuid,
            page=page,
            page_size=page_size,
            provider_uuid=provider_uuid,
            state=state,
        )
    ).parsed
