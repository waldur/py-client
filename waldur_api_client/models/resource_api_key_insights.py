import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.chart_spec import ChartSpec


T = TypeVar("T", bound="ResourceApiKeyInsights")


@_attrs_define
class ResourceApiKeyInsights:
    """
    Attributes:
        days (int):
        spent_this_month (str):
        daily_pace (str): Average spend per day over the last 7 days.
        forecast_this_month (str): This month's spend if the recent pace holds to its end.
        month_limit (Union[None, str]): The resource's own month limit as money; with resource_uuid only.
        runs_out (Union[None, datetime.date]): When the month limit is reached at the recent pace, if this month.
        active_keys (int):
        paused_keys (int):
        charts (list['ChartSpec']):
    """

    days: int
    spent_this_month: str
    daily_pace: str
    forecast_this_month: str
    month_limit: Union[None, str]
    runs_out: Union[None, datetime.date]
    active_keys: int
    paused_keys: int
    charts: list["ChartSpec"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        days = self.days

        spent_this_month = self.spent_this_month

        daily_pace = self.daily_pace

        forecast_this_month = self.forecast_this_month

        month_limit: Union[None, str]
        month_limit = self.month_limit

        runs_out: Union[None, str]
        if isinstance(self.runs_out, datetime.date):
            runs_out = self.runs_out.isoformat()
        else:
            runs_out = self.runs_out

        active_keys = self.active_keys

        paused_keys = self.paused_keys

        charts = []
        for charts_item_data in self.charts:
            charts_item = charts_item_data.to_dict()
            charts.append(charts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "days": days,
                "spent_this_month": spent_this_month,
                "daily_pace": daily_pace,
                "forecast_this_month": forecast_this_month,
                "month_limit": month_limit,
                "runs_out": runs_out,
                "active_keys": active_keys,
                "paused_keys": paused_keys,
                "charts": charts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chart_spec import ChartSpec

        d = dict(src_dict)
        days = d.pop("days")

        spent_this_month = d.pop("spent_this_month")

        daily_pace = d.pop("daily_pace")

        forecast_this_month = d.pop("forecast_this_month")

        def _parse_month_limit(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        month_limit = _parse_month_limit(d.pop("month_limit"))

        def _parse_runs_out(data: object) -> Union[None, datetime.date]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                runs_out_type_0 = isoparse(data).date()

                return runs_out_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.date], data)

        runs_out = _parse_runs_out(d.pop("runs_out"))

        active_keys = d.pop("active_keys")

        paused_keys = d.pop("paused_keys")

        charts = []
        _charts = d.pop("charts")
        for charts_item_data in _charts:
            charts_item = ChartSpec.from_dict(charts_item_data)

            charts.append(charts_item)

        resource_api_key_insights = cls(
            days=days,
            spent_this_month=spent_this_month,
            daily_pace=daily_pace,
            forecast_this_month=forecast_this_month,
            month_limit=month_limit,
            runs_out=runs_out,
            active_keys=active_keys,
            paused_keys=paused_keys,
            charts=charts,
        )

        resource_api_key_insights.additional_properties = d
        return resource_api_key_insights

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
