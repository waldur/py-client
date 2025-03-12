from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.smax_web_hook_receiver import SmaxWebHookReceiver
from ...models.smax_web_hook_receiver_request import SmaxWebHookReceiverRequest
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        SmaxWebHookReceiverRequest,
        SmaxWebHookReceiverRequest,
        SmaxWebHookReceiverRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/support-smax-webhook/",
    }

    if isinstance(body, SmaxWebHookReceiverRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, SmaxWebHookReceiverRequest):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, SmaxWebHookReceiverRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SmaxWebHookReceiver]:
    if response.status_code == 200:
        response_200 = SmaxWebHookReceiver.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SmaxWebHookReceiver]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        SmaxWebHookReceiverRequest,
        SmaxWebHookReceiverRequest,
        SmaxWebHookReceiverRequest,
    ],
) -> Response[SmaxWebHookReceiver]:
    """
    Args:
        body (SmaxWebHookReceiverRequest):
        body (SmaxWebHookReceiverRequest):
        body (SmaxWebHookReceiverRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SmaxWebHookReceiver]
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
    client: Union[AuthenticatedClient, Client],
    body: Union[
        SmaxWebHookReceiverRequest,
        SmaxWebHookReceiverRequest,
        SmaxWebHookReceiverRequest,
    ],
) -> Optional[SmaxWebHookReceiver]:
    """
    Args:
        body (SmaxWebHookReceiverRequest):
        body (SmaxWebHookReceiverRequest):
        body (SmaxWebHookReceiverRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SmaxWebHookReceiver
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        SmaxWebHookReceiverRequest,
        SmaxWebHookReceiverRequest,
        SmaxWebHookReceiverRequest,
    ],
) -> Response[SmaxWebHookReceiver]:
    """
    Args:
        body (SmaxWebHookReceiverRequest):
        body (SmaxWebHookReceiverRequest):
        body (SmaxWebHookReceiverRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SmaxWebHookReceiver]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        SmaxWebHookReceiverRequest,
        SmaxWebHookReceiverRequest,
        SmaxWebHookReceiverRequest,
    ],
) -> Optional[SmaxWebHookReceiver]:
    """
    Args:
        body (SmaxWebHookReceiverRequest):
        body (SmaxWebHookReceiverRequest):
        body (SmaxWebHookReceiverRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SmaxWebHookReceiver
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
