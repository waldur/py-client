from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_feedback import CreateFeedback
from ...models.create_feedback_request import CreateFeedbackRequest
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        CreateFeedbackRequest,
        CreateFeedbackRequest,
        CreateFeedbackRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/support-feedbacks/",
    }

    if isinstance(body, CreateFeedbackRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateFeedbackRequest):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, CreateFeedbackRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CreateFeedback]:
    if response.status_code == 201:
        response_201 = CreateFeedback.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CreateFeedback]:
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
        CreateFeedbackRequest,
        CreateFeedbackRequest,
        CreateFeedbackRequest,
    ],
) -> Response[CreateFeedback]:
    """
    Args:
        body (CreateFeedbackRequest):
        body (CreateFeedbackRequest):
        body (CreateFeedbackRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateFeedback]
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
        CreateFeedbackRequest,
        CreateFeedbackRequest,
        CreateFeedbackRequest,
    ],
) -> Optional[CreateFeedback]:
    """
    Args:
        body (CreateFeedbackRequest):
        body (CreateFeedbackRequest):
        body (CreateFeedbackRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateFeedback
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateFeedbackRequest,
        CreateFeedbackRequest,
        CreateFeedbackRequest,
    ],
) -> Response[CreateFeedback]:
    """
    Args:
        body (CreateFeedbackRequest):
        body (CreateFeedbackRequest):
        body (CreateFeedbackRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateFeedback]
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
        CreateFeedbackRequest,
        CreateFeedbackRequest,
        CreateFeedbackRequest,
    ],
) -> Optional[CreateFeedback]:
    """
    Args:
        body (CreateFeedbackRequest):
        body (CreateFeedbackRequest):
        body (CreateFeedbackRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateFeedback
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
