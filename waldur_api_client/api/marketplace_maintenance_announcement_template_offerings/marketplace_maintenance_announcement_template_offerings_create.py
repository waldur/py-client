from http import HTTPStatus
from typing import Any, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.maintenance_announcement_offering_template import MaintenanceAnnouncementOfferingTemplate
from ...models.maintenance_announcement_offering_template_request import MaintenanceAnnouncementOfferingTemplateRequest
from ...types import Response


def _get_kwargs(
    *,
    body: MaintenanceAnnouncementOfferingTemplateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/marketplace-maintenance-announcement-template-offerings/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> MaintenanceAnnouncementOfferingTemplate:
    if response.status_code == 201:
        response_201 = MaintenanceAnnouncementOfferingTemplate.from_dict(response.json())

        return response_201
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[MaintenanceAnnouncementOfferingTemplate]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: MaintenanceAnnouncementOfferingTemplateRequest,
) -> Response[MaintenanceAnnouncementOfferingTemplate]:
    """
    Args:
        body (MaintenanceAnnouncementOfferingTemplateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MaintenanceAnnouncementOfferingTemplate]
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
    body: MaintenanceAnnouncementOfferingTemplateRequest,
) -> MaintenanceAnnouncementOfferingTemplate:
    """
    Args:
        body (MaintenanceAnnouncementOfferingTemplateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MaintenanceAnnouncementOfferingTemplate
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: MaintenanceAnnouncementOfferingTemplateRequest,
) -> Response[MaintenanceAnnouncementOfferingTemplate]:
    """
    Args:
        body (MaintenanceAnnouncementOfferingTemplateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MaintenanceAnnouncementOfferingTemplate]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: MaintenanceAnnouncementOfferingTemplateRequest,
) -> MaintenanceAnnouncementOfferingTemplate:
    """
    Args:
        body (MaintenanceAnnouncementOfferingTemplateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MaintenanceAnnouncementOfferingTemplate
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
