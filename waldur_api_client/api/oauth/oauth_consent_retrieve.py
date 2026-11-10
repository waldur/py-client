from http import HTTPStatus
from typing import Any, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.consent_details import ConsentDetails
from ...models.consent_error import ConsentError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client_id: str,
    code_challenge: str,
    code_challenge_method: str,
    redirect_uri: Union[Unset, str] = UNSET,
    resource: Union[Unset, list[str]] = UNSET,
    response_type: str,
    scope: Union[Unset, str] = UNSET,
    state: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["client_id"] = client_id

    params["code_challenge"] = code_challenge

    params["code_challenge_method"] = code_challenge_method

    params["redirect_uri"] = redirect_uri

    json_resource: Union[Unset, list[str]] = UNSET
    if not isinstance(resource, Unset):
        json_resource = resource

    params["resource"] = json_resource

    params["response_type"] = response_type

    params["scope"] = scope

    params["state"] = state

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/oauth/consent/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[ConsentDetails, ConsentError]:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = ConsentDetails.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ConsentError.from_dict(response.json())

        return response_400
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ConsentDetails, ConsentError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    client_id: str,
    code_challenge: str,
    code_challenge_method: str,
    redirect_uri: Union[Unset, str] = UNSET,
    resource: Union[Unset, list[str]] = UNSET,
    response_type: str,
    scope: Union[Unset, str] = UNSET,
    state: Union[Unset, str] = UNSET,
) -> Response[Union[ConsentDetails, ConsentError]]:
    """Describe the client asking for access, for the consent page.

    Args:
        client_id (str):
        code_challenge (str):
        code_challenge_method (str):
        redirect_uri (Union[Unset, str]):
        resource (Union[Unset, list[str]]):
        response_type (str):
        scope (Union[Unset, str]):
        state (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ConsentDetails, ConsentError]]
    """

    kwargs = _get_kwargs(
        client_id=client_id,
        code_challenge=code_challenge,
        code_challenge_method=code_challenge_method,
        redirect_uri=redirect_uri,
        resource=resource,
        response_type=response_type,
        scope=scope,
        state=state,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    client_id: str,
    code_challenge: str,
    code_challenge_method: str,
    redirect_uri: Union[Unset, str] = UNSET,
    resource: Union[Unset, list[str]] = UNSET,
    response_type: str,
    scope: Union[Unset, str] = UNSET,
    state: Union[Unset, str] = UNSET,
) -> Union[ConsentDetails, ConsentError]:
    """Describe the client asking for access, for the consent page.

    Args:
        client_id (str):
        code_challenge (str):
        code_challenge_method (str):
        redirect_uri (Union[Unset, str]):
        resource (Union[Unset, list[str]]):
        response_type (str):
        scope (Union[Unset, str]):
        state (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ConsentDetails, ConsentError]
    """

    return sync_detailed(
        client=client,
        client_id=client_id,
        code_challenge=code_challenge,
        code_challenge_method=code_challenge_method,
        redirect_uri=redirect_uri,
        resource=resource,
        response_type=response_type,
        scope=scope,
        state=state,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    client_id: str,
    code_challenge: str,
    code_challenge_method: str,
    redirect_uri: Union[Unset, str] = UNSET,
    resource: Union[Unset, list[str]] = UNSET,
    response_type: str,
    scope: Union[Unset, str] = UNSET,
    state: Union[Unset, str] = UNSET,
) -> Response[Union[ConsentDetails, ConsentError]]:
    """Describe the client asking for access, for the consent page.

    Args:
        client_id (str):
        code_challenge (str):
        code_challenge_method (str):
        redirect_uri (Union[Unset, str]):
        resource (Union[Unset, list[str]]):
        response_type (str):
        scope (Union[Unset, str]):
        state (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ConsentDetails, ConsentError]]
    """

    kwargs = _get_kwargs(
        client_id=client_id,
        code_challenge=code_challenge,
        code_challenge_method=code_challenge_method,
        redirect_uri=redirect_uri,
        resource=resource,
        response_type=response_type,
        scope=scope,
        state=state,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    client_id: str,
    code_challenge: str,
    code_challenge_method: str,
    redirect_uri: Union[Unset, str] = UNSET,
    resource: Union[Unset, list[str]] = UNSET,
    response_type: str,
    scope: Union[Unset, str] = UNSET,
    state: Union[Unset, str] = UNSET,
) -> Union[ConsentDetails, ConsentError]:
    """Describe the client asking for access, for the consent page.

    Args:
        client_id (str):
        code_challenge (str):
        code_challenge_method (str):
        redirect_uri (Union[Unset, str]):
        resource (Union[Unset, list[str]]):
        response_type (str):
        scope (Union[Unset, str]):
        state (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ConsentDetails, ConsentError]
    """

    return (
        await asyncio_detailed(
            client=client,
            client_id=client_id,
            code_challenge=code_challenge,
            code_challenge_method=code_challenge_method,
            redirect_uri=redirect_uri,
            resource=resource,
            response_type=response_type,
            scope=scope,
            state=state,
        )
    ).parsed
