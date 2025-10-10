from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.onboarding_justification import OnboardingJustification
from ...models.onboarding_justification_review_request import OnboardingJustificationReviewRequest
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    *,
    body: OnboardingJustificationReviewRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/onboarding-justifications/{uuid}/approve/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> OnboardingJustification:
    if response.status_code == 200:
        response_200 = OnboardingJustification.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OnboardingJustification]:
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
    body: OnboardingJustificationReviewRequest,
) -> Response[OnboardingJustification]:
    """Approve justification and mark verification as VERIFIED.

    Args:
        uuid (UUID):
        body (OnboardingJustificationReviewRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OnboardingJustification]
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
    body: OnboardingJustificationReviewRequest,
) -> OnboardingJustification:
    """Approve justification and mark verification as VERIFIED.

    Args:
        uuid (UUID):
        body (OnboardingJustificationReviewRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OnboardingJustification
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
    body: OnboardingJustificationReviewRequest,
) -> Response[OnboardingJustification]:
    """Approve justification and mark verification as VERIFIED.

    Args:
        uuid (UUID):
        body (OnboardingJustificationReviewRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OnboardingJustification]
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
    body: OnboardingJustificationReviewRequest,
) -> OnboardingJustification:
    """Approve justification and mark verification as VERIFIED.

    Args:
        uuid (UUID):
        body (OnboardingJustificationReviewRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OnboardingJustification
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
