import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.workflow_timeline_notification import WorkflowTimelineNotification
    from ..models.workflow_timeline_step import WorkflowTimelineStep


T = TypeVar("T", bound="WorkflowTimeline")


@_attrs_define
class WorkflowTimeline:
    """
    Attributes:
        proposal_uuid (str):
        proposal_name (str):
        state (str):
        generated_at (datetime.datetime):
        steps (list['WorkflowTimelineStep']):
        notifications (list['WorkflowTimelineNotification']):
    """

    proposal_uuid: str
    proposal_name: str
    state: str
    generated_at: datetime.datetime
    steps: list["WorkflowTimelineStep"]
    notifications: list["WorkflowTimelineNotification"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        proposal_uuid = self.proposal_uuid

        proposal_name = self.proposal_name

        state = self.state

        generated_at = self.generated_at.isoformat()

        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()
            steps.append(steps_item)

        notifications = []
        for notifications_item_data in self.notifications:
            notifications_item = notifications_item_data.to_dict()
            notifications.append(notifications_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "proposal_uuid": proposal_uuid,
                "proposal_name": proposal_name,
                "state": state,
                "generated_at": generated_at,
                "steps": steps,
                "notifications": notifications,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_timeline_notification import WorkflowTimelineNotification
        from ..models.workflow_timeline_step import WorkflowTimelineStep

        d = dict(src_dict)
        proposal_uuid = d.pop("proposal_uuid")

        proposal_name = d.pop("proposal_name")

        state = d.pop("state")

        generated_at = isoparse(d.pop("generated_at"))

        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = WorkflowTimelineStep.from_dict(steps_item_data)

            steps.append(steps_item)

        notifications = []
        _notifications = d.pop("notifications")
        for notifications_item_data in _notifications:
            notifications_item = WorkflowTimelineNotification.from_dict(notifications_item_data)

            notifications.append(notifications_item)

        workflow_timeline = cls(
            proposal_uuid=proposal_uuid,
            proposal_name=proposal_name,
            state=state,
            generated_at=generated_at,
            steps=steps,
            notifications=notifications,
        )

        workflow_timeline.additional_properties = d
        return workflow_timeline

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
