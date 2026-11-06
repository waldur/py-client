from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WorkflowDescriptionPlannedStep")


@_attrs_define
class WorkflowDescriptionPlannedStep:
    """
    Attributes:
        key (str):
        stage (int):
        start_day (int): Planned start, in days from the start of evaluation.
        end_day (int): Planned end: the start plus the step's own duration.
        conditional (bool): The step has a run condition and is planned as if taken.
        critical (bool): The longest step of its stage, on the critical path.
    """

    key: str
    stage: int
    start_day: int
    end_day: int
    conditional: bool
    critical: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        stage = self.stage

        start_day = self.start_day

        end_day = self.end_day

        conditional = self.conditional

        critical = self.critical

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "stage": stage,
                "start_day": start_day,
                "end_day": end_day,
                "conditional": conditional,
                "critical": critical,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        stage = d.pop("stage")

        start_day = d.pop("start_day")

        end_day = d.pop("end_day")

        conditional = d.pop("conditional")

        critical = d.pop("critical")

        workflow_description_planned_step = cls(
            key=key,
            stage=stage,
            start_day=start_day,
            end_day=end_day,
            conditional=conditional,
            critical=critical,
        )

        workflow_description_planned_step.additional_properties = d
        return workflow_description_planned_step

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
