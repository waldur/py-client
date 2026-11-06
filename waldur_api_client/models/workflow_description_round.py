import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowDescriptionRound")


@_attrs_define
class WorkflowDescriptionRound:
    """
    Attributes:
        start_time (Union[None, datetime.datetime]):
        cutoff_time (Union[None, datetime.datetime]):
        allocation_date (Union[None, datetime.datetime]):
        open_ended (bool):
        review_duration_in_days (Union[None, int]):
        time_to_decision_days (Union[None, int]):
        time_to_decision_source (Union[None, str]):
        uuid (Union[None, Unset, str]): The call's round; calls only.
        name (Union[None, Unset, str]):
    """

    start_time: Union[None, datetime.datetime]
    cutoff_time: Union[None, datetime.datetime]
    allocation_date: Union[None, datetime.datetime]
    open_ended: bool
    review_duration_in_days: Union[None, int]
    time_to_decision_days: Union[None, int]
    time_to_decision_source: Union[None, str]
    uuid: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_time: Union[None, str]
        if isinstance(self.start_time, datetime.datetime):
            start_time = self.start_time.isoformat()
        else:
            start_time = self.start_time

        cutoff_time: Union[None, str]
        if isinstance(self.cutoff_time, datetime.datetime):
            cutoff_time = self.cutoff_time.isoformat()
        else:
            cutoff_time = self.cutoff_time

        allocation_date: Union[None, str]
        if isinstance(self.allocation_date, datetime.datetime):
            allocation_date = self.allocation_date.isoformat()
        else:
            allocation_date = self.allocation_date

        open_ended = self.open_ended

        review_duration_in_days: Union[None, int]
        review_duration_in_days = self.review_duration_in_days

        time_to_decision_days: Union[None, int]
        time_to_decision_days = self.time_to_decision_days

        time_to_decision_source: Union[None, str]
        time_to_decision_source = self.time_to_decision_source

        uuid: Union[None, Unset, str]
        if isinstance(self.uuid, Unset):
            uuid = UNSET
        else:
            uuid = self.uuid

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start_time": start_time,
                "cutoff_time": cutoff_time,
                "allocation_date": allocation_date,
                "open_ended": open_ended,
                "review_duration_in_days": review_duration_in_days,
                "time_to_decision_days": time_to_decision_days,
                "time_to_decision_source": time_to_decision_source,
            }
        )
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_start_time(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_time_type_0 = isoparse(data)

                return start_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        start_time = _parse_start_time(d.pop("start_time"))

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

        open_ended = d.pop("open_ended")

        def _parse_review_duration_in_days(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        review_duration_in_days = _parse_review_duration_in_days(d.pop("review_duration_in_days"))

        def _parse_time_to_decision_days(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        time_to_decision_days = _parse_time_to_decision_days(d.pop("time_to_decision_days"))

        def _parse_time_to_decision_source(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        time_to_decision_source = _parse_time_to_decision_source(d.pop("time_to_decision_source"))

        def _parse_uuid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        uuid = _parse_uuid(d.pop("uuid", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        workflow_description_round = cls(
            start_time=start_time,
            cutoff_time=cutoff_time,
            allocation_date=allocation_date,
            open_ended=open_ended,
            review_duration_in_days=review_duration_in_days,
            time_to_decision_days=time_to_decision_days,
            time_to_decision_source=time_to_decision_source,
            uuid=uuid,
            name=name,
        )

        workflow_description_round.additional_properties = d
        return workflow_description_round

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
