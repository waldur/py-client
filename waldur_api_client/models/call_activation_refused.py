from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.workflow_check_finding import WorkflowCheckFinding


T = TypeVar("T", bound="CallActivationRefused")


@_attrs_define
class CallActivationRefused:
    """
    Attributes:
        detail (str): Every error, in one message.
        workflow_check (list['WorkflowCheckFinding']):
    """

    detail: str
    workflow_check: list["WorkflowCheckFinding"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        detail = self.detail

        workflow_check = []
        for workflow_check_item_data in self.workflow_check:
            workflow_check_item = workflow_check_item_data.to_dict()
            workflow_check.append(workflow_check_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "detail": detail,
                "workflow_check": workflow_check,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_check_finding import WorkflowCheckFinding

        d = dict(src_dict)
        detail = d.pop("detail")

        workflow_check = []
        _workflow_check = d.pop("workflow_check")
        for workflow_check_item_data in _workflow_check:
            workflow_check_item = WorkflowCheckFinding.from_dict(workflow_check_item_data)

            workflow_check.append(workflow_check_item)

        call_activation_refused = cls(
            detail=detail,
            workflow_check=workflow_check,
        )

        call_activation_refused.additional_properties = d
        return call_activation_refused

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
