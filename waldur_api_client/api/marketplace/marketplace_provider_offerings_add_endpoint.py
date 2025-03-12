from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.nested_endpoint import NestedEndpoint
from ...models.nested_endpoint_request import NestedEndpointRequest
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    *,
    body: Union[
        NestedEndpointRequest,
        NestedEndpointRequest,
        NestedEndpointRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/marketplace-provider-offerings/{uuid}/add_endpoint/",
    }

    if isinstance(body, NestedEndpointRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, NestedEndpointRequest):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, NestedEndpointRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[NestedEndpoint]:
    if response.status_code == 200:
        response_200 = NestedEndpoint.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[NestedEndpoint]:
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
    body: Union[
        NestedEndpointRequest,
        NestedEndpointRequest,
        NestedEndpointRequest,
    ],
) -> Response[NestedEndpoint]:
    """Add endpoint to offering.

    Args:
        uuid (UUID):
        body (NestedEndpointRequest):
        body (NestedEndpointRequest):
        body (NestedEndpointRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NestedEndpoint]
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
    body: Union[
        NestedEndpointRequest,
        NestedEndpointRequest,
        NestedEndpointRequest,
    ],
) -> Optional[NestedEndpoint]:
    """Add endpoint to offering.

    Args:
        uuid (UUID):
        body (NestedEndpointRequest):
        body (NestedEndpointRequest):
        body (NestedEndpointRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NestedEndpoint
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
    body: Union[
        NestedEndpointRequest,
        NestedEndpointRequest,
        NestedEndpointRequest,
    ],
) -> Response[NestedEndpoint]:
    """Add endpoint to offering.

    Args:
        uuid (UUID):
        body (NestedEndpointRequest):
        body (NestedEndpointRequest):
        body (NestedEndpointRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NestedEndpoint]
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
    body: Union[
        NestedEndpointRequest,
        NestedEndpointRequest,
        NestedEndpointRequest,
    ],
) -> Optional[NestedEndpoint]:
    """Add endpoint to offering.

    Args:
        uuid (UUID):
        body (NestedEndpointRequest):
        body (NestedEndpointRequest):
        body (NestedEndpointRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NestedEndpoint
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
