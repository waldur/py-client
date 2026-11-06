from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workflow_description_ref_source_enum import WorkflowDescriptionRefSourceEnum

T = TypeVar("T", bound="WorkflowDescriptionRef")


@_attrs_define
class WorkflowDescriptionRef:
    """
    Attributes:
        source (WorkflowDescriptionRefSourceEnum):
        step (Union[None, str]): Key of the step.
        field (str):
        detail (Union[None, str]):
    """

    source: WorkflowDescriptionRefSourceEnum
    step: Union[None, str]
    field: str
    detail: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source = self.source.value

        step: Union[None, str]
        step = self.step

        field = self.field

        detail: Union[None, str]
        detail = self.detail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source": source,
                "step": step,
                "field": field,
                "detail": detail,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source = WorkflowDescriptionRefSourceEnum(d.pop("source"))

        def _parse_step(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        step = _parse_step(d.pop("step"))

        field = d.pop("field")

        def _parse_detail(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        detail = _parse_detail(d.pop("detail"))

        workflow_description_ref = cls(
            source=source,
            step=step,
            field=field,
            detail=detail,
        )

        workflow_description_ref.additional_properties = d
        return workflow_description_ref

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
