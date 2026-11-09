from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.my_task_summary import MyTaskSummary
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    offering_uuid: Union[Unset, UUID] = UNSET,
    provider_uuid: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_offering_uuid: Union[Unset, str] = UNSET
    if not isinstance(offering_uuid, Unset):
        json_offering_uuid = str(offering_uuid)
    params["offering_uuid"] = json_offering_uuid

    json_provider_uuid: Union[Unset, str] = UNSET
    if not isinstance(provider_uuid, Unset):
        json_provider_uuid = str(provider_uuid)
    params["provider_uuid"] = json_provider_uuid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/proposal-my-tasks/summary/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> MyTaskSummary:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = MyTaskSummary.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[MyTaskSummary]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    offering_uuid: Union[Unset, UUID] = UNSET,
    provider_uuid: Union[Unset, UUID] = UNSET,
) -> Response[MyTaskSummary]:
    """Summarise the current user's open tasks

     How many tasks the list holds, and how many of them are overdue or due soon: the counts the list's
    ``due`` filter narrows it to. Takes the list's offering_uuid and provider_uuid.

    Args:
        offering_uuid (Union[Unset, UUID]):
        provider_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MyTaskSummary]
    """

    kwargs = _get_kwargs(
        offering_uuid=offering_uuid,
        provider_uuid=provider_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    offering_uuid: Union[Unset, UUID] = UNSET,
    provider_uuid: Union[Unset, UUID] = UNSET,
) -> MyTaskSummary:
    """Summarise the current user's open tasks

     How many tasks the list holds, and how many of them are overdue or due soon: the counts the list's
    ``due`` filter narrows it to. Takes the list's offering_uuid and provider_uuid.

    Args:
        offering_uuid (Union[Unset, UUID]):
        provider_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MyTaskSummary
    """

    return sync_detailed(
        client=client,
        offering_uuid=offering_uuid,
        provider_uuid=provider_uuid,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    offering_uuid: Union[Unset, UUID] = UNSET,
    provider_uuid: Union[Unset, UUID] = UNSET,
) -> Response[MyTaskSummary]:
    """Summarise the current user's open tasks

     How many tasks the list holds, and how many of them are overdue or due soon: the counts the list's
    ``due`` filter narrows it to. Takes the list's offering_uuid and provider_uuid.

    Args:
        offering_uuid (Union[Unset, UUID]):
        provider_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MyTaskSummary]
    """

    kwargs = _get_kwargs(
        offering_uuid=offering_uuid,
        provider_uuid=provider_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    offering_uuid: Union[Unset, UUID] = UNSET,
    provider_uuid: Union[Unset, UUID] = UNSET,
) -> MyTaskSummary:
    """Summarise the current user's open tasks

     How many tasks the list holds, and how many of them are overdue or due soon: the counts the list's
    ``due`` filter narrows it to. Takes the list's offering_uuid and provider_uuid.

    Args:
        offering_uuid (Union[Unset, UUID]):
        provider_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MyTaskSummary
    """

    return (
        await asyncio_detailed(
            client=client,
            offering_uuid=offering_uuid,
            provider_uuid=provider_uuid,
        )
    ).parsed
