from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.label_kind_enum import LabelKindEnum

if TYPE_CHECKING:
    from ..models.step_audience_status_labels import StepAudienceStatusLabels


T = TypeVar("T", bound="WorkflowDescriptionApplicant")


@_attrs_define
class WorkflowDescriptionApplicant:
    """
    Attributes:
        visible (bool):
        label_kind (LabelKindEnum):
        label (str): What the applicant's tracker shows while the step is current.
        labels (StepAudienceStatusLabels):
        internal (bool):
    """

    visible: bool
    label_kind: LabelKindEnum
    label: str
    labels: "StepAudienceStatusLabels"
    internal: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        visible = self.visible

        label_kind = self.label_kind.value

        label = self.label

        labels = self.labels.to_dict()

        internal = self.internal

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "visible": visible,
                "label_kind": label_kind,
                "label": label,
                "labels": labels,
                "internal": internal,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.step_audience_status_labels import StepAudienceStatusLabels

        d = dict(src_dict)
        visible = d.pop("visible")

        label_kind = LabelKindEnum(d.pop("label_kind"))

        label = d.pop("label")

        labels = StepAudienceStatusLabels.from_dict(d.pop("labels"))

        internal = d.pop("internal")

        workflow_description_applicant = cls(
            visible=visible,
            label_kind=label_kind,
            label=label,
            labels=labels,
            internal=internal,
        )

        workflow_description_applicant.additional_properties = d
        return workflow_description_applicant

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
