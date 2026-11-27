from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.provider_site_agent_offering_config import ProviderSiteAgentOfferingConfig
from ...types import UNSET, Response, Unset
from ...utils import parse_link_header


def _get_kwargs(
    uuid: UUID,
    *,
    backend_id: Union[Unset, str] = UNSET,
    backend_id_startswith: Union[Unset, str] = UNSET,
    offering_uuid: Union[Unset, list[UUID]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["backend_id"] = backend_id

    params["backend_id_startswith"] = backend_id_startswith

    json_offering_uuid: Union[Unset, list[str]] = UNSET
    if not isinstance(offering_uuid, Unset):
        json_offering_uuid = []
        for offering_uuid_item_data in offering_uuid:
            offering_uuid_item = str(offering_uuid_item_data)
            json_offering_uuid.append(offering_uuid_item)

    params["offering_uuid"] = json_offering_uuid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/marketplace-service-providers/{uuid}/site_agent_config/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> list["ProviderSiteAgentOfferingConfig"]:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ProviderSiteAgentOfferingConfig.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["ProviderSiteAgentOfferingConfig"]]:
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
    backend_id: Union[Unset, str] = UNSET,
    backend_id_startswith: Union[Unset, str] = UNSET,
    offering_uuid: Union[Unset, list[UUID]] = UNSET,
) -> Response[list["ProviderSiteAgentOfferingConfig"]]:
    """Site agent configuration of the service provider's offerings

     For each site agent offering of the service provider that the filters select, the block the
    offering's own site_agent_config returns: its configuration without secrets, the backend secrets the
    agent keeps in its own configuration, and the version. backend_id matches exactly and
    backend_id_startswith by prefix, such as every offering of one cluster; archived offerings are left
    out of those. Without filters, every site agent offering. Who may generate the provider's
    configuration file gets every offering; anyone else, such as a site agent whose token is bound to
    some of the offerings, only those whose own site_agent_config they may read.

    Args:
        uuid (UUID):
        backend_id (Union[Unset, str]):
        backend_id_startswith (Union[Unset, str]):
        offering_uuid (Union[Unset, list[UUID]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['ProviderSiteAgentOfferingConfig']]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        backend_id=backend_id,
        backend_id_startswith=backend_id_startswith,
        offering_uuid=offering_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    backend_id: Union[Unset, str] = UNSET,
    backend_id_startswith: Union[Unset, str] = UNSET,
    offering_uuid: Union[Unset, list[UUID]] = UNSET,
) -> list["ProviderSiteAgentOfferingConfig"]:
    """Site agent configuration of the service provider's offerings

     For each site agent offering of the service provider that the filters select, the block the
    offering's own site_agent_config returns: its configuration without secrets, the backend secrets the
    agent keeps in its own configuration, and the version. backend_id matches exactly and
    backend_id_startswith by prefix, such as every offering of one cluster; archived offerings are left
    out of those. Without filters, every site agent offering. Who may generate the provider's
    configuration file gets every offering; anyone else, such as a site agent whose token is bound to
    some of the offerings, only those whose own site_agent_config they may read.

    Args:
        uuid (UUID):
        backend_id (Union[Unset, str]):
        backend_id_startswith (Union[Unset, str]):
        offering_uuid (Union[Unset, list[UUID]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['ProviderSiteAgentOfferingConfig']
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        backend_id=backend_id,
        backend_id_startswith=backend_id_startswith,
        offering_uuid=offering_uuid,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    backend_id: Union[Unset, str] = UNSET,
    backend_id_startswith: Union[Unset, str] = UNSET,
    offering_uuid: Union[Unset, list[UUID]] = UNSET,
) -> Response[list["ProviderSiteAgentOfferingConfig"]]:
    """Site agent configuration of the service provider's offerings

     For each site agent offering of the service provider that the filters select, the block the
    offering's own site_agent_config returns: its configuration without secrets, the backend secrets the
    agent keeps in its own configuration, and the version. backend_id matches exactly and
    backend_id_startswith by prefix, such as every offering of one cluster; archived offerings are left
    out of those. Without filters, every site agent offering. Who may generate the provider's
    configuration file gets every offering; anyone else, such as a site agent whose token is bound to
    some of the offerings, only those whose own site_agent_config they may read.

    Args:
        uuid (UUID):
        backend_id (Union[Unset, str]):
        backend_id_startswith (Union[Unset, str]):
        offering_uuid (Union[Unset, list[UUID]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['ProviderSiteAgentOfferingConfig']]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        backend_id=backend_id,
        backend_id_startswith=backend_id_startswith,
        offering_uuid=offering_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    backend_id: Union[Unset, str] = UNSET,
    backend_id_startswith: Union[Unset, str] = UNSET,
    offering_uuid: Union[Unset, list[UUID]] = UNSET,
) -> list["ProviderSiteAgentOfferingConfig"]:
    """Site agent configuration of the service provider's offerings

     For each site agent offering of the service provider that the filters select, the block the
    offering's own site_agent_config returns: its configuration without secrets, the backend secrets the
    agent keeps in its own configuration, and the version. backend_id matches exactly and
    backend_id_startswith by prefix, such as every offering of one cluster; archived offerings are left
    out of those. Without filters, every site agent offering. Who may generate the provider's
    configuration file gets every offering; anyone else, such as a site agent whose token is bound to
    some of the offerings, only those whose own site_agent_config they may read.

    Args:
        uuid (UUID):
        backend_id (Union[Unset, str]):
        backend_id_startswith (Union[Unset, str]):
        offering_uuid (Union[Unset, list[UUID]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['ProviderSiteAgentOfferingConfig']
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            backend_id=backend_id,
            backend_id_startswith=backend_id_startswith,
            offering_uuid=offering_uuid,
        )
    ).parsed


def sync_all(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    backend_id: Union[Unset, str] = UNSET,
    backend_id_startswith: Union[Unset, str] = UNSET,
    offering_uuid: Union[Unset, list[UUID]] = UNSET,
) -> list["ProviderSiteAgentOfferingConfig"]:
    """Get All Pages

     Fetch all pages of paginated results. This function automatically handles pagination
     by following the 'next' link in the Link header until all results are retrieved.

     Note: page_size will be set to 100 (the maximum allowed) automatically.

    Args:
        uuid (UUID):
        backend_id (Union[Unset, str]):
        backend_id_startswith (Union[Unset, str]):
        offering_uuid (Union[Unset, list[UUID]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['ProviderSiteAgentOfferingConfig']: Combined results from all pages
    """
    from urllib.parse import parse_qs, urlparse

    all_results: list[ProviderSiteAgentOfferingConfig] = []

    # Get initial request kwargs
    kwargs = _get_kwargs(
        uuid=uuid,
        backend_id=backend_id,
        backend_id_startswith=backend_id_startswith,
        offering_uuid=offering_uuid,
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
    backend_id: Union[Unset, str] = UNSET,
    backend_id_startswith: Union[Unset, str] = UNSET,
    offering_uuid: Union[Unset, list[UUID]] = UNSET,
) -> list["ProviderSiteAgentOfferingConfig"]:
    """Get All Pages (Async)

     Fetch all pages of paginated results asynchronously. This function automatically handles pagination
     by following the 'next' link in the Link header until all results are retrieved.

     Note: page_size will be set to 100 (the maximum allowed) automatically.

    Args:
        uuid (UUID):
        backend_id (Union[Unset, str]):
        backend_id_startswith (Union[Unset, str]):
        offering_uuid (Union[Unset, list[UUID]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['ProviderSiteAgentOfferingConfig']: Combined results from all pages
    """
    from urllib.parse import parse_qs, urlparse

    all_results: list[ProviderSiteAgentOfferingConfig] = []

    # Get initial request kwargs
    kwargs = _get_kwargs(
        uuid=uuid,
        backend_id=backend_id,
        backend_id_startswith=backend_id_startswith,
        offering_uuid=offering_uuid,
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
