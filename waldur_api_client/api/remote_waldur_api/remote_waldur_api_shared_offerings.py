from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.remote_credentials_request import RemoteCredentialsRequest
from ...models.remote_offering import RemoteOffering
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: Union[
        RemoteCredentialsRequest,
        RemoteCredentialsRequest,
        RemoteCredentialsRequest,
    ],
    customer_uuid: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["customer_uuid"] = customer_uuid

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/remote-waldur-api/shared_offerings/",
        "params": params,
    }

    if isinstance(body, RemoteCredentialsRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, RemoteCredentialsRequest):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, RemoteCredentialsRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["RemoteOffering"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RemoteOffering.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["RemoteOffering"]]:
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
        RemoteCredentialsRequest,
        RemoteCredentialsRequest,
        RemoteCredentialsRequest,
    ],
    customer_uuid: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[list["RemoteOffering"]]:
    """List remote importable offerings for particular customer

    Args:
        customer_uuid (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        body (RemoteCredentialsRequest):
        body (RemoteCredentialsRequest):
        body (RemoteCredentialsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['RemoteOffering']]
    """

    kwargs = _get_kwargs(
        body=body,
        customer_uuid=customer_uuid,
        page=page,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: Union[
        RemoteCredentialsRequest,
        RemoteCredentialsRequest,
        RemoteCredentialsRequest,
    ],
    customer_uuid: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Optional[list["RemoteOffering"]]:
    """List remote importable offerings for particular customer

    Args:
        customer_uuid (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        body (RemoteCredentialsRequest):
        body (RemoteCredentialsRequest):
        body (RemoteCredentialsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['RemoteOffering']
    """

    return sync_detailed(
        client=client,
        body=body,
        customer_uuid=customer_uuid,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        RemoteCredentialsRequest,
        RemoteCredentialsRequest,
        RemoteCredentialsRequest,
    ],
    customer_uuid: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[list["RemoteOffering"]]:
    """List remote importable offerings for particular customer

    Args:
        customer_uuid (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        body (RemoteCredentialsRequest):
        body (RemoteCredentialsRequest):
        body (RemoteCredentialsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['RemoteOffering']]
    """

    kwargs = _get_kwargs(
        body=body,
        customer_uuid=customer_uuid,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Union[
        RemoteCredentialsRequest,
        RemoteCredentialsRequest,
        RemoteCredentialsRequest,
    ],
    customer_uuid: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Optional[list["RemoteOffering"]]:
    """List remote importable offerings for particular customer

    Args:
        customer_uuid (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        body (RemoteCredentialsRequest):
        body (RemoteCredentialsRequest):
        body (RemoteCredentialsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['RemoteOffering']
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            customer_uuid=customer_uuid,
            page=page,
            page_size=page_size,
        )
    ).parsed
