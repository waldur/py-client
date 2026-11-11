from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.automatic_decision_guard_enum import AutomaticDecisionGuardEnum
from ..models.workflow_phase_enum import WorkflowPhaseEnum

if TYPE_CHECKING:
    from ..models.step_status_labels import StepStatusLabels
    from ..models.workflow_description_applicant import WorkflowDescriptionApplicant
    from ..models.workflow_description_checklist import WorkflowDescriptionChecklist
    from ..models.workflow_description_coi_declaration import WorkflowDescriptionCoiDeclaration
    from ..models.workflow_description_contributors import WorkflowDescriptionContributors
    from ..models.workflow_description_delegation import WorkflowDescriptionDelegation
    from ..models.workflow_description_outcome import WorkflowDescriptionOutcome
    from ..models.workflow_description_role_cell import WorkflowDescriptionRoleCell
    from ..models.workflow_description_rule import WorkflowDescriptionRule
    from ..models.workflow_description_run_condition import WorkflowDescriptionRunCondition
    from ..models.workflow_description_step_extra import WorkflowDescriptionStepExtra


T = TypeVar("T", bound="WorkflowDescriptionStep")


@_attrs_define
class WorkflowDescriptionStep:
    """
    Attributes:
        key (str):
        name (str):
        description (str):
        kind (str):
        order (Union[None, int]):
        stage (int):
        parallel_with_previous (bool):
        enabled (bool):
        phase (WorkflowPhaseEnum):
        project_end_offset_days (Union[None, int]): On the first step after the award: days before the project's end
            date that time it.
        outcome_set (Union[None, str]):
        outcomes (list['WorkflowDescriptionOutcome']):
        on_negative (Union[None, str]):
        transition_mode (Union[None, str]):
        duration_in_days (Union[None, int]):
        run_condition (Union['WorkflowDescriptionRunCondition', None]):
        input_steps (list[str]):
        is_allocation_decision (bool):
        decides_automatically (bool):
        automatic_decision_guard (Union[AutomaticDecisionGuardEnum, None]): What stops an unsuitable proposal before the
            automatic decision awards it; null unless the step decides automatically.
        allocation_time (Union[None, str]):
        include_award_response (bool):
        allows_change_requests (bool):
        allows_conditional_acceptance (bool):
        completer (Union[None, str]):
        completer_proposal_role (Union[None, str]):
        completion_lead_only (bool):
        assigns_roles (list[str]):
        contributors (WorkflowDescriptionContributors):
        delegable_to (Union['WorkflowDescriptionDelegation', None]):
        blind_review (bool):
        requires_coi_confirmation (bool):
        coi_declaration (Union['WorkflowDescriptionCoiDeclaration', None]): The conflict-of-interest declaration the
            step's evaluators confirm; null on a step asking for none.
        release_to_applicant (bool):
        collects_reviewer_suggestions (bool):
        min_score_threshold (Union[None, str]):
        checklist (Union['WorkflowDescriptionChecklist', None]):
        criteria (int): How many criteria the step scores.
        status_labels (StepStatusLabels):
        applicant (WorkflowDescriptionApplicant):
        roles (list['WorkflowDescriptionRoleCell']):
        notifications (list['WorkflowDescriptionRule']):
        extra (WorkflowDescriptionStepExtra): Fields of features described by extensions.
    """

    key: str
    name: str
    description: str
    kind: str
    order: Union[None, int]
    stage: int
    parallel_with_previous: bool
    enabled: bool
    phase: WorkflowPhaseEnum
    project_end_offset_days: Union[None, int]
    outcome_set: Union[None, str]
    outcomes: list["WorkflowDescriptionOutcome"]
    on_negative: Union[None, str]
    transition_mode: Union[None, str]
    duration_in_days: Union[None, int]
    run_condition: Union["WorkflowDescriptionRunCondition", None]
    input_steps: list[str]
    is_allocation_decision: bool
    decides_automatically: bool
    automatic_decision_guard: Union[AutomaticDecisionGuardEnum, None]
    allocation_time: Union[None, str]
    include_award_response: bool
    allows_change_requests: bool
    allows_conditional_acceptance: bool
    completer: Union[None, str]
    completer_proposal_role: Union[None, str]
    completion_lead_only: bool
    assigns_roles: list[str]
    contributors: "WorkflowDescriptionContributors"
    delegable_to: Union["WorkflowDescriptionDelegation", None]
    blind_review: bool
    requires_coi_confirmation: bool
    coi_declaration: Union["WorkflowDescriptionCoiDeclaration", None]
    release_to_applicant: bool
    collects_reviewer_suggestions: bool
    min_score_threshold: Union[None, str]
    checklist: Union["WorkflowDescriptionChecklist", None]
    criteria: int
    status_labels: "StepStatusLabels"
    applicant: "WorkflowDescriptionApplicant"
    roles: list["WorkflowDescriptionRoleCell"]
    notifications: list["WorkflowDescriptionRule"]
    extra: "WorkflowDescriptionStepExtra"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_description_checklist import WorkflowDescriptionChecklist
        from ..models.workflow_description_coi_declaration import WorkflowDescriptionCoiDeclaration
        from ..models.workflow_description_delegation import WorkflowDescriptionDelegation
        from ..models.workflow_description_run_condition import WorkflowDescriptionRunCondition

        key = self.key

        name = self.name

        description = self.description

        kind = self.kind

        order: Union[None, int]
        order = self.order

        stage = self.stage

        parallel_with_previous = self.parallel_with_previous

        enabled = self.enabled

        phase = self.phase.value

        project_end_offset_days: Union[None, int]
        project_end_offset_days = self.project_end_offset_days

        outcome_set: Union[None, str]
        outcome_set = self.outcome_set

        outcomes = []
        for outcomes_item_data in self.outcomes:
            outcomes_item = outcomes_item_data.to_dict()
            outcomes.append(outcomes_item)

        on_negative: Union[None, str]
        on_negative = self.on_negative

        transition_mode: Union[None, str]
        transition_mode = self.transition_mode

        duration_in_days: Union[None, int]
        duration_in_days = self.duration_in_days

        run_condition: Union[None, dict[str, Any]]
        if isinstance(self.run_condition, WorkflowDescriptionRunCondition):
            run_condition = self.run_condition.to_dict()
        else:
            run_condition = self.run_condition

        input_steps = self.input_steps

        is_allocation_decision = self.is_allocation_decision

        decides_automatically = self.decides_automatically

        automatic_decision_guard: Union[None, str]
        if isinstance(self.automatic_decision_guard, AutomaticDecisionGuardEnum):
            automatic_decision_guard = self.automatic_decision_guard.value
        else:
            automatic_decision_guard = self.automatic_decision_guard

        allocation_time: Union[None, str]
        allocation_time = self.allocation_time

        include_award_response = self.include_award_response

        allows_change_requests = self.allows_change_requests

        allows_conditional_acceptance = self.allows_conditional_acceptance

        completer: Union[None, str]
        completer = self.completer

        completer_proposal_role: Union[None, str]
        completer_proposal_role = self.completer_proposal_role

        completion_lead_only = self.completion_lead_only

        assigns_roles = self.assigns_roles

        contributors = self.contributors.to_dict()

        delegable_to: Union[None, dict[str, Any]]
        if isinstance(self.delegable_to, WorkflowDescriptionDelegation):
            delegable_to = self.delegable_to.to_dict()
        else:
            delegable_to = self.delegable_to

        blind_review = self.blind_review

        requires_coi_confirmation = self.requires_coi_confirmation

        coi_declaration: Union[None, dict[str, Any]]
        if isinstance(self.coi_declaration, WorkflowDescriptionCoiDeclaration):
            coi_declaration = self.coi_declaration.to_dict()
        else:
            coi_declaration = self.coi_declaration

        release_to_applicant = self.release_to_applicant

        collects_reviewer_suggestions = self.collects_reviewer_suggestions

        min_score_threshold: Union[None, str]
        min_score_threshold = self.min_score_threshold

        checklist: Union[None, dict[str, Any]]
        if isinstance(self.checklist, WorkflowDescriptionChecklist):
            checklist = self.checklist.to_dict()
        else:
            checklist = self.checklist

        criteria = self.criteria

        status_labels = self.status_labels.to_dict()

        applicant = self.applicant.to_dict()

        roles = []
        for roles_item_data in self.roles:
            roles_item = roles_item_data.to_dict()
            roles.append(roles_item)

        notifications = []
        for notifications_item_data in self.notifications:
            notifications_item = notifications_item_data.to_dict()
            notifications.append(notifications_item)

        extra = self.extra.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "name": name,
                "description": description,
                "kind": kind,
                "order": order,
                "stage": stage,
                "parallel_with_previous": parallel_with_previous,
                "enabled": enabled,
                "phase": phase,
                "project_end_offset_days": project_end_offset_days,
                "outcome_set": outcome_set,
                "outcomes": outcomes,
                "on_negative": on_negative,
                "transition_mode": transition_mode,
                "duration_in_days": duration_in_days,
                "run_condition": run_condition,
                "input_steps": input_steps,
                "is_allocation_decision": is_allocation_decision,
                "decides_automatically": decides_automatically,
                "automatic_decision_guard": automatic_decision_guard,
                "allocation_time": allocation_time,
                "include_award_response": include_award_response,
                "allows_change_requests": allows_change_requests,
                "allows_conditional_acceptance": allows_conditional_acceptance,
                "completer": completer,
                "completer_proposal_role": completer_proposal_role,
                "completion_lead_only": completion_lead_only,
                "assigns_roles": assigns_roles,
                "contributors": contributors,
                "delegable_to": delegable_to,
                "blind_review": blind_review,
                "requires_coi_confirmation": requires_coi_confirmation,
                "coi_declaration": coi_declaration,
                "release_to_applicant": release_to_applicant,
                "collects_reviewer_suggestions": collects_reviewer_suggestions,
                "min_score_threshold": min_score_threshold,
                "checklist": checklist,
                "criteria": criteria,
                "status_labels": status_labels,
                "applicant": applicant,
                "roles": roles,
                "notifications": notifications,
                "extra": extra,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.step_status_labels import StepStatusLabels
        from ..models.workflow_description_applicant import WorkflowDescriptionApplicant
        from ..models.workflow_description_checklist import WorkflowDescriptionChecklist
        from ..models.workflow_description_coi_declaration import WorkflowDescriptionCoiDeclaration
        from ..models.workflow_description_contributors import WorkflowDescriptionContributors
        from ..models.workflow_description_delegation import WorkflowDescriptionDelegation
        from ..models.workflow_description_outcome import WorkflowDescriptionOutcome
        from ..models.workflow_description_role_cell import WorkflowDescriptionRoleCell
        from ..models.workflow_description_rule import WorkflowDescriptionRule
        from ..models.workflow_description_run_condition import WorkflowDescriptionRunCondition
        from ..models.workflow_description_step_extra import WorkflowDescriptionStepExtra

        d = dict(src_dict)
        key = d.pop("key")

        name = d.pop("name")

        description = d.pop("description")

        kind = d.pop("kind")

        def _parse_order(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        order = _parse_order(d.pop("order"))

        stage = d.pop("stage")

        parallel_with_previous = d.pop("parallel_with_previous")

        enabled = d.pop("enabled")

        phase = WorkflowPhaseEnum(d.pop("phase"))

        def _parse_project_end_offset_days(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        project_end_offset_days = _parse_project_end_offset_days(d.pop("project_end_offset_days"))

        def _parse_outcome_set(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        outcome_set = _parse_outcome_set(d.pop("outcome_set"))

        outcomes = []
        _outcomes = d.pop("outcomes")
        for outcomes_item_data in _outcomes:
            outcomes_item = WorkflowDescriptionOutcome.from_dict(outcomes_item_data)

            outcomes.append(outcomes_item)

        def _parse_on_negative(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        on_negative = _parse_on_negative(d.pop("on_negative"))

        def _parse_transition_mode(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        transition_mode = _parse_transition_mode(d.pop("transition_mode"))

        def _parse_duration_in_days(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        duration_in_days = _parse_duration_in_days(d.pop("duration_in_days"))

        def _parse_run_condition(data: object) -> Union["WorkflowDescriptionRunCondition", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                run_condition_type_1 = WorkflowDescriptionRunCondition.from_dict(data)

                return run_condition_type_1
            except:  # noqa: E722
                pass
            return cast(Union["WorkflowDescriptionRunCondition", None], data)

        run_condition = _parse_run_condition(d.pop("run_condition"))

        input_steps = cast(list[str], d.pop("input_steps"))

        is_allocation_decision = d.pop("is_allocation_decision")

        decides_automatically = d.pop("decides_automatically")

        def _parse_automatic_decision_guard(data: object) -> Union[AutomaticDecisionGuardEnum, None]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                automatic_decision_guard_type_0 = AutomaticDecisionGuardEnum(data)

                return automatic_decision_guard_type_0
            except:  # noqa: E722
                pass
            return cast(Union[AutomaticDecisionGuardEnum, None], data)

        automatic_decision_guard = _parse_automatic_decision_guard(d.pop("automatic_decision_guard"))

        def _parse_allocation_time(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        allocation_time = _parse_allocation_time(d.pop("allocation_time"))

        include_award_response = d.pop("include_award_response")

        allows_change_requests = d.pop("allows_change_requests")

        allows_conditional_acceptance = d.pop("allows_conditional_acceptance")

        def _parse_completer(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        completer = _parse_completer(d.pop("completer"))

        def _parse_completer_proposal_role(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        completer_proposal_role = _parse_completer_proposal_role(d.pop("completer_proposal_role"))

        completion_lead_only = d.pop("completion_lead_only")

        assigns_roles = cast(list[str], d.pop("assigns_roles"))

        contributors = WorkflowDescriptionContributors.from_dict(d.pop("contributors"))

        def _parse_delegable_to(data: object) -> Union["WorkflowDescriptionDelegation", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                delegable_to_type_1 = WorkflowDescriptionDelegation.from_dict(data)

                return delegable_to_type_1
            except:  # noqa: E722
                pass
            return cast(Union["WorkflowDescriptionDelegation", None], data)

        delegable_to = _parse_delegable_to(d.pop("delegable_to"))

        blind_review = d.pop("blind_review")

        requires_coi_confirmation = d.pop("requires_coi_confirmation")

        def _parse_coi_declaration(data: object) -> Union["WorkflowDescriptionCoiDeclaration", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                coi_declaration_type_1 = WorkflowDescriptionCoiDeclaration.from_dict(data)

                return coi_declaration_type_1
            except:  # noqa: E722
                pass
            return cast(Union["WorkflowDescriptionCoiDeclaration", None], data)

        coi_declaration = _parse_coi_declaration(d.pop("coi_declaration"))

        release_to_applicant = d.pop("release_to_applicant")

        collects_reviewer_suggestions = d.pop("collects_reviewer_suggestions")

        def _parse_min_score_threshold(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        min_score_threshold = _parse_min_score_threshold(d.pop("min_score_threshold"))

        def _parse_checklist(data: object) -> Union["WorkflowDescriptionChecklist", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                checklist_type_1 = WorkflowDescriptionChecklist.from_dict(data)

                return checklist_type_1
            except:  # noqa: E722
                pass
            return cast(Union["WorkflowDescriptionChecklist", None], data)

        checklist = _parse_checklist(d.pop("checklist"))

        criteria = d.pop("criteria")

        status_labels = StepStatusLabels.from_dict(d.pop("status_labels"))

        applicant = WorkflowDescriptionApplicant.from_dict(d.pop("applicant"))

        roles = []
        _roles = d.pop("roles")
        for roles_item_data in _roles:
            roles_item = WorkflowDescriptionRoleCell.from_dict(roles_item_data)

            roles.append(roles_item)

        notifications = []
        _notifications = d.pop("notifications")
        for notifications_item_data in _notifications:
            notifications_item = WorkflowDescriptionRule.from_dict(notifications_item_data)

            notifications.append(notifications_item)

        extra = WorkflowDescriptionStepExtra.from_dict(d.pop("extra"))

        workflow_description_step = cls(
            key=key,
            name=name,
            description=description,
            kind=kind,
            order=order,
            stage=stage,
            parallel_with_previous=parallel_with_previous,
            enabled=enabled,
            phase=phase,
            project_end_offset_days=project_end_offset_days,
            outcome_set=outcome_set,
            outcomes=outcomes,
            on_negative=on_negative,
            transition_mode=transition_mode,
            duration_in_days=duration_in_days,
            run_condition=run_condition,
            input_steps=input_steps,
            is_allocation_decision=is_allocation_decision,
            decides_automatically=decides_automatically,
            automatic_decision_guard=automatic_decision_guard,
            allocation_time=allocation_time,
            include_award_response=include_award_response,
            allows_change_requests=allows_change_requests,
            allows_conditional_acceptance=allows_conditional_acceptance,
            completer=completer,
            completer_proposal_role=completer_proposal_role,
            completion_lead_only=completion_lead_only,
            assigns_roles=assigns_roles,
            contributors=contributors,
            delegable_to=delegable_to,
            blind_review=blind_review,
            requires_coi_confirmation=requires_coi_confirmation,
            coi_declaration=coi_declaration,
            release_to_applicant=release_to_applicant,
            collects_reviewer_suggestions=collects_reviewer_suggestions,
            min_score_threshold=min_score_threshold,
            checklist=checklist,
            criteria=criteria,
            status_labels=status_labels,
            applicant=applicant,
            roles=roles,
            notifications=notifications,
            extra=extra,
        )

        workflow_description_step.additional_properties = d
        return workflow_description_step

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
