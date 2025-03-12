from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.attachment import Attachment
from ...models.support_attachments_list_field_item import SupportAttachmentsListFieldItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    field: Union[Unset, list[SupportAttachmentsListFieldItem]] = UNSET,
    issue: Union[Unset, str] = UNSET,
    issue_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_field: Union[Unset, list[str]] = UNSET
    if not isinstance(field, Unset):
        json_field = []
        for field_item_data in field:
            field_item = field_item_data.value
            json_field.append(field_item)

    params["field"] = json_field

    params["issue"] = issue

    json_issue_uuid: Union[Unset, str] = UNSET
    if not isinstance(issue_uuid, Unset):
        json_issue_uuid = str(issue_uuid)
    params["issue_uuid"] = json_issue_uuid

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/support-attachments/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["Attachment"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_paginated_attachment_list_item_data in _response_200:
            componentsschemas_paginated_attachment_list_item = Attachment.from_dict(
                componentsschemas_paginated_attachment_list_item_data
            )

            response_200.append(componentsschemas_paginated_attachment_list_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["Attachment"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    field: Union[Unset, list[SupportAttachmentsListFieldItem]] = UNSET,
    issue: Union[Unset, str] = UNSET,
    issue_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[list["Attachment"]]:
    """
    Args:
        field (Union[Unset, list[SupportAttachmentsListFieldItem]]):
        issue (Union[Unset, str]):
        issue_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['Attachment']]
    """

    kwargs = _get_kwargs(
        field=field,
        issue=issue,
        issue_uuid=issue_uuid,
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
    field: Union[Unset, list[SupportAttachmentsListFieldItem]] = UNSET,
    issue: Union[Unset, str] = UNSET,
    issue_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Optional[list["Attachment"]]:
    """
    Args:
        field (Union[Unset, list[SupportAttachmentsListFieldItem]]):
        issue (Union[Unset, str]):
        issue_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['Attachment']
    """

    return sync_detailed(
        client=client,
        field=field,
        issue=issue,
        issue_uuid=issue_uuid,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    field: Union[Unset, list[SupportAttachmentsListFieldItem]] = UNSET,
    issue: Union[Unset, str] = UNSET,
    issue_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[list["Attachment"]]:
    """
    Args:
        field (Union[Unset, list[SupportAttachmentsListFieldItem]]):
        issue (Union[Unset, str]):
        issue_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['Attachment']]
    """

    kwargs = _get_kwargs(
        field=field,
        issue=issue,
        issue_uuid=issue_uuid,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    field: Union[Unset, list[SupportAttachmentsListFieldItem]] = UNSET,
    issue: Union[Unset, str] = UNSET,
    issue_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Optional[list["Attachment"]]:
    """
    Args:
        field (Union[Unset, list[SupportAttachmentsListFieldItem]]):
        issue (Union[Unset, str]):
        issue_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['Attachment']
    """

    return (
        await asyncio_detailed(
            client=client,
            field=field,
            issue=issue,
            issue_uuid=issue_uuid,
            page=page,
            page_size=page_size,
        )
    ).parsed
