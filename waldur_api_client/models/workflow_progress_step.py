from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workflow_phase_enum import WorkflowPhaseEnum

if TYPE_CHECKING:
    from ..models.workflow_progress_outcome import WorkflowProgressOutcome
    from ..models.workflow_progress_round_step import WorkflowProgressRoundStep


T = TypeVar("T", bound="WorkflowProgressStep")


@_attrs_define
class WorkflowProgressStep:
    """
    Attributes:
        key (str):
        name (str):
        enabled (bool):
        phase (WorkflowPhaseEnum):
        round_scoped (bool):
        rounds (list['WorkflowProgressRoundStep']): Per round, for a step run once per round.
        planned_days (Union[None, int]):
        total (int):
        pending (int):
        waiting (int): Proposals at the step now.
        overdue (int): Proposals at the step now and past its deadline.
        completed (int):
        completed_late (int): Completed after the step's deadline.
        skipped (int):
        expired (int):
        withdrawn (int):
        median_days (Union[None, float]): Median days from start to completion.
        p90_days (Union[None, float]): 90th percentile of days from start to completion.
        outcomes (list['WorkflowProgressOutcome']):
    """

    key: str
    name: str
    enabled: bool
    phase: WorkflowPhaseEnum
    round_scoped: bool
    rounds: list["WorkflowProgressRoundStep"]
    planned_days: Union[None, int]
    total: int
    pending: int
    waiting: int
    overdue: int
    completed: int
    completed_late: int
    skipped: int
    expired: int
    withdrawn: int
    median_days: Union[None, float]
    p90_days: Union[None, float]
    outcomes: list["WorkflowProgressOutcome"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        name = self.name

        enabled = self.enabled

        phase = self.phase.value

        round_scoped = self.round_scoped

        rounds = []
        for rounds_item_data in self.rounds:
            rounds_item = rounds_item_data.to_dict()
            rounds.append(rounds_item)

        planned_days: Union[None, int]
        planned_days = self.planned_days

        total = self.total

        pending = self.pending

        waiting = self.waiting

        overdue = self.overdue

        completed = self.completed

        completed_late = self.completed_late

        skipped = self.skipped

        expired = self.expired

        withdrawn = self.withdrawn

        median_days: Union[None, float]
        median_days = self.median_days

        p90_days: Union[None, float]
        p90_days = self.p90_days

        outcomes = []
        for outcomes_item_data in self.outcomes:
            outcomes_item = outcomes_item_data.to_dict()
            outcomes.append(outcomes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "name": name,
                "enabled": enabled,
                "phase": phase,
                "round_scoped": round_scoped,
                "rounds": rounds,
                "planned_days": planned_days,
                "total": total,
                "pending": pending,
                "waiting": waiting,
                "overdue": overdue,
                "completed": completed,
                "completed_late": completed_late,
                "skipped": skipped,
                "expired": expired,
                "withdrawn": withdrawn,
                "median_days": median_days,
                "p90_days": p90_days,
                "outcomes": outcomes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_progress_outcome import WorkflowProgressOutcome
        from ..models.workflow_progress_round_step import WorkflowProgressRoundStep

        d = dict(src_dict)
        key = d.pop("key")

        name = d.pop("name")

        enabled = d.pop("enabled")

        phase = WorkflowPhaseEnum(d.pop("phase"))

        round_scoped = d.pop("round_scoped")

        rounds = []
        _rounds = d.pop("rounds")
        for rounds_item_data in _rounds:
            rounds_item = WorkflowProgressRoundStep.from_dict(rounds_item_data)

            rounds.append(rounds_item)

        def _parse_planned_days(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        planned_days = _parse_planned_days(d.pop("planned_days"))

        total = d.pop("total")

        pending = d.pop("pending")

        waiting = d.pop("waiting")

        overdue = d.pop("overdue")

        completed = d.pop("completed")

        completed_late = d.pop("completed_late")

        skipped = d.pop("skipped")

        expired = d.pop("expired")

        withdrawn = d.pop("withdrawn")

        def _parse_median_days(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        median_days = _parse_median_days(d.pop("median_days"))

        def _parse_p90_days(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        p90_days = _parse_p90_days(d.pop("p90_days"))

        outcomes = []
        _outcomes = d.pop("outcomes")
        for outcomes_item_data in _outcomes:
            outcomes_item = WorkflowProgressOutcome.from_dict(outcomes_item_data)

            outcomes.append(outcomes_item)

        workflow_progress_step = cls(
            key=key,
            name=name,
            enabled=enabled,
            phase=phase,
            round_scoped=round_scoped,
            rounds=rounds,
            planned_days=planned_days,
            total=total,
            pending=pending,
            waiting=waiting,
            overdue=overdue,
            completed=completed,
            completed_late=completed_late,
            skipped=skipped,
            expired=expired,
            withdrawn=withdrawn,
            median_days=median_days,
            p90_days=p90_days,
            outcomes=outcomes,
        )

        workflow_progress_step.additional_properties = d
        return workflow_progress_step

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
