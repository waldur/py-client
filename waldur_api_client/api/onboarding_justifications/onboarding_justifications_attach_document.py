from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.onboarding_justification_documentation import OnboardingJustificationDocumentation
from ...models.onboarding_justification_documentation_request import OnboardingJustificationDocumentationRequest
from ...models.onboarding_justification_documentation_request_form import (
    OnboardingJustificationDocumentationRequestForm,
)
from ...models.onboarding_justification_documentation_request_multipart import (
    OnboardingJustificationDocumentationRequestMultipart,
)
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    *,
    body: Union[
        OnboardingJustificationDocumentationRequest,
        OnboardingJustificationDocumentationRequestForm,
        OnboardingJustificationDocumentationRequestMultipart,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/onboarding-justifications/{uuid}/attach_document/",
    }

    if isinstance(body, OnboardingJustificationDocumentationRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, OnboardingJustificationDocumentationRequestForm):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, OnboardingJustificationDocumentationRequestMultipart):
        _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> OnboardingJustificationDocumentation:
    if response.status_code == 200:
        response_200 = OnboardingJustificationDocumentation.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OnboardingJustificationDocumentation]:
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
        OnboardingJustificationDocumentationRequest,
        OnboardingJustificationDocumentationRequestForm,
        OnboardingJustificationDocumentationRequestMultipart,
    ],
) -> Response[OnboardingJustificationDocumentation]:
    """Attach supporting document to justification.

    Args:
        uuid (UUID):
        body (OnboardingJustificationDocumentationRequest):
        body (OnboardingJustificationDocumentationRequestForm):
        body (OnboardingJustificationDocumentationRequestMultipart):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OnboardingJustificationDocumentation]
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
        OnboardingJustificationDocumentationRequest,
        OnboardingJustificationDocumentationRequestForm,
        OnboardingJustificationDocumentationRequestMultipart,
    ],
) -> OnboardingJustificationDocumentation:
    """Attach supporting document to justification.

    Args:
        uuid (UUID):
        body (OnboardingJustificationDocumentationRequest):
        body (OnboardingJustificationDocumentationRequestForm):
        body (OnboardingJustificationDocumentationRequestMultipart):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OnboardingJustificationDocumentation
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
        OnboardingJustificationDocumentationRequest,
        OnboardingJustificationDocumentationRequestForm,
        OnboardingJustificationDocumentationRequestMultipart,
    ],
) -> Response[OnboardingJustificationDocumentation]:
    """Attach supporting document to justification.

    Args:
        uuid (UUID):
        body (OnboardingJustificationDocumentationRequest):
        body (OnboardingJustificationDocumentationRequestForm):
        body (OnboardingJustificationDocumentationRequestMultipart):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OnboardingJustificationDocumentation]
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
        OnboardingJustificationDocumentationRequest,
        OnboardingJustificationDocumentationRequestForm,
        OnboardingJustificationDocumentationRequestMultipart,
    ],
) -> OnboardingJustificationDocumentation:
    """Attach supporting document to justification.

    Args:
        uuid (UUID):
        body (OnboardingJustificationDocumentationRequest):
        body (OnboardingJustificationDocumentationRequestForm):
        body (OnboardingJustificationDocumentationRequestMultipart):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OnboardingJustificationDocumentation
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
