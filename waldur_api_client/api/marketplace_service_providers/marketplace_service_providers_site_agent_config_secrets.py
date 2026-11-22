import datetime
from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.call_managing_organisation_o_enum import CallManagingOrganisationOEnum
from ...models.site_agent_config_generation_request import SiteAgentConfigGenerationRequest
from ...models.site_agent_config_secret import SiteAgentConfigSecret
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    body: SiteAgentConfigGenerationRequest,
    created: Union[Unset, datetime.datetime] = UNSET,
    created_before: Union[Unset, datetime.datetime] = UNSET,
    customer: Union[Unset, str] = UNSET,
    customer_keyword: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    modified: Union[Unset, datetime.datetime] = UNSET,
    modified_before: Union[Unset, datetime.datetime] = UNSET,
    o: Union[Unset, list[CallManagingOrganisationOEnum]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_created: Union[Unset, str] = UNSET
    if not isinstance(created, Unset):
        json_created = created.isoformat()
    params["created"] = json_created

    json_created_before: Union[Unset, str] = UNSET
    if not isinstance(created_before, Unset):
        json_created_before = created_before.isoformat()
    params["created_before"] = json_created_before

    params["customer"] = customer

    params["customer_keyword"] = customer_keyword

    json_customer_uuid: Union[Unset, str] = UNSET
    if not isinstance(customer_uuid, Unset):
        json_customer_uuid = str(customer_uuid)
    params["customer_uuid"] = json_customer_uuid

    json_modified: Union[Unset, str] = UNSET
    if not isinstance(modified, Unset):
        json_modified = modified.isoformat()
    params["modified"] = json_modified

    json_modified_before: Union[Unset, str] = UNSET
    if not isinstance(modified_before, Unset):
        json_modified_before = modified_before.isoformat()
    params["modified_before"] = json_modified_before

    json_o: Union[Unset, list[str]] = UNSET
    if not isinstance(o, Unset):
        json_o = []
        for o_item_data in o:
            o_item = o_item_data.value
            json_o.append(o_item)

    params["o"] = json_o

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/marketplace-service-providers/{uuid}/site_agent_config_secrets/",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> list["SiteAgentConfigSecret"]:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = SiteAgentConfigSecret.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["SiteAgentConfigSecret"]]:
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
    body: SiteAgentConfigGenerationRequest,
    created: Union[Unset, datetime.datetime] = UNSET,
    created_before: Union[Unset, datetime.datetime] = UNSET,
    customer: Union[Unset, str] = UNSET,
    customer_keyword: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    modified: Union[Unset, datetime.datetime] = UNSET,
    modified_before: Union[Unset, datetime.datetime] = UNSET,
    o: Union[Unset, list[CallManagingOrganisationOEnum]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[list["SiteAgentConfigSecret"]]:
    """List the secrets of a generated site agent configuration

     The secrets the operator adds to the configuration that generate_site_agent_config returns for the
    same request: the Waldur API token of each offering and the secret settings of its backends, with
    where each goes and whether the file holds a placeholder for it.

    Args:
        uuid (UUID):
        created (Union[Unset, datetime.datetime]):
        created_before (Union[Unset, datetime.datetime]):
        customer (Union[Unset, str]):
        customer_keyword (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        modified (Union[Unset, datetime.datetime]):
        modified_before (Union[Unset, datetime.datetime]):
        o (Union[Unset, list[CallManagingOrganisationOEnum]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        body (SiteAgentConfigGenerationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['SiteAgentConfigSecret']]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
        created=created,
        created_before=created_before,
        customer=customer,
        customer_keyword=customer_keyword,
        customer_uuid=customer_uuid,
        modified=modified,
        modified_before=modified_before,
        o=o,
        page=page,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: SiteAgentConfigGenerationRequest,
    created: Union[Unset, datetime.datetime] = UNSET,
    created_before: Union[Unset, datetime.datetime] = UNSET,
    customer: Union[Unset, str] = UNSET,
    customer_keyword: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    modified: Union[Unset, datetime.datetime] = UNSET,
    modified_before: Union[Unset, datetime.datetime] = UNSET,
    o: Union[Unset, list[CallManagingOrganisationOEnum]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> list["SiteAgentConfigSecret"]:
    """List the secrets of a generated site agent configuration

     The secrets the operator adds to the configuration that generate_site_agent_config returns for the
    same request: the Waldur API token of each offering and the secret settings of its backends, with
    where each goes and whether the file holds a placeholder for it.

    Args:
        uuid (UUID):
        created (Union[Unset, datetime.datetime]):
        created_before (Union[Unset, datetime.datetime]):
        customer (Union[Unset, str]):
        customer_keyword (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        modified (Union[Unset, datetime.datetime]):
        modified_before (Union[Unset, datetime.datetime]):
        o (Union[Unset, list[CallManagingOrganisationOEnum]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        body (SiteAgentConfigGenerationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['SiteAgentConfigSecret']
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        body=body,
        created=created,
        created_before=created_before,
        customer=customer,
        customer_keyword=customer_keyword,
        customer_uuid=customer_uuid,
        modified=modified,
        modified_before=modified_before,
        o=o,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: SiteAgentConfigGenerationRequest,
    created: Union[Unset, datetime.datetime] = UNSET,
    created_before: Union[Unset, datetime.datetime] = UNSET,
    customer: Union[Unset, str] = UNSET,
    customer_keyword: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    modified: Union[Unset, datetime.datetime] = UNSET,
    modified_before: Union[Unset, datetime.datetime] = UNSET,
    o: Union[Unset, list[CallManagingOrganisationOEnum]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[list["SiteAgentConfigSecret"]]:
    """List the secrets of a generated site agent configuration

     The secrets the operator adds to the configuration that generate_site_agent_config returns for the
    same request: the Waldur API token of each offering and the secret settings of its backends, with
    where each goes and whether the file holds a placeholder for it.

    Args:
        uuid (UUID):
        created (Union[Unset, datetime.datetime]):
        created_before (Union[Unset, datetime.datetime]):
        customer (Union[Unset, str]):
        customer_keyword (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        modified (Union[Unset, datetime.datetime]):
        modified_before (Union[Unset, datetime.datetime]):
        o (Union[Unset, list[CallManagingOrganisationOEnum]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        body (SiteAgentConfigGenerationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['SiteAgentConfigSecret']]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
        created=created,
        created_before=created_before,
        customer=customer,
        customer_keyword=customer_keyword,
        customer_uuid=customer_uuid,
        modified=modified,
        modified_before=modified_before,
        o=o,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: SiteAgentConfigGenerationRequest,
    created: Union[Unset, datetime.datetime] = UNSET,
    created_before: Union[Unset, datetime.datetime] = UNSET,
    customer: Union[Unset, str] = UNSET,
    customer_keyword: Union[Unset, str] = UNSET,
    customer_uuid: Union[Unset, UUID] = UNSET,
    modified: Union[Unset, datetime.datetime] = UNSET,
    modified_before: Union[Unset, datetime.datetime] = UNSET,
    o: Union[Unset, list[CallManagingOrganisationOEnum]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> list["SiteAgentConfigSecret"]:
    """List the secrets of a generated site agent configuration

     The secrets the operator adds to the configuration that generate_site_agent_config returns for the
    same request: the Waldur API token of each offering and the secret settings of its backends, with
    where each goes and whether the file holds a placeholder for it.

    Args:
        uuid (UUID):
        created (Union[Unset, datetime.datetime]):
        created_before (Union[Unset, datetime.datetime]):
        customer (Union[Unset, str]):
        customer_keyword (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        modified (Union[Unset, datetime.datetime]):
        modified_before (Union[Unset, datetime.datetime]):
        o (Union[Unset, list[CallManagingOrganisationOEnum]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        body (SiteAgentConfigGenerationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['SiteAgentConfigSecret']
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
            created=created,
            created_before=created_before,
            customer=customer,
            customer_keyword=customer_keyword,
            customer_uuid=customer_uuid,
            modified=modified,
            modified_before=modified_before,
            o=o,
            page=page,
            page_size=page_size,
        )
    ).parsed
