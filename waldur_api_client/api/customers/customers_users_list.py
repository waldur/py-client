import datetime
from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.customer_user import CustomerUser
from ...models.customers_users_list_field_item import CustomersUsersListFieldItem
from ...models.customers_users_list_o import CustomersUsersListO
from ...models.customers_users_list_organization_role_item_type_0 import CustomersUsersListOrganizationRoleItemType0
from ...models.customers_users_list_project_role_item_type_0 import CustomersUsersListProjectRoleItemType0
from ...types import UNSET, Response, Unset


def _get_kwargs(
    customer_uuid: UUID,
    *,
    agreement_date: Union[Unset, datetime.datetime] = UNSET,
    civil_number: Union[Unset, str] = UNSET,
    date_joined: Union[Unset, datetime.datetime] = UNSET,
    description: Union[Unset, str] = UNSET,
    email: Union[Unset, str] = UNSET,
    field: Union[Unset, list[CustomersUsersListFieldItem]] = UNSET,
    full_name: Union[Unset, str] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
    job_title: Union[Unset, str] = UNSET,
    modified: Union[Unset, datetime.datetime] = UNSET,
    native_name: Union[Unset, str] = UNSET,
    o: Union[Unset, CustomersUsersListO] = UNSET,
    organization: Union[Unset, str] = UNSET,
    organization_role: Union[Unset, list[Union[CustomersUsersListOrganizationRoleItemType0, str]]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    phone_number: Union[Unset, str] = UNSET,
    project_role: Union[Unset, list[Union[CustomersUsersListProjectRoleItemType0, str]]] = UNSET,
    registration_method: Union[Unset, str] = UNSET,
    user_keyword: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_agreement_date: Union[Unset, str] = UNSET
    if not isinstance(agreement_date, Unset):
        json_agreement_date = agreement_date.isoformat()
    params["agreement_date"] = json_agreement_date

    params["civil_number"] = civil_number

    json_date_joined: Union[Unset, str] = UNSET
    if not isinstance(date_joined, Unset):
        json_date_joined = date_joined.isoformat()
    params["date_joined"] = json_date_joined

    params["description"] = description

    params["email"] = email

    json_field: Union[Unset, list[str]] = UNSET
    if not isinstance(field, Unset):
        json_field = []
        for field_item_data in field:
            field_item = field_item_data.value
            json_field.append(field_item)

    params["field"] = json_field

    params["full_name"] = full_name

    params["is_active"] = is_active

    params["job_title"] = job_title

    json_modified: Union[Unset, str] = UNSET
    if not isinstance(modified, Unset):
        json_modified = modified.isoformat()
    params["modified"] = json_modified

    params["native_name"] = native_name

    json_o: Union[Unset, str] = UNSET
    if not isinstance(o, Unset):
        json_o = o.value

    params["o"] = json_o

    params["organization"] = organization

    json_organization_role: Union[Unset, list[str]] = UNSET
    if not isinstance(organization_role, Unset):
        json_organization_role = []
        for organization_role_item_data in organization_role:
            organization_role_item: str
            if isinstance(organization_role_item_data, CustomersUsersListOrganizationRoleItemType0):
                organization_role_item = organization_role_item_data.value
            else:
                organization_role_item = organization_role_item_data
            json_organization_role.append(organization_role_item)

    params["organization_role"] = json_organization_role

    params["page"] = page

    params["page_size"] = page_size

    params["phone_number"] = phone_number

    json_project_role: Union[Unset, list[str]] = UNSET
    if not isinstance(project_role, Unset):
        json_project_role = []
        for project_role_item_data in project_role:
            project_role_item: str
            if isinstance(project_role_item_data, CustomersUsersListProjectRoleItemType0):
                project_role_item = project_role_item_data.value
            else:
                project_role_item = project_role_item_data
            json_project_role.append(project_role_item)

    params["project_role"] = json_project_role

    params["registration_method"] = registration_method

    params["user_keyword"] = user_keyword

    params["username"] = username

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/customers/{customer_uuid}/users/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> list["CustomerUser"]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CustomerUser.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["CustomerUser"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    customer_uuid: UUID,
    *,
    client: AuthenticatedClient,
    agreement_date: Union[Unset, datetime.datetime] = UNSET,
    civil_number: Union[Unset, str] = UNSET,
    date_joined: Union[Unset, datetime.datetime] = UNSET,
    description: Union[Unset, str] = UNSET,
    email: Union[Unset, str] = UNSET,
    field: Union[Unset, list[CustomersUsersListFieldItem]] = UNSET,
    full_name: Union[Unset, str] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
    job_title: Union[Unset, str] = UNSET,
    modified: Union[Unset, datetime.datetime] = UNSET,
    native_name: Union[Unset, str] = UNSET,
    o: Union[Unset, CustomersUsersListO] = UNSET,
    organization: Union[Unset, str] = UNSET,
    organization_role: Union[Unset, list[Union[CustomersUsersListOrganizationRoleItemType0, str]]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    phone_number: Union[Unset, str] = UNSET,
    project_role: Union[Unset, list[Union[CustomersUsersListProjectRoleItemType0, str]]] = UNSET,
    registration_method: Union[Unset, str] = UNSET,
    user_keyword: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Response[list["CustomerUser"]]:
    """A list of users connected to the customer.

    Args:
        customer_uuid (UUID):
        agreement_date (Union[Unset, datetime.datetime]):
        civil_number (Union[Unset, str]):
        date_joined (Union[Unset, datetime.datetime]):
        description (Union[Unset, str]):
        email (Union[Unset, str]):
        field (Union[Unset, list[CustomersUsersListFieldItem]]):
        full_name (Union[Unset, str]):
        is_active (Union[Unset, bool]):
        job_title (Union[Unset, str]):
        modified (Union[Unset, datetime.datetime]):
        native_name (Union[Unset, str]):
        o (Union[Unset, CustomersUsersListO]):
        organization (Union[Unset, str]):
        organization_role (Union[Unset, list[Union[CustomersUsersListOrganizationRoleItemType0,
            str]]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        phone_number (Union[Unset, str]):
        project_role (Union[Unset, list[Union[CustomersUsersListProjectRoleItemType0, str]]]):
        registration_method (Union[Unset, str]):
        user_keyword (Union[Unset, str]):
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['CustomerUser']]
    """

    kwargs = _get_kwargs(
        customer_uuid=customer_uuid,
        agreement_date=agreement_date,
        civil_number=civil_number,
        date_joined=date_joined,
        description=description,
        email=email,
        field=field,
        full_name=full_name,
        is_active=is_active,
        job_title=job_title,
        modified=modified,
        native_name=native_name,
        o=o,
        organization=organization,
        organization_role=organization_role,
        page=page,
        page_size=page_size,
        phone_number=phone_number,
        project_role=project_role,
        registration_method=registration_method,
        user_keyword=user_keyword,
        username=username,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_uuid: UUID,
    *,
    client: AuthenticatedClient,
    agreement_date: Union[Unset, datetime.datetime] = UNSET,
    civil_number: Union[Unset, str] = UNSET,
    date_joined: Union[Unset, datetime.datetime] = UNSET,
    description: Union[Unset, str] = UNSET,
    email: Union[Unset, str] = UNSET,
    field: Union[Unset, list[CustomersUsersListFieldItem]] = UNSET,
    full_name: Union[Unset, str] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
    job_title: Union[Unset, str] = UNSET,
    modified: Union[Unset, datetime.datetime] = UNSET,
    native_name: Union[Unset, str] = UNSET,
    o: Union[Unset, CustomersUsersListO] = UNSET,
    organization: Union[Unset, str] = UNSET,
    organization_role: Union[Unset, list[Union[CustomersUsersListOrganizationRoleItemType0, str]]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    phone_number: Union[Unset, str] = UNSET,
    project_role: Union[Unset, list[Union[CustomersUsersListProjectRoleItemType0, str]]] = UNSET,
    registration_method: Union[Unset, str] = UNSET,
    user_keyword: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> list["CustomerUser"]:
    """A list of users connected to the customer.

    Args:
        customer_uuid (UUID):
        agreement_date (Union[Unset, datetime.datetime]):
        civil_number (Union[Unset, str]):
        date_joined (Union[Unset, datetime.datetime]):
        description (Union[Unset, str]):
        email (Union[Unset, str]):
        field (Union[Unset, list[CustomersUsersListFieldItem]]):
        full_name (Union[Unset, str]):
        is_active (Union[Unset, bool]):
        job_title (Union[Unset, str]):
        modified (Union[Unset, datetime.datetime]):
        native_name (Union[Unset, str]):
        o (Union[Unset, CustomersUsersListO]):
        organization (Union[Unset, str]):
        organization_role (Union[Unset, list[Union[CustomersUsersListOrganizationRoleItemType0,
            str]]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        phone_number (Union[Unset, str]):
        project_role (Union[Unset, list[Union[CustomersUsersListProjectRoleItemType0, str]]]):
        registration_method (Union[Unset, str]):
        user_keyword (Union[Unset, str]):
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['CustomerUser']
    """

    return sync_detailed(
        customer_uuid=customer_uuid,
        client=client,
        agreement_date=agreement_date,
        civil_number=civil_number,
        date_joined=date_joined,
        description=description,
        email=email,
        field=field,
        full_name=full_name,
        is_active=is_active,
        job_title=job_title,
        modified=modified,
        native_name=native_name,
        o=o,
        organization=organization,
        organization_role=organization_role,
        page=page,
        page_size=page_size,
        phone_number=phone_number,
        project_role=project_role,
        registration_method=registration_method,
        user_keyword=user_keyword,
        username=username,
    ).parsed


async def asyncio_detailed(
    customer_uuid: UUID,
    *,
    client: AuthenticatedClient,
    agreement_date: Union[Unset, datetime.datetime] = UNSET,
    civil_number: Union[Unset, str] = UNSET,
    date_joined: Union[Unset, datetime.datetime] = UNSET,
    description: Union[Unset, str] = UNSET,
    email: Union[Unset, str] = UNSET,
    field: Union[Unset, list[CustomersUsersListFieldItem]] = UNSET,
    full_name: Union[Unset, str] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
    job_title: Union[Unset, str] = UNSET,
    modified: Union[Unset, datetime.datetime] = UNSET,
    native_name: Union[Unset, str] = UNSET,
    o: Union[Unset, CustomersUsersListO] = UNSET,
    organization: Union[Unset, str] = UNSET,
    organization_role: Union[Unset, list[Union[CustomersUsersListOrganizationRoleItemType0, str]]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    phone_number: Union[Unset, str] = UNSET,
    project_role: Union[Unset, list[Union[CustomersUsersListProjectRoleItemType0, str]]] = UNSET,
    registration_method: Union[Unset, str] = UNSET,
    user_keyword: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Response[list["CustomerUser"]]:
    """A list of users connected to the customer.

    Args:
        customer_uuid (UUID):
        agreement_date (Union[Unset, datetime.datetime]):
        civil_number (Union[Unset, str]):
        date_joined (Union[Unset, datetime.datetime]):
        description (Union[Unset, str]):
        email (Union[Unset, str]):
        field (Union[Unset, list[CustomersUsersListFieldItem]]):
        full_name (Union[Unset, str]):
        is_active (Union[Unset, bool]):
        job_title (Union[Unset, str]):
        modified (Union[Unset, datetime.datetime]):
        native_name (Union[Unset, str]):
        o (Union[Unset, CustomersUsersListO]):
        organization (Union[Unset, str]):
        organization_role (Union[Unset, list[Union[CustomersUsersListOrganizationRoleItemType0,
            str]]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        phone_number (Union[Unset, str]):
        project_role (Union[Unset, list[Union[CustomersUsersListProjectRoleItemType0, str]]]):
        registration_method (Union[Unset, str]):
        user_keyword (Union[Unset, str]):
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['CustomerUser']]
    """

    kwargs = _get_kwargs(
        customer_uuid=customer_uuid,
        agreement_date=agreement_date,
        civil_number=civil_number,
        date_joined=date_joined,
        description=description,
        email=email,
        field=field,
        full_name=full_name,
        is_active=is_active,
        job_title=job_title,
        modified=modified,
        native_name=native_name,
        o=o,
        organization=organization,
        organization_role=organization_role,
        page=page,
        page_size=page_size,
        phone_number=phone_number,
        project_role=project_role,
        registration_method=registration_method,
        user_keyword=user_keyword,
        username=username,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_uuid: UUID,
    *,
    client: AuthenticatedClient,
    agreement_date: Union[Unset, datetime.datetime] = UNSET,
    civil_number: Union[Unset, str] = UNSET,
    date_joined: Union[Unset, datetime.datetime] = UNSET,
    description: Union[Unset, str] = UNSET,
    email: Union[Unset, str] = UNSET,
    field: Union[Unset, list[CustomersUsersListFieldItem]] = UNSET,
    full_name: Union[Unset, str] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
    job_title: Union[Unset, str] = UNSET,
    modified: Union[Unset, datetime.datetime] = UNSET,
    native_name: Union[Unset, str] = UNSET,
    o: Union[Unset, CustomersUsersListO] = UNSET,
    organization: Union[Unset, str] = UNSET,
    organization_role: Union[Unset, list[Union[CustomersUsersListOrganizationRoleItemType0, str]]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    phone_number: Union[Unset, str] = UNSET,
    project_role: Union[Unset, list[Union[CustomersUsersListProjectRoleItemType0, str]]] = UNSET,
    registration_method: Union[Unset, str] = UNSET,
    user_keyword: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> list["CustomerUser"]:
    """A list of users connected to the customer.

    Args:
        customer_uuid (UUID):
        agreement_date (Union[Unset, datetime.datetime]):
        civil_number (Union[Unset, str]):
        date_joined (Union[Unset, datetime.datetime]):
        description (Union[Unset, str]):
        email (Union[Unset, str]):
        field (Union[Unset, list[CustomersUsersListFieldItem]]):
        full_name (Union[Unset, str]):
        is_active (Union[Unset, bool]):
        job_title (Union[Unset, str]):
        modified (Union[Unset, datetime.datetime]):
        native_name (Union[Unset, str]):
        o (Union[Unset, CustomersUsersListO]):
        organization (Union[Unset, str]):
        organization_role (Union[Unset, list[Union[CustomersUsersListOrganizationRoleItemType0,
            str]]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        phone_number (Union[Unset, str]):
        project_role (Union[Unset, list[Union[CustomersUsersListProjectRoleItemType0, str]]]):
        registration_method (Union[Unset, str]):
        user_keyword (Union[Unset, str]):
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['CustomerUser']
    """

    return (
        await asyncio_detailed(
            customer_uuid=customer_uuid,
            client=client,
            agreement_date=agreement_date,
            civil_number=civil_number,
            date_joined=date_joined,
            description=description,
            email=email,
            field=field,
            full_name=full_name,
            is_active=is_active,
            job_title=job_title,
            modified=modified,
            native_name=native_name,
            o=o,
            organization=organization,
            organization_role=organization_role,
            page=page,
            page_size=page_size,
            phone_number=phone_number,
            project_role=project_role,
            registration_method=registration_method,
            user_keyword=user_keyword,
            username=username,
        )
    ).parsed
