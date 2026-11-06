from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.workflow_path_step import WorkflowPathStep


T = TypeVar("T", bound="WorkflowPath")


@_attrs_define
class WorkflowPath:
    """
    Attributes:
        steps (list['WorkflowPathStep']):
        proposals (int):
        finished (bool): No proposal on the path is still at a step.
        covered_by_scenario (Union[None, bool]): Whether a saved scenario walks the path; null when unknown.
    """

    steps: list["WorkflowPathStep"]
    proposals: int
    finished: bool
    covered_by_scenario: Union[None, bool]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()
            steps.append(steps_item)

        proposals = self.proposals

        finished = self.finished

        covered_by_scenario: Union[None, bool]
        covered_by_scenario = self.covered_by_scenario

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "steps": steps,
                "proposals": proposals,
                "finished": finished,
                "covered_by_scenario": covered_by_scenario,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_path_step import WorkflowPathStep

        d = dict(src_dict)
        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = WorkflowPathStep.from_dict(steps_item_data)

            steps.append(steps_item)

        proposals = d.pop("proposals")

        finished = d.pop("finished")

        def _parse_covered_by_scenario(data: object) -> Union[None, bool]:
            if data is None:
                return data
            return cast(Union[None, bool], data)

        covered_by_scenario = _parse_covered_by_scenario(d.pop("covered_by_scenario"))

        workflow_path = cls(
            steps=steps,
            proposals=proposals,
            finished=finished,
            covered_by_scenario=covered_by_scenario,
        )

        workflow_path.additional_properties = d
        return workflow_path

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
