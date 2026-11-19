import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="RemoteProjectReportWindow")


@_attrs_define
class RemoteProjectReportWindow:
    """
    Attributes:
        project_uuid (Union[None, UUID]): Null if the project was deleted or the caller cannot see it.
        project_name (Union[None, str]): Null if the project was deleted or the caller cannot see it.
        start (Union[None, datetime.date]): Null if when the award arrived was not recorded.
        end (Union[None, datetime.date]): Inclusive. Null while still attached.
    """

    project_uuid: Union[None, UUID]
    project_name: Union[None, str]
    start: Union[None, datetime.date]
    end: Union[None, datetime.date]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_uuid: Union[None, str]
        if isinstance(self.project_uuid, UUID):
            project_uuid = str(self.project_uuid)
        else:
            project_uuid = self.project_uuid

        project_name: Union[None, str]
        project_name = self.project_name

        start: Union[None, str]
        if isinstance(self.start, datetime.date):
            start = self.start.isoformat()
        else:
            start = self.start

        end: Union[None, str]
        if isinstance(self.end, datetime.date):
            end = self.end.isoformat()
        else:
            end = self.end

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_uuid": project_uuid,
                "project_name": project_name,
                "start": start,
                "end": end,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_project_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                project_uuid_type_0 = UUID(data)

                return project_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        project_uuid = _parse_project_uuid(d.pop("project_uuid"))

        def _parse_project_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        project_name = _parse_project_name(d.pop("project_name"))

        def _parse_start(data: object) -> Union[None, datetime.date]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_type_0 = isoparse(data).date()

                return start_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.date], data)

        start = _parse_start(d.pop("start"))

        def _parse_end(data: object) -> Union[None, datetime.date]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_type_0 = isoparse(data).date()

                return end_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.date], data)

        end = _parse_end(d.pop("end"))

        remote_project_report_window = cls(
            project_uuid=project_uuid,
            project_name=project_name,
            start=start,
            end=end,
        )

        remote_project_report_window.additional_properties = d
        return remote_project_report_window

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
