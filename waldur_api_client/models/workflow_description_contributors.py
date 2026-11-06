from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WorkflowDescriptionContributors")


@_attrs_define
class WorkflowDescriptionContributors:
    """
    Attributes:
        source (str):
        parameter (Union[None, str]):
        per_requested_offering (bool):
        lead_only (bool):
        min_ (Union[None, int]):
        max_ (Union[None, int]):
    """

    source: str
    parameter: Union[None, str]
    per_requested_offering: bool
    lead_only: bool
    min_: Union[None, int]
    max_: Union[None, int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source = self.source

        parameter: Union[None, str]
        parameter = self.parameter

        per_requested_offering = self.per_requested_offering

        lead_only = self.lead_only

        min_: Union[None, int]
        min_ = self.min_

        max_: Union[None, int]
        max_ = self.max_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source": source,
                "parameter": parameter,
                "per_requested_offering": per_requested_offering,
                "lead_only": lead_only,
                "min": min_,
                "max": max_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source = d.pop("source")

        def _parse_parameter(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        parameter = _parse_parameter(d.pop("parameter"))

        per_requested_offering = d.pop("per_requested_offering")

        lead_only = d.pop("lead_only")

        def _parse_min_(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        min_ = _parse_min_(d.pop("min"))

        def _parse_max_(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        max_ = _parse_max_(d.pop("max"))

        workflow_description_contributors = cls(
            source=source,
            parameter=parameter,
            per_requested_offering=per_requested_offering,
            lead_only=lead_only,
            min_=min_,
            max_=max_,
        )

        workflow_description_contributors.additional_properties = d
        return workflow_description_contributors

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
