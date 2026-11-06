from http import HTTPStatus
from typing import Any, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.allocate_in_submission_order_request import AllocateInSubmissionOrderRequest
from ...models.allocate_in_submission_order_response import AllocateInSubmissionOrderResponse
from ...types import Response


def _get_kwargs(
    uuid: str,
    obj_uuid: str,
    *,
    body: AllocateInSubmissionOrderRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/allocate_in_submission_order/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> AllocateInSubmissionOrderResponse:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = AllocateInSubmissionOrderResponse.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AllocateInSubmissionOrderResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: str,
    obj_uuid: str,
    *,
    client: AuthenticatedClient,
    body: AllocateInSubmissionOrderRequest,
) -> Response[AllocateInSubmissionOrderResponse]:
    """Take the allocation decision of every proposal of an ended round at it, first come first served: in
    submission order, approve each while its award fits what remains of every budget it draws on;
    decline those below the decision's quality threshold, and those that no longer fit (or leave them,
    on_depleted=leave) -- a later, smaller proposal still gets its chance. With preview (the default)
    only the plan is returned. Refused while a proposal of the round has not reached the decision,
    unless forced with a reason (the refusal carries waiting_count). Proposals the caller applies with
    or has a conflict of interest with are skipped. Each decision is taken on its own as if taken on the
    proposal; one that fails is listed in failed.

    Args:
        uuid (str):
        obj_uuid (str):
        body (AllocateInSubmissionOrderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AllocateInSubmissionOrderResponse]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        obj_uuid=obj_uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: str,
    obj_uuid: str,
    *,
    client: AuthenticatedClient,
    body: AllocateInSubmissionOrderRequest,
) -> AllocateInSubmissionOrderResponse:
    """Take the allocation decision of every proposal of an ended round at it, first come first served: in
    submission order, approve each while its award fits what remains of every budget it draws on;
    decline those below the decision's quality threshold, and those that no longer fit (or leave them,
    on_depleted=leave) -- a later, smaller proposal still gets its chance. With preview (the default)
    only the plan is returned. Refused while a proposal of the round has not reached the decision,
    unless forced with a reason (the refusal carries waiting_count). Proposals the caller applies with
    or has a conflict of interest with are skipped. Each decision is taken on its own as if taken on the
    proposal; one that fails is listed in failed.

    Args:
        uuid (str):
        obj_uuid (str):
        body (AllocateInSubmissionOrderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AllocateInSubmissionOrderResponse
    """

    return sync_detailed(
        uuid=uuid,
        obj_uuid=obj_uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    obj_uuid: str,
    *,
    client: AuthenticatedClient,
    body: AllocateInSubmissionOrderRequest,
) -> Response[AllocateInSubmissionOrderResponse]:
    """Take the allocation decision of every proposal of an ended round at it, first come first served: in
    submission order, approve each while its award fits what remains of every budget it draws on;
    decline those below the decision's quality threshold, and those that no longer fit (or leave them,
    on_depleted=leave) -- a later, smaller proposal still gets its chance. With preview (the default)
    only the plan is returned. Refused while a proposal of the round has not reached the decision,
    unless forced with a reason (the refusal carries waiting_count). Proposals the caller applies with
    or has a conflict of interest with are skipped. Each decision is taken on its own as if taken on the
    proposal; one that fails is listed in failed.

    Args:
        uuid (str):
        obj_uuid (str):
        body (AllocateInSubmissionOrderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AllocateInSubmissionOrderResponse]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        obj_uuid=obj_uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: str,
    obj_uuid: str,
    *,
    client: AuthenticatedClient,
    body: AllocateInSubmissionOrderRequest,
) -> AllocateInSubmissionOrderResponse:
    """Take the allocation decision of every proposal of an ended round at it, first come first served: in
    submission order, approve each while its award fits what remains of every budget it draws on;
    decline those below the decision's quality threshold, and those that no longer fit (or leave them,
    on_depleted=leave) -- a later, smaller proposal still gets its chance. With preview (the default)
    only the plan is returned. Refused while a proposal of the round has not reached the decision,
    unless forced with a reason (the refusal carries waiting_count). Proposals the caller applies with
    or has a conflict of interest with are skipped. Each decision is taken on its own as if taken on the
    proposal; one that fails is listed in failed.

    Args:
        uuid (str):
        obj_uuid (str):
        body (AllocateInSubmissionOrderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AllocateInSubmissionOrderResponse
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            obj_uuid=obj_uuid,
            client=client,
            body=body,
        )
    ).parsed
