from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.call_managing_organisation import CallManagingOrganisation
from ...models.patched_call_managing_organisation_request import PatchedCallManagingOrganisationRequest
from ...models.patched_call_managing_organisation_request_form import PatchedCallManagingOrganisationRequestForm
from ...models.patched_call_managing_organisation_request_multipart import (
    PatchedCallManagingOrganisationRequestMultipart,
)
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    *,
    body: Union[
        PatchedCallManagingOrganisationRequest,
        PatchedCallManagingOrganisationRequestForm,
        PatchedCallManagingOrganisationRequestMultipart,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/api/call-managing-organisations/{uuid}/",
    }

    if isinstance(body, PatchedCallManagingOrganisationRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedCallManagingOrganisationRequestForm):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedCallManagingOrganisationRequestMultipart):
        _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> CallManagingOrganisation:
    if response.status_code == 200:
        response_200 = CallManagingOrganisation.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CallManagingOrganisation]:
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
        PatchedCallManagingOrganisationRequest,
        PatchedCallManagingOrganisationRequestForm,
        PatchedCallManagingOrganisationRequestMultipart,
    ],
) -> Response[CallManagingOrganisation]:
    """
    Args:
        uuid (UUID):
        body (PatchedCallManagingOrganisationRequest):
        body (PatchedCallManagingOrganisationRequestForm):
        body (PatchedCallManagingOrganisationRequestMultipart):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CallManagingOrganisation]
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
        PatchedCallManagingOrganisationRequest,
        PatchedCallManagingOrganisationRequestForm,
        PatchedCallManagingOrganisationRequestMultipart,
    ],
) -> CallManagingOrganisation:
    """
    Args:
        uuid (UUID):
        body (PatchedCallManagingOrganisationRequest):
        body (PatchedCallManagingOrganisationRequestForm):
        body (PatchedCallManagingOrganisationRequestMultipart):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CallManagingOrganisation
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
        PatchedCallManagingOrganisationRequest,
        PatchedCallManagingOrganisationRequestForm,
        PatchedCallManagingOrganisationRequestMultipart,
    ],
) -> Response[CallManagingOrganisation]:
    """
    Args:
        uuid (UUID):
        body (PatchedCallManagingOrganisationRequest):
        body (PatchedCallManagingOrganisationRequestForm):
        body (PatchedCallManagingOrganisationRequestMultipart):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CallManagingOrganisation]
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
        PatchedCallManagingOrganisationRequest,
        PatchedCallManagingOrganisationRequestForm,
        PatchedCallManagingOrganisationRequestMultipart,
    ],
) -> CallManagingOrganisation:
    """
    Args:
        uuid (UUID):
        body (PatchedCallManagingOrganisationRequest):
        body (PatchedCallManagingOrganisationRequestForm):
        body (PatchedCallManagingOrganisationRequestMultipart):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CallManagingOrganisation
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
