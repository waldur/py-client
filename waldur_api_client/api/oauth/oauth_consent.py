from http import HTTPStatus
from typing import Any, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.consent_decision_request import ConsentDecisionRequest
from ...models.consent_error import ConsentError
from ...models.consent_result import ConsentResult
from ...types import Response


def _get_kwargs(
    *,
    body: ConsentDecisionRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/oauth/consent/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[ConsentError, ConsentResult]:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = ConsentResult.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ConsentError.from_dict(response.json())

        return response_400
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ConsentError, ConsentResult]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ConsentDecisionRequest,
) -> Response[Union[ConsentError, ConsentResult]]:
    """Record the user's decision and return where to send the browser.

    Args:
        body (ConsentDecisionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ConsentError, ConsentResult]]
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
    body: ConsentDecisionRequest,
) -> Union[ConsentError, ConsentResult]:
    """Record the user's decision and return where to send the browser.

    Args:
        body (ConsentDecisionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ConsentError, ConsentResult]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ConsentDecisionRequest,
) -> Response[Union[ConsentError, ConsentResult]]:
    """Record the user's decision and return where to send the browser.

    Args:
        body (ConsentDecisionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ConsentError, ConsentResult]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ConsentDecisionRequest,
) -> Union[ConsentError, ConsentResult]:
    """Record the user's decision and return where to send the browser.

    Args:
        body (ConsentDecisionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ConsentError, ConsentResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
