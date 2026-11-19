import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.project_usage_report import ProjectUsageReport
    from ..models.remote_project_report_window import RemoteProjectReportWindow


T = TypeVar("T", bound="RemoteProjectUsageReport")


@_attrs_define
class RemoteProjectUsageReport:
    """
    Attributes:
        start (Union[None, datetime.date]):
        end (datetime.date):
        total_hours (float):
        report (Union['ProjectUsageReport', None]): The combined OpenPortal ProjectUsageReport. Null if the award has no
            identifier and no attachment to report under.
        windows (list['RemoteProjectReportWindow']):
    """

    start: Union[None, datetime.date]
    end: datetime.date
    total_hours: float
    report: Union["ProjectUsageReport", None]
    windows: list["RemoteProjectReportWindow"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.project_usage_report import ProjectUsageReport

        start: Union[None, str]
        if isinstance(self.start, datetime.date):
            start = self.start.isoformat()
        else:
            start = self.start

        end = self.end.isoformat()

        total_hours = self.total_hours

        report: Union[None, dict[str, Any]]
        if isinstance(self.report, ProjectUsageReport):
            report = self.report.to_dict()
        else:
            report = self.report

        windows = []
        for windows_item_data in self.windows:
            windows_item = windows_item_data.to_dict()
            windows.append(windows_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start": start,
                "end": end,
                "total_hours": total_hours,
                "report": report,
                "windows": windows,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_usage_report import ProjectUsageReport
        from ..models.remote_project_report_window import RemoteProjectReportWindow

        d = dict(src_dict)

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

        end = isoparse(d.pop("end")).date()

        total_hours = d.pop("total_hours")

        def _parse_report(data: object) -> Union["ProjectUsageReport", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                report_type_1 = ProjectUsageReport.from_dict(data)

                return report_type_1
            except:  # noqa: E722
                pass
            return cast(Union["ProjectUsageReport", None], data)

        report = _parse_report(d.pop("report"))

        windows = []
        _windows = d.pop("windows")
        for windows_item_data in _windows:
            windows_item = RemoteProjectReportWindow.from_dict(windows_item_data)

            windows.append(windows_item)

        remote_project_usage_report = cls(
            start=start,
            end=end,
            total_hours=total_hours,
            report=report,
            windows=windows,
        )

        remote_project_usage_report.additional_properties = d
        return remote_project_usage_report

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
