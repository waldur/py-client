import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.step_contribution_with_answers import StepContributionWithAnswers


T = TypeVar("T", bound="ReleasedReport")


@_attrs_define
class ReleasedReport:
    """
    Attributes:
        call_step_uuid (UUID):
        step_name (str):
        released_at (datetime.datetime):
        released_by_name (Union[None, str]): Who released it; for the call team only.
        text (str): The text released in place of the report; empty when the report itself was released.
        contributions (list['StepContributionWithAnswers']): The report: the step's submitted contributions with their
            answers. For the applicant, empty when a text was released in its place.
    """

    call_step_uuid: UUID
    step_name: str
    released_at: datetime.datetime
    released_by_name: Union[None, str]
    text: str
    contributions: list["StepContributionWithAnswers"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        call_step_uuid = str(self.call_step_uuid)

        step_name = self.step_name

        released_at = self.released_at.isoformat()

        released_by_name: Union[None, str]
        released_by_name = self.released_by_name

        text = self.text

        contributions = []
        for contributions_item_data in self.contributions:
            contributions_item = contributions_item_data.to_dict()
            contributions.append(contributions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "call_step_uuid": call_step_uuid,
                "step_name": step_name,
                "released_at": released_at,
                "released_by_name": released_by_name,
                "text": text,
                "contributions": contributions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.step_contribution_with_answers import StepContributionWithAnswers

        d = dict(src_dict)
        call_step_uuid = UUID(d.pop("call_step_uuid"))

        step_name = d.pop("step_name")

        released_at = isoparse(d.pop("released_at"))

        def _parse_released_by_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        released_by_name = _parse_released_by_name(d.pop("released_by_name"))

        text = d.pop("text")

        contributions = []
        _contributions = d.pop("contributions")
        for contributions_item_data in _contributions:
            contributions_item = StepContributionWithAnswers.from_dict(contributions_item_data)

            contributions.append(contributions_item)

        released_report = cls(
            call_step_uuid=call_step_uuid,
            step_name=step_name,
            released_at=released_at,
            released_by_name=released_by_name,
            text=text,
            contributions=contributions,
        )

        released_report.additional_properties = d
        return released_report

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
