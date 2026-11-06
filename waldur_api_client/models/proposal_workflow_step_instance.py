import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.call_step_kind_enum import CallStepKindEnum
from ..models.on_negative_enum import OnNegativeEnum
from ..models.outcome_set_enum import OutcomeSetEnum
from ..models.proposal_workflow_step_instance_status_enum import ProposalWorkflowStepInstanceStatusEnum
from ..models.skipped_reason_enum import SkippedReasonEnum
from ..models.workflow_phase_enum import WorkflowPhaseEnum

if TYPE_CHECKING:
    from ..models.step_checklist_status import StepChecklistStatus
    from ..models.step_run_condition import StepRunCondition
    from ..models.step_score_gate import StepScoreGate


T = TypeVar("T", bound="ProposalWorkflowStepInstance")


@_attrs_define
class ProposalWorkflowStepInstance:
    """
    Attributes:
        uuid (UUID):
        step (str): Key of the call step, copied from it.
        call_step_uuid (UUID):
        kind (CallStepKindEnum):
        order (int): Position of the step in this proposal's path.
        stage (int): The stage the step runs in on this proposal: steps of one stage run at the same time, and the next
            stage starts once all of them have ended.
        run_uuid (Union[None, UUID]): The extension request or final report the step belongs to; null for a step of the
            evaluation.
        phase (WorkflowPhaseEnum):
        is_overdue (bool): A final report past its due date, still to be submitted. Other steps lapse at their deadline
            instead.
        run_condition (StepRunCondition):
        skipped_reason (Union[None, SkippedReasonEnum]): Why a skipped step did not run: 'condition_not_met' when its
            run condition did not hold. Null otherwise.
        status_label (Union[None, str]): What the call configured the caller's dashboard to call the step in its state:
            the applicant team's labels on a step visible to them and on the allocation decision, else the evaluators'. Null
            to fall back to the computed label.
        outcome_set (OutcomeSetEnum):
        allowed_outcomes (list[str]):
        contributor_source (str):
        contributor_proposal_role_uuid (Union[None, UUID]): The evaluator role whose holders contribute to the step,
            when its contributors hold one.
        per_requested_offering (bool):
        round_scoped (bool): Whether the step runs once per round: it is completed for the round, never on the proposal
            alone.
        contributors_lead_only (bool): Whether only the lead of the evaluator role contributes.
        delegable_to (str): Who a contribution slot of the step can be handed to.
        awaiting_lead (Union[None, str]): Why the active step waits for the lead of its evaluator role, when only the
            lead contributes and none can; null otherwise, and for readers outside the call team.
        waiting_for (Union[None, str]): Why the active step cannot move on without someone being added or a call manager
            acting in another's place, with the way forward; null when its own people can move it, and for readers outside
            the call team.
        completion_warning (Union[None, str]): What completing the active step now leaves short, for the completer to
            confirm: a later review step needing more reviews than reviewers are assigned. Null otherwise, and for readers
            outside the call team.
        on_negative (OnNegativeEnum):
        contribution_outcomes (list[str]): Outcomes a contribution to the step may conclude with; empty when
            contributions carry no outcome of their own.
        is_allocation_decision (bool): Whether this step settles the proposal's award.
        step_name (str):
        step_description (str):
        completer (Union[None, str]):
        responsible_role (Union[None, str]):
        completer_proposal_role_uuid (Union[None, UUID]): The evaluator role whose holders complete the step, if any.
        completer_proposal_role_name (Union[None, str]):
        status (ProposalWorkflowStepInstanceStatusEnum):
        outcome (Union[None, str]): Step-specific outcome (e.g., eligible, feasible, approved).
        outcome_reason (str): Explanation for the outcome (e.g., rejection reason).
        rejection_reason (Union[None, str]):
        internal_notes (Union[None, str]):
        started_at (Union[None, datetime.datetime]): When this step became active.
        completed_at (Union[None, datetime.datetime]):
        completed_by (Union[None, UUID]):
        deadline (Union[None, datetime.datetime]): Computed from started_at + step duration_in_days.
        applicant_visible (bool):
        duration_in_days (Union[None, int]):
        is_required (bool):
        checklist_status (Union['StepChecklistStatus', None]):
        input_step_uuids (list[UUID]):
        release_to_applicant (bool): Whether the step's report is released to the applicant.
        released_at (Union[None, datetime.datetime]): When the step's report was released to the applicant.
        can_release (bool): Whether the caller may release the step's report to the applicant now: its completer or
            those overseeing the call, once the step is completed and not yet released.
        collects_reviewer_suggestions (bool): Whether the step's contributors suggest reviewers for the proposal.
        allows_change_requests (bool): Whether whoever acts on the step may send the proposal back to its applicant for
            changes.
        can_suggest_reviewers (bool): Whether the caller may suggest a reviewer through the step now: it is the active
            step collecting suggestions and the caller's own contribution to it is still open.
        ready_to_complete (bool): For whoever may complete the active step: every contribution is in and its completion
            gates are met, so it waits only for them. False for everyone else.
        score_gate (Union['StepScoreGate', None]): The active step's score against its minimum score threshold, before
            anyone decides: below it, only declining is possible. Null without a threshold, once the step is no longer
            active, and for readers outside the call team.
        decided_automatically (bool): Whether the system took this allocation decision itself, on a call whose decision
            decides automatically.
    """

    uuid: UUID
    step: str
    call_step_uuid: UUID
    kind: CallStepKindEnum
    order: int
    stage: int
    run_uuid: Union[None, UUID]
    phase: WorkflowPhaseEnum
    is_overdue: bool
    run_condition: "StepRunCondition"
    skipped_reason: Union[None, SkippedReasonEnum]
    status_label: Union[None, str]
    outcome_set: OutcomeSetEnum
    allowed_outcomes: list[str]
    contributor_source: str
    contributor_proposal_role_uuid: Union[None, UUID]
    per_requested_offering: bool
    round_scoped: bool
    contributors_lead_only: bool
    delegable_to: str
    awaiting_lead: Union[None, str]
    waiting_for: Union[None, str]
    completion_warning: Union[None, str]
    on_negative: OnNegativeEnum
    contribution_outcomes: list[str]
    is_allocation_decision: bool
    step_name: str
    step_description: str
    completer: Union[None, str]
    responsible_role: Union[None, str]
    completer_proposal_role_uuid: Union[None, UUID]
    completer_proposal_role_name: Union[None, str]
    status: ProposalWorkflowStepInstanceStatusEnum
    outcome: Union[None, str]
    outcome_reason: str
    rejection_reason: Union[None, str]
    internal_notes: Union[None, str]
    started_at: Union[None, datetime.datetime]
    completed_at: Union[None, datetime.datetime]
    completed_by: Union[None, UUID]
    deadline: Union[None, datetime.datetime]
    applicant_visible: bool
    duration_in_days: Union[None, int]
    is_required: bool
    checklist_status: Union["StepChecklistStatus", None]
    input_step_uuids: list[UUID]
    release_to_applicant: bool
    released_at: Union[None, datetime.datetime]
    can_release: bool
    collects_reviewer_suggestions: bool
    allows_change_requests: bool
    can_suggest_reviewers: bool
    ready_to_complete: bool
    score_gate: Union["StepScoreGate", None]
    decided_automatically: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.step_checklist_status import StepChecklistStatus
        from ..models.step_score_gate import StepScoreGate

        uuid = str(self.uuid)

        step = self.step

        call_step_uuid = str(self.call_step_uuid)

        kind = self.kind.value

        order = self.order

        stage = self.stage

        run_uuid: Union[None, str]
        if isinstance(self.run_uuid, UUID):
            run_uuid = str(self.run_uuid)
        else:
            run_uuid = self.run_uuid

        phase = self.phase.value

        is_overdue = self.is_overdue

        run_condition = self.run_condition.to_dict()

        skipped_reason: Union[None, str]
        if isinstance(self.skipped_reason, SkippedReasonEnum):
            skipped_reason = self.skipped_reason.value
        else:
            skipped_reason = self.skipped_reason

        status_label: Union[None, str]
        status_label = self.status_label

        outcome_set = self.outcome_set.value

        allowed_outcomes = self.allowed_outcomes

        contributor_source = self.contributor_source

        contributor_proposal_role_uuid: Union[None, str]
        if isinstance(self.contributor_proposal_role_uuid, UUID):
            contributor_proposal_role_uuid = str(self.contributor_proposal_role_uuid)
        else:
            contributor_proposal_role_uuid = self.contributor_proposal_role_uuid

        per_requested_offering = self.per_requested_offering

        round_scoped = self.round_scoped

        contributors_lead_only = self.contributors_lead_only

        delegable_to = self.delegable_to

        awaiting_lead: Union[None, str]
        awaiting_lead = self.awaiting_lead

        waiting_for: Union[None, str]
        waiting_for = self.waiting_for

        completion_warning: Union[None, str]
        completion_warning = self.completion_warning

        on_negative = self.on_negative.value

        contribution_outcomes = self.contribution_outcomes

        is_allocation_decision = self.is_allocation_decision

        step_name = self.step_name

        step_description = self.step_description

        completer: Union[None, str]
        completer = self.completer

        responsible_role: Union[None, str]
        responsible_role = self.responsible_role

        completer_proposal_role_uuid: Union[None, str]
        if isinstance(self.completer_proposal_role_uuid, UUID):
            completer_proposal_role_uuid = str(self.completer_proposal_role_uuid)
        else:
            completer_proposal_role_uuid = self.completer_proposal_role_uuid

        completer_proposal_role_name: Union[None, str]
        completer_proposal_role_name = self.completer_proposal_role_name

        status = self.status.value

        outcome: Union[None, str]
        outcome = self.outcome

        outcome_reason = self.outcome_reason

        rejection_reason: Union[None, str]
        rejection_reason = self.rejection_reason

        internal_notes: Union[None, str]
        internal_notes = self.internal_notes

        started_at: Union[None, str]
        if isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        completed_at: Union[None, str]
        if isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        completed_by: Union[None, str]
        if isinstance(self.completed_by, UUID):
            completed_by = str(self.completed_by)
        else:
            completed_by = self.completed_by

        deadline: Union[None, str]
        if isinstance(self.deadline, datetime.datetime):
            deadline = self.deadline.isoformat()
        else:
            deadline = self.deadline

        applicant_visible = self.applicant_visible

        duration_in_days: Union[None, int]
        duration_in_days = self.duration_in_days

        is_required = self.is_required

        checklist_status: Union[None, dict[str, Any]]
        if isinstance(self.checklist_status, StepChecklistStatus):
            checklist_status = self.checklist_status.to_dict()
        else:
            checklist_status = self.checklist_status

        input_step_uuids = []
        for input_step_uuids_item_data in self.input_step_uuids:
            input_step_uuids_item = str(input_step_uuids_item_data)
            input_step_uuids.append(input_step_uuids_item)

        release_to_applicant = self.release_to_applicant

        released_at: Union[None, str]
        if isinstance(self.released_at, datetime.datetime):
            released_at = self.released_at.isoformat()
        else:
            released_at = self.released_at

        can_release = self.can_release

        collects_reviewer_suggestions = self.collects_reviewer_suggestions

        allows_change_requests = self.allows_change_requests

        can_suggest_reviewers = self.can_suggest_reviewers

        ready_to_complete = self.ready_to_complete

        score_gate: Union[None, dict[str, Any]]
        if isinstance(self.score_gate, StepScoreGate):
            score_gate = self.score_gate.to_dict()
        else:
            score_gate = self.score_gate

        decided_automatically = self.decided_automatically

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "step": step,
                "call_step_uuid": call_step_uuid,
                "kind": kind,
                "order": order,
                "stage": stage,
                "run_uuid": run_uuid,
                "phase": phase,
                "is_overdue": is_overdue,
                "run_condition": run_condition,
                "skipped_reason": skipped_reason,
                "status_label": status_label,
                "outcome_set": outcome_set,
                "allowed_outcomes": allowed_outcomes,
                "contributor_source": contributor_source,
                "contributor_proposal_role_uuid": contributor_proposal_role_uuid,
                "per_requested_offering": per_requested_offering,
                "round_scoped": round_scoped,
                "contributors_lead_only": contributors_lead_only,
                "delegable_to": delegable_to,
                "awaiting_lead": awaiting_lead,
                "waiting_for": waiting_for,
                "completion_warning": completion_warning,
                "on_negative": on_negative,
                "contribution_outcomes": contribution_outcomes,
                "is_allocation_decision": is_allocation_decision,
                "step_name": step_name,
                "step_description": step_description,
                "completer": completer,
                "responsible_role": responsible_role,
                "completer_proposal_role_uuid": completer_proposal_role_uuid,
                "completer_proposal_role_name": completer_proposal_role_name,
                "status": status,
                "outcome": outcome,
                "outcome_reason": outcome_reason,
                "rejection_reason": rejection_reason,
                "internal_notes": internal_notes,
                "started_at": started_at,
                "completed_at": completed_at,
                "completed_by": completed_by,
                "deadline": deadline,
                "applicant_visible": applicant_visible,
                "duration_in_days": duration_in_days,
                "is_required": is_required,
                "checklist_status": checklist_status,
                "input_step_uuids": input_step_uuids,
                "release_to_applicant": release_to_applicant,
                "released_at": released_at,
                "can_release": can_release,
                "collects_reviewer_suggestions": collects_reviewer_suggestions,
                "allows_change_requests": allows_change_requests,
                "can_suggest_reviewers": can_suggest_reviewers,
                "ready_to_complete": ready_to_complete,
                "score_gate": score_gate,
                "decided_automatically": decided_automatically,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.step_checklist_status import StepChecklistStatus
        from ..models.step_run_condition import StepRunCondition
        from ..models.step_score_gate import StepScoreGate

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        step = d.pop("step")

        call_step_uuid = UUID(d.pop("call_step_uuid"))

        kind = CallStepKindEnum(d.pop("kind"))

        order = d.pop("order")

        stage = d.pop("stage")

        def _parse_run_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                run_uuid_type_0 = UUID(data)

                return run_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        run_uuid = _parse_run_uuid(d.pop("run_uuid"))

        phase = WorkflowPhaseEnum(d.pop("phase"))

        is_overdue = d.pop("is_overdue")

        run_condition = StepRunCondition.from_dict(d.pop("run_condition"))

        def _parse_skipped_reason(data: object) -> Union[None, SkippedReasonEnum]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                skipped_reason_type_0 = SkippedReasonEnum(data)

                return skipped_reason_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, SkippedReasonEnum], data)

        skipped_reason = _parse_skipped_reason(d.pop("skipped_reason"))

        def _parse_status_label(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        status_label = _parse_status_label(d.pop("status_label"))

        outcome_set = OutcomeSetEnum(d.pop("outcome_set"))

        allowed_outcomes = cast(list[str], d.pop("allowed_outcomes"))

        contributor_source = d.pop("contributor_source")

        def _parse_contributor_proposal_role_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                contributor_proposal_role_uuid_type_0 = UUID(data)

                return contributor_proposal_role_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        contributor_proposal_role_uuid = _parse_contributor_proposal_role_uuid(d.pop("contributor_proposal_role_uuid"))

        per_requested_offering = d.pop("per_requested_offering")

        round_scoped = d.pop("round_scoped")

        contributors_lead_only = d.pop("contributors_lead_only")

        delegable_to = d.pop("delegable_to")

        def _parse_awaiting_lead(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        awaiting_lead = _parse_awaiting_lead(d.pop("awaiting_lead"))

        def _parse_waiting_for(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        waiting_for = _parse_waiting_for(d.pop("waiting_for"))

        def _parse_completion_warning(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        completion_warning = _parse_completion_warning(d.pop("completion_warning"))

        on_negative = OnNegativeEnum(d.pop("on_negative"))

        contribution_outcomes = cast(list[str], d.pop("contribution_outcomes"))

        is_allocation_decision = d.pop("is_allocation_decision")

        step_name = d.pop("step_name")

        step_description = d.pop("step_description")

        def _parse_completer(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        completer = _parse_completer(d.pop("completer"))

        def _parse_responsible_role(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        responsible_role = _parse_responsible_role(d.pop("responsible_role"))

        def _parse_completer_proposal_role_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completer_proposal_role_uuid_type_0 = UUID(data)

                return completer_proposal_role_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        completer_proposal_role_uuid = _parse_completer_proposal_role_uuid(d.pop("completer_proposal_role_uuid"))

        def _parse_completer_proposal_role_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        completer_proposal_role_name = _parse_completer_proposal_role_name(d.pop("completer_proposal_role_name"))

        status = ProposalWorkflowStepInstanceStatusEnum(d.pop("status"))

        def _parse_outcome(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        outcome = _parse_outcome(d.pop("outcome"))

        outcome_reason = d.pop("outcome_reason")

        def _parse_rejection_reason(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        rejection_reason = _parse_rejection_reason(d.pop("rejection_reason"))

        def _parse_internal_notes(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        internal_notes = _parse_internal_notes(d.pop("internal_notes"))

        def _parse_started_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_at_type_0 = isoparse(data)

                return started_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        started_at = _parse_started_at(d.pop("started_at"))

        def _parse_completed_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = isoparse(data)

                return completed_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        completed_at = _parse_completed_at(d.pop("completed_at"))

        def _parse_completed_by(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_by_type_0 = UUID(data)

                return completed_by_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        completed_by = _parse_completed_by(d.pop("completed_by"))

        def _parse_deadline(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deadline_type_0 = isoparse(data)

                return deadline_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        deadline = _parse_deadline(d.pop("deadline"))

        applicant_visible = d.pop("applicant_visible")

        def _parse_duration_in_days(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        duration_in_days = _parse_duration_in_days(d.pop("duration_in_days"))

        is_required = d.pop("is_required")

        def _parse_checklist_status(data: object) -> Union["StepChecklistStatus", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                checklist_status_type_1 = StepChecklistStatus.from_dict(data)

                return checklist_status_type_1
            except:  # noqa: E722
                pass
            return cast(Union["StepChecklistStatus", None], data)

        checklist_status = _parse_checklist_status(d.pop("checklist_status"))

        input_step_uuids = []
        _input_step_uuids = d.pop("input_step_uuids")
        for input_step_uuids_item_data in _input_step_uuids:
            input_step_uuids_item = UUID(input_step_uuids_item_data)

            input_step_uuids.append(input_step_uuids_item)

        release_to_applicant = d.pop("release_to_applicant")

        def _parse_released_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                released_at_type_0 = isoparse(data)

                return released_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        released_at = _parse_released_at(d.pop("released_at"))

        can_release = d.pop("can_release")

        collects_reviewer_suggestions = d.pop("collects_reviewer_suggestions")

        allows_change_requests = d.pop("allows_change_requests")

        can_suggest_reviewers = d.pop("can_suggest_reviewers")

        ready_to_complete = d.pop("ready_to_complete")

        def _parse_score_gate(data: object) -> Union["StepScoreGate", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                score_gate_type_1 = StepScoreGate.from_dict(data)

                return score_gate_type_1
            except:  # noqa: E722
                pass
            return cast(Union["StepScoreGate", None], data)

        score_gate = _parse_score_gate(d.pop("score_gate"))

        decided_automatically = d.pop("decided_automatically")

        proposal_workflow_step_instance = cls(
            uuid=uuid,
            step=step,
            call_step_uuid=call_step_uuid,
            kind=kind,
            order=order,
            stage=stage,
            run_uuid=run_uuid,
            phase=phase,
            is_overdue=is_overdue,
            run_condition=run_condition,
            skipped_reason=skipped_reason,
            status_label=status_label,
            outcome_set=outcome_set,
            allowed_outcomes=allowed_outcomes,
            contributor_source=contributor_source,
            contributor_proposal_role_uuid=contributor_proposal_role_uuid,
            per_requested_offering=per_requested_offering,
            round_scoped=round_scoped,
            contributors_lead_only=contributors_lead_only,
            delegable_to=delegable_to,
            awaiting_lead=awaiting_lead,
            waiting_for=waiting_for,
            completion_warning=completion_warning,
            on_negative=on_negative,
            contribution_outcomes=contribution_outcomes,
            is_allocation_decision=is_allocation_decision,
            step_name=step_name,
            step_description=step_description,
            completer=completer,
            responsible_role=responsible_role,
            completer_proposal_role_uuid=completer_proposal_role_uuid,
            completer_proposal_role_name=completer_proposal_role_name,
            status=status,
            outcome=outcome,
            outcome_reason=outcome_reason,
            rejection_reason=rejection_reason,
            internal_notes=internal_notes,
            started_at=started_at,
            completed_at=completed_at,
            completed_by=completed_by,
            deadline=deadline,
            applicant_visible=applicant_visible,
            duration_in_days=duration_in_days,
            is_required=is_required,
            checklist_status=checklist_status,
            input_step_uuids=input_step_uuids,
            release_to_applicant=release_to_applicant,
            released_at=released_at,
            can_release=can_release,
            collects_reviewer_suggestions=collects_reviewer_suggestions,
            allows_change_requests=allows_change_requests,
            can_suggest_reviewers=can_suggest_reviewers,
            ready_to_complete=ready_to_complete,
            score_gate=score_gate,
            decided_automatically=decided_automatically,
        )

        proposal_workflow_step_instance.additional_properties = d
        return proposal_workflow_step_instance

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
