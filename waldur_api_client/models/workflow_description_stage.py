from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WorkflowDescriptionStage")


@_attrs_define
class WorkflowDescriptionStage:
    """
    Attributes:
        stage (int):
        steps (list[str]):
        start_day (int):
        end_day (int):
    """

    stage: int
    steps: list[str]
    start_day: int
    end_day: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stage = self.stage

        steps = self.steps

        start_day = self.start_day

        end_day = self.end_day

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stage": stage,
                "steps": steps,
                "start_day": start_day,
                "end_day": end_day,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        stage = d.pop("stage")

        steps = cast(list[str], d.pop("steps"))

        start_day = d.pop("start_day")

        end_day = d.pop("end_day")

        workflow_description_stage = cls(
            stage=stage,
            steps=steps,
            start_day=start_day,
            end_day=end_day,
        )

        workflow_description_stage.additional_properties = d
        return workflow_description_stage

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
