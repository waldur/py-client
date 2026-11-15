from http import HTTPStatus
from typing import Any, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.marketplace_offering_users_profile_field_warnings_retrieve_response_200 import (
    MarketplaceOfferingUsersProfileFieldWarningsRetrieveResponse200,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/marketplace-offering-users/profile_field_warnings/",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> MarketplaceOfferingUsersProfileFieldWarningsRetrieveResponse200:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = MarketplaceOfferingUsersProfileFieldWarningsRetrieveResponse200.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[MarketplaceOfferingUsersProfileFieldWarningsRetrieveResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[MarketplaceOfferingUsersProfileFieldWarningsRetrieveResponse200]:
    """Get profile field warnings

     Returns a mapping of user profile field names to offerings that expose those fields. When
    ENFORCE_OFFERING_USER_PROFILE_COMPLETENESS is enabled, clearing a field listed here would make the
    user invisible to the service provider for the associated offerings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MarketplaceOfferingUsersProfileFieldWarningsRetrieveResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> MarketplaceOfferingUsersProfileFieldWarningsRetrieveResponse200:
    """Get profile field warnings

     Returns a mapping of user profile field names to offerings that expose those fields. When
    ENFORCE_OFFERING_USER_PROFILE_COMPLETENESS is enabled, clearing a field listed here would make the
    user invisible to the service provider for the associated offerings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MarketplaceOfferingUsersProfileFieldWarningsRetrieveResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[MarketplaceOfferingUsersProfileFieldWarningsRetrieveResponse200]:
    """Get profile field warnings

     Returns a mapping of user profile field names to offerings that expose those fields. When
    ENFORCE_OFFERING_USER_PROFILE_COMPLETENESS is enabled, clearing a field listed here would make the
    user invisible to the service provider for the associated offerings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MarketplaceOfferingUsersProfileFieldWarningsRetrieveResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> MarketplaceOfferingUsersProfileFieldWarningsRetrieveResponse200:
    """Get profile field warnings

     Returns a mapping of user profile field names to offerings that expose those fields. When
    ENFORCE_OFFERING_USER_PROFILE_COMPLETENESS is enabled, clearing a field listed here would make the
    user invisible to the service provider for the associated offerings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MarketplaceOfferingUsersProfileFieldWarningsRetrieveResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
