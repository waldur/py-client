from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.saml_2_logout_complete import Saml2LogoutComplete
from ...models.saml_2_logout_complete_request import Saml2LogoutCompleteRequest
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        Saml2LogoutCompleteRequest,
        Saml2LogoutCompleteRequest,
        Saml2LogoutCompleteRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api-auth/saml2/logout/complete/",
    }

    if isinstance(body, Saml2LogoutCompleteRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, Saml2LogoutCompleteRequest):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, Saml2LogoutCompleteRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Saml2LogoutComplete]:
    if response.status_code == 200:
        response_200 = Saml2LogoutComplete.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Saml2LogoutComplete]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        Saml2LogoutCompleteRequest,
        Saml2LogoutCompleteRequest,
        Saml2LogoutCompleteRequest,
    ],
) -> Response[Saml2LogoutComplete]:
    """For IdPs which send POST requests

    Args:
        body (Saml2LogoutCompleteRequest):
        body (Saml2LogoutCompleteRequest):
        body (Saml2LogoutCompleteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Saml2LogoutComplete]
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
    client: Union[AuthenticatedClient, Client],
    body: Union[
        Saml2LogoutCompleteRequest,
        Saml2LogoutCompleteRequest,
        Saml2LogoutCompleteRequest,
    ],
) -> Optional[Saml2LogoutComplete]:
    """For IdPs which send POST requests

    Args:
        body (Saml2LogoutCompleteRequest):
        body (Saml2LogoutCompleteRequest):
        body (Saml2LogoutCompleteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Saml2LogoutComplete
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        Saml2LogoutCompleteRequest,
        Saml2LogoutCompleteRequest,
        Saml2LogoutCompleteRequest,
    ],
) -> Response[Saml2LogoutComplete]:
    """For IdPs which send POST requests

    Args:
        body (Saml2LogoutCompleteRequest):
        body (Saml2LogoutCompleteRequest):
        body (Saml2LogoutCompleteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Saml2LogoutComplete]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        Saml2LogoutCompleteRequest,
        Saml2LogoutCompleteRequest,
        Saml2LogoutCompleteRequest,
    ],
) -> Optional[Saml2LogoutComplete]:
    """For IdPs which send POST requests

    Args:
        body (Saml2LogoutCompleteRequest):
        body (Saml2LogoutCompleteRequest):
        body (Saml2LogoutCompleteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Saml2LogoutComplete
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
