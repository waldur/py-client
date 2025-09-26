from http import HTTPStatus
from typing import Any, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.offering_create import OfferingCreate
from ...models.offering_create_request import OfferingCreateRequest
from ...models.offering_create_request_form import OfferingCreateRequestForm
from ...models.offering_create_request_multipart import OfferingCreateRequestMultipart
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        OfferingCreateRequest,
        OfferingCreateRequestForm,
        OfferingCreateRequestMultipart,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/marketplace-provider-offerings/",
    }

    if isinstance(body, OfferingCreateRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, OfferingCreateRequestForm):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, OfferingCreateRequestMultipart):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> OfferingCreate:
    if response.status_code == 201:
        response_201 = OfferingCreate.from_dict(response.json())

        return response_201
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OfferingCreate]:
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
        OfferingCreateRequest,
        OfferingCreateRequestForm,
        OfferingCreateRequestMultipart,
    ],
) -> Response[OfferingCreate]:
    """
    Args:
        body (OfferingCreateRequest):
        body (OfferingCreateRequestForm):
        body (OfferingCreateRequestMultipart):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfferingCreate]
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
        OfferingCreateRequest,
        OfferingCreateRequestForm,
        OfferingCreateRequestMultipart,
    ],
) -> OfferingCreate:
    """
    Args:
        body (OfferingCreateRequest):
        body (OfferingCreateRequestForm):
        body (OfferingCreateRequestMultipart):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfferingCreate
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        OfferingCreateRequest,
        OfferingCreateRequestForm,
        OfferingCreateRequestMultipart,
    ],
) -> Response[OfferingCreate]:
    """
    Args:
        body (OfferingCreateRequest):
        body (OfferingCreateRequestForm):
        body (OfferingCreateRequestMultipart):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfferingCreate]
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
        OfferingCreateRequest,
        OfferingCreateRequestForm,
        OfferingCreateRequestMultipart,
    ],
) -> OfferingCreate:
    """
    Args:
        body (OfferingCreateRequest):
        body (OfferingCreateRequestForm):
        body (OfferingCreateRequestMultipart):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfferingCreate
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
