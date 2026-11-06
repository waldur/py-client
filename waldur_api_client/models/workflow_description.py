from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.workflow_description_actor import WorkflowDescriptionActor
    from ..models.workflow_description_call import WorkflowDescriptionCall
    from ..models.workflow_description_issues_structural_item import WorkflowDescriptionIssuesStructuralItem
    from ..models.workflow_description_notifications import WorkflowDescriptionNotifications
    from ..models.workflow_description_schedule import WorkflowDescriptionSchedule
    from ..models.workflow_description_step import WorkflowDescriptionStep


T = TypeVar("T", bound="WorkflowDescription")


@_attrs_define
class WorkflowDescription:
    """
    Attributes:
        schema (int):
        call (WorkflowDescriptionCall):
        actors (list['WorkflowDescriptionActor']):
        steps (list['WorkflowDescriptionStep']):
        notifications (WorkflowDescriptionNotifications):
        schedule (WorkflowDescriptionSchedule):
        issues_structural (list['WorkflowDescriptionIssuesStructuralItem']):
    """

    schema: int
    call: "WorkflowDescriptionCall"
    actors: list["WorkflowDescriptionActor"]
    steps: list["WorkflowDescriptionStep"]
    notifications: "WorkflowDescriptionNotifications"
    schedule: "WorkflowDescriptionSchedule"
    issues_structural: list["WorkflowDescriptionIssuesStructuralItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schema = self.schema

        call = self.call.to_dict()

        actors = []
        for actors_item_data in self.actors:
            actors_item = actors_item_data.to_dict()
            actors.append(actors_item)

        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()
            steps.append(steps_item)

        notifications = self.notifications.to_dict()

        schedule = self.schedule.to_dict()

        issues_structural = []
        for issues_structural_item_data in self.issues_structural:
            issues_structural_item = issues_structural_item_data.to_dict()
            issues_structural.append(issues_structural_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schema": schema,
                "call": call,
                "actors": actors,
                "steps": steps,
                "notifications": notifications,
                "schedule": schedule,
                "issues_structural": issues_structural,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_description_actor import WorkflowDescriptionActor
        from ..models.workflow_description_call import WorkflowDescriptionCall
        from ..models.workflow_description_issues_structural_item import WorkflowDescriptionIssuesStructuralItem
        from ..models.workflow_description_notifications import WorkflowDescriptionNotifications
        from ..models.workflow_description_schedule import WorkflowDescriptionSchedule
        from ..models.workflow_description_step import WorkflowDescriptionStep

        d = dict(src_dict)
        schema = d.pop("schema")

        call = WorkflowDescriptionCall.from_dict(d.pop("call"))

        actors = []
        _actors = d.pop("actors")
        for actors_item_data in _actors:
            actors_item = WorkflowDescriptionActor.from_dict(actors_item_data)

            actors.append(actors_item)

        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = WorkflowDescriptionStep.from_dict(steps_item_data)

            steps.append(steps_item)

        notifications = WorkflowDescriptionNotifications.from_dict(d.pop("notifications"))

        schedule = WorkflowDescriptionSchedule.from_dict(d.pop("schedule"))

        issues_structural = []
        _issues_structural = d.pop("issues_structural")
        for issues_structural_item_data in _issues_structural:
            issues_structural_item = WorkflowDescriptionIssuesStructuralItem.from_dict(issues_structural_item_data)

            issues_structural.append(issues_structural_item)

        workflow_description = cls(
            schema=schema,
            call=call,
            actors=actors,
            steps=steps,
            notifications=notifications,
            schedule=schedule,
            issues_structural=issues_structural,
        )

        workflow_description.additional_properties = d
        return workflow_description

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
