from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.web_hook import WebHook
from ...models.web_hook_request import WebHookRequest
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        WebHookRequest,
        WebHookRequest,
        WebHookRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/hooks-web/",
    }

    if isinstance(body, WebHookRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, WebHookRequest):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, WebHookRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[WebHook]:
    if response.status_code == 201:
        response_201 = WebHook.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[WebHook]:
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
        WebHookRequest,
        WebHookRequest,
        WebHookRequest,
    ],
) -> Response[WebHook]:
    r"""When hook is activated, POST request is issued against destination URL with the following data:

    .. code-block:: javascript

        {
            \"timestamp\": \"2015-07-14T12:12:56.000000\",
            \"message\": \"Customer ABC LLC has been updated.\",
            \"type\": \"customer_update_succeeded\",
            \"context\": {
                \"user_native_name\": \"Walter Lebrowski\",
                \"customer_contact_details\": \"\",
                \"user_username\": \"Walter\",
                \"user_uuid\": \"1c3323fc4ae44120b57ec40dea1be6e6\",
                \"customer_uuid\": \"4633bbbb0b3a4b91bffc0e18f853de85\",
                \"ip_address\": \"8.8.8.8\",
                \"user_full_name\": \"Walter Lebrowski\",
                \"customer_abbreviation\": \"ABC LLC\",
                \"customer_name\": \"ABC LLC\"
            },
            \"levelname\": \"INFO\"
        }

    Note that context depends on event type.

    Args:
        body (WebHookRequest):
        body (WebHookRequest):
        body (WebHookRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebHook]
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
        WebHookRequest,
        WebHookRequest,
        WebHookRequest,
    ],
) -> Optional[WebHook]:
    r"""When hook is activated, POST request is issued against destination URL with the following data:

    .. code-block:: javascript

        {
            \"timestamp\": \"2015-07-14T12:12:56.000000\",
            \"message\": \"Customer ABC LLC has been updated.\",
            \"type\": \"customer_update_succeeded\",
            \"context\": {
                \"user_native_name\": \"Walter Lebrowski\",
                \"customer_contact_details\": \"\",
                \"user_username\": \"Walter\",
                \"user_uuid\": \"1c3323fc4ae44120b57ec40dea1be6e6\",
                \"customer_uuid\": \"4633bbbb0b3a4b91bffc0e18f853de85\",
                \"ip_address\": \"8.8.8.8\",
                \"user_full_name\": \"Walter Lebrowski\",
                \"customer_abbreviation\": \"ABC LLC\",
                \"customer_name\": \"ABC LLC\"
            },
            \"levelname\": \"INFO\"
        }

    Note that context depends on event type.

    Args:
        body (WebHookRequest):
        body (WebHookRequest):
        body (WebHookRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebHook
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        WebHookRequest,
        WebHookRequest,
        WebHookRequest,
    ],
) -> Response[WebHook]:
    r"""When hook is activated, POST request is issued against destination URL with the following data:

    .. code-block:: javascript

        {
            \"timestamp\": \"2015-07-14T12:12:56.000000\",
            \"message\": \"Customer ABC LLC has been updated.\",
            \"type\": \"customer_update_succeeded\",
            \"context\": {
                \"user_native_name\": \"Walter Lebrowski\",
                \"customer_contact_details\": \"\",
                \"user_username\": \"Walter\",
                \"user_uuid\": \"1c3323fc4ae44120b57ec40dea1be6e6\",
                \"customer_uuid\": \"4633bbbb0b3a4b91bffc0e18f853de85\",
                \"ip_address\": \"8.8.8.8\",
                \"user_full_name\": \"Walter Lebrowski\",
                \"customer_abbreviation\": \"ABC LLC\",
                \"customer_name\": \"ABC LLC\"
            },
            \"levelname\": \"INFO\"
        }

    Note that context depends on event type.

    Args:
        body (WebHookRequest):
        body (WebHookRequest):
        body (WebHookRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebHook]
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
        WebHookRequest,
        WebHookRequest,
        WebHookRequest,
    ],
) -> Optional[WebHook]:
    r"""When hook is activated, POST request is issued against destination URL with the following data:

    .. code-block:: javascript

        {
            \"timestamp\": \"2015-07-14T12:12:56.000000\",
            \"message\": \"Customer ABC LLC has been updated.\",
            \"type\": \"customer_update_succeeded\",
            \"context\": {
                \"user_native_name\": \"Walter Lebrowski\",
                \"customer_contact_details\": \"\",
                \"user_username\": \"Walter\",
                \"user_uuid\": \"1c3323fc4ae44120b57ec40dea1be6e6\",
                \"customer_uuid\": \"4633bbbb0b3a4b91bffc0e18f853de85\",
                \"ip_address\": \"8.8.8.8\",
                \"user_full_name\": \"Walter Lebrowski\",
                \"customer_abbreviation\": \"ABC LLC\",
                \"customer_name\": \"ABC LLC\"
            },
            \"levelname\": \"INFO\"
        }

    Note that context depends on event type.

    Args:
        body (WebHookRequest):
        body (WebHookRequest):
        body (WebHookRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebHook
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
