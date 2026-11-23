from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.order_flow_description import OrderFlowDescription
from ...models.order_flow_description_order_kind_enum import OrderFlowDescriptionOrderKindEnum
from ...models.order_flow_description_orderer_enum import OrderFlowDescriptionOrdererEnum
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    order_kind: Union[Unset, OrderFlowDescriptionOrderKindEnum] = UNSET,
    orderer: Union[Unset, OrderFlowDescriptionOrdererEnum] = UNSET,
    role: Union[Unset, str] = UNSET,
    with_stats: Union[Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_order_kind: Union[Unset, str] = UNSET
    if not isinstance(order_kind, Unset):
        json_order_kind = order_kind.value

    params["order_kind"] = json_order_kind

    json_orderer: Union[Unset, str] = UNSET
    if not isinstance(orderer, Unset):
        json_orderer = orderer.value

    params["orderer"] = json_orderer

    params["role"] = role

    params["with_stats"] = with_stats

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/marketplace-provider-offerings/{uuid}/order_flow_description/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> OrderFlowDescription:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = OrderFlowDescription.from_dict(response.json())

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OrderFlowDescription]:
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
    order_kind: Union[Unset, OrderFlowDescriptionOrderKindEnum] = UNSET,
    orderer: Union[Unset, OrderFlowDescriptionOrdererEnum] = UNSET,
    role: Union[Unset, str] = UNSET,
    with_stats: Union[Unset, bool] = False,
) -> Response[OrderFlowDescription]:
    """Describe how orders for the offering move from placement to done

     For one kind of order and one kind of orderer: the steps an order goes through, who acts at each,
    the rules that decide whether a review step runs and the settings each rule reads. Review steps are
    decided by the same rules that route real orders. A fact that depends on the order, such as an
    attached purchase order, is drawn as a branch. With `with_stats`, how many of the offering's orders
    are in each state and how long each step has taken.

    Args:
        uuid (UUID):
        order_kind (Union[Unset, OrderFlowDescriptionOrderKindEnum]):
        orderer (Union[Unset, OrderFlowDescriptionOrdererEnum]):
        role (Union[Unset, str]):
        with_stats (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrderFlowDescription]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        order_kind=order_kind,
        orderer=orderer,
        role=role,
        with_stats=with_stats,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    order_kind: Union[Unset, OrderFlowDescriptionOrderKindEnum] = UNSET,
    orderer: Union[Unset, OrderFlowDescriptionOrdererEnum] = UNSET,
    role: Union[Unset, str] = UNSET,
    with_stats: Union[Unset, bool] = False,
) -> OrderFlowDescription:
    """Describe how orders for the offering move from placement to done

     For one kind of order and one kind of orderer: the steps an order goes through, who acts at each,
    the rules that decide whether a review step runs and the settings each rule reads. Review steps are
    decided by the same rules that route real orders. A fact that depends on the order, such as an
    attached purchase order, is drawn as a branch. With `with_stats`, how many of the offering's orders
    are in each state and how long each step has taken.

    Args:
        uuid (UUID):
        order_kind (Union[Unset, OrderFlowDescriptionOrderKindEnum]):
        orderer (Union[Unset, OrderFlowDescriptionOrdererEnum]):
        role (Union[Unset, str]):
        with_stats (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrderFlowDescription
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        order_kind=order_kind,
        orderer=orderer,
        role=role,
        with_stats=with_stats,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    order_kind: Union[Unset, OrderFlowDescriptionOrderKindEnum] = UNSET,
    orderer: Union[Unset, OrderFlowDescriptionOrdererEnum] = UNSET,
    role: Union[Unset, str] = UNSET,
    with_stats: Union[Unset, bool] = False,
) -> Response[OrderFlowDescription]:
    """Describe how orders for the offering move from placement to done

     For one kind of order and one kind of orderer: the steps an order goes through, who acts at each,
    the rules that decide whether a review step runs and the settings each rule reads. Review steps are
    decided by the same rules that route real orders. A fact that depends on the order, such as an
    attached purchase order, is drawn as a branch. With `with_stats`, how many of the offering's orders
    are in each state and how long each step has taken.

    Args:
        uuid (UUID):
        order_kind (Union[Unset, OrderFlowDescriptionOrderKindEnum]):
        orderer (Union[Unset, OrderFlowDescriptionOrdererEnum]):
        role (Union[Unset, str]):
        with_stats (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrderFlowDescription]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        order_kind=order_kind,
        orderer=orderer,
        role=role,
        with_stats=with_stats,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    order_kind: Union[Unset, OrderFlowDescriptionOrderKindEnum] = UNSET,
    orderer: Union[Unset, OrderFlowDescriptionOrdererEnum] = UNSET,
    role: Union[Unset, str] = UNSET,
    with_stats: Union[Unset, bool] = False,
) -> OrderFlowDescription:
    """Describe how orders for the offering move from placement to done

     For one kind of order and one kind of orderer: the steps an order goes through, who acts at each,
    the rules that decide whether a review step runs and the settings each rule reads. Review steps are
    decided by the same rules that route real orders. A fact that depends on the order, such as an
    attached purchase order, is drawn as a branch. With `with_stats`, how many of the offering's orders
    are in each state and how long each step has taken.

    Args:
        uuid (UUID):
        order_kind (Union[Unset, OrderFlowDescriptionOrderKindEnum]):
        orderer (Union[Unset, OrderFlowDescriptionOrdererEnum]):
        role (Union[Unset, str]):
        with_stats (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrderFlowDescription
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            order_kind=order_kind,
            orderer=orderer,
            role=role,
            with_stats=with_stats,
        )
    ).parsed
