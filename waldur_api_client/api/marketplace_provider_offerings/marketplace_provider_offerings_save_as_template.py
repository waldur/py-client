from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.offering_save_as_template_request import OfferingSaveAsTemplateRequest
from ...models.offering_template import OfferingTemplate
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    *,
    body: OfferingSaveAsTemplateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/marketplace-provider-offerings/{uuid}/save_as_template/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> OfferingTemplate:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 201:
        response_201 = OfferingTemplate.from_dict(response.json())

        return response_201
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OfferingTemplate]:
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
    body: OfferingSaveAsTemplateRequest,
) -> Response[OfferingTemplate]:
    """Save the offering as an offering template

     Save the offering's setup -- options, plugin options, agent configuration, components, plans,
    endpoints and terms of service -- as a new, unpublished offering template. Secrets, organization
    groups, screenshots and files are left out. The values that tie the offering to its site (its
    backend ID, access and endpoint URLs, the cluster name, account prefixes and service URLs in the
    agent configuration) are removed and declared as required parameters. Staff only.

    Args:
        uuid (UUID):
        body (OfferingSaveAsTemplateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfferingTemplate]
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
    body: OfferingSaveAsTemplateRequest,
) -> OfferingTemplate:
    """Save the offering as an offering template

     Save the offering's setup -- options, plugin options, agent configuration, components, plans,
    endpoints and terms of service -- as a new, unpublished offering template. Secrets, organization
    groups, screenshots and files are left out. The values that tie the offering to its site (its
    backend ID, access and endpoint URLs, the cluster name, account prefixes and service URLs in the
    agent configuration) are removed and declared as required parameters. Staff only.

    Args:
        uuid (UUID):
        body (OfferingSaveAsTemplateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfferingTemplate
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
    body: OfferingSaveAsTemplateRequest,
) -> Response[OfferingTemplate]:
    """Save the offering as an offering template

     Save the offering's setup -- options, plugin options, agent configuration, components, plans,
    endpoints and terms of service -- as a new, unpublished offering template. Secrets, organization
    groups, screenshots and files are left out. The values that tie the offering to its site (its
    backend ID, access and endpoint URLs, the cluster name, account prefixes and service URLs in the
    agent configuration) are removed and declared as required parameters. Staff only.

    Args:
        uuid (UUID):
        body (OfferingSaveAsTemplateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfferingTemplate]
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
    body: OfferingSaveAsTemplateRequest,
) -> OfferingTemplate:
    """Save the offering as an offering template

     Save the offering's setup -- options, plugin options, agent configuration, components, plans,
    endpoints and terms of service -- as a new, unpublished offering template. Secrets, organization
    groups, screenshots and files are left out. The values that tie the offering to its site (its
    backend ID, access and endpoint URLs, the cluster name, account prefixes and service URLs in the
    agent configuration) are removed and declared as required parameters. Staff only.

    Args:
        uuid (UUID):
        body (OfferingSaveAsTemplateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfferingTemplate
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
