from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.round_meeting_note import RoundMeetingNote
    from ..models.round_step_proposal_result import RoundStepProposalResult


T = TypeVar("T", bound="SubmitRoundReportResponse")


@_attrs_define
class SubmitRoundReportResponse:
    """
    Attributes:
        report (RoundMeetingNote):
        completed (list['RoundStepProposalResult']):
        failed (list['RoundStepProposalResult']):
    """

    report: "RoundMeetingNote"
    completed: list["RoundStepProposalResult"]
    failed: list["RoundStepProposalResult"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        report = self.report.to_dict()

        completed = []
        for completed_item_data in self.completed:
            completed_item = completed_item_data.to_dict()
            completed.append(completed_item)

        failed = []
        for failed_item_data in self.failed:
            failed_item = failed_item_data.to_dict()
            failed.append(failed_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "report": report,
                "completed": completed,
                "failed": failed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.round_meeting_note import RoundMeetingNote
        from ..models.round_step_proposal_result import RoundStepProposalResult

        d = dict(src_dict)
        report = RoundMeetingNote.from_dict(d.pop("report"))

        completed = []
        _completed = d.pop("completed")
        for completed_item_data in _completed:
            completed_item = RoundStepProposalResult.from_dict(completed_item_data)

            completed.append(completed_item)

        failed = []
        _failed = d.pop("failed")
        for failed_item_data in _failed:
            failed_item = RoundStepProposalResult.from_dict(failed_item_data)

            failed.append(failed_item)

        submit_round_report_response = cls(
            report=report,
            completed=completed,
            failed=failed,
        )

        submit_round_report_response.additional_properties = d
        return submit_round_report_response

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
