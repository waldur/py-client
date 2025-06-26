from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.slurm_association import SlurmAssociation
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    allocation: Union[Unset, str] = UNSET,
    allocation_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["allocation"] = allocation

    json_allocation_uuid: Union[Unset, str] = UNSET
    if not isinstance(allocation_uuid, Unset):
        json_allocation_uuid = str(allocation_uuid)
    params["allocation_uuid"] = json_allocation_uuid

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/slurm-associations/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> list["SlurmAssociation"]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = SlurmAssociation.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["SlurmAssociation"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    allocation: Union[Unset, str] = UNSET,
    allocation_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[list["SlurmAssociation"]]:
    """
    Args:
        allocation (Union[Unset, str]):
        allocation_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['SlurmAssociation']]
    """

    kwargs = _get_kwargs(
        allocation=allocation,
        allocation_uuid=allocation_uuid,
        page=page,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    allocation: Union[Unset, str] = UNSET,
    allocation_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> list["SlurmAssociation"]:
    """
    Args:
        allocation (Union[Unset, str]):
        allocation_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['SlurmAssociation']
    """

    return sync_detailed(
        client=client,
        allocation=allocation,
        allocation_uuid=allocation_uuid,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    allocation: Union[Unset, str] = UNSET,
    allocation_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[list["SlurmAssociation"]]:
    """
    Args:
        allocation (Union[Unset, str]):
        allocation_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['SlurmAssociation']]
    """

    kwargs = _get_kwargs(
        allocation=allocation,
        allocation_uuid=allocation_uuid,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    allocation: Union[Unset, str] = UNSET,
    allocation_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> list["SlurmAssociation"]:
    """
    Args:
        allocation (Union[Unset, str]):
        allocation_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['SlurmAssociation']
    """

    return (
        await asyncio_detailed(
            client=client,
            allocation=allocation,
            allocation_uuid=allocation_uuid,
            page=page,
            page_size=page_size,
        )
    ).parsed
