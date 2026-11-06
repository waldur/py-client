import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="WorkflowProgressRound")


@_attrs_define
class WorkflowProgressRound:
    """
    Attributes:
        uuid (str):
        name (str):
        start_time (Union[None, datetime.datetime]):
        cutoff_time (Union[None, datetime.datetime]):
        allocation_date (Union[None, datetime.datetime]):
    """

    uuid: str
    name: str
    start_time: Union[None, datetime.datetime]
    cutoff_time: Union[None, datetime.datetime]
    allocation_date: Union[None, datetime.datetime]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = self.uuid

        name = self.name

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "name": name,
                "start_time": start_time,
                "cutoff_time": cutoff_time,
                "allocation_date": allocation_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = d.pop("uuid")

        name = d.pop("name")

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

        workflow_progress_round = cls(
            uuid=uuid,
            name=name,
            start_time=start_time,
            cutoff_time=cutoff_time,
            allocation_date=allocation_date,
        )

        workflow_progress_round.additional_properties = d
        return workflow_progress_round

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
