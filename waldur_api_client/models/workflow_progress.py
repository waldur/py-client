import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.workflow_progress_round import WorkflowProgressRound
    from ..models.workflow_progress_step import WorkflowProgressStep


T = TypeVar("T", bound="WorkflowProgress")


@_attrs_define
class WorkflowProgress:
    """
    Attributes:
        round_ (Union[None, str]): The round counted; null for every round.
        rounds (list['WorkflowProgressRound']):
        generated_at (datetime.datetime):
        proposals (int): Proposals that have entered the workflow.
        steps (list['WorkflowProgressStep']):
    """

    round_: Union[None, str]
    rounds: list["WorkflowProgressRound"]
    generated_at: datetime.datetime
    proposals: int
    steps: list["WorkflowProgressStep"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        round_: Union[None, str]
        round_ = self.round_

        rounds = []
        for rounds_item_data in self.rounds:
            rounds_item = rounds_item_data.to_dict()
            rounds.append(rounds_item)

        generated_at = self.generated_at.isoformat()

        proposals = self.proposals

        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()
            steps.append(steps_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "round": round_,
                "rounds": rounds,
                "generated_at": generated_at,
                "proposals": proposals,
                "steps": steps,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_progress_round import WorkflowProgressRound
        from ..models.workflow_progress_step import WorkflowProgressStep

        d = dict(src_dict)

        def _parse_round_(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        round_ = _parse_round_(d.pop("round"))

        rounds = []
        _rounds = d.pop("rounds")
        for rounds_item_data in _rounds:
            rounds_item = WorkflowProgressRound.from_dict(rounds_item_data)

            rounds.append(rounds_item)

        generated_at = isoparse(d.pop("generated_at"))

        proposals = d.pop("proposals")

        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = WorkflowProgressStep.from_dict(steps_item_data)

            steps.append(steps_item)

        workflow_progress = cls(
            round_=round_,
            rounds=rounds,
            generated_at=generated_at,
            proposals=proposals,
            steps=steps,
        )

        workflow_progress.additional_properties = d
        return workflow_progress

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
