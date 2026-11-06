from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.call_workflow_scenarios import CallWorkflowScenarios
from ...types import Response


def _get_kwargs(
    uuid: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/proposal-protected-calls/{uuid}/workflow-scenarios/",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> CallWorkflowScenarios:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = CallWorkflowScenarios.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CallWorkflowScenarios]:
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
) -> Response[CallWorkflowScenarios]:
    """The call's saved scenarios and their last results

     The scenarios of the template the call was created from, and how they went when last run on the
    call: passed, failed at the first assertion that did not hold, or an error. 'running' while a run
    asked for has not finished. For those who configure the call, staff and support.

    Args:
        uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CallWorkflowScenarios]
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
) -> CallWorkflowScenarios:
    """The call's saved scenarios and their last results

     The scenarios of the template the call was created from, and how they went when last run on the
    call: passed, failed at the first assertion that did not hold, or an error. 'running' while a run
    asked for has not finished. For those who configure the call, staff and support.

    Args:
        uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CallWorkflowScenarios
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[CallWorkflowScenarios]:
    """The call's saved scenarios and their last results

     The scenarios of the template the call was created from, and how they went when last run on the
    call: passed, failed at the first assertion that did not hold, or an error. 'running' while a run
    asked for has not finished. For those who configure the call, staff and support.

    Args:
        uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CallWorkflowScenarios]
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
) -> CallWorkflowScenarios:
    """The call's saved scenarios and their last results

     The scenarios of the template the call was created from, and how they went when last run on the
    call: passed, failed at the first assertion that did not hold, or an error. 'running' while a run
    asked for has not finished. For those who configure the call, staff and support.

    Args:
        uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CallWorkflowScenarios
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
        )
    ).parsed
