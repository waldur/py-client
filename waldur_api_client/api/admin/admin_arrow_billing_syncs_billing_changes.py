from http import HTTPStatus
from typing import Any, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.billing_changes_job import BillingChangesJob
from ...models.billing_changes_request_request import BillingChangesRequestRequest
from ...types import Response


def _get_kwargs(
    *,
    body: BillingChangesRequestRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/admin/arrow/billing-syncs/billing_changes/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[Any, BillingChangesJob]:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 202:
        response_202 = BillingChangesJob.from_dict(response.json())

        return response_202
    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, BillingChangesJob]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BillingChangesRequestRequest,
) -> Response[Union[Any, BillingChangesJob]]:
    """Start an Arrow billing action as a background job that reports the invoice items it creates, changes
    or deletes. With dry_run (the default) nothing is kept, so the report is a preview of applying the
    same action. Poll billing_changes_job for the report.

    Args:
        body (BillingChangesRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BillingChangesJob]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: BillingChangesRequestRequest,
) -> Union[Any, BillingChangesJob]:
    """Start an Arrow billing action as a background job that reports the invoice items it creates, changes
    or deletes. With dry_run (the default) nothing is kept, so the report is a preview of applying the
    same action. Poll billing_changes_job for the report.

    Args:
        body (BillingChangesRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BillingChangesJob]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BillingChangesRequestRequest,
) -> Response[Union[Any, BillingChangesJob]]:
    """Start an Arrow billing action as a background job that reports the invoice items it creates, changes
    or deletes. With dry_run (the default) nothing is kept, so the report is a preview of applying the
    same action. Poll billing_changes_job for the report.

    Args:
        body (BillingChangesRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BillingChangesJob]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BillingChangesRequestRequest,
) -> Union[Any, BillingChangesJob]:
    """Start an Arrow billing action as a background job that reports the invoice items it creates, changes
    or deletes. With dry_run (the default) nothing is kept, so the report is a preview of applying the
    same action. Poll billing_changes_job for the report.

    Args:
        body (BillingChangesRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BillingChangesJob]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
