from http import HTTPStatus
from typing import Any, Union, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.site_agent_offering_config import SiteAgentOfferingConfig
from ...types import Response


def _get_kwargs(
    uuid: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/marketplace-provider-offerings/{uuid}/site_agent_config/",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[Any, SiteAgentOfferingConfig]:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = SiteAgentOfferingConfig.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, SiteAgentOfferingConfig]]:
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
) -> Response[Union[Any, SiteAgentOfferingConfig]]:
    """Site agent configuration of an offering

     The configuration a site agent loads for this offering: the offering block that
    generate_site_agent_config writes, from the same build, without the Waldur API URL, token and
    offering UUID the agent needs to make this call. No secret is included, not even as a placeholder:
    each secret the offering's backends declare is listed in secrets, for the agent to take from its own
    configuration. version changes when, and only when, offering does. Site agent offerings only.

    Args:
        uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SiteAgentOfferingConfig]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
) -> Union[Any, SiteAgentOfferingConfig]:
    """Site agent configuration of an offering

     The configuration a site agent loads for this offering: the offering block that
    generate_site_agent_config writes, from the same build, without the Waldur API URL, token and
    offering UUID the agent needs to make this call. No secret is included, not even as a placeholder:
    each secret the offering's backends declare is listed in secrets, for the agent to take from its own
    configuration. version changes when, and only when, offering does. Site agent offerings only.

    Args:
        uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SiteAgentOfferingConfig]
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, SiteAgentOfferingConfig]]:
    """Site agent configuration of an offering

     The configuration a site agent loads for this offering: the offering block that
    generate_site_agent_config writes, from the same build, without the Waldur API URL, token and
    offering UUID the agent needs to make this call. No secret is included, not even as a placeholder:
    each secret the offering's backends declare is listed in secrets, for the agent to take from its own
    configuration. version changes when, and only when, offering does. Site agent offerings only.

    Args:
        uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SiteAgentOfferingConfig]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
) -> Union[Any, SiteAgentOfferingConfig]:
    """Site agent configuration of an offering

     The configuration a site agent loads for this offering: the offering block that
    generate_site_agent_config writes, from the same build, without the Waldur API URL, token and
    offering UUID the agent needs to make this call. No secret is included, not even as a placeholder:
    each secret the offering's backends declare is listed in secrets, for the agent to take from its own
    configuration. version changes when, and only when, offering does. Site agent offerings only.

    Args:
        uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SiteAgentOfferingConfig]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
        )
    ).parsed
