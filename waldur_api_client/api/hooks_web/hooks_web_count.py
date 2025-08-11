import datetime
from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.hooks_web_count_content_type import HooksWebCountContentType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    author_email: Union[Unset, str] = UNSET,
    author_fullname: Union[Unset, str] = UNSET,
    author_username: Union[Unset, str] = UNSET,
    author_uuid: Union[Unset, UUID] = UNSET,
    content_type: Union[Unset, HooksWebCountContentType] = UNSET,
    destination_url: Union[Unset, str] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
    last_published: Union[Unset, datetime.datetime] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["author_email"] = author_email

    params["author_fullname"] = author_fullname

    params["author_username"] = author_username

    json_author_uuid: Union[Unset, str] = UNSET
    if not isinstance(author_uuid, Unset):
        json_author_uuid = str(author_uuid)
    params["author_uuid"] = json_author_uuid

    json_content_type: Union[Unset, int] = UNSET
    if not isinstance(content_type, Unset):
        json_content_type = content_type.value

    params["content_type"] = json_content_type

    params["destination_url"] = destination_url

    params["is_active"] = is_active

    json_last_published: Union[Unset, str] = UNSET
    if not isinstance(last_published, Unset):
        json_last_published = last_published.isoformat()
    params["last_published"] = json_last_published

    params["page"] = page

    params["page_size"] = page_size

    params["query"] = query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "head",
        "url": "/api/hooks-web/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> int:
    if response.status_code == HTTPStatus.OK:
        try:
            return int(response.headers["x-result-count"])
        except KeyError:
            raise errors.UnexpectedStatus(
                response.status_code, b"Expected 'X-Result-Count' header for HEAD request, but it was not found."
            )
        except ValueError:
            count_val = response.headers.get("x-result-count")
            msg = f"Expected 'X-Result-Count' header to be an integer, but got '{count_val}'."
            raise errors.UnexpectedStatus(response.status_code, msg.encode())
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[int]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    author_email: Union[Unset, str] = UNSET,
    author_fullname: Union[Unset, str] = UNSET,
    author_username: Union[Unset, str] = UNSET,
    author_uuid: Union[Unset, UUID] = UNSET,
    content_type: Union[Unset, HooksWebCountContentType] = UNSET,
    destination_url: Union[Unset, str] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
    last_published: Union[Unset, datetime.datetime] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
) -> Response[int]:
    """Get number of items in the collection matching the request parameters.

    Args:
        author_email (Union[Unset, str]):
        author_fullname (Union[Unset, str]):
        author_username (Union[Unset, str]):
        author_uuid (Union[Unset, UUID]):
        content_type (Union[Unset, HooksWebCountContentType]):
        destination_url (Union[Unset, str]):
        is_active (Union[Unset, bool]):
        last_published (Union[Unset, datetime.datetime]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        query (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[int]
    """

    kwargs = _get_kwargs(
        author_email=author_email,
        author_fullname=author_fullname,
        author_username=author_username,
        author_uuid=author_uuid,
        content_type=content_type,
        destination_url=destination_url,
        is_active=is_active,
        last_published=last_published,
        page=page,
        page_size=page_size,
        query=query,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    author_email: Union[Unset, str] = UNSET,
    author_fullname: Union[Unset, str] = UNSET,
    author_username: Union[Unset, str] = UNSET,
    author_uuid: Union[Unset, UUID] = UNSET,
    content_type: Union[Unset, HooksWebCountContentType] = UNSET,
    destination_url: Union[Unset, str] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
    last_published: Union[Unset, datetime.datetime] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
) -> int:
    """Get number of items in the collection matching the request parameters.

    Args:
        author_email (Union[Unset, str]):
        author_fullname (Union[Unset, str]):
        author_username (Union[Unset, str]):
        author_uuid (Union[Unset, UUID]):
        content_type (Union[Unset, HooksWebCountContentType]):
        destination_url (Union[Unset, str]):
        is_active (Union[Unset, bool]):
        last_published (Union[Unset, datetime.datetime]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        query (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        int
    """

    return sync_detailed(
        client=client,
        author_email=author_email,
        author_fullname=author_fullname,
        author_username=author_username,
        author_uuid=author_uuid,
        content_type=content_type,
        destination_url=destination_url,
        is_active=is_active,
        last_published=last_published,
        page=page,
        page_size=page_size,
        query=query,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    author_email: Union[Unset, str] = UNSET,
    author_fullname: Union[Unset, str] = UNSET,
    author_username: Union[Unset, str] = UNSET,
    author_uuid: Union[Unset, UUID] = UNSET,
    content_type: Union[Unset, HooksWebCountContentType] = UNSET,
    destination_url: Union[Unset, str] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
    last_published: Union[Unset, datetime.datetime] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
) -> Response[int]:
    """Get number of items in the collection matching the request parameters.

    Args:
        author_email (Union[Unset, str]):
        author_fullname (Union[Unset, str]):
        author_username (Union[Unset, str]):
        author_uuid (Union[Unset, UUID]):
        content_type (Union[Unset, HooksWebCountContentType]):
        destination_url (Union[Unset, str]):
        is_active (Union[Unset, bool]):
        last_published (Union[Unset, datetime.datetime]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        query (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[int]
    """

    kwargs = _get_kwargs(
        author_email=author_email,
        author_fullname=author_fullname,
        author_username=author_username,
        author_uuid=author_uuid,
        content_type=content_type,
        destination_url=destination_url,
        is_active=is_active,
        last_published=last_published,
        page=page,
        page_size=page_size,
        query=query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    author_email: Union[Unset, str] = UNSET,
    author_fullname: Union[Unset, str] = UNSET,
    author_username: Union[Unset, str] = UNSET,
    author_uuid: Union[Unset, UUID] = UNSET,
    content_type: Union[Unset, HooksWebCountContentType] = UNSET,
    destination_url: Union[Unset, str] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
    last_published: Union[Unset, datetime.datetime] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
) -> int:
    """Get number of items in the collection matching the request parameters.

    Args:
        author_email (Union[Unset, str]):
        author_fullname (Union[Unset, str]):
        author_username (Union[Unset, str]):
        author_uuid (Union[Unset, UUID]):
        content_type (Union[Unset, HooksWebCountContentType]):
        destination_url (Union[Unset, str]):
        is_active (Union[Unset, bool]):
        last_published (Union[Unset, datetime.datetime]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        query (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        int
    """

    return (
        await asyncio_detailed(
            client=client,
            author_email=author_email,
            author_fullname=author_fullname,
            author_username=author_username,
            author_uuid=author_uuid,
            content_type=content_type,
            destination_url=destination_url,
            is_active=is_active,
            last_published=last_published,
            page=page,
            page_size=page_size,
            query=query,
        )
    ).parsed
