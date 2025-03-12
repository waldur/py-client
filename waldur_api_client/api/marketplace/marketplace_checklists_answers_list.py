from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.answer_list import AnswerList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    checklist_uuid: str,
    *,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/marketplace-checklists/{checklist_uuid}/answers/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["AnswerList"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_paginated_answer_list_list_item_data in _response_200:
            componentsschemas_paginated_answer_list_list_item = AnswerList.from_dict(
                componentsschemas_paginated_answer_list_list_item_data
            )

            response_200.append(componentsschemas_paginated_answer_list_list_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["AnswerList"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    checklist_uuid: str,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[list["AnswerList"]]:
    """
    Args:
        checklist_uuid (str):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['AnswerList']]
    """

    kwargs = _get_kwargs(
        checklist_uuid=checklist_uuid,
        page=page,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    checklist_uuid: str,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Optional[list["AnswerList"]]:
    """
    Args:
        checklist_uuid (str):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['AnswerList']
    """

    return sync_detailed(
        checklist_uuid=checklist_uuid,
        client=client,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    checklist_uuid: str,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[list["AnswerList"]]:
    """
    Args:
        checklist_uuid (str):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['AnswerList']]
    """

    kwargs = _get_kwargs(
        checklist_uuid=checklist_uuid,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    checklist_uuid: str,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Optional[list["AnswerList"]]:
    """
    Args:
        checklist_uuid (str):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['AnswerList']
    """

    return (
        await asyncio_detailed(
            checklist_uuid=checklist_uuid,
            client=client,
            page=page,
            page_size=page_size,
        )
    ).parsed
