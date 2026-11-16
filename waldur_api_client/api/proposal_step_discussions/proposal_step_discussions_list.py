from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.step_discussion import StepDiscussion
from ...models.step_discussion_state_enum_1 import StepDiscussionStateEnum1
from ...types import UNSET, Response, Unset
from ...utils import parse_link_header


def _get_kwargs(
    *,
    call_step_uuid: Union[Unset, UUID] = UNSET,
    call_uuid: Union[Unset, UUID] = UNSET,
    mine: Union[Unset, bool] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    proposal_uuid: Union[Unset, UUID] = UNSET,
    round_uuid: Union[Unset, UUID] = UNSET,
    state: Union[Unset, StepDiscussionStateEnum1] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_call_step_uuid: Union[Unset, str] = UNSET
    if not isinstance(call_step_uuid, Unset):
        json_call_step_uuid = str(call_step_uuid)
    params["call_step_uuid"] = json_call_step_uuid

    json_call_uuid: Union[Unset, str] = UNSET
    if not isinstance(call_uuid, Unset):
        json_call_uuid = str(call_uuid)
    params["call_uuid"] = json_call_uuid

    params["mine"] = mine

    params["page"] = page

    params["page_size"] = page_size

    json_proposal_uuid: Union[Unset, str] = UNSET
    if not isinstance(proposal_uuid, Unset):
        json_proposal_uuid = str(proposal_uuid)
    params["proposal_uuid"] = json_proposal_uuid

    json_round_uuid: Union[Unset, str] = UNSET
    if not isinstance(round_uuid, Unset):
        json_round_uuid = str(round_uuid)
    params["round_uuid"] = json_round_uuid

    json_state: Union[Unset, str] = UNSET
    if not isinstance(state, Unset):
        json_state = state.value

    params["state"] = json_state

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/proposal-step-discussions/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> list["StepDiscussion"]:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = StepDiscussion.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["StepDiscussion"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    call_step_uuid: Union[Unset, UUID] = UNSET,
    call_uuid: Union[Unset, UUID] = UNSET,
    mine: Union[Unset, bool] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    proposal_uuid: Union[Unset, UUID] = UNSET,
    round_uuid: Union[Unset, UUID] = UNSET,
    state: Union[Unset, StepDiscussionStateEnum1] = UNSET,
) -> Response[list["StepDiscussion"]]:
    """
    Args:
        call_step_uuid (Union[Unset, UUID]):
        call_uuid (Union[Unset, UUID]):
        mine (Union[Unset, bool]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        proposal_uuid (Union[Unset, UUID]):
        round_uuid (Union[Unset, UUID]):
        state (Union[Unset, StepDiscussionStateEnum1]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['StepDiscussion']]
    """

    kwargs = _get_kwargs(
        call_step_uuid=call_step_uuid,
        call_uuid=call_uuid,
        mine=mine,
        page=page,
        page_size=page_size,
        proposal_uuid=proposal_uuid,
        round_uuid=round_uuid,
        state=state,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    call_step_uuid: Union[Unset, UUID] = UNSET,
    call_uuid: Union[Unset, UUID] = UNSET,
    mine: Union[Unset, bool] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    proposal_uuid: Union[Unset, UUID] = UNSET,
    round_uuid: Union[Unset, UUID] = UNSET,
    state: Union[Unset, StepDiscussionStateEnum1] = UNSET,
) -> list["StepDiscussion"]:
    """
    Args:
        call_step_uuid (Union[Unset, UUID]):
        call_uuid (Union[Unset, UUID]):
        mine (Union[Unset, bool]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        proposal_uuid (Union[Unset, UUID]):
        round_uuid (Union[Unset, UUID]):
        state (Union[Unset, StepDiscussionStateEnum1]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['StepDiscussion']
    """

    return sync_detailed(
        client=client,
        call_step_uuid=call_step_uuid,
        call_uuid=call_uuid,
        mine=mine,
        page=page,
        page_size=page_size,
        proposal_uuid=proposal_uuid,
        round_uuid=round_uuid,
        state=state,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    call_step_uuid: Union[Unset, UUID] = UNSET,
    call_uuid: Union[Unset, UUID] = UNSET,
    mine: Union[Unset, bool] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    proposal_uuid: Union[Unset, UUID] = UNSET,
    round_uuid: Union[Unset, UUID] = UNSET,
    state: Union[Unset, StepDiscussionStateEnum1] = UNSET,
) -> Response[list["StepDiscussion"]]:
    """
    Args:
        call_step_uuid (Union[Unset, UUID]):
        call_uuid (Union[Unset, UUID]):
        mine (Union[Unset, bool]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        proposal_uuid (Union[Unset, UUID]):
        round_uuid (Union[Unset, UUID]):
        state (Union[Unset, StepDiscussionStateEnum1]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['StepDiscussion']]
    """

    kwargs = _get_kwargs(
        call_step_uuid=call_step_uuid,
        call_uuid=call_uuid,
        mine=mine,
        page=page,
        page_size=page_size,
        proposal_uuid=proposal_uuid,
        round_uuid=round_uuid,
        state=state,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    call_step_uuid: Union[Unset, UUID] = UNSET,
    call_uuid: Union[Unset, UUID] = UNSET,
    mine: Union[Unset, bool] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    proposal_uuid: Union[Unset, UUID] = UNSET,
    round_uuid: Union[Unset, UUID] = UNSET,
    state: Union[Unset, StepDiscussionStateEnum1] = UNSET,
) -> list["StepDiscussion"]:
    """
    Args:
        call_step_uuid (Union[Unset, UUID]):
        call_uuid (Union[Unset, UUID]):
        mine (Union[Unset, bool]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        proposal_uuid (Union[Unset, UUID]):
        round_uuid (Union[Unset, UUID]):
        state (Union[Unset, StepDiscussionStateEnum1]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['StepDiscussion']
    """

    return (
        await asyncio_detailed(
            client=client,
            call_step_uuid=call_step_uuid,
            call_uuid=call_uuid,
            mine=mine,
            page=page,
            page_size=page_size,
            proposal_uuid=proposal_uuid,
            round_uuid=round_uuid,
            state=state,
        )
    ).parsed


def sync_all(
    *,
    client: AuthenticatedClient,
    call_step_uuid: Union[Unset, UUID] = UNSET,
    call_uuid: Union[Unset, UUID] = UNSET,
    mine: Union[Unset, bool] = UNSET,
    proposal_uuid: Union[Unset, UUID] = UNSET,
    round_uuid: Union[Unset, UUID] = UNSET,
    state: Union[Unset, StepDiscussionStateEnum1] = UNSET,
) -> list["StepDiscussion"]:
    """Get All Pages

     Fetch all pages of paginated results. This function automatically handles pagination
     by following the 'next' link in the Link header until all results are retrieved.

     Note: page_size will be set to 100 (the maximum allowed) automatically.

    Args:
        call_step_uuid (Union[Unset, UUID]):
        call_uuid (Union[Unset, UUID]):
        mine (Union[Unset, bool]):
        proposal_uuid (Union[Unset, UUID]):
        round_uuid (Union[Unset, UUID]):
        state (Union[Unset, StepDiscussionStateEnum1]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['StepDiscussion']: Combined results from all pages
    """
    from urllib.parse import parse_qs, urlparse

    all_results: list[StepDiscussion] = []

    # Get initial request kwargs
    kwargs = _get_kwargs(
        call_step_uuid=call_step_uuid,
        call_uuid=call_uuid,
        mine=mine,
        proposal_uuid=proposal_uuid,
        round_uuid=round_uuid,
        state=state,
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
    call_step_uuid: Union[Unset, UUID] = UNSET,
    call_uuid: Union[Unset, UUID] = UNSET,
    mine: Union[Unset, bool] = UNSET,
    proposal_uuid: Union[Unset, UUID] = UNSET,
    round_uuid: Union[Unset, UUID] = UNSET,
    state: Union[Unset, StepDiscussionStateEnum1] = UNSET,
) -> list["StepDiscussion"]:
    """Get All Pages (Async)

     Fetch all pages of paginated results asynchronously. This function automatically handles pagination
     by following the 'next' link in the Link header until all results are retrieved.

     Note: page_size will be set to 100 (the maximum allowed) automatically.

    Args:
        call_step_uuid (Union[Unset, UUID]):
        call_uuid (Union[Unset, UUID]):
        mine (Union[Unset, bool]):
        proposal_uuid (Union[Unset, UUID]):
        round_uuid (Union[Unset, UUID]):
        state (Union[Unset, StepDiscussionStateEnum1]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['StepDiscussion']: Combined results from all pages
    """
    from urllib.parse import parse_qs, urlparse

    all_results: list[StepDiscussion] = []

    # Get initial request kwargs
    kwargs = _get_kwargs(
        call_step_uuid=call_step_uuid,
        call_uuid=call_uuid,
        mine=mine,
        proposal_uuid=proposal_uuid,
        round_uuid=round_uuid,
        state=state,
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
