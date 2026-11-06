import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.blank_enum import BlankEnum
from ..models.undecided_at_round_completion_enum import UndecidedAtRoundCompletionEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedRoundRequest")


@_attrs_define
class ProtectedRoundRequest:
    """
    Attributes:
        start_time (datetime.datetime):
        cutoff_time (Union[None, Unset, datetime.datetime]): When submission closes. Empty: the round stays open until a
            call manager closes it.
        allocation_date (Union[None, Unset, datetime.datetime]):
        review_duration_in_days (Union[None, Unset, int]): Deprecated: a review is due when the step it contributes to
            is (see the round's step due dates). Only a review whose step has no deadline is still due this many days after
            it was created.
        undecided_at_round_completion (Union[BlankEnum, None, UndecidedAtRoundCompletionEnum, Unset]): Overrides the
            call's rule for proposals still without a decision when the round is completed. Empty: the call's rule applies.
    """

    start_time: datetime.datetime
    cutoff_time: Union[None, Unset, datetime.datetime] = UNSET
    allocation_date: Union[None, Unset, datetime.datetime] = UNSET
    review_duration_in_days: Union[None, Unset, int] = UNSET
    undecided_at_round_completion: Union[BlankEnum, None, UndecidedAtRoundCompletionEnum, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_time = self.start_time.isoformat()

        cutoff_time: Union[None, Unset, str]
        if isinstance(self.cutoff_time, Unset):
            cutoff_time = UNSET
        elif isinstance(self.cutoff_time, datetime.datetime):
            cutoff_time = self.cutoff_time.isoformat()
        else:
            cutoff_time = self.cutoff_time

        allocation_date: Union[None, Unset, str]
        if isinstance(self.allocation_date, Unset):
            allocation_date = UNSET
        elif isinstance(self.allocation_date, datetime.datetime):
            allocation_date = self.allocation_date.isoformat()
        else:
            allocation_date = self.allocation_date

        review_duration_in_days: Union[None, Unset, int]
        if isinstance(self.review_duration_in_days, Unset):
            review_duration_in_days = UNSET
        else:
            review_duration_in_days = self.review_duration_in_days

        undecided_at_round_completion: Union[None, Unset, str]
        if isinstance(self.undecided_at_round_completion, Unset):
            undecided_at_round_completion = UNSET
        elif isinstance(self.undecided_at_round_completion, UndecidedAtRoundCompletionEnum):
            undecided_at_round_completion = self.undecided_at_round_completion.value
        elif isinstance(self.undecided_at_round_completion, BlankEnum):
            undecided_at_round_completion = self.undecided_at_round_completion.value
        else:
            undecided_at_round_completion = self.undecided_at_round_completion

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start_time": start_time,
            }
        )
        if cutoff_time is not UNSET:
            field_dict["cutoff_time"] = cutoff_time
        if allocation_date is not UNSET:
            field_dict["allocation_date"] = allocation_date
        if review_duration_in_days is not UNSET:
            field_dict["review_duration_in_days"] = review_duration_in_days
        if undecided_at_round_completion is not UNSET:
            field_dict["undecided_at_round_completion"] = undecided_at_round_completion

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_time = isoparse(d.pop("start_time"))

        def _parse_cutoff_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cutoff_time_type_0 = isoparse(data)

                return cutoff_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        cutoff_time = _parse_cutoff_time(d.pop("cutoff_time", UNSET))

        def _parse_allocation_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                allocation_date_type_0 = isoparse(data)

                return allocation_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        allocation_date = _parse_allocation_date(d.pop("allocation_date", UNSET))

        def _parse_review_duration_in_days(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        review_duration_in_days = _parse_review_duration_in_days(d.pop("review_duration_in_days", UNSET))

        def _parse_undecided_at_round_completion(
            data: object,
        ) -> Union[BlankEnum, None, UndecidedAtRoundCompletionEnum, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                undecided_at_round_completion_type_0 = UndecidedAtRoundCompletionEnum(data)

                return undecided_at_round_completion_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                undecided_at_round_completion_type_1 = BlankEnum(data)

                return undecided_at_round_completion_type_1
            except:  # noqa: E722
                pass
            return cast(Union[BlankEnum, None, UndecidedAtRoundCompletionEnum, Unset], data)

        undecided_at_round_completion = _parse_undecided_at_round_completion(
            d.pop("undecided_at_round_completion", UNSET)
        )

        protected_round_request = cls(
            start_time=start_time,
            cutoff_time=cutoff_time,
            allocation_date=allocation_date,
            review_duration_in_days=review_duration_in_days,
            undecided_at_round_completion=undecided_at_round_completion,
        )

        protected_round_request.additional_properties = d
        return protected_round_request

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
