from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patched_requested_resource_request import PatchedRequestedResourceRequest
from ...models.requested_resource import RequestedResource
from ...types import Response


def _get_kwargs(
    uuid: str,
    obj_uuid: str,
    *,
    body: Union[
        PatchedRequestedResourceRequest,
        PatchedRequestedResourceRequest,
        PatchedRequestedResourceRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/api/proposal-proposals/{uuid}/resources/{obj_uuid}/",
    }

    if isinstance(body, PatchedRequestedResourceRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedRequestedResourceRequest):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedRequestedResourceRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[RequestedResource]:
    if response.status_code == 200:
        response_200 = RequestedResource.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[RequestedResource]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: str,
    obj_uuid: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        PatchedRequestedResourceRequest,
        PatchedRequestedResourceRequest,
        PatchedRequestedResourceRequest,
    ],
) -> Response[RequestedResource]:
    """
    Args:
        uuid (str):
        obj_uuid (str):
        body (PatchedRequestedResourceRequest):
        body (PatchedRequestedResourceRequest):
        body (PatchedRequestedResourceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RequestedResource]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        obj_uuid=obj_uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: str,
    obj_uuid: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        PatchedRequestedResourceRequest,
        PatchedRequestedResourceRequest,
        PatchedRequestedResourceRequest,
    ],
) -> Optional[RequestedResource]:
    """
    Args:
        uuid (str):
        obj_uuid (str):
        body (PatchedRequestedResourceRequest):
        body (PatchedRequestedResourceRequest):
        body (PatchedRequestedResourceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RequestedResource
    """

    return sync_detailed(
        uuid=uuid,
        obj_uuid=obj_uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    obj_uuid: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        PatchedRequestedResourceRequest,
        PatchedRequestedResourceRequest,
        PatchedRequestedResourceRequest,
    ],
) -> Response[RequestedResource]:
    """
    Args:
        uuid (str):
        obj_uuid (str):
        body (PatchedRequestedResourceRequest):
        body (PatchedRequestedResourceRequest):
        body (PatchedRequestedResourceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RequestedResource]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        obj_uuid=obj_uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: str,
    obj_uuid: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        PatchedRequestedResourceRequest,
        PatchedRequestedResourceRequest,
        PatchedRequestedResourceRequest,
    ],
) -> Optional[RequestedResource]:
    """
    Args:
        uuid (str):
        obj_uuid (str):
        body (PatchedRequestedResourceRequest):
        body (PatchedRequestedResourceRequest):
        body (PatchedRequestedResourceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RequestedResource
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            obj_uuid=obj_uuid,
            client=client,
            body=body,
        )
    ).parsed
