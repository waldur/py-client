from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workflow_phase_enum import WorkflowPhaseEnum

if TYPE_CHECKING:
    from ..models.workflow_description_planned_step import WorkflowDescriptionPlannedStep
    from ..models.workflow_description_stage import WorkflowDescriptionStage


T = TypeVar("T", bound="WorkflowDescriptionPostAwardSchedule")


@_attrs_define
class WorkflowDescriptionPostAwardSchedule:
    """
    Attributes:
        phase (WorkflowPhaseEnum):
        project_end_offset_days (Union[None, int]):
        stages (list['WorkflowDescriptionStage']):
        steps (list['WorkflowDescriptionPlannedStep']): Planned in days from the start of the phase's run.
        total_days (int):
        steps_without_duration (list[str]):
    """

    phase: WorkflowPhaseEnum
    project_end_offset_days: Union[None, int]
    stages: list["WorkflowDescriptionStage"]
    steps: list["WorkflowDescriptionPlannedStep"]
    total_days: int
    steps_without_duration: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        phase = self.phase.value

        project_end_offset_days: Union[None, int]
        project_end_offset_days = self.project_end_offset_days

        stages = []
        for stages_item_data in self.stages:
            stages_item = stages_item_data.to_dict()
            stages.append(stages_item)

        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()
            steps.append(steps_item)

        total_days = self.total_days

        steps_without_duration = self.steps_without_duration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "phase": phase,
                "project_end_offset_days": project_end_offset_days,
                "stages": stages,
                "steps": steps,
                "total_days": total_days,
                "steps_without_duration": steps_without_duration,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_description_planned_step import WorkflowDescriptionPlannedStep
        from ..models.workflow_description_stage import WorkflowDescriptionStage

        d = dict(src_dict)
        phase = WorkflowPhaseEnum(d.pop("phase"))

        def _parse_project_end_offset_days(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        project_end_offset_days = _parse_project_end_offset_days(d.pop("project_end_offset_days"))

        stages = []
        _stages = d.pop("stages")
        for stages_item_data in _stages:
            stages_item = WorkflowDescriptionStage.from_dict(stages_item_data)

            stages.append(stages_item)

        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = WorkflowDescriptionPlannedStep.from_dict(steps_item_data)

            steps.append(steps_item)

        total_days = d.pop("total_days")

        steps_without_duration = cast(list[str], d.pop("steps_without_duration"))

        workflow_description_post_award_schedule = cls(
            phase=phase,
            project_end_offset_days=project_end_offset_days,
            stages=stages,
            steps=steps,
            total_days=total_days,
            steps_without_duration=steps_without_duration,
        )

        workflow_description_post_award_schedule.additional_properties = d
        return workflow_description_post_award_schedule

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
