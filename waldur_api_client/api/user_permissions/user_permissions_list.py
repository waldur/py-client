from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.permission import Permission
from ...models.user_permissions_list_o_item import UserPermissionsListOItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    full_name: Union[Unset, str] = UNSET,
    native_name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[UserPermissionsListOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    user: Union[Unset, UUID] = UNSET,
    user_slug: Union[Unset, str] = UNSET,
    user_url: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["full_name"] = full_name

    params["native_name"] = native_name

    json_o: Union[Unset, list[str]] = UNSET
    if not isinstance(o, Unset):
        json_o = []
        for o_item_data in o:
            o_item = o_item_data.value
            json_o.append(o_item)

    params["o"] = json_o

    params["page"] = page

    params["page_size"] = page_size

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
        "url": "/api/user-permissions/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["Permission"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Permission.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["Permission"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    full_name: Union[Unset, str] = UNSET,
    native_name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[UserPermissionsListOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    user: Union[Unset, UUID] = UNSET,
    user_slug: Union[Unset, str] = UNSET,
    user_url: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Response[list["Permission"]]:
    """
    Args:
        full_name (Union[Unset, str]):
        native_name (Union[Unset, str]):
        o (Union[Unset, list[UserPermissionsListOItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        user (Union[Unset, UUID]):
        user_slug (Union[Unset, str]):
        user_url (Union[Unset, str]):
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['Permission']]
    """

    kwargs = _get_kwargs(
        full_name=full_name,
        native_name=native_name,
        o=o,
        page=page,
        page_size=page_size,
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
    full_name: Union[Unset, str] = UNSET,
    native_name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[UserPermissionsListOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    user: Union[Unset, UUID] = UNSET,
    user_slug: Union[Unset, str] = UNSET,
    user_url: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Optional[list["Permission"]]:
    """
    Args:
        full_name (Union[Unset, str]):
        native_name (Union[Unset, str]):
        o (Union[Unset, list[UserPermissionsListOItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        user (Union[Unset, UUID]):
        user_slug (Union[Unset, str]):
        user_url (Union[Unset, str]):
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['Permission']
    """

    return sync_detailed(
        client=client,
        full_name=full_name,
        native_name=native_name,
        o=o,
        page=page,
        page_size=page_size,
        user=user,
        user_slug=user_slug,
        user_url=user_url,
        username=username,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    full_name: Union[Unset, str] = UNSET,
    native_name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[UserPermissionsListOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    user: Union[Unset, UUID] = UNSET,
    user_slug: Union[Unset, str] = UNSET,
    user_url: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Response[list["Permission"]]:
    """
    Args:
        full_name (Union[Unset, str]):
        native_name (Union[Unset, str]):
        o (Union[Unset, list[UserPermissionsListOItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        user (Union[Unset, UUID]):
        user_slug (Union[Unset, str]):
        user_url (Union[Unset, str]):
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['Permission']]
    """

    kwargs = _get_kwargs(
        full_name=full_name,
        native_name=native_name,
        o=o,
        page=page,
        page_size=page_size,
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
    full_name: Union[Unset, str] = UNSET,
    native_name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[UserPermissionsListOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    user: Union[Unset, UUID] = UNSET,
    user_slug: Union[Unset, str] = UNSET,
    user_url: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Optional[list["Permission"]]:
    """
    Args:
        full_name (Union[Unset, str]):
        native_name (Union[Unset, str]):
        o (Union[Unset, list[UserPermissionsListOItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        user (Union[Unset, UUID]):
        user_slug (Union[Unset, str]):
        user_url (Union[Unset, str]):
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['Permission']
    """

    return (
        await asyncio_detailed(
            client=client,
            full_name=full_name,
            native_name=native_name,
            o=o,
            page=page,
            page_size=page_size,
            user=user,
            user_slug=user_slug,
            user_url=user_url,
            username=username,
        )
    ).parsed
