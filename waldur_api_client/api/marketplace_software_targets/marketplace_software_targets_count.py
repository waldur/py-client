from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.marketplace_software_targets_count_o_item import MarketplaceSoftwareTargetsCountOItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    catalog_uuid: Union[Unset, UUID] = UNSET,
    cpu_family: Union[Unset, str] = UNSET,
    cpu_microarchitecture: Union[Unset, str] = UNSET,
    o: Union[Unset, list[MarketplaceSoftwareTargetsCountOItem]] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    package_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    path: Union[Unset, str] = UNSET,
    version_uuid: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_catalog_uuid: Union[Unset, str] = UNSET
    if not isinstance(catalog_uuid, Unset):
        json_catalog_uuid = str(catalog_uuid)
    params["catalog_uuid"] = json_catalog_uuid

    params["cpu_family"] = cpu_family

    params["cpu_microarchitecture"] = cpu_microarchitecture

    json_o: Union[Unset, list[str]] = UNSET
    if not isinstance(o, Unset):
        json_o = []
        for o_item_data in o:
            o_item = o_item_data.value
            json_o.append(o_item)

    params["o"] = json_o

    json_offering_uuid: Union[Unset, str] = UNSET
    if not isinstance(offering_uuid, Unset):
        json_offering_uuid = str(offering_uuid)
    params["offering_uuid"] = json_offering_uuid

    json_package_uuid: Union[Unset, str] = UNSET
    if not isinstance(package_uuid, Unset):
        json_package_uuid = str(package_uuid)
    params["package_uuid"] = json_package_uuid

    params["page"] = page

    params["page_size"] = page_size

    params["path"] = path

    json_version_uuid: Union[Unset, str] = UNSET
    if not isinstance(version_uuid, Unset):
        json_version_uuid = str(version_uuid)
    params["version_uuid"] = json_version_uuid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "head",
        "url": "/api/marketplace-software-targets/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> int:
    if response.status_code == HTTPStatus.OK:
        try:
            return int(response.headers["x-result-count"])
        except KeyError:
            raise errors.UnexpectedStatus(
                response.status_code, b"Expected 'X-Result-Count' header for HEAD request, but it was not found."
            )
        except ValueError:
            count_val = response.headers.get("x-result-count")
            msg = f"Expected 'X-Result-Count' header to be an integer, but got '{count_val}'."
            raise errors.UnexpectedStatus(response.status_code, msg.encode())
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[int]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    catalog_uuid: Union[Unset, UUID] = UNSET,
    cpu_family: Union[Unset, str] = UNSET,
    cpu_microarchitecture: Union[Unset, str] = UNSET,
    o: Union[Unset, list[MarketplaceSoftwareTargetsCountOItem]] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    package_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    path: Union[Unset, str] = UNSET,
    version_uuid: Union[Unset, UUID] = UNSET,
) -> Response[int]:
    """Get number of items in the collection matching the request parameters.

    Args:
        catalog_uuid (Union[Unset, UUID]):
        cpu_family (Union[Unset, str]):
        cpu_microarchitecture (Union[Unset, str]):
        o (Union[Unset, list[MarketplaceSoftwareTargetsCountOItem]]):
        offering_uuid (Union[Unset, UUID]):
        package_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        path (Union[Unset, str]):
        version_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[int]
    """

    kwargs = _get_kwargs(
        catalog_uuid=catalog_uuid,
        cpu_family=cpu_family,
        cpu_microarchitecture=cpu_microarchitecture,
        o=o,
        offering_uuid=offering_uuid,
        package_uuid=package_uuid,
        page=page,
        page_size=page_size,
        path=path,
        version_uuid=version_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    catalog_uuid: Union[Unset, UUID] = UNSET,
    cpu_family: Union[Unset, str] = UNSET,
    cpu_microarchitecture: Union[Unset, str] = UNSET,
    o: Union[Unset, list[MarketplaceSoftwareTargetsCountOItem]] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    package_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    path: Union[Unset, str] = UNSET,
    version_uuid: Union[Unset, UUID] = UNSET,
) -> int:
    """Get number of items in the collection matching the request parameters.

    Args:
        catalog_uuid (Union[Unset, UUID]):
        cpu_family (Union[Unset, str]):
        cpu_microarchitecture (Union[Unset, str]):
        o (Union[Unset, list[MarketplaceSoftwareTargetsCountOItem]]):
        offering_uuid (Union[Unset, UUID]):
        package_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        path (Union[Unset, str]):
        version_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        int
    """

    return sync_detailed(
        client=client,
        catalog_uuid=catalog_uuid,
        cpu_family=cpu_family,
        cpu_microarchitecture=cpu_microarchitecture,
        o=o,
        offering_uuid=offering_uuid,
        package_uuid=package_uuid,
        page=page,
        page_size=page_size,
        path=path,
        version_uuid=version_uuid,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    catalog_uuid: Union[Unset, UUID] = UNSET,
    cpu_family: Union[Unset, str] = UNSET,
    cpu_microarchitecture: Union[Unset, str] = UNSET,
    o: Union[Unset, list[MarketplaceSoftwareTargetsCountOItem]] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    package_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    path: Union[Unset, str] = UNSET,
    version_uuid: Union[Unset, UUID] = UNSET,
) -> Response[int]:
    """Get number of items in the collection matching the request parameters.

    Args:
        catalog_uuid (Union[Unset, UUID]):
        cpu_family (Union[Unset, str]):
        cpu_microarchitecture (Union[Unset, str]):
        o (Union[Unset, list[MarketplaceSoftwareTargetsCountOItem]]):
        offering_uuid (Union[Unset, UUID]):
        package_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        path (Union[Unset, str]):
        version_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[int]
    """

    kwargs = _get_kwargs(
        catalog_uuid=catalog_uuid,
        cpu_family=cpu_family,
        cpu_microarchitecture=cpu_microarchitecture,
        o=o,
        offering_uuid=offering_uuid,
        package_uuid=package_uuid,
        page=page,
        page_size=page_size,
        path=path,
        version_uuid=version_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    catalog_uuid: Union[Unset, UUID] = UNSET,
    cpu_family: Union[Unset, str] = UNSET,
    cpu_microarchitecture: Union[Unset, str] = UNSET,
    o: Union[Unset, list[MarketplaceSoftwareTargetsCountOItem]] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    package_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    path: Union[Unset, str] = UNSET,
    version_uuid: Union[Unset, UUID] = UNSET,
) -> int:
    """Get number of items in the collection matching the request parameters.

    Args:
        catalog_uuid (Union[Unset, UUID]):
        cpu_family (Union[Unset, str]):
        cpu_microarchitecture (Union[Unset, str]):
        o (Union[Unset, list[MarketplaceSoftwareTargetsCountOItem]]):
        offering_uuid (Union[Unset, UUID]):
        package_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        path (Union[Unset, str]):
        version_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        int
    """

    return (
        await asyncio_detailed(
            client=client,
            catalog_uuid=catalog_uuid,
            cpu_family=cpu_family,
            cpu_microarchitecture=cpu_microarchitecture,
            o=o,
            offering_uuid=offering_uuid,
            package_uuid=package_uuid,
            page=page,
            page_size=page_size,
            path=path,
            version_uuid=version_uuid,
        )
    ).parsed
