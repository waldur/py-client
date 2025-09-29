from http import HTTPStatus
from typing import Any, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.checklist_category import ChecklistCategory
from ...models.checklist_category_request import ChecklistCategoryRequest
from ...models.checklist_category_request_form import ChecklistCategoryRequestForm
from ...models.checklist_category_request_multipart import ChecklistCategoryRequestMultipart
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        ChecklistCategoryRequest,
        ChecklistCategoryRequestForm,
        ChecklistCategoryRequestMultipart,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/checklists-admin-categories/",
    }

    if isinstance(body, ChecklistCategoryRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, ChecklistCategoryRequestForm):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, ChecklistCategoryRequestMultipart):
        _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> ChecklistCategory:
    if response.status_code == 201:
        response_201 = ChecklistCategory.from_dict(response.json())

        return response_201
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ChecklistCategory]:
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
        ChecklistCategoryRequest,
        ChecklistCategoryRequestForm,
        ChecklistCategoryRequestMultipart,
    ],
) -> Response[ChecklistCategory]:
    """
    Args:
        body (ChecklistCategoryRequest):
        body (ChecklistCategoryRequestForm):
        body (ChecklistCategoryRequestMultipart):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChecklistCategory]
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
        ChecklistCategoryRequest,
        ChecklistCategoryRequestForm,
        ChecklistCategoryRequestMultipart,
    ],
) -> ChecklistCategory:
    """
    Args:
        body (ChecklistCategoryRequest):
        body (ChecklistCategoryRequestForm):
        body (ChecklistCategoryRequestMultipart):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChecklistCategory
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        ChecklistCategoryRequest,
        ChecklistCategoryRequestForm,
        ChecklistCategoryRequestMultipart,
    ],
) -> Response[ChecklistCategory]:
    """
    Args:
        body (ChecklistCategoryRequest):
        body (ChecklistCategoryRequestForm):
        body (ChecklistCategoryRequestMultipart):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChecklistCategory]
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
        ChecklistCategoryRequest,
        ChecklistCategoryRequestForm,
        ChecklistCategoryRequestMultipart,
    ],
) -> ChecklistCategory:
    """
    Args:
        body (ChecklistCategoryRequest):
        body (ChecklistCategoryRequestForm):
        body (ChecklistCategoryRequestMultipart):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChecklistCategory
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
