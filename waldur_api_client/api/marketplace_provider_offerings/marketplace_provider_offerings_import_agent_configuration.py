from http import HTTPStatus
from typing import Any, Union, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_configuration_import_request import AgentConfigurationImportRequest
from ...models.agent_configuration_import_result import AgentConfigurationImportResult
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    *,
    body: AgentConfigurationImportRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/marketplace-provider-offerings/{uuid}/import_agent_configuration/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[AgentConfigurationImportResult, Any]:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = AgentConfigurationImportResult.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[AgentConfigurationImportResult, Any]]:
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
    body: AgentConfigurationImportRequest,
) -> Response[Union[AgentConfigurationImportResult, Any]]:
    """Import a site agent configuration file into the agent configuration

     Reads one offering block of an existing site agent configuration file (YAML) into this offering's
    agent configuration: role backends (backend_type fills the three agent roles when the block sets
    none), event and agent settings, backend_settings and the agent-only fields of backend_components.
    Secrets, including ${VARIABLE} placeholders, are left out and listed in dropped_secrets: they stay
    on the agent host. A ${VARIABLE} placeholder of a setting that is not secret is left out and listed
    in unresolved; values gives such settings, or ones the file lacks, their values. How the agent
    reaches Waldur and other keys Waldur does not hold are listed in ignored. Component fields the
    offering's components hold are not imported; where they differ they are listed in
    component_differences. The block is chosen by offering_index, else the one whose
    waldur_offering_uuid is this offering, else the only one; otherwise the 400 on offering_index lists
    the file's offerings. With dry_run (the default) nothing is saved, and a configuration that could
    not be saved is still previewed, with the reasons in errors; otherwise the configuration is saved as
    update_integration saves it, with the same validation, permission check and change record. By choice
    the import also sets component fields the file holds (apply_components, as update_offering_component
    would, with its permission) and creates or updates the offering's SLURM periodic usage policy from
    policy_settings (apply_policy, as that policy's own endpoint would); everything is saved together or
    not at all. Site agent offerings only.

    Args:
        uuid (UUID):
        body (AgentConfigurationImportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AgentConfigurationImportResult, Any]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: AgentConfigurationImportRequest,
) -> Union[AgentConfigurationImportResult, Any]:
    """Import a site agent configuration file into the agent configuration

     Reads one offering block of an existing site agent configuration file (YAML) into this offering's
    agent configuration: role backends (backend_type fills the three agent roles when the block sets
    none), event and agent settings, backend_settings and the agent-only fields of backend_components.
    Secrets, including ${VARIABLE} placeholders, are left out and listed in dropped_secrets: they stay
    on the agent host. A ${VARIABLE} placeholder of a setting that is not secret is left out and listed
    in unresolved; values gives such settings, or ones the file lacks, their values. How the agent
    reaches Waldur and other keys Waldur does not hold are listed in ignored. Component fields the
    offering's components hold are not imported; where they differ they are listed in
    component_differences. The block is chosen by offering_index, else the one whose
    waldur_offering_uuid is this offering, else the only one; otherwise the 400 on offering_index lists
    the file's offerings. With dry_run (the default) nothing is saved, and a configuration that could
    not be saved is still previewed, with the reasons in errors; otherwise the configuration is saved as
    update_integration saves it, with the same validation, permission check and change record. By choice
    the import also sets component fields the file holds (apply_components, as update_offering_component
    would, with its permission) and creates or updates the offering's SLURM periodic usage policy from
    policy_settings (apply_policy, as that policy's own endpoint would); everything is saved together or
    not at all. Site agent offerings only.

    Args:
        uuid (UUID):
        body (AgentConfigurationImportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AgentConfigurationImportResult, Any]
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: AgentConfigurationImportRequest,
) -> Response[Union[AgentConfigurationImportResult, Any]]:
    """Import a site agent configuration file into the agent configuration

     Reads one offering block of an existing site agent configuration file (YAML) into this offering's
    agent configuration: role backends (backend_type fills the three agent roles when the block sets
    none), event and agent settings, backend_settings and the agent-only fields of backend_components.
    Secrets, including ${VARIABLE} placeholders, are left out and listed in dropped_secrets: they stay
    on the agent host. A ${VARIABLE} placeholder of a setting that is not secret is left out and listed
    in unresolved; values gives such settings, or ones the file lacks, their values. How the agent
    reaches Waldur and other keys Waldur does not hold are listed in ignored. Component fields the
    offering's components hold are not imported; where they differ they are listed in
    component_differences. The block is chosen by offering_index, else the one whose
    waldur_offering_uuid is this offering, else the only one; otherwise the 400 on offering_index lists
    the file's offerings. With dry_run (the default) nothing is saved, and a configuration that could
    not be saved is still previewed, with the reasons in errors; otherwise the configuration is saved as
    update_integration saves it, with the same validation, permission check and change record. By choice
    the import also sets component fields the file holds (apply_components, as update_offering_component
    would, with its permission) and creates or updates the offering's SLURM periodic usage policy from
    policy_settings (apply_policy, as that policy's own endpoint would); everything is saved together or
    not at all. Site agent offerings only.

    Args:
        uuid (UUID):
        body (AgentConfigurationImportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AgentConfigurationImportResult, Any]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: AgentConfigurationImportRequest,
) -> Union[AgentConfigurationImportResult, Any]:
    """Import a site agent configuration file into the agent configuration

     Reads one offering block of an existing site agent configuration file (YAML) into this offering's
    agent configuration: role backends (backend_type fills the three agent roles when the block sets
    none), event and agent settings, backend_settings and the agent-only fields of backend_components.
    Secrets, including ${VARIABLE} placeholders, are left out and listed in dropped_secrets: they stay
    on the agent host. A ${VARIABLE} placeholder of a setting that is not secret is left out and listed
    in unresolved; values gives such settings, or ones the file lacks, their values. How the agent
    reaches Waldur and other keys Waldur does not hold are listed in ignored. Component fields the
    offering's components hold are not imported; where they differ they are listed in
    component_differences. The block is chosen by offering_index, else the one whose
    waldur_offering_uuid is this offering, else the only one; otherwise the 400 on offering_index lists
    the file's offerings. With dry_run (the default) nothing is saved, and a configuration that could
    not be saved is still previewed, with the reasons in errors; otherwise the configuration is saved as
    update_integration saves it, with the same validation, permission check and change record. By choice
    the import also sets component fields the file holds (apply_components, as update_offering_component
    would, with its permission) and creates or updates the offering's SLURM periodic usage policy from
    policy_settings (apply_policy, as that policy's own endpoint would); everything is saved together or
    not at all. Site agent offerings only.

    Args:
        uuid (UUID):
        body (AgentConfigurationImportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AgentConfigurationImportResult, Any]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
