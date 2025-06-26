from http import HTTPStatus
from typing import Any, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.pull_marketplace_script_resource_request import PullMarketplaceScriptResourceRequest
from ...types import Response


def _get_kwargs(
    *,
    body: PullMarketplaceScriptResourceRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/marketplace-script-sync-resource/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Any:
    if response.status_code == 202:
        return None
    if response.status_code == 404:
        return None
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PullMarketplaceScriptResourceRequest,
) -> Response[Any]:
    """This view allows a user to trigger a pull operation for a marketplace script resource.
            The user must be a service consumer and have access to the resource.
            The pull operation is performed asynchronously using Celery.

     Pull a marketplace script resource.

    Args:
        body (PullMarketplaceScriptResourceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PullMarketplaceScriptResourceRequest,
) -> Response[Any]:
    """This view allows a user to trigger a pull operation for a marketplace script resource.
            The user must be a service consumer and have access to the resource.
            The pull operation is performed asynchronously using Celery.

     Pull a marketplace script resource.

    Args:
        body (PullMarketplaceScriptResourceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
