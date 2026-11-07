from http import HTTPStatus
from typing import Any, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.protected_call import ProtectedCall
from ...models.protected_call_request import ProtectedCallRequest
from ...models.protected_call_request_form import ProtectedCallRequestForm
from ...models.protected_call_request_multipart import ProtectedCallRequestMultipart
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        ProtectedCallRequest,
        ProtectedCallRequestForm,
        ProtectedCallRequestMultipart,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/proposal-protected-calls/",
    }

    if isinstance(body, ProtectedCallRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, ProtectedCallRequestForm):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, ProtectedCallRequestMultipart):
        _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> ProtectedCall:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 201:
        response_201 = ProtectedCall.from_dict(response.json())

        return response_201
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[ProtectedCall]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        ProtectedCallRequest,
        ProtectedCallRequestForm,
        ProtectedCallRequestMultipart,
    ],
) -> Response[ProtectedCall]:
    """
    Args:
        body (ProtectedCallRequest):
        body (ProtectedCallRequestForm):
        body (ProtectedCallRequestMultipart):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProtectedCall]
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
    body: Union[
        ProtectedCallRequest,
        ProtectedCallRequestForm,
        ProtectedCallRequestMultipart,
    ],
) -> ProtectedCall:
    """
    Args:
        body (ProtectedCallRequest):
        body (ProtectedCallRequestForm):
        body (ProtectedCallRequestMultipart):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProtectedCall
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        ProtectedCallRequest,
        ProtectedCallRequestForm,
        ProtectedCallRequestMultipart,
    ],
) -> Response[ProtectedCall]:
    """
    Args:
        body (ProtectedCallRequest):
        body (ProtectedCallRequestForm):
        body (ProtectedCallRequestMultipart):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProtectedCall]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Union[
        ProtectedCallRequest,
        ProtectedCallRequestForm,
        ProtectedCallRequestMultipart,
    ],
) -> ProtectedCall:
    """
    Args:
        body (ProtectedCallRequest):
        body (ProtectedCallRequestForm):
        body (ProtectedCallRequestMultipart):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProtectedCall
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
