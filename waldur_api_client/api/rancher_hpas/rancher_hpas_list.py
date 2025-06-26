from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rancher_hpa import RancherHPA
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cluster_uuid: Union[Unset, UUID] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    namespace_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    settings: Union[Unset, str] = UNSET,
    settings_uuid: Union[Unset, UUID] = UNSET,
    workload_uuid: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_cluster_uuid: Union[Unset, str] = UNSET
    if not isinstance(cluster_uuid, Unset):
        json_cluster_uuid = str(cluster_uuid)
    params["cluster_uuid"] = json_cluster_uuid

    params["name"] = name

    params["name_exact"] = name_exact

    json_namespace_uuid: Union[Unset, str] = UNSET
    if not isinstance(namespace_uuid, Unset):
        json_namespace_uuid = str(namespace_uuid)
    params["namespace_uuid"] = json_namespace_uuid

    params["page"] = page

    params["page_size"] = page_size

    json_project_uuid: Union[Unset, str] = UNSET
    if not isinstance(project_uuid, Unset):
        json_project_uuid = str(project_uuid)
    params["project_uuid"] = json_project_uuid

    params["settings"] = settings

    json_settings_uuid: Union[Unset, str] = UNSET
    if not isinstance(settings_uuid, Unset):
        json_settings_uuid = str(settings_uuid)
    params["settings_uuid"] = json_settings_uuid

    json_workload_uuid: Union[Unset, str] = UNSET
    if not isinstance(workload_uuid, Unset):
        json_workload_uuid = str(workload_uuid)
    params["workload_uuid"] = json_workload_uuid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/rancher-hpas/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> list["RancherHPA"]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RancherHPA.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["RancherHPA"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    cluster_uuid: Union[Unset, UUID] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    namespace_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    settings: Union[Unset, str] = UNSET,
    settings_uuid: Union[Unset, UUID] = UNSET,
    workload_uuid: Union[Unset, UUID] = UNSET,
) -> Response[list["RancherHPA"]]:
    """
    Args:
        cluster_uuid (Union[Unset, UUID]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        namespace_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        project_uuid (Union[Unset, UUID]):
        settings (Union[Unset, str]):
        settings_uuid (Union[Unset, UUID]):
        workload_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['RancherHPA']]
    """

    kwargs = _get_kwargs(
        cluster_uuid=cluster_uuid,
        name=name,
        name_exact=name_exact,
        namespace_uuid=namespace_uuid,
        page=page,
        page_size=page_size,
        project_uuid=project_uuid,
        settings=settings,
        settings_uuid=settings_uuid,
        workload_uuid=workload_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    cluster_uuid: Union[Unset, UUID] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    namespace_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    settings: Union[Unset, str] = UNSET,
    settings_uuid: Union[Unset, UUID] = UNSET,
    workload_uuid: Union[Unset, UUID] = UNSET,
) -> list["RancherHPA"]:
    """
    Args:
        cluster_uuid (Union[Unset, UUID]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        namespace_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        project_uuid (Union[Unset, UUID]):
        settings (Union[Unset, str]):
        settings_uuid (Union[Unset, UUID]):
        workload_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['RancherHPA']
    """

    return sync_detailed(
        client=client,
        cluster_uuid=cluster_uuid,
        name=name,
        name_exact=name_exact,
        namespace_uuid=namespace_uuid,
        page=page,
        page_size=page_size,
        project_uuid=project_uuid,
        settings=settings,
        settings_uuid=settings_uuid,
        workload_uuid=workload_uuid,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    cluster_uuid: Union[Unset, UUID] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    namespace_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    settings: Union[Unset, str] = UNSET,
    settings_uuid: Union[Unset, UUID] = UNSET,
    workload_uuid: Union[Unset, UUID] = UNSET,
) -> Response[list["RancherHPA"]]:
    """
    Args:
        cluster_uuid (Union[Unset, UUID]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        namespace_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        project_uuid (Union[Unset, UUID]):
        settings (Union[Unset, str]):
        settings_uuid (Union[Unset, UUID]):
        workload_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['RancherHPA']]
    """

    kwargs = _get_kwargs(
        cluster_uuid=cluster_uuid,
        name=name,
        name_exact=name_exact,
        namespace_uuid=namespace_uuid,
        page=page,
        page_size=page_size,
        project_uuid=project_uuid,
        settings=settings,
        settings_uuid=settings_uuid,
        workload_uuid=workload_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    cluster_uuid: Union[Unset, UUID] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    namespace_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    settings: Union[Unset, str] = UNSET,
    settings_uuid: Union[Unset, UUID] = UNSET,
    workload_uuid: Union[Unset, UUID] = UNSET,
) -> list["RancherHPA"]:
    """
    Args:
        cluster_uuid (Union[Unset, UUID]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        namespace_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        project_uuid (Union[Unset, UUID]):
        settings (Union[Unset, str]):
        settings_uuid (Union[Unset, UUID]):
        workload_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['RancherHPA']
    """

    return (
        await asyncio_detailed(
            client=client,
            cluster_uuid=cluster_uuid,
            name=name,
            name_exact=name_exact,
            namespace_uuid=namespace_uuid,
            page=page,
            page_size=page_size,
            project_uuid=project_uuid,
            settings=settings,
            settings_uuid=settings_uuid,
            workload_uuid=workload_uuid,
        )
    ).parsed
