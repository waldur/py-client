from http import HTTPStatus
from typing import Any, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.notification_template_detail_serializers import NotificationTemplateDetailSerializers
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    is_overridden: Union[Unset, bool] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    path: Union[Unset, str] = UNSET,
    path_exact: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["is_overridden"] = is_overridden

    params["name"] = name

    params["name_exact"] = name_exact

    params["page"] = page

    params["page_size"] = page_size

    params["path"] = path

    params["path_exact"] = path_exact

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/notification-messages-templates/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> list["NotificationTemplateDetailSerializers"]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = NotificationTemplateDetailSerializers.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["NotificationTemplateDetailSerializers"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    is_overridden: Union[Unset, bool] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    path: Union[Unset, str] = UNSET,
    path_exact: Union[Unset, str] = UNSET,
) -> Response[list["NotificationTemplateDetailSerializers"]]:
    """Mixin to optimize HEAD requests for DRF views bypassing serializer processing

    Args:
        is_overridden (Union[Unset, bool]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        path (Union[Unset, str]):
        path_exact (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['NotificationTemplateDetailSerializers']]
    """

    kwargs = _get_kwargs(
        is_overridden=is_overridden,
        name=name,
        name_exact=name_exact,
        page=page,
        page_size=page_size,
        path=path,
        path_exact=path_exact,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    is_overridden: Union[Unset, bool] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    path: Union[Unset, str] = UNSET,
    path_exact: Union[Unset, str] = UNSET,
) -> list["NotificationTemplateDetailSerializers"]:
    """Mixin to optimize HEAD requests for DRF views bypassing serializer processing

    Args:
        is_overridden (Union[Unset, bool]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        path (Union[Unset, str]):
        path_exact (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['NotificationTemplateDetailSerializers']
    """

    return sync_detailed(
        client=client,
        is_overridden=is_overridden,
        name=name,
        name_exact=name_exact,
        page=page,
        page_size=page_size,
        path=path,
        path_exact=path_exact,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    is_overridden: Union[Unset, bool] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    path: Union[Unset, str] = UNSET,
    path_exact: Union[Unset, str] = UNSET,
) -> Response[list["NotificationTemplateDetailSerializers"]]:
    """Mixin to optimize HEAD requests for DRF views bypassing serializer processing

    Args:
        is_overridden (Union[Unset, bool]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        path (Union[Unset, str]):
        path_exact (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['NotificationTemplateDetailSerializers']]
    """

    kwargs = _get_kwargs(
        is_overridden=is_overridden,
        name=name,
        name_exact=name_exact,
        page=page,
        page_size=page_size,
        path=path,
        path_exact=path_exact,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    is_overridden: Union[Unset, bool] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    path: Union[Unset, str] = UNSET,
    path_exact: Union[Unset, str] = UNSET,
) -> list["NotificationTemplateDetailSerializers"]:
    """Mixin to optimize HEAD requests for DRF views bypassing serializer processing

    Args:
        is_overridden (Union[Unset, bool]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        path (Union[Unset, str]):
        path_exact (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['NotificationTemplateDetailSerializers']
    """

    return (
        await asyncio_detailed(
            client=client,
            is_overridden=is_overridden,
            name=name,
            name_exact=name_exact,
            page=page,
            page_size=page_size,
            path=path,
            path_exact=path_exact,
        )
    ).parsed
