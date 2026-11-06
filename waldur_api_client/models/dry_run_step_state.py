from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workflow_phase_enum import WorkflowPhaseEnum

if TYPE_CHECKING:
    from ..models.dry_run_contribution_state import DryRunContributionState
    from ..models.dry_run_step_state_condition_type_0 import DryRunStepStateConditionType0
    from ..models.dry_run_step_state_extra import DryRunStepStateExtra


T = TypeVar("T", bound="DryRunStepState")


@_attrs_define
class DryRunStepState:
    """
    Attributes:
        key (str):
        name (str):
        order (int):
        stage (int):
        phase (WorkflowPhaseEnum):
        run (Union[None, int]): Which extension request or final report, counted from 1.
        round_scoped (bool):
        status (str):
        outcome (Union[None, str]):
        skipped_reason (Union[None, str]):
        condition (Union['DryRunStepStateConditionType0', None]):
        started_day (Union[None, int]):
        deadline_day (Union[None, int]):
        ended_day (Union[None, int]):
        is_allocation_decision (bool):
        decides_automatically (bool):
        automatic (bool):
        released (bool):
        changes_requested (bool):
        outcomes (list[str]):
        contribution_outcomes (list[str]):
        contributions (list['DryRunContributionState']):
        extra (DryRunStepStateExtra):
    """

    key: str
    name: str
    order: int
    stage: int
    phase: WorkflowPhaseEnum
    run: Union[None, int]
    round_scoped: bool
    status: str
    outcome: Union[None, str]
    skipped_reason: Union[None, str]
    condition: Union["DryRunStepStateConditionType0", None]
    started_day: Union[None, int]
    deadline_day: Union[None, int]
    ended_day: Union[None, int]
    is_allocation_decision: bool
    decides_automatically: bool
    automatic: bool
    released: bool
    changes_requested: bool
    outcomes: list[str]
    contribution_outcomes: list[str]
    contributions: list["DryRunContributionState"]
    extra: "DryRunStepStateExtra"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.dry_run_step_state_condition_type_0 import DryRunStepStateConditionType0

        key = self.key

        name = self.name

        order = self.order

        stage = self.stage

        phase = self.phase.value

        run: Union[None, int]
        run = self.run

        round_scoped = self.round_scoped

        status = self.status

        outcome: Union[None, str]
        outcome = self.outcome

        skipped_reason: Union[None, str]
        skipped_reason = self.skipped_reason

        condition: Union[None, dict[str, Any]]
        if isinstance(self.condition, DryRunStepStateConditionType0):
            condition = self.condition.to_dict()
        else:
            condition = self.condition

        started_day: Union[None, int]
        started_day = self.started_day

        deadline_day: Union[None, int]
        deadline_day = self.deadline_day

        ended_day: Union[None, int]
        ended_day = self.ended_day

        is_allocation_decision = self.is_allocation_decision

        decides_automatically = self.decides_automatically

        automatic = self.automatic

        released = self.released

        changes_requested = self.changes_requested

        outcomes = self.outcomes

        contribution_outcomes = self.contribution_outcomes

        contributions = []
        for contributions_item_data in self.contributions:
            contributions_item = contributions_item_data.to_dict()
            contributions.append(contributions_item)

        extra = self.extra.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "name": name,
                "order": order,
                "stage": stage,
                "phase": phase,
                "run": run,
                "round_scoped": round_scoped,
                "status": status,
                "outcome": outcome,
                "skipped_reason": skipped_reason,
                "condition": condition,
                "started_day": started_day,
                "deadline_day": deadline_day,
                "ended_day": ended_day,
                "is_allocation_decision": is_allocation_decision,
                "decides_automatically": decides_automatically,
                "automatic": automatic,
                "released": released,
                "changes_requested": changes_requested,
                "outcomes": outcomes,
                "contribution_outcomes": contribution_outcomes,
                "contributions": contributions,
                "extra": extra,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dry_run_contribution_state import DryRunContributionState
        from ..models.dry_run_step_state_condition_type_0 import DryRunStepStateConditionType0
        from ..models.dry_run_step_state_extra import DryRunStepStateExtra

        d = dict(src_dict)
        key = d.pop("key")

        name = d.pop("name")

        order = d.pop("order")

        stage = d.pop("stage")

        phase = WorkflowPhaseEnum(d.pop("phase"))

        def _parse_run(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        run = _parse_run(d.pop("run"))

        round_scoped = d.pop("round_scoped")

        status = d.pop("status")

        def _parse_outcome(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        outcome = _parse_outcome(d.pop("outcome"))

        def _parse_skipped_reason(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        skipped_reason = _parse_skipped_reason(d.pop("skipped_reason"))

        def _parse_condition(data: object) -> Union["DryRunStepStateConditionType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                condition_type_0 = DryRunStepStateConditionType0.from_dict(data)

                return condition_type_0
            except:  # noqa: E722
                pass
            return cast(Union["DryRunStepStateConditionType0", None], data)

        condition = _parse_condition(d.pop("condition"))

        def _parse_started_day(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        started_day = _parse_started_day(d.pop("started_day"))

        def _parse_deadline_day(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        deadline_day = _parse_deadline_day(d.pop("deadline_day"))

        def _parse_ended_day(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        ended_day = _parse_ended_day(d.pop("ended_day"))

        is_allocation_decision = d.pop("is_allocation_decision")

        decides_automatically = d.pop("decides_automatically")

        automatic = d.pop("automatic")

        released = d.pop("released")

        changes_requested = d.pop("changes_requested")

        outcomes = cast(list[str], d.pop("outcomes"))

        contribution_outcomes = cast(list[str], d.pop("contribution_outcomes"))

        contributions = []
        _contributions = d.pop("contributions")
        for contributions_item_data in _contributions:
            contributions_item = DryRunContributionState.from_dict(contributions_item_data)

            contributions.append(contributions_item)

        extra = DryRunStepStateExtra.from_dict(d.pop("extra"))

        dry_run_step_state = cls(
            key=key,
            name=name,
            order=order,
            stage=stage,
            phase=phase,
            run=run,
            round_scoped=round_scoped,
            status=status,
            outcome=outcome,
            skipped_reason=skipped_reason,
            condition=condition,
            started_day=started_day,
            deadline_day=deadline_day,
            ended_day=ended_day,
            is_allocation_decision=is_allocation_decision,
            decides_automatically=decides_automatically,
            automatic=automatic,
            released=released,
            changes_requested=changes_requested,
            outcomes=outcomes,
            contribution_outcomes=contribution_outcomes,
            contributions=contributions,
            extra=extra,
        )

        dry_run_step_state.additional_properties = d
        return dry_run_step_state

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
