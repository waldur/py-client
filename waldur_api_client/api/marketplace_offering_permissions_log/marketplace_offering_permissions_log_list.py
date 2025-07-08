import datetime
from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.marketplace_offering_permissions_log_list_o_item import MarketplaceOfferingPermissionsLogListOItem
from ...models.offering_permission import OfferingPermission
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    created: Union[Unset, datetime.datetime] = UNSET,
    customer: Union[Unset, UUID] = UNSET,
    full_name: Union[Unset, str] = UNSET,
    modified: Union[Unset, datetime.datetime] = UNSET,
    native_name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[MarketplaceOfferingPermissionsLogListOItem]] = UNSET,
    offering: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    role_name: Union[Unset, str] = UNSET,
    role_uuid: Union[Unset, UUID] = UNSET,
    scope_name: Union[Unset, str] = UNSET,
    scope_type: Union[Unset, str] = UNSET,
    scope_uuid: Union[Unset, str] = UNSET,
    user: Union[Unset, UUID] = UNSET,
    user_slug: Union[Unset, str] = UNSET,
    user_url: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_created: Union[Unset, str] = UNSET
    if not isinstance(created, Unset):
        json_created = created.isoformat()
    params["created"] = json_created

    json_customer: Union[Unset, str] = UNSET
    if not isinstance(customer, Unset):
        json_customer = str(customer)
    params["customer"] = json_customer

    params["full_name"] = full_name

    json_modified: Union[Unset, str] = UNSET
    if not isinstance(modified, Unset):
        json_modified = modified.isoformat()
    params["modified"] = json_modified

    params["native_name"] = native_name

    json_o: Union[Unset, list[str]] = UNSET
    if not isinstance(o, Unset):
        json_o = []
        for o_item_data in o:
            o_item = o_item_data.value
            json_o.append(o_item)

    params["o"] = json_o

    json_offering: Union[Unset, str] = UNSET
    if not isinstance(offering, Unset):
        json_offering = str(offering)
    params["offering"] = json_offering

    params["page"] = page

    params["page_size"] = page_size

    params["role_name"] = role_name

    json_role_uuid: Union[Unset, str] = UNSET
    if not isinstance(role_uuid, Unset):
        json_role_uuid = str(role_uuid)
    params["role_uuid"] = json_role_uuid

    params["scope_name"] = scope_name

    params["scope_type"] = scope_type

    params["scope_uuid"] = scope_uuid

    json_user: Union[Unset, str] = UNSET
    if not isinstance(user, Unset):
        json_user = str(user)
    params["user"] = json_user

    params["user_slug"] = user_slug

    params["user_url"] = user_url

    params["username"] = username

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/marketplace-offering-permissions-log/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> list["OfferingPermission"]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = OfferingPermission.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["OfferingPermission"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    created: Union[Unset, datetime.datetime] = UNSET,
    customer: Union[Unset, UUID] = UNSET,
    full_name: Union[Unset, str] = UNSET,
    modified: Union[Unset, datetime.datetime] = UNSET,
    native_name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[MarketplaceOfferingPermissionsLogListOItem]] = UNSET,
    offering: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    role_name: Union[Unset, str] = UNSET,
    role_uuid: Union[Unset, UUID] = UNSET,
    scope_name: Union[Unset, str] = UNSET,
    scope_type: Union[Unset, str] = UNSET,
    scope_uuid: Union[Unset, str] = UNSET,
    user: Union[Unset, UUID] = UNSET,
    user_slug: Union[Unset, str] = UNSET,
    user_url: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Response[list["OfferingPermission"]]:
    """Mixin to optimize HEAD requests for DRF views bypassing serializer processing

    Args:
        created (Union[Unset, datetime.datetime]):
        customer (Union[Unset, UUID]):
        full_name (Union[Unset, str]):
        modified (Union[Unset, datetime.datetime]):
        native_name (Union[Unset, str]):
        o (Union[Unset, list[MarketplaceOfferingPermissionsLogListOItem]]):
        offering (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        role_name (Union[Unset, str]):
        role_uuid (Union[Unset, UUID]):
        scope_name (Union[Unset, str]):
        scope_type (Union[Unset, str]):
        scope_uuid (Union[Unset, str]):
        user (Union[Unset, UUID]):
        user_slug (Union[Unset, str]):
        user_url (Union[Unset, str]):
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['OfferingPermission']]
    """

    kwargs = _get_kwargs(
        created=created,
        customer=customer,
        full_name=full_name,
        modified=modified,
        native_name=native_name,
        o=o,
        offering=offering,
        page=page,
        page_size=page_size,
        role_name=role_name,
        role_uuid=role_uuid,
        scope_name=scope_name,
        scope_type=scope_type,
        scope_uuid=scope_uuid,
        user=user,
        user_slug=user_slug,
        user_url=user_url,
        username=username,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    created: Union[Unset, datetime.datetime] = UNSET,
    customer: Union[Unset, UUID] = UNSET,
    full_name: Union[Unset, str] = UNSET,
    modified: Union[Unset, datetime.datetime] = UNSET,
    native_name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[MarketplaceOfferingPermissionsLogListOItem]] = UNSET,
    offering: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    role_name: Union[Unset, str] = UNSET,
    role_uuid: Union[Unset, UUID] = UNSET,
    scope_name: Union[Unset, str] = UNSET,
    scope_type: Union[Unset, str] = UNSET,
    scope_uuid: Union[Unset, str] = UNSET,
    user: Union[Unset, UUID] = UNSET,
    user_slug: Union[Unset, str] = UNSET,
    user_url: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> list["OfferingPermission"]:
    """Mixin to optimize HEAD requests for DRF views bypassing serializer processing

    Args:
        created (Union[Unset, datetime.datetime]):
        customer (Union[Unset, UUID]):
        full_name (Union[Unset, str]):
        modified (Union[Unset, datetime.datetime]):
        native_name (Union[Unset, str]):
        o (Union[Unset, list[MarketplaceOfferingPermissionsLogListOItem]]):
        offering (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        role_name (Union[Unset, str]):
        role_uuid (Union[Unset, UUID]):
        scope_name (Union[Unset, str]):
        scope_type (Union[Unset, str]):
        scope_uuid (Union[Unset, str]):
        user (Union[Unset, UUID]):
        user_slug (Union[Unset, str]):
        user_url (Union[Unset, str]):
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['OfferingPermission']
    """

    return sync_detailed(
        client=client,
        created=created,
        customer=customer,
        full_name=full_name,
        modified=modified,
        native_name=native_name,
        o=o,
        offering=offering,
        page=page,
        page_size=page_size,
        role_name=role_name,
        role_uuid=role_uuid,
        scope_name=scope_name,
        scope_type=scope_type,
        scope_uuid=scope_uuid,
        user=user,
        user_slug=user_slug,
        user_url=user_url,
        username=username,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    created: Union[Unset, datetime.datetime] = UNSET,
    customer: Union[Unset, UUID] = UNSET,
    full_name: Union[Unset, str] = UNSET,
    modified: Union[Unset, datetime.datetime] = UNSET,
    native_name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[MarketplaceOfferingPermissionsLogListOItem]] = UNSET,
    offering: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    role_name: Union[Unset, str] = UNSET,
    role_uuid: Union[Unset, UUID] = UNSET,
    scope_name: Union[Unset, str] = UNSET,
    scope_type: Union[Unset, str] = UNSET,
    scope_uuid: Union[Unset, str] = UNSET,
    user: Union[Unset, UUID] = UNSET,
    user_slug: Union[Unset, str] = UNSET,
    user_url: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Response[list["OfferingPermission"]]:
    """Mixin to optimize HEAD requests for DRF views bypassing serializer processing

    Args:
        created (Union[Unset, datetime.datetime]):
        customer (Union[Unset, UUID]):
        full_name (Union[Unset, str]):
        modified (Union[Unset, datetime.datetime]):
        native_name (Union[Unset, str]):
        o (Union[Unset, list[MarketplaceOfferingPermissionsLogListOItem]]):
        offering (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        role_name (Union[Unset, str]):
        role_uuid (Union[Unset, UUID]):
        scope_name (Union[Unset, str]):
        scope_type (Union[Unset, str]):
        scope_uuid (Union[Unset, str]):
        user (Union[Unset, UUID]):
        user_slug (Union[Unset, str]):
        user_url (Union[Unset, str]):
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['OfferingPermission']]
    """

    kwargs = _get_kwargs(
        created=created,
        customer=customer,
        full_name=full_name,
        modified=modified,
        native_name=native_name,
        o=o,
        offering=offering,
        page=page,
        page_size=page_size,
        role_name=role_name,
        role_uuid=role_uuid,
        scope_name=scope_name,
        scope_type=scope_type,
        scope_uuid=scope_uuid,
        user=user,
        user_slug=user_slug,
        user_url=user_url,
        username=username,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    created: Union[Unset, datetime.datetime] = UNSET,
    customer: Union[Unset, UUID] = UNSET,
    full_name: Union[Unset, str] = UNSET,
    modified: Union[Unset, datetime.datetime] = UNSET,
    native_name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[MarketplaceOfferingPermissionsLogListOItem]] = UNSET,
    offering: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    role_name: Union[Unset, str] = UNSET,
    role_uuid: Union[Unset, UUID] = UNSET,
    scope_name: Union[Unset, str] = UNSET,
    scope_type: Union[Unset, str] = UNSET,
    scope_uuid: Union[Unset, str] = UNSET,
    user: Union[Unset, UUID] = UNSET,
    user_slug: Union[Unset, str] = UNSET,
    user_url: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> list["OfferingPermission"]:
    """Mixin to optimize HEAD requests for DRF views bypassing serializer processing

    Args:
        created (Union[Unset, datetime.datetime]):
        customer (Union[Unset, UUID]):
        full_name (Union[Unset, str]):
        modified (Union[Unset, datetime.datetime]):
        native_name (Union[Unset, str]):
        o (Union[Unset, list[MarketplaceOfferingPermissionsLogListOItem]]):
        offering (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        role_name (Union[Unset, str]):
        role_uuid (Union[Unset, UUID]):
        scope_name (Union[Unset, str]):
        scope_type (Union[Unset, str]):
        scope_uuid (Union[Unset, str]):
        user (Union[Unset, UUID]):
        user_slug (Union[Unset, str]):
        user_url (Union[Unset, str]):
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['OfferingPermission']
    """

    return (
        await asyncio_detailed(
            client=client,
            created=created,
            customer=customer,
            full_name=full_name,
            modified=modified,
            native_name=native_name,
            o=o,
            offering=offering,
            page=page,
            page_size=page_size,
            role_name=role_name,
            role_uuid=role_uuid,
            scope_name=scope_name,
            scope_type=scope_type,
            scope_uuid=scope_uuid,
            user=user,
            user_slug=user_slug,
            user_url=user_url,
            username=username,
        )
    ).parsed
