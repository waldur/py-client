from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.workflow_check_finding import WorkflowCheckFinding
    from ..models.workflow_check_summary import WorkflowCheckSummary


T = TypeVar("T", bound="WorkflowCheck")


@_attrs_define
class WorkflowCheck:
    """
    Attributes:
        findings (list['WorkflowCheckFinding']):
        summary (WorkflowCheckSummary):
        can_activate (bool): Whether no finding is an error; warnings never block.
    """

    findings: list["WorkflowCheckFinding"]
    summary: "WorkflowCheckSummary"
    can_activate: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        findings = []
        for findings_item_data in self.findings:
            findings_item = findings_item_data.to_dict()
            findings.append(findings_item)

        summary = self.summary.to_dict()

        can_activate = self.can_activate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "findings": findings,
                "summary": summary,
                "can_activate": can_activate,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_check_finding import WorkflowCheckFinding
        from ..models.workflow_check_summary import WorkflowCheckSummary

        d = dict(src_dict)
        findings = []
        _findings = d.pop("findings")
        for findings_item_data in _findings:
            findings_item = WorkflowCheckFinding.from_dict(findings_item_data)

            findings.append(findings_item)

        summary = WorkflowCheckSummary.from_dict(d.pop("summary"))

        can_activate = d.pop("can_activate")

        workflow_check = cls(
            findings=findings,
            summary=summary,
            can_activate=can_activate,
        )

        workflow_check.additional_properties = d
        return workflow_check

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
