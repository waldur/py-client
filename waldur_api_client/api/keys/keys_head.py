import datetime
from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.keys_head_o_item import KeysHeadOItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    created: Union[Unset, datetime.datetime] = UNSET,
    fingerprint_md5: Union[Unset, str] = UNSET,
    fingerprint_sha256: Union[Unset, str] = UNSET,
    fingerprint_sha512: Union[Unset, str] = UNSET,
    is_shared: Union[Unset, bool] = UNSET,
    modified: Union[Unset, datetime.datetime] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    o: Union[Unset, list[KeysHeadOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    user_uuid: Union[Unset, UUID] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_created: Union[Unset, str] = UNSET
    if not isinstance(created, Unset):
        json_created = created.isoformat()
    params["created"] = json_created

    params["fingerprint_md5"] = fingerprint_md5

    params["fingerprint_sha256"] = fingerprint_sha256

    params["fingerprint_sha512"] = fingerprint_sha512

    params["is_shared"] = is_shared

    json_modified: Union[Unset, str] = UNSET
    if not isinstance(modified, Unset):
        json_modified = modified.isoformat()
    params["modified"] = json_modified

    params["name"] = name

    params["name_exact"] = name_exact

    json_o: Union[Unset, list[str]] = UNSET
    if not isinstance(o, Unset):
        json_o = []
        for o_item_data in o:
            o_item = o_item_data.value
            json_o.append(o_item)

    params["o"] = json_o

    params["page"] = page

    params["page_size"] = page_size

    json_user_uuid: Union[Unset, str] = UNSET
    if not isinstance(user_uuid, Unset):
        json_user_uuid = str(user_uuid)
    params["user_uuid"] = json_user_uuid

    json_uuid: Union[Unset, str] = UNSET
    if not isinstance(uuid, Unset):
        json_uuid = str(uuid)
    params["uuid"] = json_uuid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "head",
        "url": "/api/keys/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Any:
    if response.status_code == 200:
        return None
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    created: Union[Unset, datetime.datetime] = UNSET,
    fingerprint_md5: Union[Unset, str] = UNSET,
    fingerprint_sha256: Union[Unset, str] = UNSET,
    fingerprint_sha512: Union[Unset, str] = UNSET,
    is_shared: Union[Unset, bool] = UNSET,
    modified: Union[Unset, datetime.datetime] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    o: Union[Unset, list[KeysHeadOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    user_uuid: Union[Unset, UUID] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
) -> Response[Any]:
    """Mixin to optimize HEAD requests for DRF views bypassing serializer processing

    Args:
        created (Union[Unset, datetime.datetime]):
        fingerprint_md5 (Union[Unset, str]):
        fingerprint_sha256 (Union[Unset, str]):
        fingerprint_sha512 (Union[Unset, str]):
        is_shared (Union[Unset, bool]):
        modified (Union[Unset, datetime.datetime]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        o (Union[Unset, list[KeysHeadOItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        user_uuid (Union[Unset, UUID]):
        uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        created=created,
        fingerprint_md5=fingerprint_md5,
        fingerprint_sha256=fingerprint_sha256,
        fingerprint_sha512=fingerprint_sha512,
        is_shared=is_shared,
        modified=modified,
        name=name,
        name_exact=name_exact,
        o=o,
        page=page,
        page_size=page_size,
        user_uuid=user_uuid,
        uuid=uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    created: Union[Unset, datetime.datetime] = UNSET,
    fingerprint_md5: Union[Unset, str] = UNSET,
    fingerprint_sha256: Union[Unset, str] = UNSET,
    fingerprint_sha512: Union[Unset, str] = UNSET,
    is_shared: Union[Unset, bool] = UNSET,
    modified: Union[Unset, datetime.datetime] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_exact: Union[Unset, str] = UNSET,
    o: Union[Unset, list[KeysHeadOItem]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    user_uuid: Union[Unset, UUID] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
) -> Response[Any]:
    """Mixin to optimize HEAD requests for DRF views bypassing serializer processing

    Args:
        created (Union[Unset, datetime.datetime]):
        fingerprint_md5 (Union[Unset, str]):
        fingerprint_sha256 (Union[Unset, str]):
        fingerprint_sha512 (Union[Unset, str]):
        is_shared (Union[Unset, bool]):
        modified (Union[Unset, datetime.datetime]):
        name (Union[Unset, str]):
        name_exact (Union[Unset, str]):
        o (Union[Unset, list[KeysHeadOItem]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        user_uuid (Union[Unset, UUID]):
        uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        created=created,
        fingerprint_md5=fingerprint_md5,
        fingerprint_sha256=fingerprint_sha256,
        fingerprint_sha512=fingerprint_sha512,
        is_shared=is_shared,
        modified=modified,
        name=name,
        name_exact=name_exact,
        o=o,
        page=page,
        page_size=page_size,
        user_uuid=user_uuid,
        uuid=uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
