from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.resource_option_secret_set_request import ResourceOptionSecretSetRequest
from ...models.resource_option_secret_status import ResourceOptionSecretStatus
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    *,
    body: ResourceOptionSecretSetRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/marketplace-provider-resources/{uuid}/set_option_secret/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> ResourceOptionSecretStatus:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = ResourceOptionSecretStatus.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ResourceOptionSecretStatus]:
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
    body: ResourceOptionSecretSetRequest,
) -> Response[ResourceOptionSecretStatus]:
    """Set the value of a secret option

     Lets the service provider or its site agent store, or replace, the value of one of the resource's
    secret options, encrypted, whoever the option's source. The value is never returned; the response
    says whether it is set. Audited.

    Args:
        uuid (UUID):
        body (ResourceOptionSecretSetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResourceOptionSecretStatus]
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
    body: ResourceOptionSecretSetRequest,
) -> ResourceOptionSecretStatus:
    """Set the value of a secret option

     Lets the service provider or its site agent store, or replace, the value of one of the resource's
    secret options, encrypted, whoever the option's source. The value is never returned; the response
    says whether it is set. Audited.

    Args:
        uuid (UUID):
        body (ResourceOptionSecretSetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResourceOptionSecretStatus
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
    body: ResourceOptionSecretSetRequest,
) -> Response[ResourceOptionSecretStatus]:
    """Set the value of a secret option

     Lets the service provider or its site agent store, or replace, the value of one of the resource's
    secret options, encrypted, whoever the option's source. The value is never returned; the response
    says whether it is set. Audited.

    Args:
        uuid (UUID):
        body (ResourceOptionSecretSetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResourceOptionSecretStatus]
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
    body: ResourceOptionSecretSetRequest,
) -> ResourceOptionSecretStatus:
    """Set the value of a secret option

     Lets the service provider or its site agent store, or replace, the value of one of the resource's
    secret options, encrypted, whoever the option's source. The value is never returned; the response
    says whether it is set. Audited.

    Args:
        uuid (UUID):
        body (ResourceOptionSecretSetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResourceOptionSecretStatus
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
