from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.azure_sql_database_create import AzureSqlDatabaseCreate
from ...models.azure_sql_database_create_request import AzureSqlDatabaseCreateRequest
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    *,
    body: Union[
        AzureSqlDatabaseCreateRequest,
        AzureSqlDatabaseCreateRequest,
        AzureSqlDatabaseCreateRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/azure-sql-servers/{uuid}/create_database/",
    }

    if isinstance(body, AzureSqlDatabaseCreateRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, AzureSqlDatabaseCreateRequest):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, AzureSqlDatabaseCreateRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AzureSqlDatabaseCreate]:
    if response.status_code == 200:
        response_200 = AzureSqlDatabaseCreate.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AzureSqlDatabaseCreate]:
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
        AzureSqlDatabaseCreateRequest,
        AzureSqlDatabaseCreateRequest,
        AzureSqlDatabaseCreateRequest,
    ],
) -> Response[AzureSqlDatabaseCreate]:
    """
    Args:
        uuid (UUID):
        body (AzureSqlDatabaseCreateRequest):
        body (AzureSqlDatabaseCreateRequest):
        body (AzureSqlDatabaseCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AzureSqlDatabaseCreate]
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
        AzureSqlDatabaseCreateRequest,
        AzureSqlDatabaseCreateRequest,
        AzureSqlDatabaseCreateRequest,
    ],
) -> Optional[AzureSqlDatabaseCreate]:
    """
    Args:
        uuid (UUID):
        body (AzureSqlDatabaseCreateRequest):
        body (AzureSqlDatabaseCreateRequest):
        body (AzureSqlDatabaseCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AzureSqlDatabaseCreate
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
        AzureSqlDatabaseCreateRequest,
        AzureSqlDatabaseCreateRequest,
        AzureSqlDatabaseCreateRequest,
    ],
) -> Response[AzureSqlDatabaseCreate]:
    """
    Args:
        uuid (UUID):
        body (AzureSqlDatabaseCreateRequest):
        body (AzureSqlDatabaseCreateRequest):
        body (AzureSqlDatabaseCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AzureSqlDatabaseCreate]
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
        AzureSqlDatabaseCreateRequest,
        AzureSqlDatabaseCreateRequest,
        AzureSqlDatabaseCreateRequest,
    ],
) -> Optional[AzureSqlDatabaseCreate]:
    """
    Args:
        uuid (UUID):
        body (AzureSqlDatabaseCreateRequest):
        body (AzureSqlDatabaseCreateRequest):
        body (AzureSqlDatabaseCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AzureSqlDatabaseCreate
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
