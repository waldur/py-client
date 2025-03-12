from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.proposal_proposals_resources_list_o_item import ProposalProposalsResourcesListOItem
from ...models.proposal_proposals_resources_list_state_item import ProposalProposalsResourcesListStateItem
from ...models.requested_resource import RequestedResource
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    call_uuid: Union[Unset, UUID] = UNSET,
    name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[ProposalProposalsResourcesListOItem]] = UNSET,
    organization_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    round_: Union[Unset, UUID] = UNSET,
    state: Union[Unset, list[ProposalProposalsResourcesListStateItem]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_call_uuid: Union[Unset, str] = UNSET
    if not isinstance(call_uuid, Unset):
        json_call_uuid = str(call_uuid)
    params["call_uuid"] = json_call_uuid

    params["name"] = name

    json_o: Union[Unset, list[str]] = UNSET
    if not isinstance(o, Unset):
        json_o = []
        for o_item_data in o:
            o_item = o_item_data.value
            json_o.append(o_item)

    params["o"] = json_o

    json_organization_uuid: Union[Unset, str] = UNSET
    if not isinstance(organization_uuid, Unset):
        json_organization_uuid = str(organization_uuid)
    params["organization_uuid"] = json_organization_uuid

    params["page"] = page

    params["page_size"] = page_size

    json_round_: Union[Unset, str] = UNSET
    if not isinstance(round_, Unset):
        json_round_ = str(round_)
    params["round"] = json_round_

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
        "url": f"/api/proposal-proposals/{uuid}/resources/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["RequestedResource"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_paginated_requested_resource_list_item_data in _response_200:
            componentsschemas_paginated_requested_resource_list_item = RequestedResource.from_dict(
                componentsschemas_paginated_requested_resource_list_item_data
            )

            response_200.append(componentsschemas_paginated_requested_resource_list_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["RequestedResource"]]:
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
    call_uuid: Union[Unset, UUID] = UNSET,
    name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[ProposalProposalsResourcesListOItem]] = UNSET,
    organization_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    round_: Union[Unset, UUID] = UNSET,
    state: Union[Unset, list[ProposalProposalsResourcesListStateItem]] = UNSET,
) -> Response[list["RequestedResource"]]:
    """List resources for a proposal.

    Args:
        uuid (UUID):
        call_uuid (Union[Unset, UUID]):
        name (Union[Unset, str]):
        o (Union[Unset, list[ProposalProposalsResourcesListOItem]]):
        organization_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        round_ (Union[Unset, UUID]):
        state (Union[Unset, list[ProposalProposalsResourcesListStateItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['RequestedResource']]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        call_uuid=call_uuid,
        name=name,
        o=o,
        organization_uuid=organization_uuid,
        page=page,
        page_size=page_size,
        round_=round_,
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
    call_uuid: Union[Unset, UUID] = UNSET,
    name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[ProposalProposalsResourcesListOItem]] = UNSET,
    organization_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    round_: Union[Unset, UUID] = UNSET,
    state: Union[Unset, list[ProposalProposalsResourcesListStateItem]] = UNSET,
) -> Optional[list["RequestedResource"]]:
    """List resources for a proposal.

    Args:
        uuid (UUID):
        call_uuid (Union[Unset, UUID]):
        name (Union[Unset, str]):
        o (Union[Unset, list[ProposalProposalsResourcesListOItem]]):
        organization_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        round_ (Union[Unset, UUID]):
        state (Union[Unset, list[ProposalProposalsResourcesListStateItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['RequestedResource']
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        call_uuid=call_uuid,
        name=name,
        o=o,
        organization_uuid=organization_uuid,
        page=page,
        page_size=page_size,
        round_=round_,
        state=state,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    call_uuid: Union[Unset, UUID] = UNSET,
    name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[ProposalProposalsResourcesListOItem]] = UNSET,
    organization_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    round_: Union[Unset, UUID] = UNSET,
    state: Union[Unset, list[ProposalProposalsResourcesListStateItem]] = UNSET,
) -> Response[list["RequestedResource"]]:
    """List resources for a proposal.

    Args:
        uuid (UUID):
        call_uuid (Union[Unset, UUID]):
        name (Union[Unset, str]):
        o (Union[Unset, list[ProposalProposalsResourcesListOItem]]):
        organization_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        round_ (Union[Unset, UUID]):
        state (Union[Unset, list[ProposalProposalsResourcesListStateItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['RequestedResource']]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        call_uuid=call_uuid,
        name=name,
        o=o,
        organization_uuid=organization_uuid,
        page=page,
        page_size=page_size,
        round_=round_,
        state=state,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    call_uuid: Union[Unset, UUID] = UNSET,
    name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[ProposalProposalsResourcesListOItem]] = UNSET,
    organization_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    round_: Union[Unset, UUID] = UNSET,
    state: Union[Unset, list[ProposalProposalsResourcesListStateItem]] = UNSET,
) -> Optional[list["RequestedResource"]]:
    """List resources for a proposal.

    Args:
        uuid (UUID):
        call_uuid (Union[Unset, UUID]):
        name (Union[Unset, str]):
        o (Union[Unset, list[ProposalProposalsResourcesListOItem]]):
        organization_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        round_ (Union[Unset, UUID]):
        state (Union[Unset, list[ProposalProposalsResourcesListStateItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['RequestedResource']
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            call_uuid=call_uuid,
            name=name,
            o=o,
            organization_uuid=organization_uuid,
            page=page,
            page_size=page_size,
            round_=round_,
            state=state,
        )
    ).parsed
