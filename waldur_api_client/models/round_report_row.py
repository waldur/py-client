import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.current_stage_enum import CurrentStageEnum
from ..models.round_report_row_status_enum import RoundReportRowStatusEnum

T = TypeVar("T", bound="RoundReportRow")


@_attrs_define
class RoundReportRow:
    """
    Attributes:
        call_uuid (UUID):
        call_name (str):
        call_slug (str):
        organisation_uuid (UUID): The call's call managing organization.
        organisation_name (str): The name of the call managing organization's customer.
        round_uuid (UUID):
        round_name (str):
        round_slug (str):
        call_state (str):
        status (RoundReportRowStatusEnum):
        lifecycle_state (Union[None, str]): Where the round stands after its cut-off.
        proposals_submitted (int):
        start_time (datetime.datetime):
        cutoff_time (Union[None, datetime.datetime]):
        evaluation_started_at (Union[None, datetime.datetime]):
        deciding_started_at (Union[None, datetime.datetime]):
        results_published_at (Union[None, datetime.datetime]):
        adopted_at (Union[None, datetime.date]):
        closed_at (Union[None, datetime.datetime]):
        allocation_date (Union[None, datetime.datetime]):
        days_cutoff_to_evaluation (Union[None, float]):
        days_evaluating (Union[None, float]): From the evaluation start to deciding.
        days_deciding (Union[None, float]): From deciding to the results' publication.
        days_published_to_adopted (Union[None, float]): Whole days from the day the results were published to the day of
            their adoption. Negative when they were adopted first, as a call that requires adoption has them: it publishes
            only adopted results.
        days_cutoff_to_published (Union[None, float]):
        days_after_allocation_date (Union[None, int]): Whole days from the allocation date to the day the results were
            published (negative: early); to today while unpublished past the date. Empty without an allocation date, or
            before it.
        late (bool): Results published on a day after the allocation date, or still unpublished past it.
        current_stage (Union[CurrentStageEnum, None]): Where a round not closed yet stands: not open yet, open for
            submissions, past its cut-off with its evaluation not started, evaluating, deciding, or with its results
            published; call_archived or call_draft for a round of an archived or a draft call. Empty once closed.
        days_in_current_stage (Union[None, float]): Days since the round entered its current stage, to now. Empty for a
            closed round, one not open yet, and one of a call not active.
    """

    call_uuid: UUID
    call_name: str
    call_slug: str
    organisation_uuid: UUID
    organisation_name: str
    round_uuid: UUID
    round_name: str
    round_slug: str
    call_state: str
    status: RoundReportRowStatusEnum
    lifecycle_state: Union[None, str]
    proposals_submitted: int
    start_time: datetime.datetime
    cutoff_time: Union[None, datetime.datetime]
    evaluation_started_at: Union[None, datetime.datetime]
    deciding_started_at: Union[None, datetime.datetime]
    results_published_at: Union[None, datetime.datetime]
    adopted_at: Union[None, datetime.date]
    closed_at: Union[None, datetime.datetime]
    allocation_date: Union[None, datetime.datetime]
    days_cutoff_to_evaluation: Union[None, float]
    days_evaluating: Union[None, float]
    days_deciding: Union[None, float]
    days_published_to_adopted: Union[None, float]
    days_cutoff_to_published: Union[None, float]
    days_after_allocation_date: Union[None, int]
    late: bool
    current_stage: Union[CurrentStageEnum, None]
    days_in_current_stage: Union[None, float]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        call_uuid = str(self.call_uuid)

        call_name = self.call_name

        call_slug = self.call_slug

        organisation_uuid = str(self.organisation_uuid)

        organisation_name = self.organisation_name

        round_uuid = str(self.round_uuid)

        round_name = self.round_name

        round_slug = self.round_slug

        call_state = self.call_state

        status = self.status.value

        lifecycle_state: Union[None, str]
        lifecycle_state = self.lifecycle_state

        proposals_submitted = self.proposals_submitted

        start_time = self.start_time.isoformat()

        cutoff_time: Union[None, str]
        if isinstance(self.cutoff_time, datetime.datetime):
            cutoff_time = self.cutoff_time.isoformat()
        else:
            cutoff_time = self.cutoff_time

        evaluation_started_at: Union[None, str]
        if isinstance(self.evaluation_started_at, datetime.datetime):
            evaluation_started_at = self.evaluation_started_at.isoformat()
        else:
            evaluation_started_at = self.evaluation_started_at

        deciding_started_at: Union[None, str]
        if isinstance(self.deciding_started_at, datetime.datetime):
            deciding_started_at = self.deciding_started_at.isoformat()
        else:
            deciding_started_at = self.deciding_started_at

        results_published_at: Union[None, str]
        if isinstance(self.results_published_at, datetime.datetime):
            results_published_at = self.results_published_at.isoformat()
        else:
            results_published_at = self.results_published_at

        adopted_at: Union[None, str]
        if isinstance(self.adopted_at, datetime.date):
            adopted_at = self.adopted_at.isoformat()
        else:
            adopted_at = self.adopted_at

        closed_at: Union[None, str]
        if isinstance(self.closed_at, datetime.datetime):
            closed_at = self.closed_at.isoformat()
        else:
            closed_at = self.closed_at

        allocation_date: Union[None, str]
        if isinstance(self.allocation_date, datetime.datetime):
            allocation_date = self.allocation_date.isoformat()
        else:
            allocation_date = self.allocation_date

        days_cutoff_to_evaluation: Union[None, float]
        days_cutoff_to_evaluation = self.days_cutoff_to_evaluation

        days_evaluating: Union[None, float]
        days_evaluating = self.days_evaluating

        days_deciding: Union[None, float]
        days_deciding = self.days_deciding

        days_published_to_adopted: Union[None, float]
        days_published_to_adopted = self.days_published_to_adopted

        days_cutoff_to_published: Union[None, float]
        days_cutoff_to_published = self.days_cutoff_to_published

        days_after_allocation_date: Union[None, int]
        days_after_allocation_date = self.days_after_allocation_date

        late = self.late

        current_stage: Union[None, str]
        if isinstance(self.current_stage, CurrentStageEnum):
            current_stage = self.current_stage.value
        else:
            current_stage = self.current_stage

        days_in_current_stage: Union[None, float]
        days_in_current_stage = self.days_in_current_stage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "call_uuid": call_uuid,
                "call_name": call_name,
                "call_slug": call_slug,
                "organisation_uuid": organisation_uuid,
                "organisation_name": organisation_name,
                "round_uuid": round_uuid,
                "round_name": round_name,
                "round_slug": round_slug,
                "call_state": call_state,
                "status": status,
                "lifecycle_state": lifecycle_state,
                "proposals_submitted": proposals_submitted,
                "start_time": start_time,
                "cutoff_time": cutoff_time,
                "evaluation_started_at": evaluation_started_at,
                "deciding_started_at": deciding_started_at,
                "results_published_at": results_published_at,
                "adopted_at": adopted_at,
                "closed_at": closed_at,
                "allocation_date": allocation_date,
                "days_cutoff_to_evaluation": days_cutoff_to_evaluation,
                "days_evaluating": days_evaluating,
                "days_deciding": days_deciding,
                "days_published_to_adopted": days_published_to_adopted,
                "days_cutoff_to_published": days_cutoff_to_published,
                "days_after_allocation_date": days_after_allocation_date,
                "late": late,
                "current_stage": current_stage,
                "days_in_current_stage": days_in_current_stage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        call_uuid = UUID(d.pop("call_uuid"))

        call_name = d.pop("call_name")

        call_slug = d.pop("call_slug")

        organisation_uuid = UUID(d.pop("organisation_uuid"))

        organisation_name = d.pop("organisation_name")

        round_uuid = UUID(d.pop("round_uuid"))

        round_name = d.pop("round_name")

        round_slug = d.pop("round_slug")

        call_state = d.pop("call_state")

        status = RoundReportRowStatusEnum(d.pop("status"))

        def _parse_lifecycle_state(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        lifecycle_state = _parse_lifecycle_state(d.pop("lifecycle_state"))

        proposals_submitted = d.pop("proposals_submitted")

        start_time = isoparse(d.pop("start_time"))

        def _parse_cutoff_time(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cutoff_time_type_0 = isoparse(data)

                return cutoff_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        cutoff_time = _parse_cutoff_time(d.pop("cutoff_time"))

        def _parse_evaluation_started_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                evaluation_started_at_type_0 = isoparse(data)

                return evaluation_started_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        evaluation_started_at = _parse_evaluation_started_at(d.pop("evaluation_started_at"))

        def _parse_deciding_started_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deciding_started_at_type_0 = isoparse(data)

                return deciding_started_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        deciding_started_at = _parse_deciding_started_at(d.pop("deciding_started_at"))

        def _parse_results_published_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                results_published_at_type_0 = isoparse(data)

                return results_published_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        results_published_at = _parse_results_published_at(d.pop("results_published_at"))

        def _parse_adopted_at(data: object) -> Union[None, datetime.date]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                adopted_at_type_0 = isoparse(data).date()

                return adopted_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.date], data)

        adopted_at = _parse_adopted_at(d.pop("adopted_at"))

        def _parse_closed_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                closed_at_type_0 = isoparse(data)

                return closed_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        closed_at = _parse_closed_at(d.pop("closed_at"))

        def _parse_allocation_date(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                allocation_date_type_0 = isoparse(data)

                return allocation_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        allocation_date = _parse_allocation_date(d.pop("allocation_date"))

        def _parse_days_cutoff_to_evaluation(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        days_cutoff_to_evaluation = _parse_days_cutoff_to_evaluation(d.pop("days_cutoff_to_evaluation"))

        def _parse_days_evaluating(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        days_evaluating = _parse_days_evaluating(d.pop("days_evaluating"))

        def _parse_days_deciding(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        days_deciding = _parse_days_deciding(d.pop("days_deciding"))

        def _parse_days_published_to_adopted(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        days_published_to_adopted = _parse_days_published_to_adopted(d.pop("days_published_to_adopted"))

        def _parse_days_cutoff_to_published(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        days_cutoff_to_published = _parse_days_cutoff_to_published(d.pop("days_cutoff_to_published"))

        def _parse_days_after_allocation_date(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        days_after_allocation_date = _parse_days_after_allocation_date(d.pop("days_after_allocation_date"))

        late = d.pop("late")

        def _parse_current_stage(data: object) -> Union[CurrentStageEnum, None]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                current_stage_type_0 = CurrentStageEnum(data)

                return current_stage_type_0
            except:  # noqa: E722
                pass
            return cast(Union[CurrentStageEnum, None], data)

        current_stage = _parse_current_stage(d.pop("current_stage"))

        def _parse_days_in_current_stage(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        days_in_current_stage = _parse_days_in_current_stage(d.pop("days_in_current_stage"))

        round_report_row = cls(
            call_uuid=call_uuid,
            call_name=call_name,
            call_slug=call_slug,
            organisation_uuid=organisation_uuid,
            organisation_name=organisation_name,
            round_uuid=round_uuid,
            round_name=round_name,
            round_slug=round_slug,
            call_state=call_state,
            status=status,
            lifecycle_state=lifecycle_state,
            proposals_submitted=proposals_submitted,
            start_time=start_time,
            cutoff_time=cutoff_time,
            evaluation_started_at=evaluation_started_at,
            deciding_started_at=deciding_started_at,
            results_published_at=results_published_at,
            adopted_at=adopted_at,
            closed_at=closed_at,
            allocation_date=allocation_date,
            days_cutoff_to_evaluation=days_cutoff_to_evaluation,
            days_evaluating=days_evaluating,
            days_deciding=days_deciding,
            days_published_to_adopted=days_published_to_adopted,
            days_cutoff_to_published=days_cutoff_to_published,
            days_after_allocation_date=days_after_allocation_date,
            late=late,
            current_stage=current_stage,
            days_in_current_stage=days_in_current_stage,
        )

        round_report_row.additional_properties = d
        return round_report_row

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
