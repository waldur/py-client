import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.workflow_report_step import WorkflowReportStep


T = TypeVar("T", bound="WorkflowReport")


@_attrs_define
class WorkflowReport:
    """
    Attributes:
        generated_at (datetime.datetime):
        proposals (int): Proposals with a step instance in the scope.
        steps (list['WorkflowReportStep']): Per step key, summed over the calls, in workflow order.
    """

    generated_at: datetime.datetime
    proposals: int
    steps: list["WorkflowReportStep"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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
                "generated_at": generated_at,
                "proposals": proposals,
                "steps": steps,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_report_step import WorkflowReportStep

        d = dict(src_dict)
        generated_at = isoparse(d.pop("generated_at"))

        proposals = d.pop("proposals")

        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = WorkflowReportStep.from_dict(steps_item_data)

            steps.append(steps_item)

        workflow_report = cls(
            generated_at=generated_at,
            proposals=proposals,
            steps=steps,
        )

        workflow_report.additional_properties = d
        return workflow_report

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
