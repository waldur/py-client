from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rancher_cluster import RancherCluster
from ...models.rancher_cluster_request import RancherClusterRequest
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    *,
    body: Union[
        RancherClusterRequest,
        RancherClusterRequest,
        RancherClusterRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/rancher-clusters/{uuid}/create_management_security_group/",
    }

    if isinstance(body, RancherClusterRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, RancherClusterRequest):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, RancherClusterRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[RancherCluster]:
    if response.status_code == 200:
        response_200 = RancherCluster.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[RancherCluster]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: Union[
        RancherClusterRequest,
        RancherClusterRequest,
        RancherClusterRequest,
    ],
) -> Response[RancherCluster]:
    """
    Args:
        uuid (UUID):
        body (RancherClusterRequest):
        body (RancherClusterRequest):
        body (RancherClusterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RancherCluster]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: Union[
        RancherClusterRequest,
        RancherClusterRequest,
        RancherClusterRequest,
    ],
) -> Optional[RancherCluster]:
    """
    Args:
        uuid (UUID):
        body (RancherClusterRequest):
        body (RancherClusterRequest):
        body (RancherClusterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RancherCluster
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: Union[
        RancherClusterRequest,
        RancherClusterRequest,
        RancherClusterRequest,
    ],
) -> Response[RancherCluster]:
    """
    Args:
        uuid (UUID):
        body (RancherClusterRequest):
        body (RancherClusterRequest):
        body (RancherClusterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RancherCluster]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: Union[
        RancherClusterRequest,
        RancherClusterRequest,
        RancherClusterRequest,
    ],
) -> Optional[RancherCluster]:
    """
    Args:
        uuid (UUID):
        body (RancherClusterRequest):
        body (RancherClusterRequest):
        body (RancherClusterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RancherCluster
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
