from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.offering_template_diff import OfferingTemplateDiff
from ...types import Response


def _get_kwargs(
    uuid: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/marketplace-provider-offerings/{uuid}/template_diff/",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> OfferingTemplateDiff:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = OfferingTemplateDiff.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OfferingTemplateDiff]:
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
) -> Response[OfferingTemplateDiff]:
    """Compare the offering with its offering template

     Where the offering differs from the offering template it was created from: from the version it was
    created from, and from the template's latest version, both filled in with the parameter values the
    offering was created with (a parameter added since takes its default). The latest version is left
    out, as null, for who may not see the template: it is unpublished. Only what the template sets is
    compared, and the offering's name is not. The agent configuration is compared only for who may see
    the integration settings. Refused for an offering not created from a template, or whose template was
    deleted.

    Args:
        uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfferingTemplateDiff]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
) -> OfferingTemplateDiff:
    """Compare the offering with its offering template

     Where the offering differs from the offering template it was created from: from the version it was
    created from, and from the template's latest version, both filled in with the parameter values the
    offering was created with (a parameter added since takes its default). The latest version is left
    out, as null, for who may not see the template: it is unpublished. Only what the template sets is
    compared, and the offering's name is not. The agent configuration is compared only for who may see
    the integration settings. Refused for an offering not created from a template, or whose template was
    deleted.

    Args:
        uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfferingTemplateDiff
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[OfferingTemplateDiff]:
    """Compare the offering with its offering template

     Where the offering differs from the offering template it was created from: from the version it was
    created from, and from the template's latest version, both filled in with the parameter values the
    offering was created with (a parameter added since takes its default). The latest version is left
    out, as null, for who may not see the template: it is unpublished. Only what the template sets is
    compared, and the offering's name is not. The agent configuration is compared only for who may see
    the integration settings. Refused for an offering not created from a template, or whose template was
    deleted.

    Args:
        uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfferingTemplateDiff]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
) -> OfferingTemplateDiff:
    """Compare the offering with its offering template

     Where the offering differs from the offering template it was created from: from the version it was
    created from, and from the template's latest version, both filled in with the parameter values the
    offering was created with (a parameter added since takes its default). The latest version is left
    out, as null, for who may not see the template: it is unpublished. Only what the template sets is
    compared, and the offering's name is not. The agent configuration is compared only for who may see
    the integration settings. Refused for an offering not created from a template, or whose template was
    deleted.

    Args:
        uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfferingTemplateDiff
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
        )
    ).parsed
