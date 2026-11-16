from http import HTTPStatus
from typing import Any, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.open_step_discussion_request import OpenStepDiscussionRequest
from ...models.step_discussion import StepDiscussion
from ...types import Response


def _get_kwargs(
    *,
    body: OpenStepDiscussionRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/proposal-step-discussions/open/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> StepDiscussion:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = StepDiscussion.from_dict(response.json())

        return response_200
    if response.status_code == 201:
        response_201 = StepDiscussion.from_dict(response.json())

        return response_201
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[StepDiscussion]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: OpenStepDiscussionRequest,
) -> Response[StepDiscussion]:
    """Open a step's discussion

     Open the discussion of a proposal's step, or of a round step for one of the call's panels, as one of
    the people working on it: 201 with the discussion the first time, which creates its Matrix room, 200
    with the same one afterwards. 403 for anyone who does not take part in it, before anything is said
    about the step's state. Then 400 when the step has no discussion or Matrix chat is disabled, 409
    when the step is not active or its discussion has closed.

    Args:
        body (OpenStepDiscussionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StepDiscussion]
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
    body: OpenStepDiscussionRequest,
) -> StepDiscussion:
    """Open a step's discussion

     Open the discussion of a proposal's step, or of a round step for one of the call's panels, as one of
    the people working on it: 201 with the discussion the first time, which creates its Matrix room, 200
    with the same one afterwards. 403 for anyone who does not take part in it, before anything is said
    about the step's state. Then 400 when the step has no discussion or Matrix chat is disabled, 409
    when the step is not active or its discussion has closed.

    Args:
        body (OpenStepDiscussionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StepDiscussion
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: OpenStepDiscussionRequest,
) -> Response[StepDiscussion]:
    """Open a step's discussion

     Open the discussion of a proposal's step, or of a round step for one of the call's panels, as one of
    the people working on it: 201 with the discussion the first time, which creates its Matrix room, 200
    with the same one afterwards. 403 for anyone who does not take part in it, before anything is said
    about the step's state. Then 400 when the step has no discussion or Matrix chat is disabled, 409
    when the step is not active or its discussion has closed.

    Args:
        body (OpenStepDiscussionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StepDiscussion]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: OpenStepDiscussionRequest,
) -> StepDiscussion:
    """Open a step's discussion

     Open the discussion of a proposal's step, or of a round step for one of the call's panels, as one of
    the people working on it: 201 with the discussion the first time, which creates its Matrix room, 200
    with the same one afterwards. 403 for anyone who does not take part in it, before anything is said
    about the step's state. Then 400 when the step has no discussion or Matrix chat is disabled, 409
    when the step is not active or its discussion has closed.

    Args:
        body (OpenStepDiscussionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StepDiscussion
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
