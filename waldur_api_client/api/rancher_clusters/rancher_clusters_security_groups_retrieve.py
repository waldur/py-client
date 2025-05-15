from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cluster_security_group import ClusterSecurityGroup
from ...types import Response


def _get_kwargs(
    cluster_uuid: UUID,
    id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/rancher-clusters/{cluster_uuid}/security-groups/{id}/",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ClusterSecurityGroup]:
    if response.status_code == 200:
        response_200 = ClusterSecurityGroup.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ClusterSecurityGroup]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cluster_uuid: UUID,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ClusterSecurityGroup]:
    """Retrieve security group of Rancher cluster.

    Args:
        cluster_uuid (UUID):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ClusterSecurityGroup]
    """

    kwargs = _get_kwargs(
        cluster_uuid=cluster_uuid,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cluster_uuid: UUID,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[ClusterSecurityGroup]:
    """Retrieve security group of Rancher cluster.

    Args:
        cluster_uuid (UUID):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ClusterSecurityGroup
    """

    return sync_detailed(
        cluster_uuid=cluster_uuid,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    cluster_uuid: UUID,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ClusterSecurityGroup]:
    """Retrieve security group of Rancher cluster.

    Args:
        cluster_uuid (UUID):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ClusterSecurityGroup]
    """

    kwargs = _get_kwargs(
        cluster_uuid=cluster_uuid,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cluster_uuid: UUID,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[ClusterSecurityGroup]:
    """Retrieve security group of Rancher cluster.

    Args:
        cluster_uuid (UUID):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ClusterSecurityGroup
    """

    return (
        await asyncio_detailed(
            cluster_uuid=cluster_uuid,
            id=id,
            client=client,
        )
    ).parsed
