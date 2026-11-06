from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.proposal_role_candidate import ProposalRoleCandidate
from ...types import UNSET, Response, Unset
from ...utils import parse_link_header


def _get_kwargs(
    uuid: UUID,
    *,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
    role_uuid: UUID,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["page_size"] = page_size

    params["query"] = query

    json_role_uuid = str(role_uuid)
    params["role_uuid"] = json_role_uuid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/proposal-proposals/{uuid}/role_assignment_candidates/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> list["ProposalRoleCandidate"]:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ProposalRoleCandidate.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["ProposalRoleCandidate"]]:
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
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
    role_uuid: UUID,
) -> Response[list["ProposalRoleCandidate"]]:
    """Users who may hold the role on the proposal by its eligibility, at most 50 (10 for a role any user
    may hold), with whether they can be assigned: a conflict of interest on record or another evaluator
    role on the proposal rules them out. The applicant team is left out. Email, and whether a conflict
    is on record, are shown to staff and those overseeing the call only -- email for a role any user may
    hold to staff only; anyone else finds a user by email only by their whole address. For whoever may
    assign the role.

    Args:
        uuid (UUID):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        query (Union[Unset, str]):
        role_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['ProposalRoleCandidate']]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        page=page,
        page_size=page_size,
        query=query,
        role_uuid=role_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
    role_uuid: UUID,
) -> list["ProposalRoleCandidate"]:
    """Users who may hold the role on the proposal by its eligibility, at most 50 (10 for a role any user
    may hold), with whether they can be assigned: a conflict of interest on record or another evaluator
    role on the proposal rules them out. The applicant team is left out. Email, and whether a conflict
    is on record, are shown to staff and those overseeing the call only -- email for a role any user may
    hold to staff only; anyone else finds a user by email only by their whole address. For whoever may
    assign the role.

    Args:
        uuid (UUID):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        query (Union[Unset, str]):
        role_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['ProposalRoleCandidate']
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        page=page,
        page_size=page_size,
        query=query,
        role_uuid=role_uuid,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
    role_uuid: UUID,
) -> Response[list["ProposalRoleCandidate"]]:
    """Users who may hold the role on the proposal by its eligibility, at most 50 (10 for a role any user
    may hold), with whether they can be assigned: a conflict of interest on record or another evaluator
    role on the proposal rules them out. The applicant team is left out. Email, and whether a conflict
    is on record, are shown to staff and those overseeing the call only -- email for a role any user may
    hold to staff only; anyone else finds a user by email only by their whole address. For whoever may
    assign the role.

    Args:
        uuid (UUID):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        query (Union[Unset, str]):
        role_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['ProposalRoleCandidate']]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        page=page,
        page_size=page_size,
        query=query,
        role_uuid=role_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
    role_uuid: UUID,
) -> list["ProposalRoleCandidate"]:
    """Users who may hold the role on the proposal by its eligibility, at most 50 (10 for a role any user
    may hold), with whether they can be assigned: a conflict of interest on record or another evaluator
    role on the proposal rules them out. The applicant team is left out. Email, and whether a conflict
    is on record, are shown to staff and those overseeing the call only -- email for a role any user may
    hold to staff only; anyone else finds a user by email only by their whole address. For whoever may
    assign the role.

    Args:
        uuid (UUID):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        query (Union[Unset, str]):
        role_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['ProposalRoleCandidate']
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            page=page,
            page_size=page_size,
            query=query,
            role_uuid=role_uuid,
        )
    ).parsed


def sync_all(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    query: Union[Unset, str] = UNSET,
    role_uuid: UUID,
) -> list["ProposalRoleCandidate"]:
    """Get All Pages

     Fetch all pages of paginated results. This function automatically handles pagination
     by following the 'next' link in the Link header until all results are retrieved.

     Note: page_size will be set to 100 (the maximum allowed) automatically.

    Args:
        uuid (UUID):
        query (Union[Unset, str]):
        role_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['ProposalRoleCandidate']: Combined results from all pages
    """
    from urllib.parse import parse_qs, urlparse

    all_results: list[ProposalRoleCandidate] = []

    # Get initial request kwargs
    kwargs = _get_kwargs(
        uuid=uuid,
        query=query,
        role_uuid=role_uuid,
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
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    query: Union[Unset, str] = UNSET,
    role_uuid: UUID,
) -> list["ProposalRoleCandidate"]:
    """Get All Pages (Async)

     Fetch all pages of paginated results asynchronously. This function automatically handles pagination
     by following the 'next' link in the Link header until all results are retrieved.

     Note: page_size will be set to 100 (the maximum allowed) automatically.

    Args:
        uuid (UUID):
        query (Union[Unset, str]):
        role_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['ProposalRoleCandidate']: Combined results from all pages
    """
    from urllib.parse import parse_qs, urlparse

    all_results: list[ProposalRoleCandidate] = []

    # Get initial request kwargs
    kwargs = _get_kwargs(
        uuid=uuid,
        query=query,
        role_uuid=role_uuid,
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
