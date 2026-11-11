from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.allocation_time_enum import AllocationTimeEnum
from ..models.automatic_decision_guard_enum import AutomaticDecisionGuardEnum
from ..models.blank_enum import BlankEnum
from ..models.call_step_kind_enum import CallStepKindEnum
from ..models.on_negative_enum import OnNegativeEnum
from ..models.outcome_set_enum import OutcomeSetEnum
from ..models.responsible_role_enum import ResponsibleRoleEnum
from ..models.transition_mode_enum import TransitionModeEnum
from ..models.workflow_phase_enum import WorkflowPhaseEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.step_run_condition_request import StepRunConditionRequest
    from ..models.step_status_labels_request import StepStatusLabelsRequest
    from ..models.workflow_criterion_request import WorkflowCriterionRequest


T = TypeVar("T", bound="CallWorkflowStepRequest")


@_attrs_define
class CallWorkflowStepRequest:
    """
    Attributes:
        key (Union[Unset, str]): Identifier of the step within its call. Derived from the name when left out. Cannot
            change once the step exists.
        step (Union[Unset, str]): Deprecated alias of key.
        kind (Union[Unset, CallStepKindEnum]):
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        order (Union[Unset, int]): Position in the call's workflow. A step already there, and every step after it, moves
            one down. Appended when left out.
        outcome_set (Union[Unset, OutcomeSetEnum]):
        on_negative (Union[Unset, OnNegativeEnum]):
        is_enabled (Union[Unset, bool]): Whether this step is enabled. Disabled steps are skipped.
        is_allocation_decision (Union[Unset, bool]): The decision step that settles the award. A call is activated with
            exactly one enabled.
        duration_in_days (Union[None, Unset, int]): Duration in days. Used to calculate deadlines.
        checklist (Union[None, UUID, Unset]):
        checklist_required (Union[Unset, bool]): When the step has a checklist, block completion until its required
            questions are answered. Set False to make the checklist advisory.
        blind_review (Union[Unset, bool]): Evaluators cannot see each other's assessments.
        requires_coi_confirmation (Union[Unset, bool]): Evaluator must confirm absence of conflict of interest.
        coi_declaration_text (Union[Unset, str]): The conflict-of-interest declaration this step's evaluators confirm;
            empty for the call's, or the platform's standard one.
        contributor_source (Union[Unset, str]): Who contributes to the step, each with a contribution of their own:
            none, requested_offering_team, assigned_reviewers, proposal_role:<id> or
            call_role:<call_manager|reviewer|panel_member>.
        per_requested_offering (Union[Unset, bool]): One contribution per offering the proposal requests, which any
            member of that offering's team may fill.
        contributors_lead_only (Union[Unset, bool]): Only the lead of the evaluator role the contributor source names
            contributes: one slot, the lead's, which moves when the lead changes. The step waits while the role has no lead.
        delegable_to (Union[Unset, str]): Who a contribution slot of the step can be handed to by its holder or the
            call's managers: empty for nobody, offering_team for anyone with a role on the slot's own offering (per-offering
            steps), or proposal_role:<id> for the holders of an evaluator role on the proposal (per-person steps). The
            person it is handed to accepts or declines it.
        min_contributions (Union[None, Unset, int]): Minimum contributions submitted before the step can complete. On a
            step without contributors, the minimum of the proposal's submitted reviews.
        max_contributions (Union[None, Unset, int]): Most contributions the step accepts; no limit when empty.
        min_reviewers (Union[None, Unset, int]): Deprecated alias of min_contributions.
        min_score_threshold (Union[None, Unset, str]): Minimum average score required before this step can complete with
            any outcome but declined (a completion gate; it does not auto-reject lower scores). A step with contributors
            scores its own submitted reviews. A step without contributors that reads input steps takes the score of the
            latest completed input step that has one: the average of its reviews, else of the rating answers in its
            checklists. Otherwise all the proposal's submitted reviews count.
        applicant_visible (Union[Unset, bool]): Whether the applicant can see step details (not just status).
        completer (Union[BlankEnum, None, ResponsibleRoleEnum, Unset]): Role expected to complete this step.
        responsible_role (Union[None, ResponsibleRoleEnum, Unset]): Deprecated alias of completer.
        completer_proposal_role (Union[None, UUID, Unset]): The call's evaluator role whose holders complete the step;
            required when the completer is proposal_role.
        assigns_roles (Union[Unset, list[UUID]]): Assignment step: the call's evaluator roles whose holders the
            completer picks, such as a lead and a second rapporteur.
        input_steps (Union[Unset, list[UUID]]): Earlier steps of the call whose outputs this step's contributors and
            completer read; on an applicant step, whose public parts the applicant reads.
        release_to_applicant (Union[Unset, bool]): Assessment step: once completed, its report can be released to the
            applicant, such as a consolidated report or final feedback.
        collects_reviewer_suggestions (Union[Unset, bool]): Assessment step of evaluator-role holders: each holder may
            suggest reviewers for the proposal while the step is active. The call's managers turn suggestions into pool
            invitations.
        allows_change_requests (Union[Unset, bool]): Whoever acts on the step may send the proposal back to the
            applicant to change the parts they unlock, as often as needed. The proposal stays in review on the step
            meanwhile. Not for the allocation decision nor an applicant step.
        allows_conditional_acceptance (Union[Unset, bool]): Per-offering assessment: a contribution may accept a
            requested offering under conditions. Off, it accepts or rejects it.
        transition_mode (Union[Unset, TransitionModeEnum]):
        run_condition (Union['StepRunConditionRequest', None, Unset]): When the step runs: empty to run on every
            proposal; the key of an earlier step and the outcomes of it, or of its contributions, on which it runs; or the
            key of an earlier step and "score_spread_above": the points by which the highest and lowest scores its
            contributions gave must differ for the step to run. A proposal on which it does not hold skips the step. Fixed
            for a proposal when it is submitted.
        parallel_with_previous (Union[Unset, bool]): Start together with the step before it, as one stage: every step of
            a stage starts at once, and the next stage starts when all of them have ended.
        round_scoped (Union[Unset, bool]): Run the step once per round rather than per proposal, such as a panel meeting
            after the cut-off: the call's managers open it for the round's proposals together, its contributors write one
            round report each covering their proposals, and it is completed for the round, never on one proposal.
        phase (Union[Unset, WorkflowPhaseEnum]):
        project_end_offset_days (Union[None, Unset, int]): First step of an extension or closing phase: days before the
            project's end date. An extension can be asked for until then; the closing opens then (0: on the end date).
        status_labels (Union['StepStatusLabelsRequest', None, Unset]): What each audience's dashboard calls the step, as
            entered: per audience, while active, once completed, per outcome and while changes are requested. Left out, the
            computed label stays.
        include_award_response (Union[Unset, bool]): Allocation decision: require applicant award response after
            decision.
        decides_automatically (Union[Unset, bool]): Allocation decision: approve on reaching this step, as the system,
            with the award as requested; fall back to the completer when the approval is refused.
        automatic_decision_guard (Union[Unset, AutomaticDecisionGuardEnum]):
        allocation_time (Union[Unset, AllocationTimeEnum]):
        display_order (Union[None, Unset, int]): Deprecated: steps are ordered by order.
        criteria (Union[Unset, list['WorkflowCriterionRequest']]):
    """

    key: Union[Unset, str] = UNSET
    step: Union[Unset, str] = UNSET
    kind: Union[Unset, CallStepKindEnum] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    order: Union[Unset, int] = UNSET
    outcome_set: Union[Unset, OutcomeSetEnum] = UNSET
    on_negative: Union[Unset, OnNegativeEnum] = UNSET
    is_enabled: Union[Unset, bool] = UNSET
    is_allocation_decision: Union[Unset, bool] = UNSET
    duration_in_days: Union[None, Unset, int] = UNSET
    checklist: Union[None, UUID, Unset] = UNSET
    checklist_required: Union[Unset, bool] = UNSET
    blind_review: Union[Unset, bool] = UNSET
    requires_coi_confirmation: Union[Unset, bool] = UNSET
    coi_declaration_text: Union[Unset, str] = UNSET
    contributor_source: Union[Unset, str] = UNSET
    per_requested_offering: Union[Unset, bool] = UNSET
    contributors_lead_only: Union[Unset, bool] = UNSET
    delegable_to: Union[Unset, str] = UNSET
    min_contributions: Union[None, Unset, int] = UNSET
    max_contributions: Union[None, Unset, int] = UNSET
    min_reviewers: Union[None, Unset, int] = UNSET
    min_score_threshold: Union[None, Unset, str] = UNSET
    applicant_visible: Union[Unset, bool] = UNSET
    completer: Union[BlankEnum, None, ResponsibleRoleEnum, Unset] = UNSET
    responsible_role: Union[None, ResponsibleRoleEnum, Unset] = UNSET
    completer_proposal_role: Union[None, UUID, Unset] = UNSET
    assigns_roles: Union[Unset, list[UUID]] = UNSET
    input_steps: Union[Unset, list[UUID]] = UNSET
    release_to_applicant: Union[Unset, bool] = UNSET
    collects_reviewer_suggestions: Union[Unset, bool] = UNSET
    allows_change_requests: Union[Unset, bool] = UNSET
    allows_conditional_acceptance: Union[Unset, bool] = UNSET
    transition_mode: Union[Unset, TransitionModeEnum] = UNSET
    run_condition: Union["StepRunConditionRequest", None, Unset] = UNSET
    parallel_with_previous: Union[Unset, bool] = UNSET
    round_scoped: Union[Unset, bool] = UNSET
    phase: Union[Unset, WorkflowPhaseEnum] = UNSET
    project_end_offset_days: Union[None, Unset, int] = UNSET
    status_labels: Union["StepStatusLabelsRequest", None, Unset] = UNSET
    include_award_response: Union[Unset, bool] = UNSET
    decides_automatically: Union[Unset, bool] = UNSET
    automatic_decision_guard: Union[Unset, AutomaticDecisionGuardEnum] = UNSET
    allocation_time: Union[Unset, AllocationTimeEnum] = UNSET
    display_order: Union[None, Unset, int] = UNSET
    criteria: Union[Unset, list["WorkflowCriterionRequest"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.step_run_condition_request import StepRunConditionRequest
        from ..models.step_status_labels_request import StepStatusLabelsRequest

        key = self.key

        step = self.step

        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        name = self.name

        description = self.description

        order = self.order

        outcome_set: Union[Unset, str] = UNSET
        if not isinstance(self.outcome_set, Unset):
            outcome_set = self.outcome_set.value

        on_negative: Union[Unset, str] = UNSET
        if not isinstance(self.on_negative, Unset):
            on_negative = self.on_negative.value

        is_enabled = self.is_enabled

        is_allocation_decision = self.is_allocation_decision

        duration_in_days: Union[None, Unset, int]
        if isinstance(self.duration_in_days, Unset):
            duration_in_days = UNSET
        else:
            duration_in_days = self.duration_in_days

        checklist: Union[None, Unset, str]
        if isinstance(self.checklist, Unset):
            checklist = UNSET
        elif isinstance(self.checklist, UUID):
            checklist = str(self.checklist)
        else:
            checklist = self.checklist

        checklist_required = self.checklist_required

        blind_review = self.blind_review

        requires_coi_confirmation = self.requires_coi_confirmation

        coi_declaration_text = self.coi_declaration_text

        contributor_source = self.contributor_source

        per_requested_offering = self.per_requested_offering

        contributors_lead_only = self.contributors_lead_only

        delegable_to = self.delegable_to

        min_contributions: Union[None, Unset, int]
        if isinstance(self.min_contributions, Unset):
            min_contributions = UNSET
        else:
            min_contributions = self.min_contributions

        max_contributions: Union[None, Unset, int]
        if isinstance(self.max_contributions, Unset):
            max_contributions = UNSET
        else:
            max_contributions = self.max_contributions

        min_reviewers: Union[None, Unset, int]
        if isinstance(self.min_reviewers, Unset):
            min_reviewers = UNSET
        else:
            min_reviewers = self.min_reviewers

        min_score_threshold: Union[None, Unset, str]
        if isinstance(self.min_score_threshold, Unset):
            min_score_threshold = UNSET
        else:
            min_score_threshold = self.min_score_threshold

        applicant_visible = self.applicant_visible

        completer: Union[None, Unset, str]
        if isinstance(self.completer, Unset):
            completer = UNSET
        elif isinstance(self.completer, ResponsibleRoleEnum):
            completer = self.completer.value
        elif isinstance(self.completer, BlankEnum):
            completer = self.completer.value
        else:
            completer = self.completer

        responsible_role: Union[None, Unset, str]
        if isinstance(self.responsible_role, Unset):
            responsible_role = UNSET
        elif isinstance(self.responsible_role, ResponsibleRoleEnum):
            responsible_role = self.responsible_role.value
        else:
            responsible_role = self.responsible_role

        completer_proposal_role: Union[None, Unset, str]
        if isinstance(self.completer_proposal_role, Unset):
            completer_proposal_role = UNSET
        elif isinstance(self.completer_proposal_role, UUID):
            completer_proposal_role = str(self.completer_proposal_role)
        else:
            completer_proposal_role = self.completer_proposal_role

        assigns_roles: Union[Unset, list[str]] = UNSET
        if not isinstance(self.assigns_roles, Unset):
            assigns_roles = []
            for assigns_roles_item_data in self.assigns_roles:
                assigns_roles_item = str(assigns_roles_item_data)
                assigns_roles.append(assigns_roles_item)

        input_steps: Union[Unset, list[str]] = UNSET
        if not isinstance(self.input_steps, Unset):
            input_steps = []
            for input_steps_item_data in self.input_steps:
                input_steps_item = str(input_steps_item_data)
                input_steps.append(input_steps_item)

        release_to_applicant = self.release_to_applicant

        collects_reviewer_suggestions = self.collects_reviewer_suggestions

        allows_change_requests = self.allows_change_requests

        allows_conditional_acceptance = self.allows_conditional_acceptance

        transition_mode: Union[Unset, str] = UNSET
        if not isinstance(self.transition_mode, Unset):
            transition_mode = self.transition_mode.value

        run_condition: Union[None, Unset, dict[str, Any]]
        if isinstance(self.run_condition, Unset):
            run_condition = UNSET
        elif isinstance(self.run_condition, StepRunConditionRequest):
            run_condition = self.run_condition.to_dict()
        else:
            run_condition = self.run_condition

        parallel_with_previous = self.parallel_with_previous

        round_scoped = self.round_scoped

        phase: Union[Unset, str] = UNSET
        if not isinstance(self.phase, Unset):
            phase = self.phase.value

        project_end_offset_days: Union[None, Unset, int]
        if isinstance(self.project_end_offset_days, Unset):
            project_end_offset_days = UNSET
        else:
            project_end_offset_days = self.project_end_offset_days

        status_labels: Union[None, Unset, dict[str, Any]]
        if isinstance(self.status_labels, Unset):
            status_labels = UNSET
        elif isinstance(self.status_labels, StepStatusLabelsRequest):
            status_labels = self.status_labels.to_dict()
        else:
            status_labels = self.status_labels

        include_award_response = self.include_award_response

        decides_automatically = self.decides_automatically

        automatic_decision_guard: Union[Unset, str] = UNSET
        if not isinstance(self.automatic_decision_guard, Unset):
            automatic_decision_guard = self.automatic_decision_guard.value

        allocation_time: Union[Unset, str] = UNSET
        if not isinstance(self.allocation_time, Unset):
            allocation_time = self.allocation_time.value

        display_order: Union[None, Unset, int]
        if isinstance(self.display_order, Unset):
            display_order = UNSET
        else:
            display_order = self.display_order

        criteria: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.criteria, Unset):
            criteria = []
            for criteria_item_data in self.criteria:
                criteria_item = criteria_item_data.to_dict()
                criteria.append(criteria_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if step is not UNSET:
            field_dict["step"] = step
        if kind is not UNSET:
            field_dict["kind"] = kind
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if order is not UNSET:
            field_dict["order"] = order
        if outcome_set is not UNSET:
            field_dict["outcome_set"] = outcome_set
        if on_negative is not UNSET:
            field_dict["on_negative"] = on_negative
        if is_enabled is not UNSET:
            field_dict["is_enabled"] = is_enabled
        if is_allocation_decision is not UNSET:
            field_dict["is_allocation_decision"] = is_allocation_decision
        if duration_in_days is not UNSET:
            field_dict["duration_in_days"] = duration_in_days
        if checklist is not UNSET:
            field_dict["checklist"] = checklist
        if checklist_required is not UNSET:
            field_dict["checklist_required"] = checklist_required
        if blind_review is not UNSET:
            field_dict["blind_review"] = blind_review
        if requires_coi_confirmation is not UNSET:
            field_dict["requires_coi_confirmation"] = requires_coi_confirmation
        if coi_declaration_text is not UNSET:
            field_dict["coi_declaration_text"] = coi_declaration_text
        if contributor_source is not UNSET:
            field_dict["contributor_source"] = contributor_source
        if per_requested_offering is not UNSET:
            field_dict["per_requested_offering"] = per_requested_offering
        if contributors_lead_only is not UNSET:
            field_dict["contributors_lead_only"] = contributors_lead_only
        if delegable_to is not UNSET:
            field_dict["delegable_to"] = delegable_to
        if min_contributions is not UNSET:
            field_dict["min_contributions"] = min_contributions
        if max_contributions is not UNSET:
            field_dict["max_contributions"] = max_contributions
        if min_reviewers is not UNSET:
            field_dict["min_reviewers"] = min_reviewers
        if min_score_threshold is not UNSET:
            field_dict["min_score_threshold"] = min_score_threshold
        if applicant_visible is not UNSET:
            field_dict["applicant_visible"] = applicant_visible
        if completer is not UNSET:
            field_dict["completer"] = completer
        if responsible_role is not UNSET:
            field_dict["responsible_role"] = responsible_role
        if completer_proposal_role is not UNSET:
            field_dict["completer_proposal_role"] = completer_proposal_role
        if assigns_roles is not UNSET:
            field_dict["assigns_roles"] = assigns_roles
        if input_steps is not UNSET:
            field_dict["input_steps"] = input_steps
        if release_to_applicant is not UNSET:
            field_dict["release_to_applicant"] = release_to_applicant
        if collects_reviewer_suggestions is not UNSET:
            field_dict["collects_reviewer_suggestions"] = collects_reviewer_suggestions
        if allows_change_requests is not UNSET:
            field_dict["allows_change_requests"] = allows_change_requests
        if allows_conditional_acceptance is not UNSET:
            field_dict["allows_conditional_acceptance"] = allows_conditional_acceptance
        if transition_mode is not UNSET:
            field_dict["transition_mode"] = transition_mode
        if run_condition is not UNSET:
            field_dict["run_condition"] = run_condition
        if parallel_with_previous is not UNSET:
            field_dict["parallel_with_previous"] = parallel_with_previous
        if round_scoped is not UNSET:
            field_dict["round_scoped"] = round_scoped
        if phase is not UNSET:
            field_dict["phase"] = phase
        if project_end_offset_days is not UNSET:
            field_dict["project_end_offset_days"] = project_end_offset_days
        if status_labels is not UNSET:
            field_dict["status_labels"] = status_labels
        if include_award_response is not UNSET:
            field_dict["include_award_response"] = include_award_response
        if decides_automatically is not UNSET:
            field_dict["decides_automatically"] = decides_automatically
        if automatic_decision_guard is not UNSET:
            field_dict["automatic_decision_guard"] = automatic_decision_guard
        if allocation_time is not UNSET:
            field_dict["allocation_time"] = allocation_time
        if display_order is not UNSET:
            field_dict["display_order"] = display_order
        if criteria is not UNSET:
            field_dict["criteria"] = criteria

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.step_run_condition_request import StepRunConditionRequest
        from ..models.step_status_labels_request import StepStatusLabelsRequest
        from ..models.workflow_criterion_request import WorkflowCriterionRequest

        d = dict(src_dict)
        key = d.pop("key", UNSET)

        step = d.pop("step", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, CallStepKindEnum]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = CallStepKindEnum(_kind)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        order = d.pop("order", UNSET)

        _outcome_set = d.pop("outcome_set", UNSET)
        outcome_set: Union[Unset, OutcomeSetEnum]
        if isinstance(_outcome_set, Unset):
            outcome_set = UNSET
        else:
            outcome_set = OutcomeSetEnum(_outcome_set)

        _on_negative = d.pop("on_negative", UNSET)
        on_negative: Union[Unset, OnNegativeEnum]
        if isinstance(_on_negative, Unset):
            on_negative = UNSET
        else:
            on_negative = OnNegativeEnum(_on_negative)

        is_enabled = d.pop("is_enabled", UNSET)

        is_allocation_decision = d.pop("is_allocation_decision", UNSET)

        def _parse_duration_in_days(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        duration_in_days = _parse_duration_in_days(d.pop("duration_in_days", UNSET))

        def _parse_checklist(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                checklist_type_0 = UUID(data)

                return checklist_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        checklist = _parse_checklist(d.pop("checklist", UNSET))

        checklist_required = d.pop("checklist_required", UNSET)

        blind_review = d.pop("blind_review", UNSET)

        requires_coi_confirmation = d.pop("requires_coi_confirmation", UNSET)

        coi_declaration_text = d.pop("coi_declaration_text", UNSET)

        contributor_source = d.pop("contributor_source", UNSET)

        per_requested_offering = d.pop("per_requested_offering", UNSET)

        contributors_lead_only = d.pop("contributors_lead_only", UNSET)

        delegable_to = d.pop("delegable_to", UNSET)

        def _parse_min_contributions(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        min_contributions = _parse_min_contributions(d.pop("min_contributions", UNSET))

        def _parse_max_contributions(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_contributions = _parse_max_contributions(d.pop("max_contributions", UNSET))

        def _parse_min_reviewers(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        min_reviewers = _parse_min_reviewers(d.pop("min_reviewers", UNSET))

        def _parse_min_score_threshold(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        min_score_threshold = _parse_min_score_threshold(d.pop("min_score_threshold", UNSET))

        applicant_visible = d.pop("applicant_visible", UNSET)

        def _parse_completer(data: object) -> Union[BlankEnum, None, ResponsibleRoleEnum, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completer_type_0 = ResponsibleRoleEnum(data)

                return completer_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completer_type_1 = BlankEnum(data)

                return completer_type_1
            except:  # noqa: E722
                pass
            return cast(Union[BlankEnum, None, ResponsibleRoleEnum, Unset], data)

        completer = _parse_completer(d.pop("completer", UNSET))

        def _parse_responsible_role(data: object) -> Union[None, ResponsibleRoleEnum, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                responsible_role_type_0 = ResponsibleRoleEnum(data)

                return responsible_role_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, ResponsibleRoleEnum, Unset], data)

        responsible_role = _parse_responsible_role(d.pop("responsible_role", UNSET))

        def _parse_completer_proposal_role(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completer_proposal_role_type_0 = UUID(data)

                return completer_proposal_role_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        completer_proposal_role = _parse_completer_proposal_role(d.pop("completer_proposal_role", UNSET))

        assigns_roles = []
        _assigns_roles = d.pop("assigns_roles", UNSET)
        for assigns_roles_item_data in _assigns_roles or []:
            assigns_roles_item = UUID(assigns_roles_item_data)

            assigns_roles.append(assigns_roles_item)

        input_steps = []
        _input_steps = d.pop("input_steps", UNSET)
        for input_steps_item_data in _input_steps or []:
            input_steps_item = UUID(input_steps_item_data)

            input_steps.append(input_steps_item)

        release_to_applicant = d.pop("release_to_applicant", UNSET)

        collects_reviewer_suggestions = d.pop("collects_reviewer_suggestions", UNSET)

        allows_change_requests = d.pop("allows_change_requests", UNSET)

        allows_conditional_acceptance = d.pop("allows_conditional_acceptance", UNSET)

        _transition_mode = d.pop("transition_mode", UNSET)
        transition_mode: Union[Unset, TransitionModeEnum]
        if isinstance(_transition_mode, Unset):
            transition_mode = UNSET
        else:
            transition_mode = TransitionModeEnum(_transition_mode)

        def _parse_run_condition(data: object) -> Union["StepRunConditionRequest", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                run_condition_type_1 = StepRunConditionRequest.from_dict(data)

                return run_condition_type_1
            except:  # noqa: E722
                pass
            return cast(Union["StepRunConditionRequest", None, Unset], data)

        run_condition = _parse_run_condition(d.pop("run_condition", UNSET))

        parallel_with_previous = d.pop("parallel_with_previous", UNSET)

        round_scoped = d.pop("round_scoped", UNSET)

        _phase = d.pop("phase", UNSET)
        phase: Union[Unset, WorkflowPhaseEnum]
        if isinstance(_phase, Unset):
            phase = UNSET
        else:
            phase = WorkflowPhaseEnum(_phase)

        def _parse_project_end_offset_days(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        project_end_offset_days = _parse_project_end_offset_days(d.pop("project_end_offset_days", UNSET))

        def _parse_status_labels(data: object) -> Union["StepStatusLabelsRequest", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                status_labels_type_1 = StepStatusLabelsRequest.from_dict(data)

                return status_labels_type_1
            except:  # noqa: E722
                pass
            return cast(Union["StepStatusLabelsRequest", None, Unset], data)

        status_labels = _parse_status_labels(d.pop("status_labels", UNSET))

        include_award_response = d.pop("include_award_response", UNSET)

        decides_automatically = d.pop("decides_automatically", UNSET)

        _automatic_decision_guard = d.pop("automatic_decision_guard", UNSET)
        automatic_decision_guard: Union[Unset, AutomaticDecisionGuardEnum]
        if isinstance(_automatic_decision_guard, Unset):
            automatic_decision_guard = UNSET
        else:
            automatic_decision_guard = AutomaticDecisionGuardEnum(_automatic_decision_guard)

        _allocation_time = d.pop("allocation_time", UNSET)
        allocation_time: Union[Unset, AllocationTimeEnum]
        if isinstance(_allocation_time, Unset):
            allocation_time = UNSET
        else:
            allocation_time = AllocationTimeEnum(_allocation_time)

        def _parse_display_order(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        display_order = _parse_display_order(d.pop("display_order", UNSET))

        criteria = []
        _criteria = d.pop("criteria", UNSET)
        for criteria_item_data in _criteria or []:
            criteria_item = WorkflowCriterionRequest.from_dict(criteria_item_data)

            criteria.append(criteria_item)

        call_workflow_step_request = cls(
            key=key,
            step=step,
            kind=kind,
            name=name,
            description=description,
            order=order,
            outcome_set=outcome_set,
            on_negative=on_negative,
            is_enabled=is_enabled,
            is_allocation_decision=is_allocation_decision,
            duration_in_days=duration_in_days,
            checklist=checklist,
            checklist_required=checklist_required,
            blind_review=blind_review,
            requires_coi_confirmation=requires_coi_confirmation,
            coi_declaration_text=coi_declaration_text,
            contributor_source=contributor_source,
            per_requested_offering=per_requested_offering,
            contributors_lead_only=contributors_lead_only,
            delegable_to=delegable_to,
            min_contributions=min_contributions,
            max_contributions=max_contributions,
            min_reviewers=min_reviewers,
            min_score_threshold=min_score_threshold,
            applicant_visible=applicant_visible,
            completer=completer,
            responsible_role=responsible_role,
            completer_proposal_role=completer_proposal_role,
            assigns_roles=assigns_roles,
            input_steps=input_steps,
            release_to_applicant=release_to_applicant,
            collects_reviewer_suggestions=collects_reviewer_suggestions,
            allows_change_requests=allows_change_requests,
            allows_conditional_acceptance=allows_conditional_acceptance,
            transition_mode=transition_mode,
            run_condition=run_condition,
            parallel_with_previous=parallel_with_previous,
            round_scoped=round_scoped,
            phase=phase,
            project_end_offset_days=project_end_offset_days,
            status_labels=status_labels,
            include_award_response=include_award_response,
            decides_automatically=decides_automatically,
            automatic_decision_guard=automatic_decision_guard,
            allocation_time=allocation_time,
            display_order=display_order,
            criteria=criteria,
        )

        call_workflow_step_request.additional_properties = d
        return call_workflow_step_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
