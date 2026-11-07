from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.offering_dependent import OfferingDependent
from ...models.offering_dependent_change_enum import OfferingDependentChangeEnum
from ...types import UNSET, Response, Unset
from ...utils import parse_link_header


def _get_kwargs(
    uuid: UUID,
    *,
    change: OfferingDependentChangeEnum,
    component_type: Union[Unset, str] = UNSET,
    plan_uuid: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_change = change.value
    params["change"] = json_change

    params["component_type"] = component_type

    json_plan_uuid: Union[Unset, str] = UNSET
    if not isinstance(plan_uuid, Unset):
        json_plan_uuid = str(plan_uuid)
    params["plan_uuid"] = json_plan_uuid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/marketplace-provider-offerings/{uuid}/dependents/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> list["OfferingDependent"]:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = OfferingDependent.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["OfferingDependent"]]:
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
    change: OfferingDependentChangeEnum,
    component_type: Union[Unset, str] = UNSET,
    plan_uuid: Union[Unset, UUID] = UNSET,
) -> Response[list["OfferingDependent"]]:
    """What depends on an offering

     What other parts of the portal -- calls for proposals, say -- have built on the offering, one of its
    plans or one of its components, and whether they would refuse the given change. Shown before the
    change is confirmed. Open to whoever may change the offering: staff, and holders of OFFERING.UPDATE
    on the offering, its organization or its service provider. They see every dependent, including calls
    run by other organizations, since those are what the change would break.

    Args:
        uuid (UUID):
        change (OfferingDependentChangeEnum):
        component_type (Union[Unset, str]):
        plan_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['OfferingDependent']]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        change=change,
        component_type=component_type,
        plan_uuid=plan_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    change: OfferingDependentChangeEnum,
    component_type: Union[Unset, str] = UNSET,
    plan_uuid: Union[Unset, UUID] = UNSET,
) -> list["OfferingDependent"]:
    """What depends on an offering

     What other parts of the portal -- calls for proposals, say -- have built on the offering, one of its
    plans or one of its components, and whether they would refuse the given change. Shown before the
    change is confirmed. Open to whoever may change the offering: staff, and holders of OFFERING.UPDATE
    on the offering, its organization or its service provider. They see every dependent, including calls
    run by other organizations, since those are what the change would break.

    Args:
        uuid (UUID):
        change (OfferingDependentChangeEnum):
        component_type (Union[Unset, str]):
        plan_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['OfferingDependent']
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        change=change,
        component_type=component_type,
        plan_uuid=plan_uuid,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    change: OfferingDependentChangeEnum,
    component_type: Union[Unset, str] = UNSET,
    plan_uuid: Union[Unset, UUID] = UNSET,
) -> Response[list["OfferingDependent"]]:
    """What depends on an offering

     What other parts of the portal -- calls for proposals, say -- have built on the offering, one of its
    plans or one of its components, and whether they would refuse the given change. Shown before the
    change is confirmed. Open to whoever may change the offering: staff, and holders of OFFERING.UPDATE
    on the offering, its organization or its service provider. They see every dependent, including calls
    run by other organizations, since those are what the change would break.

    Args:
        uuid (UUID):
        change (OfferingDependentChangeEnum):
        component_type (Union[Unset, str]):
        plan_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['OfferingDependent']]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        change=change,
        component_type=component_type,
        plan_uuid=plan_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    change: OfferingDependentChangeEnum,
    component_type: Union[Unset, str] = UNSET,
    plan_uuid: Union[Unset, UUID] = UNSET,
) -> list["OfferingDependent"]:
    """What depends on an offering

     What other parts of the portal -- calls for proposals, say -- have built on the offering, one of its
    plans or one of its components, and whether they would refuse the given change. Shown before the
    change is confirmed. Open to whoever may change the offering: staff, and holders of OFFERING.UPDATE
    on the offering, its organization or its service provider. They see every dependent, including calls
    run by other organizations, since those are what the change would break.

    Args:
        uuid (UUID):
        change (OfferingDependentChangeEnum):
        component_type (Union[Unset, str]):
        plan_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['OfferingDependent']
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            change=change,
            component_type=component_type,
            plan_uuid=plan_uuid,
        )
    ).parsed


def sync_all(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    change: OfferingDependentChangeEnum,
    component_type: Union[Unset, str] = UNSET,
    plan_uuid: Union[Unset, UUID] = UNSET,
) -> list["OfferingDependent"]:
    """Get All Pages

     Fetch all pages of paginated results. This function automatically handles pagination
     by following the 'next' link in the Link header until all results are retrieved.

     Note: page_size will be set to 100 (the maximum allowed) automatically.

    Args:
        uuid (UUID):
        change (OfferingDependentChangeEnum):
        component_type (Union[Unset, str]):
        plan_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['OfferingDependent']: Combined results from all pages
    """
    from urllib.parse import parse_qs, urlparse

    all_results: list[OfferingDependent] = []

    # Get initial request kwargs
    kwargs = _get_kwargs(
        uuid=uuid,
        change=change,
        component_type=component_type,
        plan_uuid=plan_uuid,
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
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    change: OfferingDependentChangeEnum,
    component_type: Union[Unset, str] = UNSET,
    plan_uuid: Union[Unset, UUID] = UNSET,
) -> list["OfferingDependent"]:
    """Get All Pages (Async)

     Fetch all pages of paginated results asynchronously. This function automatically handles pagination
     by following the 'next' link in the Link header until all results are retrieved.

     Note: page_size will be set to 100 (the maximum allowed) automatically.

    Args:
        uuid (UUID):
        change (OfferingDependentChangeEnum):
        component_type (Union[Unset, str]):
        plan_uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['OfferingDependent']: Combined results from all pages
    """
    from urllib.parse import parse_qs, urlparse

    all_results: list[OfferingDependent] = []

    # Get initial request kwargs
    kwargs = _get_kwargs(
        uuid=uuid,
        change=change,
        component_type=component_type,
        plan_uuid=plan_uuid,
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
