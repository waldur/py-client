from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.workflow_description_planned_step import WorkflowDescriptionPlannedStep
    from ..models.workflow_description_post_award_schedule import WorkflowDescriptionPostAwardSchedule
    from ..models.workflow_description_stage import WorkflowDescriptionStage


T = TypeVar("T", bound="WorkflowDescriptionSchedule")


@_attrs_define
class WorkflowDescriptionSchedule:
    """
    Attributes:
        stages (list['WorkflowDescriptionStage']):
        steps (list['WorkflowDescriptionPlannedStep']):
        total_days (int):
        critical_path (list[str]):
        steps_without_duration (list[str]):
        post_award (list['WorkflowDescriptionPostAwardSchedule']): The extension and the closing, each planned on its
            own after the award; the evaluation's schedule leaves them out.
    """

    stages: list["WorkflowDescriptionStage"]
    steps: list["WorkflowDescriptionPlannedStep"]
    total_days: int
    critical_path: list[str]
    steps_without_duration: list[str]
    post_award: list["WorkflowDescriptionPostAwardSchedule"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stages = []
        for stages_item_data in self.stages:
            stages_item = stages_item_data.to_dict()
            stages.append(stages_item)

        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()
            steps.append(steps_item)

        total_days = self.total_days

        critical_path = self.critical_path

        steps_without_duration = self.steps_without_duration

        post_award = []
        for post_award_item_data in self.post_award:
            post_award_item = post_award_item_data.to_dict()
            post_award.append(post_award_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stages": stages,
                "steps": steps,
                "total_days": total_days,
                "critical_path": critical_path,
                "steps_without_duration": steps_without_duration,
                "post_award": post_award,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_description_planned_step import WorkflowDescriptionPlannedStep
        from ..models.workflow_description_post_award_schedule import WorkflowDescriptionPostAwardSchedule
        from ..models.workflow_description_stage import WorkflowDescriptionStage

        d = dict(src_dict)
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

        critical_path = cast(list[str], d.pop("critical_path"))

        steps_without_duration = cast(list[str], d.pop("steps_without_duration"))

        post_award = []
        _post_award = d.pop("post_award")
        for post_award_item_data in _post_award:
            post_award_item = WorkflowDescriptionPostAwardSchedule.from_dict(post_award_item_data)

            post_award.append(post_award_item)

        workflow_description_schedule = cls(
            stages=stages,
            steps=steps,
            total_days=total_days,
            critical_path=critical_path,
            steps_without_duration=steps_without_duration,
            post_award=post_award,
        )

        workflow_description_schedule.additional_properties = d
        return workflow_description_schedule

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
