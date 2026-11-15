import datetime
from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.email_hook import EmailHook
from ...models.web_hook import WebHook
from ...types import UNSET, Response, Unset
from ...utils import parse_link_header


def _get_kwargs(
    *,
    author_email: Union[Unset, str] = UNSET,
    author_fullname: Union[Unset, str] = UNSET,
    author_username: Union[Unset, str] = UNSET,
    author_uuid: Union[Unset, UUID] = UNSET,
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
        "method": "get",
        "url": "/api/hooks/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> list[Union["EmailHook", "WebHook"]]:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:

            def _parse_response_200_item(data: object) -> Union["EmailHook", "WebHook"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_hook_type_0 = WebHook.from_dict(data)

                    return componentsschemas_hook_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_hook_type_1 = EmailHook.from_dict(data)

                return componentsschemas_hook_type_1

            response_200_item = _parse_response_200_item(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list[Union["EmailHook", "WebHook"]]]:
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
    is_active: Union[Unset, bool] = UNSET,
    last_published: Union[Unset, datetime.datetime] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
) -> Response[list[Union["EmailHook", "WebHook"]]]:
    """
    Args:
        author_email (Union[Unset, str]):
        author_fullname (Union[Unset, str]):
        author_username (Union[Unset, str]):
        author_uuid (Union[Unset, UUID]):
        is_active (Union[Unset, bool]):
        last_published (Union[Unset, datetime.datetime]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        query (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Union['EmailHook', 'WebHook']]]
    """

    kwargs = _get_kwargs(
        author_email=author_email,
        author_fullname=author_fullname,
        author_username=author_username,
        author_uuid=author_uuid,
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
    is_active: Union[Unset, bool] = UNSET,
    last_published: Union[Unset, datetime.datetime] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
) -> list[Union["EmailHook", "WebHook"]]:
    """
    Args:
        author_email (Union[Unset, str]):
        author_fullname (Union[Unset, str]):
        author_username (Union[Unset, str]):
        author_uuid (Union[Unset, UUID]):
        is_active (Union[Unset, bool]):
        last_published (Union[Unset, datetime.datetime]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        query (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Union['EmailHook', 'WebHook']]
    """

    return sync_detailed(
        client=client,
        author_email=author_email,
        author_fullname=author_fullname,
        author_username=author_username,
        author_uuid=author_uuid,
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
    is_active: Union[Unset, bool] = UNSET,
    last_published: Union[Unset, datetime.datetime] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
) -> Response[list[Union["EmailHook", "WebHook"]]]:
    """
    Args:
        author_email (Union[Unset, str]):
        author_fullname (Union[Unset, str]):
        author_username (Union[Unset, str]):
        author_uuid (Union[Unset, UUID]):
        is_active (Union[Unset, bool]):
        last_published (Union[Unset, datetime.datetime]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        query (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Union['EmailHook', 'WebHook']]]
    """

    kwargs = _get_kwargs(
        author_email=author_email,
        author_fullname=author_fullname,
        author_username=author_username,
        author_uuid=author_uuid,
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
    is_active: Union[Unset, bool] = UNSET,
    last_published: Union[Unset, datetime.datetime] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    query: Union[Unset, str] = UNSET,
) -> list[Union["EmailHook", "WebHook"]]:
    """
    Args:
        author_email (Union[Unset, str]):
        author_fullname (Union[Unset, str]):
        author_username (Union[Unset, str]):
        author_uuid (Union[Unset, UUID]):
        is_active (Union[Unset, bool]):
        last_published (Union[Unset, datetime.datetime]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        query (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Union['EmailHook', 'WebHook']]
    """

    return (
        await asyncio_detailed(
            client=client,
            author_email=author_email,
            author_fullname=author_fullname,
            author_username=author_username,
            author_uuid=author_uuid,
            is_active=is_active,
            last_published=last_published,
            page=page,
            page_size=page_size,
            query=query,
        )
    ).parsed


def sync_all(
    *,
    client: AuthenticatedClient,
    author_email: Union[Unset, str] = UNSET,
    author_fullname: Union[Unset, str] = UNSET,
    author_username: Union[Unset, str] = UNSET,
    author_uuid: Union[Unset, UUID] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
    last_published: Union[Unset, datetime.datetime] = UNSET,
    query: Union[Unset, str] = UNSET,
) -> list[Union["EmailHook", "WebHook"]]:
    """Get All Pages

     Fetch all pages of paginated results. This function automatically handles pagination
     by following the 'next' link in the Link header until all results are retrieved.

     Note: page_size will be set to 100 (the maximum allowed) automatically.

    Args:
        author_email (Union[Unset, str]):
        author_fullname (Union[Unset, str]):
        author_username (Union[Unset, str]):
        author_uuid (Union[Unset, UUID]):
        is_active (Union[Unset, bool]):
        last_published (Union[Unset, datetime.datetime]):
        query (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Union['EmailHook', 'WebHook']]: Combined results from all pages
    """
    from urllib.parse import parse_qs, urlparse

    all_results: list[Union[EmailHook, WebHook]] = []

    # Get initial request kwargs
    kwargs = _get_kwargs(
        author_email=author_email,
        author_fullname=author_fullname,
        author_username=author_username,
        author_uuid=author_uuid,
        is_active=is_active,
        last_published=last_published,
        query=query,
    )

    # Set page_size to maximum
    if "params" not in kwargs:
        kwargs["params"] = {}
    kwargs["params"]["page_size"] = 100

    # Make initial request
    response = client.get_httpx_client().request(**kwargs)
    parsed_response = _parse_response(client=client, response=response)

    if parsed_response:
        all_results.extend(parsed_response)

    # Follow pagination links
    while True:
        link_header = response.headers.get("Link", "")
        links = parse_link_header(link_header)

        if "next" not in links:
            break

        # Extract page number from next URL
        next_url = links["next"]
        parsed_url = urlparse(next_url)
        next_params = parse_qs(parsed_url.query)

        if "page" not in next_params:
            break

        # Update only the page parameter, keep all other params
        page_number = next_params["page"][0]
        kwargs["params"]["page"] = page_number

        # Fetch next page
        response = client.get_httpx_client().request(**kwargs)
        parsed_response = _parse_response(client=client, response=response)

        if parsed_response:
            all_results.extend(parsed_response)

    return all_results


async def asyncio_all(
    *,
    client: AuthenticatedClient,
    author_email: Union[Unset, str] = UNSET,
    author_fullname: Union[Unset, str] = UNSET,
    author_username: Union[Unset, str] = UNSET,
    author_uuid: Union[Unset, UUID] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
    last_published: Union[Unset, datetime.datetime] = UNSET,
    query: Union[Unset, str] = UNSET,
) -> list[Union["EmailHook", "WebHook"]]:
    """Get All Pages (Async)

     Fetch all pages of paginated results asynchronously. This function automatically handles pagination
     by following the 'next' link in the Link header until all results are retrieved.

     Note: page_size will be set to 100 (the maximum allowed) automatically.

    Args:
        author_email (Union[Unset, str]):
        author_fullname (Union[Unset, str]):
        author_username (Union[Unset, str]):
        author_uuid (Union[Unset, UUID]):
        is_active (Union[Unset, bool]):
        last_published (Union[Unset, datetime.datetime]):
        query (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Union['EmailHook', 'WebHook']]: Combined results from all pages
    """
    from urllib.parse import parse_qs, urlparse

    all_results: list[Union[EmailHook, WebHook]] = []

    # Get initial request kwargs
    kwargs = _get_kwargs(
        author_email=author_email,
        author_fullname=author_fullname,
        author_username=author_username,
        author_uuid=author_uuid,
        is_active=is_active,
        last_published=last_published,
        query=query,
    )

    # Set page_size to maximum
    if "params" not in kwargs:
        kwargs["params"] = {}
    kwargs["params"]["page_size"] = 100

    # Make initial request
    response = await client.get_async_httpx_client().request(**kwargs)
    parsed_response = _parse_response(client=client, response=response)

    if parsed_response:
        all_results.extend(parsed_response)

    # Follow pagination links
    while True:
        link_header = response.headers.get("Link", "")
        links = parse_link_header(link_header)

        if "next" not in links:
            break

        # Extract page number from next URL
        next_url = links["next"]
        parsed_url = urlparse(next_url)
        next_params = parse_qs(parsed_url.query)

        if "page" not in next_params:
            break

        # Update only the page parameter, keep all other params
        page_number = next_params["page"][0]
        kwargs["params"]["page"] = page_number

        # Fetch next page
        response = await client.get_async_httpx_client().request(**kwargs)
        parsed_response = _parse_response(client=client, response=response)

        if parsed_response:
            all_results.extend(parsed_response)

    return all_results
