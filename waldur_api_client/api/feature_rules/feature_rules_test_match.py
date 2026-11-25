from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.feature_rule_test_match_request_request import FeatureRuleTestMatchRequestRequest
from ...models.feature_rule_test_match_response import FeatureRuleTestMatchResponse
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    *,
    body: FeatureRuleTestMatchRequestRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/feature-rules/{uuid}/test-match/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> FeatureRuleTestMatchResponse:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = FeatureRuleTestMatchResponse.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[FeatureRuleTestMatchResponse]:
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
    body: FeatureRuleTestMatchRequestRequest,
) -> Response[FeatureRuleTestMatchResponse]:
    """Evaluate a feature rule against a user

     Checks each criterion of this rule against the given user and reports whether the rule matches.
    Nothing is changed.

    Args:
        uuid (UUID):
        body (FeatureRuleTestMatchRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FeatureRuleTestMatchResponse]
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
    body: FeatureRuleTestMatchRequestRequest,
) -> FeatureRuleTestMatchResponse:
    """Evaluate a feature rule against a user

     Checks each criterion of this rule against the given user and reports whether the rule matches.
    Nothing is changed.

    Args:
        uuid (UUID):
        body (FeatureRuleTestMatchRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FeatureRuleTestMatchResponse
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
    body: FeatureRuleTestMatchRequestRequest,
) -> Response[FeatureRuleTestMatchResponse]:
    """Evaluate a feature rule against a user

     Checks each criterion of this rule against the given user and reports whether the rule matches.
    Nothing is changed.

    Args:
        uuid (UUID):
        body (FeatureRuleTestMatchRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FeatureRuleTestMatchResponse]
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
    body: FeatureRuleTestMatchRequestRequest,
) -> FeatureRuleTestMatchResponse:
    """Evaluate a feature rule against a user

     Checks each criterion of this rule against the given user and reports whether the rule matches.
    Nothing is changed.

    Args:
        uuid (UUID):
        body (FeatureRuleTestMatchRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FeatureRuleTestMatchResponse
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
