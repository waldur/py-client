from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.step_audience_status_labels_request_outcomes import StepAudienceStatusLabelsRequestOutcomes


T = TypeVar("T", bound="StepAudienceStatusLabelsRequest")


@_attrs_define
class StepAudienceStatusLabelsRequest:
    """
    Attributes:
        active (Union[Unset, str]): While the step runs on the proposal.
        completed (Union[Unset, str]): Once the step has ended on the proposal.
        changes_requested (Union[Unset, str]): While the step has sent the proposal back for changes.
        outcomes (Union[Unset, StepAudienceStatusLabelsRequestOutcomes]): Once the step has ended with an outcome the
            reader is shown, by outcome; in place of 'completed'.
    """

    active: Union[Unset, str] = UNSET
    completed: Union[Unset, str] = UNSET
    changes_requested: Union[Unset, str] = UNSET
    outcomes: Union[Unset, "StepAudienceStatusLabelsRequestOutcomes"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        completed = self.completed

        changes_requested = self.changes_requested

        outcomes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.outcomes, Unset):
            outcomes = self.outcomes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if completed is not UNSET:
            field_dict["completed"] = completed
        if changes_requested is not UNSET:
            field_dict["changes_requested"] = changes_requested
        if outcomes is not UNSET:
            field_dict["outcomes"] = outcomes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.step_audience_status_labels_request_outcomes import StepAudienceStatusLabelsRequestOutcomes

        d = dict(src_dict)
        active = d.pop("active", UNSET)

        completed = d.pop("completed", UNSET)

        changes_requested = d.pop("changes_requested", UNSET)

        _outcomes = d.pop("outcomes", UNSET)
        outcomes: Union[Unset, StepAudienceStatusLabelsRequestOutcomes]
        if isinstance(_outcomes, Unset):
            outcomes = UNSET
        else:
            outcomes = StepAudienceStatusLabelsRequestOutcomes.from_dict(_outcomes)

        step_audience_status_labels_request = cls(
            active=active,
            completed=completed,
            changes_requested=changes_requested,
            outcomes=outcomes,
        )

        step_audience_status_labels_request.additional_properties = d
        return step_audience_status_labels_request

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
