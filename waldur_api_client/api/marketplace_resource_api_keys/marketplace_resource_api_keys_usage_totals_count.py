import datetime
from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.resource_api_key_action import ResourceApiKeyAction
from ...models.resource_api_key_state import ResourceApiKeyState
from ...models.resource_api_key_status_o_enum import ResourceApiKeyStatusOEnum
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    customer_uuid: Union[Unset, UUID] = UNSET,
    has_pending_action: Union[Unset, bool] = UNSET,
    modified_before: Union[Unset, datetime.datetime] = UNSET,
    o: Union[Unset, list[ResourceApiKeyStatusOEnum]] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    paused_by_limit: Union[Unset, bool] = UNSET,
    pending_action: Union[Unset, list[ResourceApiKeyAction]] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    provider_uuid: Union[Unset, UUID] = UNSET,
    resource_uuid: Union[Unset, UUID] = UNSET,
    state: Union[Unset, list[ResourceApiKeyState]] = UNSET,
    user_uuid: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_customer_uuid: Union[Unset, str] = UNSET
    if not isinstance(customer_uuid, Unset):
        json_customer_uuid = str(customer_uuid)
    params["customer_uuid"] = json_customer_uuid

    params["has_pending_action"] = has_pending_action

    json_modified_before: Union[Unset, str] = UNSET
    if not isinstance(modified_before, Unset):
        json_modified_before = modified_before.isoformat()
    params["modified_before"] = json_modified_before

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

    params["paused_by_limit"] = paused_by_limit

    json_pending_action: Union[Unset, list[str]] = UNSET
    if not isinstance(pending_action, Unset):
        json_pending_action = []
        for pending_action_item_data in pending_action:
            pending_action_item = pending_action_item_data.value
            json_pending_action.append(pending_action_item)

    params["pending_action"] = json_pending_action

    json_project_uuid: Union[Unset, str] = UNSET
    if not isinstance(project_uuid, Unset):
        json_project_uuid = str(project_uuid)
    params["project_uuid"] = json_project_uuid

    json_provider_uuid: Union[Unset, str] = UNSET
    if not isinstance(provider_uuid, Unset):
        json_provider_uuid = str(provider_uuid)
    params["provider_uuid"] = json_provider_uuid

    json_resource_uuid: Union[Unset, str] = UNSET
    if not isinstance(resource_uuid, Unset):
        json_resource_uuid = str(resource_uuid)
    params["resource_uuid"] = json_resource_uuid

    json_state: Union[Unset, list[str]] = UNSET
    if not isinstance(state, Unset):
        json_state = []
        for state_item_data in state:
            state_item = state_item_data.value
            json_state.append(state_item)

    params["state"] = json_state

    json_user_uuid: Union[Unset, str] = UNSET
    if not isinstance(user_uuid, Unset):
        json_user_uuid = str(user_uuid)
    params["user_uuid"] = json_user_uuid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "head",
        "url": "/api/marketplace-resource-api-keys/usage_totals/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> int:
    if response.status_code == HTTPStatus.OK:
        try:
            return int(response.headers["x-result-count"])
        except KeyError:
            raise errors.UnexpectedStatus(
                response.status_code,
                b"Expected 'X-Result-Count' header for HEAD request, but it was not found.",
                response.url,
            )
        except ValueError:
            count_val = response.headers.get("x-result-count")
            msg = f"Expected 'X-Result-Count' header to be an integer, but got '{count_val}'."
            raise errors.UnexpectedStatus(response.status_code, msg.encode(), response.url)
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


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
    customer_uuid: Union[Unset, UUID] = UNSET,
    has_pending_action: Union[Unset, bool] = UNSET,
    modified_before: Union[Unset, datetime.datetime] = UNSET,
    o: Union[Unset, list[ResourceApiKeyStatusOEnum]] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    paused_by_limit: Union[Unset, bool] = UNSET,
    pending_action: Union[Unset, list[ResourceApiKeyAction]] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    provider_uuid: Union[Unset, UUID] = UNSET,
    resource_uuid: Union[Unset, UUID] = UNSET,
    state: Union[Unset, list[ResourceApiKeyState]] = UNSET,
    user_uuid: Union[Unset, UUID] = UNSET,
) -> Response[int]:
    """Total API key usage of a resource, offering or provider

     Get number of items in the collection matching the request parameters.

    Args:
        customer_uuid (Union[Unset, UUID]):
        has_pending_action (Union[Unset, bool]):
        modified_before (Union[Unset, datetime.datetime]):
        o (Union[Unset, list[ResourceApiKeyStatusOEnum]]):
        offering_uuid (Union[Unset, UUID]):
        paused_by_limit (Union[Unset, bool]):
        pending_action (Union[Unset, list[ResourceApiKeyAction]]):
        project_uuid (Union[Unset, UUID]):
        provider_uuid (Union[Unset, UUID]):
        resource_uuid (Union[Unset, UUID]):
        state (Union[Unset, list[ResourceApiKeyState]]):
        user_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[int]
    """

    kwargs = _get_kwargs(
        customer_uuid=customer_uuid,
        has_pending_action=has_pending_action,
        modified_before=modified_before,
        o=o,
        offering_uuid=offering_uuid,
        paused_by_limit=paused_by_limit,
        pending_action=pending_action,
        project_uuid=project_uuid,
        provider_uuid=provider_uuid,
        resource_uuid=resource_uuid,
        state=state,
        user_uuid=user_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    customer_uuid: Union[Unset, UUID] = UNSET,
    has_pending_action: Union[Unset, bool] = UNSET,
    modified_before: Union[Unset, datetime.datetime] = UNSET,
    o: Union[Unset, list[ResourceApiKeyStatusOEnum]] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    paused_by_limit: Union[Unset, bool] = UNSET,
    pending_action: Union[Unset, list[ResourceApiKeyAction]] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    provider_uuid: Union[Unset, UUID] = UNSET,
    resource_uuid: Union[Unset, UUID] = UNSET,
    state: Union[Unset, list[ResourceApiKeyState]] = UNSET,
    user_uuid: Union[Unset, UUID] = UNSET,
) -> int:
    """Total API key usage of a resource, offering or provider

     Get number of items in the collection matching the request parameters.

    Args:
        customer_uuid (Union[Unset, UUID]):
        has_pending_action (Union[Unset, bool]):
        modified_before (Union[Unset, datetime.datetime]):
        o (Union[Unset, list[ResourceApiKeyStatusOEnum]]):
        offering_uuid (Union[Unset, UUID]):
        paused_by_limit (Union[Unset, bool]):
        pending_action (Union[Unset, list[ResourceApiKeyAction]]):
        project_uuid (Union[Unset, UUID]):
        provider_uuid (Union[Unset, UUID]):
        resource_uuid (Union[Unset, UUID]):
        state (Union[Unset, list[ResourceApiKeyState]]):
        user_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        int
    """

    return sync_detailed(
        client=client,
        customer_uuid=customer_uuid,
        has_pending_action=has_pending_action,
        modified_before=modified_before,
        o=o,
        offering_uuid=offering_uuid,
        paused_by_limit=paused_by_limit,
        pending_action=pending_action,
        project_uuid=project_uuid,
        provider_uuid=provider_uuid,
        resource_uuid=resource_uuid,
        state=state,
        user_uuid=user_uuid,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    customer_uuid: Union[Unset, UUID] = UNSET,
    has_pending_action: Union[Unset, bool] = UNSET,
    modified_before: Union[Unset, datetime.datetime] = UNSET,
    o: Union[Unset, list[ResourceApiKeyStatusOEnum]] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    paused_by_limit: Union[Unset, bool] = UNSET,
    pending_action: Union[Unset, list[ResourceApiKeyAction]] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    provider_uuid: Union[Unset, UUID] = UNSET,
    resource_uuid: Union[Unset, UUID] = UNSET,
    state: Union[Unset, list[ResourceApiKeyState]] = UNSET,
    user_uuid: Union[Unset, UUID] = UNSET,
) -> Response[int]:
    """Total API key usage of a resource, offering or provider

     Get number of items in the collection matching the request parameters.

    Args:
        customer_uuid (Union[Unset, UUID]):
        has_pending_action (Union[Unset, bool]):
        modified_before (Union[Unset, datetime.datetime]):
        o (Union[Unset, list[ResourceApiKeyStatusOEnum]]):
        offering_uuid (Union[Unset, UUID]):
        paused_by_limit (Union[Unset, bool]):
        pending_action (Union[Unset, list[ResourceApiKeyAction]]):
        project_uuid (Union[Unset, UUID]):
        provider_uuid (Union[Unset, UUID]):
        resource_uuid (Union[Unset, UUID]):
        state (Union[Unset, list[ResourceApiKeyState]]):
        user_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[int]
    """

    kwargs = _get_kwargs(
        customer_uuid=customer_uuid,
        has_pending_action=has_pending_action,
        modified_before=modified_before,
        o=o,
        offering_uuid=offering_uuid,
        paused_by_limit=paused_by_limit,
        pending_action=pending_action,
        project_uuid=project_uuid,
        provider_uuid=provider_uuid,
        resource_uuid=resource_uuid,
        state=state,
        user_uuid=user_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    customer_uuid: Union[Unset, UUID] = UNSET,
    has_pending_action: Union[Unset, bool] = UNSET,
    modified_before: Union[Unset, datetime.datetime] = UNSET,
    o: Union[Unset, list[ResourceApiKeyStatusOEnum]] = UNSET,
    offering_uuid: Union[Unset, UUID] = UNSET,
    paused_by_limit: Union[Unset, bool] = UNSET,
    pending_action: Union[Unset, list[ResourceApiKeyAction]] = UNSET,
    project_uuid: Union[Unset, UUID] = UNSET,
    provider_uuid: Union[Unset, UUID] = UNSET,
    resource_uuid: Union[Unset, UUID] = UNSET,
    state: Union[Unset, list[ResourceApiKeyState]] = UNSET,
    user_uuid: Union[Unset, UUID] = UNSET,
) -> int:
    """Total API key usage of a resource, offering or provider

     Get number of items in the collection matching the request parameters.

    Args:
        customer_uuid (Union[Unset, UUID]):
        has_pending_action (Union[Unset, bool]):
        modified_before (Union[Unset, datetime.datetime]):
        o (Union[Unset, list[ResourceApiKeyStatusOEnum]]):
        offering_uuid (Union[Unset, UUID]):
        paused_by_limit (Union[Unset, bool]):
        pending_action (Union[Unset, list[ResourceApiKeyAction]]):
        project_uuid (Union[Unset, UUID]):
        provider_uuid (Union[Unset, UUID]):
        resource_uuid (Union[Unset, UUID]):
        state (Union[Unset, list[ResourceApiKeyState]]):
        user_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        int
    """

    return (
        await asyncio_detailed(
            client=client,
            customer_uuid=customer_uuid,
            has_pending_action=has_pending_action,
            modified_before=modified_before,
            o=o,
            offering_uuid=offering_uuid,
            paused_by_limit=paused_by_limit,
            pending_action=pending_action,
            project_uuid=project_uuid,
            provider_uuid=provider_uuid,
            resource_uuid=resource_uuid,
            state=state,
            user_uuid=user_uuid,
        )
    ).parsed
