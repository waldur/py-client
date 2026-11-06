from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.call_save_as_template_request import CallSaveAsTemplateRequest
from ...models.call_template import CallTemplate
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    *,
    body: CallSaveAsTemplateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/proposal-protected-calls/{uuid}/save_as_template/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> CallTemplate:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 201:
        response_201 = CallTemplate.from_dict(response.json())

        return response_201
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[CallTemplate]:
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
    body: CallSaveAsTemplateRequest,
) -> Response[CallTemplate]:
    """Save call configuration as a template

     Save the call's settings and workflow -- proposal roles, steps, notification rules and the steps'
    forms -- as a new, unpublished call template. Rounds, requested offerings and documents are left
    out. Staff only: the template carries the call's forms, which publishing it shows to every call
    manager.

    Args:
        uuid (UUID):
        body (CallSaveAsTemplateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CallTemplate]
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
    body: CallSaveAsTemplateRequest,
) -> CallTemplate:
    """Save call configuration as a template

     Save the call's settings and workflow -- proposal roles, steps, notification rules and the steps'
    forms -- as a new, unpublished call template. Rounds, requested offerings and documents are left
    out. Staff only: the template carries the call's forms, which publishing it shows to every call
    manager.

    Args:
        uuid (UUID):
        body (CallSaveAsTemplateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CallTemplate
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
    body: CallSaveAsTemplateRequest,
) -> Response[CallTemplate]:
    """Save call configuration as a template

     Save the call's settings and workflow -- proposal roles, steps, notification rules and the steps'
    forms -- as a new, unpublished call template. Rounds, requested offerings and documents are left
    out. Staff only: the template carries the call's forms, which publishing it shows to every call
    manager.

    Args:
        uuid (UUID):
        body (CallSaveAsTemplateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CallTemplate]
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
    body: CallSaveAsTemplateRequest,
) -> CallTemplate:
    """Save call configuration as a template

     Save the call's settings and workflow -- proposal roles, steps, notification rules and the steps'
    forms -- as a new, unpublished call template. Rounds, requested offerings and documents are left
    out. Staff only: the template carries the call's forms, which publishing it shows to every call
    manager.

    Args:
        uuid (UUID):
        body (CallSaveAsTemplateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CallTemplate
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
