from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.step_audience_status_labels import StepAudienceStatusLabels


T = TypeVar("T", bound="StepStatusLabels")


@_attrs_define
class StepStatusLabels:
    """
    Attributes:
        applicant (Union[Unset, StepAudienceStatusLabels]):
        evaluators (Union[Unset, StepAudienceStatusLabels]):
        call_team (Union[Unset, StepAudienceStatusLabels]):
        offering_team (Union[Unset, StepAudienceStatusLabels]):
    """

    applicant: Union[Unset, "StepAudienceStatusLabels"] = UNSET
    evaluators: Union[Unset, "StepAudienceStatusLabels"] = UNSET
    call_team: Union[Unset, "StepAudienceStatusLabels"] = UNSET
    offering_team: Union[Unset, "StepAudienceStatusLabels"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        applicant: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.applicant, Unset):
            applicant = self.applicant.to_dict()

        evaluators: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.evaluators, Unset):
            evaluators = self.evaluators.to_dict()

        call_team: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.call_team, Unset):
            call_team = self.call_team.to_dict()

        offering_team: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.offering_team, Unset):
            offering_team = self.offering_team.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if applicant is not UNSET:
            field_dict["applicant"] = applicant
        if evaluators is not UNSET:
            field_dict["evaluators"] = evaluators
        if call_team is not UNSET:
            field_dict["call_team"] = call_team
        if offering_team is not UNSET:
            field_dict["offering_team"] = offering_team

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.step_audience_status_labels import StepAudienceStatusLabels

        d = dict(src_dict)
        _applicant = d.pop("applicant", UNSET)
        applicant: Union[Unset, StepAudienceStatusLabels]
        if isinstance(_applicant, Unset):
            applicant = UNSET
        else:
            applicant = StepAudienceStatusLabels.from_dict(_applicant)

        _evaluators = d.pop("evaluators", UNSET)
        evaluators: Union[Unset, StepAudienceStatusLabels]
        if isinstance(_evaluators, Unset):
            evaluators = UNSET
        else:
            evaluators = StepAudienceStatusLabels.from_dict(_evaluators)

        _call_team = d.pop("call_team", UNSET)
        call_team: Union[Unset, StepAudienceStatusLabels]
        if isinstance(_call_team, Unset):
            call_team = UNSET
        else:
            call_team = StepAudienceStatusLabels.from_dict(_call_team)

        _offering_team = d.pop("offering_team", UNSET)
        offering_team: Union[Unset, StepAudienceStatusLabels]
        if isinstance(_offering_team, Unset):
            offering_team = UNSET
        else:
            offering_team = StepAudienceStatusLabels.from_dict(_offering_team)

        step_status_labels = cls(
            applicant=applicant,
            evaluators=evaluators,
            call_team=call_team,
            offering_team=offering_team,
        )

        step_status_labels.additional_properties = d
        return step_status_labels

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
