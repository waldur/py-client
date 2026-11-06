from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.workflow_entity_change import WorkflowEntityChange
    from ..models.workflow_field_change import WorkflowFieldChange
    from ..models.workflow_version_summary import WorkflowVersionSummary


T = TypeVar("T", bound="WorkflowChanges")


@_attrs_define
class WorkflowChanges:
    """
    Attributes:
        steps (list['WorkflowEntityChange']):
        call (list['WorkflowFieldChange']):
        proposal_roles (list['WorkflowEntityChange']):
        panels (list['WorkflowEntityChange']):
        forms (list['WorkflowEntityChange']):
        summary (WorkflowVersionSummary):
    """

    steps: list["WorkflowEntityChange"]
    call: list["WorkflowFieldChange"]
    proposal_roles: list["WorkflowEntityChange"]
    panels: list["WorkflowEntityChange"]
    forms: list["WorkflowEntityChange"]
    summary: "WorkflowVersionSummary"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()
            steps.append(steps_item)

        call = []
        for call_item_data in self.call:
            call_item = call_item_data.to_dict()
            call.append(call_item)

        proposal_roles = []
        for proposal_roles_item_data in self.proposal_roles:
            proposal_roles_item = proposal_roles_item_data.to_dict()
            proposal_roles.append(proposal_roles_item)

        panels = []
        for panels_item_data in self.panels:
            panels_item = panels_item_data.to_dict()
            panels.append(panels_item)

        forms = []
        for forms_item_data in self.forms:
            forms_item = forms_item_data.to_dict()
            forms.append(forms_item)

        summary = self.summary.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "steps": steps,
                "call": call,
                "proposal_roles": proposal_roles,
                "panels": panels,
                "forms": forms,
                "summary": summary,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_entity_change import WorkflowEntityChange
        from ..models.workflow_field_change import WorkflowFieldChange
        from ..models.workflow_version_summary import WorkflowVersionSummary

        d = dict(src_dict)
        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = WorkflowEntityChange.from_dict(steps_item_data)

            steps.append(steps_item)

        call = []
        _call = d.pop("call")
        for call_item_data in _call:
            call_item = WorkflowFieldChange.from_dict(call_item_data)

            call.append(call_item)

        proposal_roles = []
        _proposal_roles = d.pop("proposal_roles")
        for proposal_roles_item_data in _proposal_roles:
            proposal_roles_item = WorkflowEntityChange.from_dict(proposal_roles_item_data)

            proposal_roles.append(proposal_roles_item)

        panels = []
        _panels = d.pop("panels")
        for panels_item_data in _panels:
            panels_item = WorkflowEntityChange.from_dict(panels_item_data)

            panels.append(panels_item)

        forms = []
        _forms = d.pop("forms")
        for forms_item_data in _forms:
            forms_item = WorkflowEntityChange.from_dict(forms_item_data)

            forms.append(forms_item)

        summary = WorkflowVersionSummary.from_dict(d.pop("summary"))

        workflow_changes = cls(
            steps=steps,
            call=call,
            proposal_roles=proposal_roles,
            panels=panels,
            forms=forms,
            summary=summary,
        )

        workflow_changes.additional_properties = d
        return workflow_changes

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
