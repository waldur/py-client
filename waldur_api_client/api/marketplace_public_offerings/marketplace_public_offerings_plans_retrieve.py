from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_public_plan import BasePublicPlan
from ...types import Response


def _get_kwargs(
    uuid: str,
    plan_uuid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/marketplace-public-offerings/{uuid}/plans/{plan_uuid}/",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[BasePublicPlan]:
    if response.status_code == 200:
        response_200 = BasePublicPlan.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[BasePublicPlan]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: str,
    plan_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[BasePublicPlan]:
    """
    Args:
        uuid (str):
        plan_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BasePublicPlan]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        plan_uuid=plan_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: str,
    plan_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Optional[BasePublicPlan]:
    """
    Args:
        uuid (str):
        plan_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BasePublicPlan
    """

    return sync_detailed(
        uuid=uuid,
        plan_uuid=plan_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    plan_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[BasePublicPlan]:
    """
    Args:
        uuid (str):
        plan_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BasePublicPlan]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        plan_uuid=plan_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: str,
    plan_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Optional[BasePublicPlan]:
    """
    Args:
        uuid (str):
        plan_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BasePublicPlan
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            plan_uuid=plan_uuid,
            client=client,
        )
    ).parsed
