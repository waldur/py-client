from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_award_status_enum import PostAwardStatusEnum
from ...models.proposal_o_enum import ProposalOEnum
from ...models.proposal_run_phase_enum import ProposalRunPhaseEnum
from ...models.proposal_run_state_enum import ProposalRunStateEnum
from ...models.proposal_states import ProposalStates
from ...models.responsible_role_enum import ResponsibleRoleEnum
from ...models.step_contribution_with_answers import StepContributionWithAnswers
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    as_role: Union[Unset, ResponsibleRoleEnum] = UNSET,
    call_uuid: Union[Unset, UUID] = UNSET,
    changes_requested: Union[Unset, bool] = UNSET,
    created_by_uuid: Union[Unset, UUID] = UNSET,
    final_report_overdue: Union[Unset, bool] = UNSET,
    involved: Union[Unset, bool] = UNSET,
    my_proposals: Union[Unset, bool] = UNSET,
    name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[ProposalOEnum]] = UNSET,
    organization_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    panel_uuid: Union[Unset, UUID] = UNSET,
    post_award_status: Union[Unset, list[PostAwardStatusEnum]] = UNSET,
    round_: Union[Unset, UUID] = UNSET,
    round_uuid: Union[Unset, UUID] = UNSET,
    run_phase: Union[Unset, ProposalRunPhaseEnum] = UNSET,
    run_state: Union[Unset, ProposalRunStateEnum] = UNSET,
    slug: Union[Unset, str] = UNSET,
    state: Union[Unset, list[ProposalStates]] = UNSET,
    step: Union[Unset, str] = UNSET,
    step_uuid: Union[Unset, UUID] = UNSET,
    workflow_step: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_as_role: Union[Unset, str] = UNSET
    if not isinstance(as_role, Unset):
        json_as_role = as_role.value

    params["as_role"] = json_as_role

    json_call_uuid: Union[Unset, str] = UNSET
    if not isinstance(call_uuid, Unset):
        json_call_uuid = str(call_uuid)
    params["call_uuid"] = json_call_uuid

    params["changes_requested"] = changes_requested

    json_created_by_uuid: Union[Unset, str] = UNSET
    if not isinstance(created_by_uuid, Unset):
        json_created_by_uuid = str(created_by_uuid)
    params["created_by_uuid"] = json_created_by_uuid

    params["final_report_overdue"] = final_report_overdue

    params["involved"] = involved

    params["my_proposals"] = my_proposals

    params["name"] = name

    json_o: Union[Unset, list[str]] = UNSET
    if not isinstance(o, Unset):
        json_o = []
        for o_item_data in o:
            o_item = o_item_data.value
            json_o.append(o_item)

    params["o"] = json_o

    json_organization_uuid: Union[Unset, str] = UNSET
    if not isinstance(organization_uuid, Unset):
        json_organization_uuid = str(organization_uuid)
    params["organization_uuid"] = json_organization_uuid

    params["page"] = page

    params["page_size"] = page_size

    json_panel_uuid: Union[Unset, str] = UNSET
    if not isinstance(panel_uuid, Unset):
        json_panel_uuid = str(panel_uuid)
    params["panel_uuid"] = json_panel_uuid

    json_post_award_status: Union[Unset, list[str]] = UNSET
    if not isinstance(post_award_status, Unset):
        json_post_award_status = []
        for post_award_status_item_data in post_award_status:
            post_award_status_item = post_award_status_item_data.value
            json_post_award_status.append(post_award_status_item)

    params["post_award_status"] = json_post_award_status

    json_round_: Union[Unset, str] = UNSET
    if not isinstance(round_, Unset):
        json_round_ = str(round_)
    params["round"] = json_round_

    json_round_uuid: Union[Unset, str] = UNSET
    if not isinstance(round_uuid, Unset):
        json_round_uuid = str(round_uuid)
    params["round_uuid"] = json_round_uuid

    json_run_phase: Union[Unset, str] = UNSET
    if not isinstance(run_phase, Unset):
        json_run_phase = run_phase.value

    params["run_phase"] = json_run_phase

    json_run_state: Union[Unset, str] = UNSET
    if not isinstance(run_state, Unset):
        json_run_state = run_state.value

    params["run_state"] = json_run_state

    params["slug"] = slug

    json_state: Union[Unset, list[str]] = UNSET
    if not isinstance(state, Unset):
        json_state = []
        for state_item_data in state:
            state_item = state_item_data.value
            json_state.append(state_item)

    params["state"] = json_state

    params["step"] = step

    json_step_uuid: Union[Unset, str] = UNSET
    if not isinstance(step_uuid, Unset):
        json_step_uuid = str(step_uuid)
    params["step_uuid"] = json_step_uuid

    json_workflow_step: Union[Unset, list[str]] = UNSET
    if not isinstance(workflow_step, Unset):
        json_workflow_step = workflow_step

    params["workflow_step"] = json_workflow_step

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/proposal-proposals/{uuid}/step-checklist-responses/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[Any, list["StepContributionWithAnswers"]]:
    if response.status_code == 404:
        raise errors.UnexpectedStatus(response.status_code, response.content, response.url)
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = StepContributionWithAnswers.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = response.json()
        return response_400
    raise errors.UnexpectedStatus(response.status_code, response.content, response.url)


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, list["StepContributionWithAnswers"]]]:
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
    as_role: Union[Unset, ResponsibleRoleEnum] = UNSET,
    call_uuid: Union[Unset, UUID] = UNSET,
    changes_requested: Union[Unset, bool] = UNSET,
    created_by_uuid: Union[Unset, UUID] = UNSET,
    final_report_overdue: Union[Unset, bool] = UNSET,
    involved: Union[Unset, bool] = UNSET,
    my_proposals: Union[Unset, bool] = UNSET,
    name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[ProposalOEnum]] = UNSET,
    organization_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    panel_uuid: Union[Unset, UUID] = UNSET,
    post_award_status: Union[Unset, list[PostAwardStatusEnum]] = UNSET,
    round_: Union[Unset, UUID] = UNSET,
    round_uuid: Union[Unset, UUID] = UNSET,
    run_phase: Union[Unset, ProposalRunPhaseEnum] = UNSET,
    run_state: Union[Unset, ProposalRunStateEnum] = UNSET,
    slug: Union[Unset, str] = UNSET,
    state: Union[Unset, list[ProposalStates]] = UNSET,
    step: Union[Unset, str] = UNSET,
    step_uuid: Union[Unset, UUID] = UNSET,
    workflow_step: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, list["StepContributionWithAnswers"]]]:
    """List the contributions to a workflow step with their checklist answers, for the threaded view of the
    step: one entry per contribution (per person or per requested offering) the caller may read.

    Args:
        uuid (UUID):
        as_role (Union[Unset, ResponsibleRoleEnum]):
        call_uuid (Union[Unset, UUID]):
        changes_requested (Union[Unset, bool]):
        created_by_uuid (Union[Unset, UUID]):
        final_report_overdue (Union[Unset, bool]):
        involved (Union[Unset, bool]):
        my_proposals (Union[Unset, bool]):
        name (Union[Unset, str]):
        o (Union[Unset, list[ProposalOEnum]]):
        organization_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        panel_uuid (Union[Unset, UUID]):
        post_award_status (Union[Unset, list[PostAwardStatusEnum]]):
        round_ (Union[Unset, UUID]):
        round_uuid (Union[Unset, UUID]):
        run_phase (Union[Unset, ProposalRunPhaseEnum]):
        run_state (Union[Unset, ProposalRunStateEnum]):
        slug (Union[Unset, str]):
        state (Union[Unset, list[ProposalStates]]):
        step (Union[Unset, str]):
        step_uuid (Union[Unset, UUID]):
        workflow_step (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['StepContributionWithAnswers']]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        as_role=as_role,
        call_uuid=call_uuid,
        changes_requested=changes_requested,
        created_by_uuid=created_by_uuid,
        final_report_overdue=final_report_overdue,
        involved=involved,
        my_proposals=my_proposals,
        name=name,
        o=o,
        organization_uuid=organization_uuid,
        page=page,
        page_size=page_size,
        panel_uuid=panel_uuid,
        post_award_status=post_award_status,
        round_=round_,
        round_uuid=round_uuid,
        run_phase=run_phase,
        run_state=run_state,
        slug=slug,
        state=state,
        step=step,
        step_uuid=step_uuid,
        workflow_step=workflow_step,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    as_role: Union[Unset, ResponsibleRoleEnum] = UNSET,
    call_uuid: Union[Unset, UUID] = UNSET,
    changes_requested: Union[Unset, bool] = UNSET,
    created_by_uuid: Union[Unset, UUID] = UNSET,
    final_report_overdue: Union[Unset, bool] = UNSET,
    involved: Union[Unset, bool] = UNSET,
    my_proposals: Union[Unset, bool] = UNSET,
    name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[ProposalOEnum]] = UNSET,
    organization_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    panel_uuid: Union[Unset, UUID] = UNSET,
    post_award_status: Union[Unset, list[PostAwardStatusEnum]] = UNSET,
    round_: Union[Unset, UUID] = UNSET,
    round_uuid: Union[Unset, UUID] = UNSET,
    run_phase: Union[Unset, ProposalRunPhaseEnum] = UNSET,
    run_state: Union[Unset, ProposalRunStateEnum] = UNSET,
    slug: Union[Unset, str] = UNSET,
    state: Union[Unset, list[ProposalStates]] = UNSET,
    step: Union[Unset, str] = UNSET,
    step_uuid: Union[Unset, UUID] = UNSET,
    workflow_step: Union[Unset, list[str]] = UNSET,
) -> Union[Any, list["StepContributionWithAnswers"]]:
    """List the contributions to a workflow step with their checklist answers, for the threaded view of the
    step: one entry per contribution (per person or per requested offering) the caller may read.

    Args:
        uuid (UUID):
        as_role (Union[Unset, ResponsibleRoleEnum]):
        call_uuid (Union[Unset, UUID]):
        changes_requested (Union[Unset, bool]):
        created_by_uuid (Union[Unset, UUID]):
        final_report_overdue (Union[Unset, bool]):
        involved (Union[Unset, bool]):
        my_proposals (Union[Unset, bool]):
        name (Union[Unset, str]):
        o (Union[Unset, list[ProposalOEnum]]):
        organization_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        panel_uuid (Union[Unset, UUID]):
        post_award_status (Union[Unset, list[PostAwardStatusEnum]]):
        round_ (Union[Unset, UUID]):
        round_uuid (Union[Unset, UUID]):
        run_phase (Union[Unset, ProposalRunPhaseEnum]):
        run_state (Union[Unset, ProposalRunStateEnum]):
        slug (Union[Unset, str]):
        state (Union[Unset, list[ProposalStates]]):
        step (Union[Unset, str]):
        step_uuid (Union[Unset, UUID]):
        workflow_step (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['StepContributionWithAnswers']]
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        as_role=as_role,
        call_uuid=call_uuid,
        changes_requested=changes_requested,
        created_by_uuid=created_by_uuid,
        final_report_overdue=final_report_overdue,
        involved=involved,
        my_proposals=my_proposals,
        name=name,
        o=o,
        organization_uuid=organization_uuid,
        page=page,
        page_size=page_size,
        panel_uuid=panel_uuid,
        post_award_status=post_award_status,
        round_=round_,
        round_uuid=round_uuid,
        run_phase=run_phase,
        run_state=run_state,
        slug=slug,
        state=state,
        step=step,
        step_uuid=step_uuid,
        workflow_step=workflow_step,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    as_role: Union[Unset, ResponsibleRoleEnum] = UNSET,
    call_uuid: Union[Unset, UUID] = UNSET,
    changes_requested: Union[Unset, bool] = UNSET,
    created_by_uuid: Union[Unset, UUID] = UNSET,
    final_report_overdue: Union[Unset, bool] = UNSET,
    involved: Union[Unset, bool] = UNSET,
    my_proposals: Union[Unset, bool] = UNSET,
    name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[ProposalOEnum]] = UNSET,
    organization_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    panel_uuid: Union[Unset, UUID] = UNSET,
    post_award_status: Union[Unset, list[PostAwardStatusEnum]] = UNSET,
    round_: Union[Unset, UUID] = UNSET,
    round_uuid: Union[Unset, UUID] = UNSET,
    run_phase: Union[Unset, ProposalRunPhaseEnum] = UNSET,
    run_state: Union[Unset, ProposalRunStateEnum] = UNSET,
    slug: Union[Unset, str] = UNSET,
    state: Union[Unset, list[ProposalStates]] = UNSET,
    step: Union[Unset, str] = UNSET,
    step_uuid: Union[Unset, UUID] = UNSET,
    workflow_step: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, list["StepContributionWithAnswers"]]]:
    """List the contributions to a workflow step with their checklist answers, for the threaded view of the
    step: one entry per contribution (per person or per requested offering) the caller may read.

    Args:
        uuid (UUID):
        as_role (Union[Unset, ResponsibleRoleEnum]):
        call_uuid (Union[Unset, UUID]):
        changes_requested (Union[Unset, bool]):
        created_by_uuid (Union[Unset, UUID]):
        final_report_overdue (Union[Unset, bool]):
        involved (Union[Unset, bool]):
        my_proposals (Union[Unset, bool]):
        name (Union[Unset, str]):
        o (Union[Unset, list[ProposalOEnum]]):
        organization_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        panel_uuid (Union[Unset, UUID]):
        post_award_status (Union[Unset, list[PostAwardStatusEnum]]):
        round_ (Union[Unset, UUID]):
        round_uuid (Union[Unset, UUID]):
        run_phase (Union[Unset, ProposalRunPhaseEnum]):
        run_state (Union[Unset, ProposalRunStateEnum]):
        slug (Union[Unset, str]):
        state (Union[Unset, list[ProposalStates]]):
        step (Union[Unset, str]):
        step_uuid (Union[Unset, UUID]):
        workflow_step (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['StepContributionWithAnswers']]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        as_role=as_role,
        call_uuid=call_uuid,
        changes_requested=changes_requested,
        created_by_uuid=created_by_uuid,
        final_report_overdue=final_report_overdue,
        involved=involved,
        my_proposals=my_proposals,
        name=name,
        o=o,
        organization_uuid=organization_uuid,
        page=page,
        page_size=page_size,
        panel_uuid=panel_uuid,
        post_award_status=post_award_status,
        round_=round_,
        round_uuid=round_uuid,
        run_phase=run_phase,
        run_state=run_state,
        slug=slug,
        state=state,
        step=step,
        step_uuid=step_uuid,
        workflow_step=workflow_step,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    as_role: Union[Unset, ResponsibleRoleEnum] = UNSET,
    call_uuid: Union[Unset, UUID] = UNSET,
    changes_requested: Union[Unset, bool] = UNSET,
    created_by_uuid: Union[Unset, UUID] = UNSET,
    final_report_overdue: Union[Unset, bool] = UNSET,
    involved: Union[Unset, bool] = UNSET,
    my_proposals: Union[Unset, bool] = UNSET,
    name: Union[Unset, str] = UNSET,
    o: Union[Unset, list[ProposalOEnum]] = UNSET,
    organization_uuid: Union[Unset, UUID] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    panel_uuid: Union[Unset, UUID] = UNSET,
    post_award_status: Union[Unset, list[PostAwardStatusEnum]] = UNSET,
    round_: Union[Unset, UUID] = UNSET,
    round_uuid: Union[Unset, UUID] = UNSET,
    run_phase: Union[Unset, ProposalRunPhaseEnum] = UNSET,
    run_state: Union[Unset, ProposalRunStateEnum] = UNSET,
    slug: Union[Unset, str] = UNSET,
    state: Union[Unset, list[ProposalStates]] = UNSET,
    step: Union[Unset, str] = UNSET,
    step_uuid: Union[Unset, UUID] = UNSET,
    workflow_step: Union[Unset, list[str]] = UNSET,
) -> Union[Any, list["StepContributionWithAnswers"]]:
    """List the contributions to a workflow step with their checklist answers, for the threaded view of the
    step: one entry per contribution (per person or per requested offering) the caller may read.

    Args:
        uuid (UUID):
        as_role (Union[Unset, ResponsibleRoleEnum]):
        call_uuid (Union[Unset, UUID]):
        changes_requested (Union[Unset, bool]):
        created_by_uuid (Union[Unset, UUID]):
        final_report_overdue (Union[Unset, bool]):
        involved (Union[Unset, bool]):
        my_proposals (Union[Unset, bool]):
        name (Union[Unset, str]):
        o (Union[Unset, list[ProposalOEnum]]):
        organization_uuid (Union[Unset, UUID]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        panel_uuid (Union[Unset, UUID]):
        post_award_status (Union[Unset, list[PostAwardStatusEnum]]):
        round_ (Union[Unset, UUID]):
        round_uuid (Union[Unset, UUID]):
        run_phase (Union[Unset, ProposalRunPhaseEnum]):
        run_state (Union[Unset, ProposalRunStateEnum]):
        slug (Union[Unset, str]):
        state (Union[Unset, list[ProposalStates]]):
        step (Union[Unset, str]):
        step_uuid (Union[Unset, UUID]):
        workflow_step (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['StepContributionWithAnswers']]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            as_role=as_role,
            call_uuid=call_uuid,
            changes_requested=changes_requested,
            created_by_uuid=created_by_uuid,
            final_report_overdue=final_report_overdue,
            involved=involved,
            my_proposals=my_proposals,
            name=name,
            o=o,
            organization_uuid=organization_uuid,
            page=page,
            page_size=page_size,
            panel_uuid=panel_uuid,
            post_award_status=post_award_status,
            round_=round_,
            round_uuid=round_uuid,
            run_phase=run_phase,
            run_state=run_state,
            slug=slug,
            state=state,
            step=step,
            step_uuid=step_uuid,
            workflow_step=workflow_step,
        )
    ).parsed
