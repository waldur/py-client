from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.notification_preview import NotificationPreview
from ...models.recipient_enum import RecipientEnum
from ...models.trigger_enum import TriggerEnum
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    days_before: Union[Unset, int] = UNSET,
    mail_type: Union[Unset, str] = UNSET,
    recipient: Union[Unset, RecipientEnum] = UNSET,
    step: Union[Unset, str] = UNSET,
    trigger: Union[Unset, TriggerEnum] = UNSET,
    variant: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["days_before"] = days_before

    params["mail_type"] = mail_type

    json_recipient: Union[Unset, str] = UNSET
    if not isinstance(recipient, Unset):
        json_recipient = recipient.value

    params["recipient"] = json_recipient

    params["step"] = step

    json_trigger: Union[Unset, str] = UNSET
    if not isinstance(trigger, Unset):
        json_trigger = trigger.value

    params["trigger"] = json_trigger

    params["variant"] = variant

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/proposal-protected-calls/{uuid}/notification_preview/",
        "params": params,
    }

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
    days_before: Union[Unset, int] = UNSET,
    mail_type: Union[Unset, str] = UNSET,
    recipient: Union[Unset, RecipientEnum] = UNSET,
    step: Union[Unset, str] = UNSET,
    trigger: Union[Unset, TriggerEnum] = UNSET,
    variant: Union[Unset, str] = UNSET,
) -> Response[NotificationPreview]:
    """Preview a mail of the call

     The mail a notification rule's cell -- step, trigger and recipient -- or a mail type would send,
    rendered with the real templates and the call's own wording, on a synthetic proposal of the call:
    subject, text and HTML. Nothing is sent or kept, and no real person is named. For those who
    configure the call, staff and support.

    Args:
        uuid (UUID):
        days_before (Union[Unset, int]):
        mail_type (Union[Unset, str]):
        recipient (Union[Unset, RecipientEnum]):
        step (Union[Unset, str]):
        trigger (Union[Unset, TriggerEnum]):
        variant (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NotificationPreview]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        days_before=days_before,
        mail_type=mail_type,
        recipient=recipient,
        step=step,
        trigger=trigger,
        variant=variant,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    days_before: Union[Unset, int] = UNSET,
    mail_type: Union[Unset, str] = UNSET,
    recipient: Union[Unset, RecipientEnum] = UNSET,
    step: Union[Unset, str] = UNSET,
    trigger: Union[Unset, TriggerEnum] = UNSET,
    variant: Union[Unset, str] = UNSET,
) -> NotificationPreview:
    """Preview a mail of the call

     The mail a notification rule's cell -- step, trigger and recipient -- or a mail type would send,
    rendered with the real templates and the call's own wording, on a synthetic proposal of the call:
    subject, text and HTML. Nothing is sent or kept, and no real person is named. For those who
    configure the call, staff and support.

    Args:
        uuid (UUID):
        days_before (Union[Unset, int]):
        mail_type (Union[Unset, str]):
        recipient (Union[Unset, RecipientEnum]):
        step (Union[Unset, str]):
        trigger (Union[Unset, TriggerEnum]):
        variant (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NotificationPreview
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        days_before=days_before,
        mail_type=mail_type,
        recipient=recipient,
        step=step,
        trigger=trigger,
        variant=variant,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    days_before: Union[Unset, int] = UNSET,
    mail_type: Union[Unset, str] = UNSET,
    recipient: Union[Unset, RecipientEnum] = UNSET,
    step: Union[Unset, str] = UNSET,
    trigger: Union[Unset, TriggerEnum] = UNSET,
    variant: Union[Unset, str] = UNSET,
) -> Response[NotificationPreview]:
    """Preview a mail of the call

     The mail a notification rule's cell -- step, trigger and recipient -- or a mail type would send,
    rendered with the real templates and the call's own wording, on a synthetic proposal of the call:
    subject, text and HTML. Nothing is sent or kept, and no real person is named. For those who
    configure the call, staff and support.

    Args:
        uuid (UUID):
        days_before (Union[Unset, int]):
        mail_type (Union[Unset, str]):
        recipient (Union[Unset, RecipientEnum]):
        step (Union[Unset, str]):
        trigger (Union[Unset, TriggerEnum]):
        variant (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NotificationPreview]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        days_before=days_before,
        mail_type=mail_type,
        recipient=recipient,
        step=step,
        trigger=trigger,
        variant=variant,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    days_before: Union[Unset, int] = UNSET,
    mail_type: Union[Unset, str] = UNSET,
    recipient: Union[Unset, RecipientEnum] = UNSET,
    step: Union[Unset, str] = UNSET,
    trigger: Union[Unset, TriggerEnum] = UNSET,
    variant: Union[Unset, str] = UNSET,
) -> NotificationPreview:
    """Preview a mail of the call

     The mail a notification rule's cell -- step, trigger and recipient -- or a mail type would send,
    rendered with the real templates and the call's own wording, on a synthetic proposal of the call:
    subject, text and HTML. Nothing is sent or kept, and no real person is named. For those who
    configure the call, staff and support.

    Args:
        uuid (UUID):
        days_before (Union[Unset, int]):
        mail_type (Union[Unset, str]):
        recipient (Union[Unset, RecipientEnum]):
        step (Union[Unset, str]):
        trigger (Union[Unset, TriggerEnum]):
        variant (Union[Unset, str]):

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
            days_before=days_before,
            mail_type=mail_type,
            recipient=recipient,
            step=step,
            trigger=trigger,
            variant=variant,
        )
    ).parsed
