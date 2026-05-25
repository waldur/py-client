from http import HTTPStatus
from typing import Any, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.openportal_user_mapping_retrieve_response_200 import OpenportalUserMappingRetrieveResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    identifier: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_identifier: Union[Unset, list[str]] = UNSET
    if not isinstance(identifier, Unset):
        json_identifier = identifier

    params["identifier"] = json_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/openportal/user_mapping/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> OpenportalUserMappingRetrieveResponse200:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = OpenportalUserMappingRetrieveResponse200.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OpenportalUserMappingRetrieveResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    identifier: Union[Unset, list[str]] = UNSET,
) -> Response[OpenportalUserMappingRetrieveResponse200]:
    """Map OpenPortal UserIdentifier strings (or email addresses) to Waldur User objects. Pass each value
    as a repeated 'identifier' query parameter. If the values contain '@' they are treated as email
    addresses (used for cached reports from remote portals); otherwise they are treated as
    UserIdentifier strings (used for local OpenPortal resources). Returns a dict keyed by the supplied
    string; unknown values map to null. Staff and support see all users; regular users may only look up
    users who share a project with them.

    Args:
        identifier (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OpenportalUserMappingRetrieveResponse200]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    identifier: Union[Unset, list[str]] = UNSET,
) -> OpenportalUserMappingRetrieveResponse200:
    """Map OpenPortal UserIdentifier strings (or email addresses) to Waldur User objects. Pass each value
    as a repeated 'identifier' query parameter. If the values contain '@' they are treated as email
    addresses (used for cached reports from remote portals); otherwise they are treated as
    UserIdentifier strings (used for local OpenPortal resources). Returns a dict keyed by the supplied
    string; unknown values map to null. Staff and support see all users; regular users may only look up
    users who share a project with them.

    Args:
        identifier (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OpenportalUserMappingRetrieveResponse200
    """

    return sync_detailed(
        client=client,
        identifier=identifier,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    identifier: Union[Unset, list[str]] = UNSET,
) -> Response[OpenportalUserMappingRetrieveResponse200]:
    """Map OpenPortal UserIdentifier strings (or email addresses) to Waldur User objects. Pass each value
    as a repeated 'identifier' query parameter. If the values contain '@' they are treated as email
    addresses (used for cached reports from remote portals); otherwise they are treated as
    UserIdentifier strings (used for local OpenPortal resources). Returns a dict keyed by the supplied
    string; unknown values map to null. Staff and support see all users; regular users may only look up
    users who share a project with them.

    Args:
        identifier (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OpenportalUserMappingRetrieveResponse200]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    identifier: Union[Unset, list[str]] = UNSET,
) -> OpenportalUserMappingRetrieveResponse200:
    """Map OpenPortal UserIdentifier strings (or email addresses) to Waldur User objects. Pass each value
    as a repeated 'identifier' query parameter. If the values contain '@' they are treated as email
    addresses (used for cached reports from remote portals); otherwise they are treated as
    UserIdentifier strings (used for local OpenPortal resources). Returns a dict keyed by the supplied
    string; unknown values map to null. Staff and support see all users; regular users may only look up
    users who share a project with them.

    Args:
        identifier (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OpenportalUserMappingRetrieveResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            identifier=identifier,
        )
    ).parsed
