from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.issue import Issue
from ...models.support_issues_list_o_item import SupportIssuesListOItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    assignee: Union[Unset, str] = UNSET,
    assignee_name: Union[Unset, str] = UNSET,
    caller: Union[Unset, str] = UNSET,
    caller_full_name: Union[Unset, str] = UNSET,
    customer: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    key: Union[Unset, str] = UNSET,
    o: Union[Unset, list[SupportIssuesListOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    project: Union[Unset, str] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    query: Union[Unset, str] = UNSET,
    remote_id: Union[Unset, str] = UNSET,
    reporter: Union[Unset, str] = UNSET,
    reporter_name: Union[Unset, str] = UNSET,
    resolution_year_month: Union[Unset, str] = UNSET,
    resource_external_ip: Union[Unset, str] = UNSET,
    resource_internal_ip: Union[Unset, str] = UNSET,
    resource_uuid: Union[Unset, UUID] = UNSET,
    status: Union[Unset, str] = UNSET,
    summary: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["assignee"] = assignee

    params["assignee_name"] = assignee_name

    params["caller"] = caller

    params["caller_full_name"] = caller_full_name

    params["customer"] = customer

    json_customer_uuid: Union[Unset, str] = UNSET
    if not isinstance(customer_uuid, Unset):
        json_customer_uuid = str(customer_uuid)
    params["customer_uuid"] = json_customer_uuid

    params["key"] = key

    json_o: Union[Unset, list[str]] = UNSET
    if not isinstance(o, Unset):
        json_o = []
        for o_item_data in o:
            o_item = o_item_data.value
            json_o.append(o_item)

    params["o"] = json_o

    params["page"] = page

    params["page_size"] = page_size

    params["project"] = project

    json_project_uuid: Union[Unset, str] = UNSET
    if not isinstance(project_uuid, Unset):
        json_project_uuid = str(project_uuid)
    params["project_uuid"] = json_project_uuid

    params["query"] = query

    params["remote_id"] = remote_id

    params["reporter"] = reporter

    params["reporter_name"] = reporter_name

    params["resolution_year_month"] = resolution_year_month

    params["resource_external_ip"] = resource_external_ip

    params["resource_internal_ip"] = resource_internal_ip

    json_resource_uuid: Union[Unset, str] = UNSET
    if not isinstance(resource_uuid, Unset):
        json_resource_uuid = str(resource_uuid)
    params["resource_uuid"] = json_resource_uuid

    params["status"] = status

    params["summary"] = summary

    params["type"] = type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/support-issues/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> list["Issue"]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Issue.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[list["Issue"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    assignee: Union[Unset, str] = UNSET,
    assignee_name: Union[Unset, str] = UNSET,
    caller: Union[Unset, str] = UNSET,
    caller_full_name: Union[Unset, str] = UNSET,
    customer: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    key: Union[Unset, str] = UNSET,
    o: Union[Unset, list[SupportIssuesListOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    project: Union[Unset, str] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    query: Union[Unset, str] = UNSET,
    remote_id: Union[Unset, str] = UNSET,
    reporter: Union[Unset, str] = UNSET,
    reporter_name: Union[Unset, str] = UNSET,
    resolution_year_month: Union[Unset, str] = UNSET,
    resource_external_ip: Union[Unset, str] = UNSET,
    resource_internal_ip: Union[Unset, str] = UNSET,
    resource_uuid: Union[Unset, UUID] = UNSET,
    status: Union[Unset, str] = UNSET,
    summary: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> Response[list["Issue"]]:
    """Mixin to optimize HEAD requests for DRF views bypassing serializer processing

    Args:
        assignee (Union[Unset, str]):
        assignee_name (Union[Unset, str]):
        caller (Union[Unset, str]):
        caller_full_name (Union[Unset, str]):
        customer (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        key (Union[Unset, str]):
        o (Union[Unset, list[SupportIssuesListOItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        project (Union[Unset, str]):
        project_uuid (Union[Unset, UUID]):
        query (Union[Unset, str]):
        remote_id (Union[Unset, str]):
        reporter (Union[Unset, str]):
        reporter_name (Union[Unset, str]):
        resolution_year_month (Union[Unset, str]):
        resource_external_ip (Union[Unset, str]):
        resource_internal_ip (Union[Unset, str]):
        resource_uuid (Union[Unset, UUID]):
        status (Union[Unset, str]):
        summary (Union[Unset, str]):
        type_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['Issue']]
    """

    kwargs = _get_kwargs(
        assignee=assignee,
        assignee_name=assignee_name,
        caller=caller,
        caller_full_name=caller_full_name,
        customer=customer,
        customer_uuid=customer_uuid,
        key=key,
        o=o,
        page=page,
        page_size=page_size,
        project=project,
        project_uuid=project_uuid,
        query=query,
        remote_id=remote_id,
        reporter=reporter,
        reporter_name=reporter_name,
        resolution_year_month=resolution_year_month,
        resource_external_ip=resource_external_ip,
        resource_internal_ip=resource_internal_ip,
        resource_uuid=resource_uuid,
        status=status,
        summary=summary,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    assignee: Union[Unset, str] = UNSET,
    assignee_name: Union[Unset, str] = UNSET,
    caller: Union[Unset, str] = UNSET,
    caller_full_name: Union[Unset, str] = UNSET,
    customer: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    key: Union[Unset, str] = UNSET,
    o: Union[Unset, list[SupportIssuesListOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    project: Union[Unset, str] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    query: Union[Unset, str] = UNSET,
    remote_id: Union[Unset, str] = UNSET,
    reporter: Union[Unset, str] = UNSET,
    reporter_name: Union[Unset, str] = UNSET,
    resolution_year_month: Union[Unset, str] = UNSET,
    resource_external_ip: Union[Unset, str] = UNSET,
    resource_internal_ip: Union[Unset, str] = UNSET,
    resource_uuid: Union[Unset, UUID] = UNSET,
    status: Union[Unset, str] = UNSET,
    summary: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> list["Issue"]:
    """Mixin to optimize HEAD requests for DRF views bypassing serializer processing

    Args:
        assignee (Union[Unset, str]):
        assignee_name (Union[Unset, str]):
        caller (Union[Unset, str]):
        caller_full_name (Union[Unset, str]):
        customer (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        key (Union[Unset, str]):
        o (Union[Unset, list[SupportIssuesListOItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        project (Union[Unset, str]):
        project_uuid (Union[Unset, UUID]):
        query (Union[Unset, str]):
        remote_id (Union[Unset, str]):
        reporter (Union[Unset, str]):
        reporter_name (Union[Unset, str]):
        resolution_year_month (Union[Unset, str]):
        resource_external_ip (Union[Unset, str]):
        resource_internal_ip (Union[Unset, str]):
        resource_uuid (Union[Unset, UUID]):
        status (Union[Unset, str]):
        summary (Union[Unset, str]):
        type_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['Issue']
    """

    return sync_detailed(
        client=client,
        assignee=assignee,
        assignee_name=assignee_name,
        caller=caller,
        caller_full_name=caller_full_name,
        customer=customer,
        customer_uuid=customer_uuid,
        key=key,
        o=o,
        page=page,
        page_size=page_size,
        project=project,
        project_uuid=project_uuid,
        query=query,
        remote_id=remote_id,
        reporter=reporter,
        reporter_name=reporter_name,
        resolution_year_month=resolution_year_month,
        resource_external_ip=resource_external_ip,
        resource_internal_ip=resource_internal_ip,
        resource_uuid=resource_uuid,
        status=status,
        summary=summary,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    assignee: Union[Unset, str] = UNSET,
    assignee_name: Union[Unset, str] = UNSET,
    caller: Union[Unset, str] = UNSET,
    caller_full_name: Union[Unset, str] = UNSET,
    customer: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    key: Union[Unset, str] = UNSET,
    o: Union[Unset, list[SupportIssuesListOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    project: Union[Unset, str] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    query: Union[Unset, str] = UNSET,
    remote_id: Union[Unset, str] = UNSET,
    reporter: Union[Unset, str] = UNSET,
    reporter_name: Union[Unset, str] = UNSET,
    resolution_year_month: Union[Unset, str] = UNSET,
    resource_external_ip: Union[Unset, str] = UNSET,
    resource_internal_ip: Union[Unset, str] = UNSET,
    resource_uuid: Union[Unset, UUID] = UNSET,
    status: Union[Unset, str] = UNSET,
    summary: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> Response[list["Issue"]]:
    """Mixin to optimize HEAD requests for DRF views bypassing serializer processing

    Args:
        assignee (Union[Unset, str]):
        assignee_name (Union[Unset, str]):
        caller (Union[Unset, str]):
        caller_full_name (Union[Unset, str]):
        customer (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        key (Union[Unset, str]):
        o (Union[Unset, list[SupportIssuesListOItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        project (Union[Unset, str]):
        project_uuid (Union[Unset, UUID]):
        query (Union[Unset, str]):
        remote_id (Union[Unset, str]):
        reporter (Union[Unset, str]):
        reporter_name (Union[Unset, str]):
        resolution_year_month (Union[Unset, str]):
        resource_external_ip (Union[Unset, str]):
        resource_internal_ip (Union[Unset, str]):
        resource_uuid (Union[Unset, UUID]):
        status (Union[Unset, str]):
        summary (Union[Unset, str]):
        type_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['Issue']]
    """

    kwargs = _get_kwargs(
        assignee=assignee,
        assignee_name=assignee_name,
        caller=caller,
        caller_full_name=caller_full_name,
        customer=customer,
        customer_uuid=customer_uuid,
        key=key,
        o=o,
        page=page,
        page_size=page_size,
        project=project,
        project_uuid=project_uuid,
        query=query,
        remote_id=remote_id,
        reporter=reporter,
        reporter_name=reporter_name,
        resolution_year_month=resolution_year_month,
        resource_external_ip=resource_external_ip,
        resource_internal_ip=resource_internal_ip,
        resource_uuid=resource_uuid,
        status=status,
        summary=summary,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    assignee: Union[Unset, str] = UNSET,
    assignee_name: Union[Unset, str] = UNSET,
    caller: Union[Unset, str] = UNSET,
    caller_full_name: Union[Unset, str] = UNSET,
    customer: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    key: Union[Unset, str] = UNSET,
    o: Union[Unset, list[SupportIssuesListOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    project: Union[Unset, str] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    query: Union[Unset, str] = UNSET,
    remote_id: Union[Unset, str] = UNSET,
    reporter: Union[Unset, str] = UNSET,
    reporter_name: Union[Unset, str] = UNSET,
    resolution_year_month: Union[Unset, str] = UNSET,
    resource_external_ip: Union[Unset, str] = UNSET,
    resource_internal_ip: Union[Unset, str] = UNSET,
    resource_uuid: Union[Unset, UUID] = UNSET,
    status: Union[Unset, str] = UNSET,
    summary: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> list["Issue"]:
    """Mixin to optimize HEAD requests for DRF views bypassing serializer processing

    Args:
        assignee (Union[Unset, str]):
        assignee_name (Union[Unset, str]):
        caller (Union[Unset, str]):
        caller_full_name (Union[Unset, str]):
        customer (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        key (Union[Unset, str]):
        o (Union[Unset, list[SupportIssuesListOItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        project (Union[Unset, str]):
        project_uuid (Union[Unset, UUID]):
        query (Union[Unset, str]):
        remote_id (Union[Unset, str]):
        reporter (Union[Unset, str]):
        reporter_name (Union[Unset, str]):
        resolution_year_month (Union[Unset, str]):
        resource_external_ip (Union[Unset, str]):
        resource_internal_ip (Union[Unset, str]):
        resource_uuid (Union[Unset, UUID]):
        status (Union[Unset, str]):
        summary (Union[Unset, str]):
        type_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['Issue']
    """

    return (
        await asyncio_detailed(
            client=client,
            assignee=assignee,
            assignee_name=assignee_name,
            caller=caller,
            caller_full_name=caller_full_name,
            customer=customer,
            customer_uuid=customer_uuid,
            key=key,
            o=o,
            page=page,
            page_size=page_size,
            project=project,
            project_uuid=project_uuid,
            query=query,
            remote_id=remote_id,
            reporter=reporter,
            reporter_name=reporter_name,
            resolution_year_month=resolution_year_month,
            resource_external_ip=resource_external_ip,
            resource_internal_ip=resource_internal_ip,
            resource_uuid=resource_uuid,
            status=status,
            summary=summary,
            type_=type_,
        )
    ).parsed
