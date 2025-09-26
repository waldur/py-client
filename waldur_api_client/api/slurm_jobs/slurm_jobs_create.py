from http import HTTPStatus
from typing import Any, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.firecrest_job import FirecrestJob
from ...models.firecrest_job_request import FirecrestJobRequest
from ...models.firecrest_job_request_form import FirecrestJobRequestForm
from ...models.firecrest_job_request_multipart import FirecrestJobRequestMultipart
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        FirecrestJobRequest,
        FirecrestJobRequestForm,
        FirecrestJobRequestMultipart,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/slurm-jobs/",
    }

    if isinstance(body, FirecrestJobRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, FirecrestJobRequestForm):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, FirecrestJobRequestMultipart):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> FirecrestJob:
    if response.status_code == 201:
        response_201 = FirecrestJob.from_dict(response.json())

        return response_201
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[FirecrestJob]:
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
        FirecrestJobRequest,
        FirecrestJobRequestForm,
        FirecrestJobRequestMultipart,
    ],
) -> Response[FirecrestJob]:
    """
    Args:
        body (FirecrestJobRequest):
        body (FirecrestJobRequestForm):
        body (FirecrestJobRequestMultipart):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FirecrestJob]
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
        FirecrestJobRequest,
        FirecrestJobRequestForm,
        FirecrestJobRequestMultipart,
    ],
) -> FirecrestJob:
    """
    Args:
        body (FirecrestJobRequest):
        body (FirecrestJobRequestForm):
        body (FirecrestJobRequestMultipart):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FirecrestJob
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        FirecrestJobRequest,
        FirecrestJobRequestForm,
        FirecrestJobRequestMultipart,
    ],
) -> Response[FirecrestJob]:
    """
    Args:
        body (FirecrestJobRequest):
        body (FirecrestJobRequestForm):
        body (FirecrestJobRequestMultipart):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FirecrestJob]
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
        FirecrestJobRequest,
        FirecrestJobRequestForm,
        FirecrestJobRequestMultipart,
    ],
) -> FirecrestJob:
    """
    Args:
        body (FirecrestJobRequest):
        body (FirecrestJobRequestForm):
        body (FirecrestJobRequestMultipart):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FirecrestJob
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
