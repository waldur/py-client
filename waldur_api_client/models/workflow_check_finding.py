from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workflow_check_severity import WorkflowCheckSeverity

if TYPE_CHECKING:
    from ..models.workflow_description_ref import WorkflowDescriptionRef


T = TypeVar("T", bound="WorkflowCheckFinding")


@_attrs_define
class WorkflowCheckFinding:
    """
    Attributes:
        code (str): Stable identifier of the rule.
        title (str): The rule's name in a few words, for a list of findings.
        severity (WorkflowCheckSeverity):
        step (Union[None, str]): Key of the step; null for the call.
        step_name (Union[None, str]):
        field (Union[None, str]): The setting that fixes it: a step field, or a call-level section such as rounds,
            offerings or panels.
        message (str):
        because (list['WorkflowDescriptionRef']):
    """

    code: str
    title: str
    severity: WorkflowCheckSeverity
    step: Union[None, str]
    step_name: Union[None, str]
    field: Union[None, str]
    message: str
    because: list["WorkflowDescriptionRef"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        title = self.title

        severity = self.severity.value

        step: Union[None, str]
        step = self.step

        step_name: Union[None, str]
        step_name = self.step_name

        field: Union[None, str]
        field = self.field

        message = self.message

        because = []
        for because_item_data in self.because:
            because_item = because_item_data.to_dict()
            because.append(because_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "title": title,
                "severity": severity,
                "step": step,
                "step_name": step_name,
                "field": field,
                "message": message,
                "because": because,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_description_ref import WorkflowDescriptionRef

        d = dict(src_dict)
        code = d.pop("code")

        title = d.pop("title")

        severity = WorkflowCheckSeverity(d.pop("severity"))

        def _parse_step(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        step = _parse_step(d.pop("step"))

        def _parse_step_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        step_name = _parse_step_name(d.pop("step_name"))

        def _parse_field(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        field = _parse_field(d.pop("field"))

        message = d.pop("message")

        because = []
        _because = d.pop("because")
        for because_item_data in _because:
            because_item = WorkflowDescriptionRef.from_dict(because_item_data)

            because.append(because_item)

        workflow_check_finding = cls(
            code=code,
            title=title,
            severity=severity,
            step=step,
            step_name=step_name,
            field=field,
            message=message,
            because=because,
        )

        workflow_check_finding.additional_properties = d
        return workflow_check_finding

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
