import datetime
from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.marketplace_robot_accounts_list_state import MarketplaceRobotAccountsListState
from ...models.robot_account_details import RobotAccountDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    created: Union[Unset, datetime.datetime] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    modified: Union[Unset, datetime.datetime] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    provider_uuid: Union[Unset, UUID] = UNSET,
    resource: Union[Unset, str] = UNSET,
    resource_uuid: Union[Unset, UUID] = UNSET,
    state: Union[Unset, MarketplaceRobotAccountsListState] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_created: Union[Unset, str] = UNSET
    if not isinstance(created, Unset):
        json_created = created.isoformat()
    params["created"] = json_created

    json_customer_uuid: Union[Unset, str] = UNSET
    if not isinstance(customer_uuid, Unset):
        json_customer_uuid = str(customer_uuid)
    params["customer_uuid"] = json_customer_uuid

    json_modified: Union[Unset, str] = UNSET
    if not isinstance(modified, Unset):
        json_modified = modified.isoformat()
    params["modified"] = json_modified

    params["page"] = page

    params["page_size"] = page_size

    json_project_uuid: Union[Unset, str] = UNSET
    if not isinstance(project_uuid, Unset):
        json_project_uuid = str(project_uuid)
    params["project_uuid"] = json_project_uuid

    json_provider_uuid: Union[Unset, str] = UNSET
    if not isinstance(provider_uuid, Unset):
        json_provider_uuid = str(provider_uuid)
    params["provider_uuid"] = json_provider_uuid

    params["resource"] = resource

    json_resource_uuid: Union[Unset, str] = UNSET
    if not isinstance(resource_uuid, Unset):
        json_resource_uuid = str(resource_uuid)
    params["resource_uuid"] = json_resource_uuid

    json_state: Union[Unset, int] = UNSET
    if not isinstance(state, Unset):
        json_state = state.value

    params["state"] = json_state

    params["type"] = type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/marketplace-robot-accounts/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> list["RobotAccountDetails"]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RobotAccountDetails.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["RobotAccountDetails"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    created: Union[Unset, datetime.datetime] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    modified: Union[Unset, datetime.datetime] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    provider_uuid: Union[Unset, UUID] = UNSET,
    resource: Union[Unset, str] = UNSET,
    resource_uuid: Union[Unset, UUID] = UNSET,
    state: Union[Unset, MarketplaceRobotAccountsListState] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> Response[list["RobotAccountDetails"]]:
    """
    Args:
        created (Union[Unset, datetime.datetime]):
        customer_uuid (Union[Unset, UUID]):
        modified (Union[Unset, datetime.datetime]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        project_uuid (Union[Unset, UUID]):
        provider_uuid (Union[Unset, UUID]):
        resource (Union[Unset, str]):
        resource_uuid (Union[Unset, UUID]):
        state (Union[Unset, MarketplaceRobotAccountsListState]):
        type_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['RobotAccountDetails']]
    """

    kwargs = _get_kwargs(
        created=created,
        customer_uuid=customer_uuid,
        modified=modified,
        page=page,
        page_size=page_size,
        project_uuid=project_uuid,
        provider_uuid=provider_uuid,
        resource=resource,
        resource_uuid=resource_uuid,
        state=state,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    created: Union[Unset, datetime.datetime] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    modified: Union[Unset, datetime.datetime] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    provider_uuid: Union[Unset, UUID] = UNSET,
    resource: Union[Unset, str] = UNSET,
    resource_uuid: Union[Unset, UUID] = UNSET,
    state: Union[Unset, MarketplaceRobotAccountsListState] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> list["RobotAccountDetails"]:
    """
    Args:
        created (Union[Unset, datetime.datetime]):
        customer_uuid (Union[Unset, UUID]):
        modified (Union[Unset, datetime.datetime]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        project_uuid (Union[Unset, UUID]):
        provider_uuid (Union[Unset, UUID]):
        resource (Union[Unset, str]):
        resource_uuid (Union[Unset, UUID]):
        state (Union[Unset, MarketplaceRobotAccountsListState]):
        type_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['RobotAccountDetails']
    """

    return sync_detailed(
        client=client,
        created=created,
        customer_uuid=customer_uuid,
        modified=modified,
        page=page,
        page_size=page_size,
        project_uuid=project_uuid,
        provider_uuid=provider_uuid,
        resource=resource,
        resource_uuid=resource_uuid,
        state=state,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    created: Union[Unset, datetime.datetime] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    modified: Union[Unset, datetime.datetime] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    provider_uuid: Union[Unset, UUID] = UNSET,
    resource: Union[Unset, str] = UNSET,
    resource_uuid: Union[Unset, UUID] = UNSET,
    state: Union[Unset, MarketplaceRobotAccountsListState] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> Response[list["RobotAccountDetails"]]:
    """
    Args:
        created (Union[Unset, datetime.datetime]):
        customer_uuid (Union[Unset, UUID]):
        modified (Union[Unset, datetime.datetime]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        project_uuid (Union[Unset, UUID]):
        provider_uuid (Union[Unset, UUID]):
        resource (Union[Unset, str]):
        resource_uuid (Union[Unset, UUID]):
        state (Union[Unset, MarketplaceRobotAccountsListState]):
        type_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['RobotAccountDetails']]
    """

    kwargs = _get_kwargs(
        created=created,
        customer_uuid=customer_uuid,
        modified=modified,
        page=page,
        page_size=page_size,
        project_uuid=project_uuid,
        provider_uuid=provider_uuid,
        resource=resource,
        resource_uuid=resource_uuid,
        state=state,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    created: Union[Unset, datetime.datetime] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    modified: Union[Unset, datetime.datetime] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    provider_uuid: Union[Unset, UUID] = UNSET,
    resource: Union[Unset, str] = UNSET,
    resource_uuid: Union[Unset, UUID] = UNSET,
    state: Union[Unset, MarketplaceRobotAccountsListState] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> list["RobotAccountDetails"]:
    """
    Args:
        created (Union[Unset, datetime.datetime]):
        customer_uuid (Union[Unset, UUID]):
        modified (Union[Unset, datetime.datetime]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        project_uuid (Union[Unset, UUID]):
        provider_uuid (Union[Unset, UUID]):
        resource (Union[Unset, str]):
        resource_uuid (Union[Unset, UUID]):
        state (Union[Unset, MarketplaceRobotAccountsListState]):
        type_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['RobotAccountDetails']
    """

    return (
        await asyncio_detailed(
            client=client,
            created=created,
            customer_uuid=customer_uuid,
            modified=modified,
            page=page,
            page_size=page_size,
            project_uuid=project_uuid,
            provider_uuid=provider_uuid,
            resource=resource,
            resource_uuid=resource_uuid,
            state=state,
            type_=type_,
        )
    ).parsed
