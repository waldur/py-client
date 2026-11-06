from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dry_run_next_step import DryRunNextStep


T = TypeVar("T", bound="DryRunNext")


@_attrs_define
class DryRunNext:
    """
    Attributes:
        steps (list['DryRunNextStep']):
        can_submit_changes (bool):
        can_advance (bool):
        can_publish (bool):
        can_extend (bool):
        can_open_final_report (bool):
        can_exhaust_budget (bool):
    """

    steps: list["DryRunNextStep"]
    can_submit_changes: bool
    can_advance: bool
    can_publish: bool
    can_extend: bool
    can_open_final_report: bool
    can_exhaust_budget: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()
            steps.append(steps_item)

        can_submit_changes = self.can_submit_changes

        can_advance = self.can_advance

        can_publish = self.can_publish

        can_extend = self.can_extend

        can_open_final_report = self.can_open_final_report

        can_exhaust_budget = self.can_exhaust_budget

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "steps": steps,
                "can_submit_changes": can_submit_changes,
                "can_advance": can_advance,
                "can_publish": can_publish,
                "can_extend": can_extend,
                "can_open_final_report": can_open_final_report,
                "can_exhaust_budget": can_exhaust_budget,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dry_run_next_step import DryRunNextStep

        d = dict(src_dict)
        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = DryRunNextStep.from_dict(steps_item_data)

            steps.append(steps_item)

        can_submit_changes = d.pop("can_submit_changes")

        can_advance = d.pop("can_advance")

        can_publish = d.pop("can_publish")

        can_extend = d.pop("can_extend")

        can_open_final_report = d.pop("can_open_final_report")

        can_exhaust_budget = d.pop("can_exhaust_budget")

        dry_run_next = cls(
            steps=steps,
            can_submit_changes=can_submit_changes,
            can_advance=can_advance,
            can_publish=can_publish,
            can_extend=can_extend,
            can_open_final_report=can_open_final_report,
            can_exhaust_budget=can_exhaust_budget,
        )

        dry_run_next.additional_properties = d
        return dry_run_next

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
