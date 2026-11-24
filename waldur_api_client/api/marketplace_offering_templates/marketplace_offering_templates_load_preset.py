from http import HTTPStatus
from typing import Any, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.load_offering_template_preset_request import LoadOfferingTemplatePresetRequest
from ...models.load_offering_template_preset_response import LoadOfferingTemplatePresetResponse
from ...types import Response


def _get_kwargs(
    *,
    body: LoadOfferingTemplatePresetRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/marketplace-offering-templates/load_preset/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> LoadOfferingTemplatePresetResponse:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = LoadOfferingTemplatePresetResponse.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[LoadOfferingTemplatePresetResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: LoadOfferingTemplatePresetRequest,
) -> Response[LoadOfferingTemplatePresetResponse]:
    """Load offering template presets

     Create an offering template from each preset given: a copy that keeps no link to the preset.
    Refused, with nothing created, when a template already holds the name a preset would be loaded
    under. The templates are published only if publish is set.

    Args:
        body (LoadOfferingTemplatePresetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadOfferingTemplatePresetResponse]
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
    body: LoadOfferingTemplatePresetRequest,
) -> LoadOfferingTemplatePresetResponse:
    """Load offering template presets

     Create an offering template from each preset given: a copy that keeps no link to the preset.
    Refused, with nothing created, when a template already holds the name a preset would be loaded
    under. The templates are published only if publish is set.

    Args:
        body (LoadOfferingTemplatePresetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadOfferingTemplatePresetResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: LoadOfferingTemplatePresetRequest,
) -> Response[LoadOfferingTemplatePresetResponse]:
    """Load offering template presets

     Create an offering template from each preset given: a copy that keeps no link to the preset.
    Refused, with nothing created, when a template already holds the name a preset would be loaded
    under. The templates are published only if publish is set.

    Args:
        body (LoadOfferingTemplatePresetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadOfferingTemplatePresetResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: LoadOfferingTemplatePresetRequest,
) -> LoadOfferingTemplatePresetResponse:
    """Load offering template presets

     Create an offering template from each preset given: a copy that keeps no link to the preset.
    Refused, with nothing created, when a template already holds the name a preset would be loaded
    under. The templates are published only if publish is set.

    Args:
        body (LoadOfferingTemplatePresetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadOfferingTemplatePresetResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
