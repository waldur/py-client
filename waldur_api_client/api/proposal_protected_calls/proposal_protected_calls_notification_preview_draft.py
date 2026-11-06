from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.notification_preview import NotificationPreview
from ...models.notification_preview_draft_request import NotificationPreviewDraftRequest
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    *,
    body: NotificationPreviewDraftRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/proposal-protected-calls/{uuid}/notification_preview_draft/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> NotificationPreview:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = NotificationPreview.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[NotificationPreview]:
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
    body: NotificationPreviewDraftRequest,
) -> Response[NotificationPreview]:
    """Preview a draft of the call's wording of a mail

     As notification_preview, in the wording given -- subject, text body and HTML body -- which is
    validated in the sandbox and not saved. For those who may update the call.

    Args:
        uuid (UUID):
        body (NotificationPreviewDraftRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NotificationPreview]
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
    body: NotificationPreviewDraftRequest,
) -> NotificationPreview:
    """Preview a draft of the call's wording of a mail

     As notification_preview, in the wording given -- subject, text body and HTML body -- which is
    validated in the sandbox and not saved. For those who may update the call.

    Args:
        uuid (UUID):
        body (NotificationPreviewDraftRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NotificationPreview
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
    body: NotificationPreviewDraftRequest,
) -> Response[NotificationPreview]:
    """Preview a draft of the call's wording of a mail

     As notification_preview, in the wording given -- subject, text body and HTML body -- which is
    validated in the sandbox and not saved. For those who may update the call.

    Args:
        uuid (UUID):
        body (NotificationPreviewDraftRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NotificationPreview]
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
    body: NotificationPreviewDraftRequest,
) -> NotificationPreview:
    """Preview a draft of the call's wording of a mail

     As notification_preview, in the wording given -- subject, text body and HTML body -- which is
    validated in the sandbox and not saved. For those who may update the call.

    Args:
        uuid (UUID):
        body (NotificationPreviewDraftRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NotificationPreview
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
