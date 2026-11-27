from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.k8s_sites import K8SSites
from ...models.k8s_sites_topology_enum import K8SSitesTopologyEnum
from ...types import UNSET, Response


def _get_kwargs(
    uuid: UUID,
    *,
    option: str,
    topology: K8SSitesTopologyEnum,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["option"] = option

    json_topology = topology.value
    params["topology"] = json_topology

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/marketplace-public-offerings/{uuid}/k8s_sites/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> K8SSites:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = K8SSites.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[K8SSites]:
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
    option: str,
    topology: K8SSitesTopologyEnum,
) -> Response[K8SSites]:
    """List the sites and common flavors of a Kubernetes option

     For a k8s_cluster_config order option whose provider fixed the OpenStack sites (infrastructure_mode
    provider_fixed): the sites of a topology, in order, and the flavors every site has under one name
    with the same vCPUs and RAM. Each flavor lists every site's own flavor UUID. Works for any caller
    who can see the offering, whether or not they can see the OpenStack offerings.

    Args:
        uuid (UUID):
        option (str):
        topology (K8SSitesTopologyEnum):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[K8SSites]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        option=option,
        topology=topology,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    option: str,
    topology: K8SSitesTopologyEnum,
) -> K8SSites:
    """List the sites and common flavors of a Kubernetes option

     For a k8s_cluster_config order option whose provider fixed the OpenStack sites (infrastructure_mode
    provider_fixed): the sites of a topology, in order, and the flavors every site has under one name
    with the same vCPUs and RAM. Each flavor lists every site's own flavor UUID. Works for any caller
    who can see the offering, whether or not they can see the OpenStack offerings.

    Args:
        uuid (UUID):
        option (str):
        topology (K8SSitesTopologyEnum):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        K8SSites
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        option=option,
        topology=topology,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    option: str,
    topology: K8SSitesTopologyEnum,
) -> Response[K8SSites]:
    """List the sites and common flavors of a Kubernetes option

     For a k8s_cluster_config order option whose provider fixed the OpenStack sites (infrastructure_mode
    provider_fixed): the sites of a topology, in order, and the flavors every site has under one name
    with the same vCPUs and RAM. Each flavor lists every site's own flavor UUID. Works for any caller
    who can see the offering, whether or not they can see the OpenStack offerings.

    Args:
        uuid (UUID):
        option (str):
        topology (K8SSitesTopologyEnum):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[K8SSites]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        option=option,
        topology=topology,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    option: str,
    topology: K8SSitesTopologyEnum,
) -> K8SSites:
    """List the sites and common flavors of a Kubernetes option

     For a k8s_cluster_config order option whose provider fixed the OpenStack sites (infrastructure_mode
    provider_fixed): the sites of a topology, in order, and the flavors every site has under one name
    with the same vCPUs and RAM. Each flavor lists every site's own flavor UUID. Works for any caller
    who can see the offering, whether or not they can see the OpenStack offerings.

    Args:
        uuid (UUID):
        option (str):
        topology (K8SSitesTopologyEnum):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        K8SSites
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            option=option,
            topology=topology,
        )
    ).parsed
