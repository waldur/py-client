import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.project_storage_report import ProjectStorageReport
    from ..models.remote_project_report_window import RemoteProjectReportWindow


T = TypeVar("T", bound="RemoteProjectStorageReport")


@_attrs_define
class RemoteProjectStorageReport:
    """
    Attributes:
        start (Union[None, datetime.date]):
        end (datetime.date):
        latest (Union[None, datetime.datetime]): When the latest snapshot in range was taken. Null if none was.
        report (Union['ProjectStorageReport', None]): The combined OpenPortal ProjectStorageReport. Its top level is the
            latest snapshot in range; daily_reports holds the others. Null if the award has no identifier and no attachment
            to report under.
        windows (list['RemoteProjectReportWindow']):
    """

    start: Union[None, datetime.date]
    end: datetime.date
    latest: Union[None, datetime.datetime]
    report: Union["ProjectStorageReport", None]
    windows: list["RemoteProjectReportWindow"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.project_storage_report import ProjectStorageReport

        start: Union[None, str]
        if isinstance(self.start, datetime.date):
            start = self.start.isoformat()
        else:
            start = self.start

        end = self.end.isoformat()

        latest: Union[None, str]
        if isinstance(self.latest, datetime.datetime):
            latest = self.latest.isoformat()
        else:
            latest = self.latest

        report: Union[None, dict[str, Any]]
        if isinstance(self.report, ProjectStorageReport):
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
                "latest": latest,
                "report": report,
                "windows": windows,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_storage_report import ProjectStorageReport
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

        def _parse_latest(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                latest_type_0 = isoparse(data)

                return latest_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        latest = _parse_latest(d.pop("latest"))

        def _parse_report(data: object) -> Union["ProjectStorageReport", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                report_type_1 = ProjectStorageReport.from_dict(data)

                return report_type_1
            except:  # noqa: E722
                pass
            return cast(Union["ProjectStorageReport", None], data)

        report = _parse_report(d.pop("report"))

        windows = []
        _windows = d.pop("windows")
        for windows_item_data in _windows:
            windows_item = RemoteProjectReportWindow.from_dict(windows_item_data)

            windows.append(windows_item)

        remote_project_storage_report = cls(
            start=start,
            end=end,
            latest=latest,
            report=report,
            windows=windows,
        )

        remote_project_storage_report.additional_properties = d
        return remote_project_storage_report

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
