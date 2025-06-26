from http import HTTPStatus
from typing import Any, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.digital_ocean_image import DigitalOceanImage
from ...models.digitalocean_images_list_o_item import DigitaloceanImagesListOItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    distribution: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    o: Union[Unset, list[DigitaloceanImagesListOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["distribution"] = distribution

    params["name"] = name

    params["name_exact"] = name_exact

    json_o: Union[Unset, list[str]] = UNSET
    if not isinstance(o, Unset):
        json_o = []
        for o_item_data in o:
            o_item = o_item_data.value
            json_o.append(o_item)

    params["o"] = json_o

    params["page"] = page

    params["page_size"] = page_size

    params["type"] = type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/digitalocean-images/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> list["DigitalOceanImage"]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DigitalOceanImage.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["DigitalOceanImage"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    distribution: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    o: Union[Unset, list[DigitaloceanImagesListOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> Response[list["DigitalOceanImage"]]:
    """
    Args:
        distribution (Union[Unset, str]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        o (Union[Unset, list[DigitaloceanImagesListOItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        type_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['DigitalOceanImage']]
    """

    kwargs = _get_kwargs(
        distribution=distribution,
        name=name,
        name_exact=name_exact,
        o=o,
        page=page,
        page_size=page_size,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    distribution: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    o: Union[Unset, list[DigitaloceanImagesListOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> list["DigitalOceanImage"]:
    """
    Args:
        distribution (Union[Unset, str]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        o (Union[Unset, list[DigitaloceanImagesListOItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        type_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['DigitalOceanImage']
    """

    return sync_detailed(
        client=client,
        distribution=distribution,
        name=name,
        name_exact=name_exact,
        o=o,
        page=page,
        page_size=page_size,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    distribution: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    o: Union[Unset, list[DigitaloceanImagesListOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> Response[list["DigitalOceanImage"]]:
    """
    Args:
        distribution (Union[Unset, str]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        o (Union[Unset, list[DigitaloceanImagesListOItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        type_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['DigitalOceanImage']]
    """

    kwargs = _get_kwargs(
        distribution=distribution,
        name=name,
        name_exact=name_exact,
        o=o,
        page=page,
        page_size=page_size,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    distribution: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    o: Union[Unset, list[DigitaloceanImagesListOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> list["DigitalOceanImage"]:
    """
    Args:
        distribution (Union[Unset, str]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        o (Union[Unset, list[DigitaloceanImagesListOItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        type_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['DigitalOceanImage']
    """

    return (
        await asyncio_detailed(
            client=client,
            distribution=distribution,
            name=name,
            name_exact=name_exact,
            o=o,
            page=page,
            page_size=page_size,
            type_=type_,
        )
    ).parsed
