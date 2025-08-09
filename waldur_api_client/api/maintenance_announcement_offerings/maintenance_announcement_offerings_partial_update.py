from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.maintenance_announcement_offering import MaintenanceAnnouncementOffering
from ...models.patched_maintenance_announcement_offering_request import PatchedMaintenanceAnnouncementOfferingRequest
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    *,
    body: PatchedMaintenanceAnnouncementOfferingRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/api/maintenance-announcement-offerings/{uuid}/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> MaintenanceAnnouncementOffering:
    if response.status_code == 200:
        response_200 = MaintenanceAnnouncementOffering.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[MaintenanceAnnouncementOffering]:
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
    body: PatchedMaintenanceAnnouncementOfferingRequest,
) -> Response[MaintenanceAnnouncementOffering]:
    """
    Args:
        uuid (UUID):
        body (PatchedMaintenanceAnnouncementOfferingRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MaintenanceAnnouncementOffering]
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
    body: PatchedMaintenanceAnnouncementOfferingRequest,
) -> MaintenanceAnnouncementOffering:
    """
    Args:
        uuid (UUID):
        body (PatchedMaintenanceAnnouncementOfferingRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MaintenanceAnnouncementOffering
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
    body: PatchedMaintenanceAnnouncementOfferingRequest,
) -> Response[MaintenanceAnnouncementOffering]:
    """
    Args:
        uuid (UUID):
        body (PatchedMaintenanceAnnouncementOfferingRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MaintenanceAnnouncementOffering]
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
    body: PatchedMaintenanceAnnouncementOfferingRequest,
) -> MaintenanceAnnouncementOffering:
    """
    Args:
        uuid (UUID):
        body (PatchedMaintenanceAnnouncementOfferingRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MaintenanceAnnouncementOffering
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
