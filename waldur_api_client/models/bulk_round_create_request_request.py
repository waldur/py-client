import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.allocation_time_enum import AllocationTimeEnum
from ..models.cadence_enum import CadenceEnum
from ..models.deciding_entity_enum import DecidingEntityEnum
from ..models.review_strategy_enum import ReviewStrategyEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkRoundCreateRequestRequest")


@_attrs_define
class BulkRoundCreateRequestRequest:
    """
    Attributes:
        start_time (datetime.datetime):
        cadence (CadenceEnum):
        submission_window_days (int):
        number_of_rounds (int):
        review_strategy (Union[Unset, ReviewStrategyEnum]):
        deciding_entity (Union[Unset, DecidingEntityEnum]):
        allocation_time (Union[Unset, AllocationTimeEnum]):
        review_duration_in_days (Union[None, Unset, int]):
        minimum_number_of_reviewers (Union[None, Unset, int]):
        minimal_average_scoring (Union[None, Unset, str]):
        custom_interval_months (Union[None, Unset, int]):
    """

    start_time: datetime.datetime
    cadence: CadenceEnum
    submission_window_days: int
    number_of_rounds: int
    review_strategy: Union[Unset, ReviewStrategyEnum] = UNSET
    deciding_entity: Union[Unset, DecidingEntityEnum] = UNSET
    allocation_time: Union[Unset, AllocationTimeEnum] = UNSET
    review_duration_in_days: Union[None, Unset, int] = UNSET
    minimum_number_of_reviewers: Union[None, Unset, int] = UNSET
    minimal_average_scoring: Union[None, Unset, str] = UNSET
    custom_interval_months: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_time = self.start_time.isoformat()

        cadence = self.cadence.value

        submission_window_days = self.submission_window_days

        number_of_rounds = self.number_of_rounds

        review_strategy: Union[Unset, str] = UNSET
        if not isinstance(self.review_strategy, Unset):
            review_strategy = self.review_strategy.value

        deciding_entity: Union[Unset, str] = UNSET
        if not isinstance(self.deciding_entity, Unset):
            deciding_entity = self.deciding_entity.value

        allocation_time: Union[Unset, str] = UNSET
        if not isinstance(self.allocation_time, Unset):
            allocation_time = self.allocation_time.value

        review_duration_in_days: Union[None, Unset, int]
        if isinstance(self.review_duration_in_days, Unset):
            review_duration_in_days = UNSET
        else:
            review_duration_in_days = self.review_duration_in_days

        minimum_number_of_reviewers: Union[None, Unset, int]
        if isinstance(self.minimum_number_of_reviewers, Unset):
            minimum_number_of_reviewers = UNSET
        else:
            minimum_number_of_reviewers = self.minimum_number_of_reviewers

        minimal_average_scoring: Union[None, Unset, str]
        if isinstance(self.minimal_average_scoring, Unset):
            minimal_average_scoring = UNSET
        else:
            minimal_average_scoring = self.minimal_average_scoring

        custom_interval_months: Union[None, Unset, int]
        if isinstance(self.custom_interval_months, Unset):
            custom_interval_months = UNSET
        else:
            custom_interval_months = self.custom_interval_months

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start_time": start_time,
                "cadence": cadence,
                "submission_window_days": submission_window_days,
                "number_of_rounds": number_of_rounds,
            }
        )
        if review_strategy is not UNSET:
            field_dict["review_strategy"] = review_strategy
        if deciding_entity is not UNSET:
            field_dict["deciding_entity"] = deciding_entity
        if allocation_time is not UNSET:
            field_dict["allocation_time"] = allocation_time
        if review_duration_in_days is not UNSET:
            field_dict["review_duration_in_days"] = review_duration_in_days
        if minimum_number_of_reviewers is not UNSET:
            field_dict["minimum_number_of_reviewers"] = minimum_number_of_reviewers
        if minimal_average_scoring is not UNSET:
            field_dict["minimal_average_scoring"] = minimal_average_scoring
        if custom_interval_months is not UNSET:
            field_dict["custom_interval_months"] = custom_interval_months

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_time = isoparse(d.pop("start_time"))

        cadence = CadenceEnum(d.pop("cadence"))

        submission_window_days = d.pop("submission_window_days")

        number_of_rounds = d.pop("number_of_rounds")

        _review_strategy = d.pop("review_strategy", UNSET)
        review_strategy: Union[Unset, ReviewStrategyEnum]
        if isinstance(_review_strategy, Unset):
            review_strategy = UNSET
        else:
            review_strategy = ReviewStrategyEnum(_review_strategy)

        _deciding_entity = d.pop("deciding_entity", UNSET)
        deciding_entity: Union[Unset, DecidingEntityEnum]
        if isinstance(_deciding_entity, Unset):
            deciding_entity = UNSET
        else:
            deciding_entity = DecidingEntityEnum(_deciding_entity)

        _allocation_time = d.pop("allocation_time", UNSET)
        allocation_time: Union[Unset, AllocationTimeEnum]
        if isinstance(_allocation_time, Unset):
            allocation_time = UNSET
        else:
            allocation_time = AllocationTimeEnum(_allocation_time)

        def _parse_review_duration_in_days(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        review_duration_in_days = _parse_review_duration_in_days(d.pop("review_duration_in_days", UNSET))

        def _parse_minimum_number_of_reviewers(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        minimum_number_of_reviewers = _parse_minimum_number_of_reviewers(d.pop("minimum_number_of_reviewers", UNSET))

        def _parse_minimal_average_scoring(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        minimal_average_scoring = _parse_minimal_average_scoring(d.pop("minimal_average_scoring", UNSET))

        def _parse_custom_interval_months(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        custom_interval_months = _parse_custom_interval_months(d.pop("custom_interval_months", UNSET))

        bulk_round_create_request_request = cls(
            start_time=start_time,
            cadence=cadence,
            submission_window_days=submission_window_days,
            number_of_rounds=number_of_rounds,
            review_strategy=review_strategy,
            deciding_entity=deciding_entity,
            allocation_time=allocation_time,
            review_duration_in_days=review_duration_in_days,
            minimum_number_of_reviewers=minimum_number_of_reviewers,
            minimal_average_scoring=minimal_average_scoring,
            custom_interval_months=custom_interval_months,
        )

        bulk_round_create_request_request.additional_properties = d
        return bulk_round_create_request_request

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
