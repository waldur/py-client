import datetime
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CategoryComponentUsage")


@_attrs_define
class CategoryComponentUsage:
    """
    Attributes:
        name (str): Display name for the measured unit, for example, Floating IP.
        type_ (str): Unique internal name of the measured unit, for example floating_ip.
        measured_unit (str): Unit of measurement, for example, GB.
        category_title (str):
        category_uuid (UUID):
        date (datetime.date):
        scope (str):
        reported_usage (Union[None, Unset, int]):
        fixed_usage (Union[None, Unset, int]):
    """

    name: str
    type_: str
    measured_unit: str
    category_title: str
    category_uuid: UUID
    date: datetime.date
    scope: str
    reported_usage: Union[None, Unset, int] = UNSET
    fixed_usage: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_

        measured_unit = self.measured_unit

        category_title = self.category_title

        category_uuid = str(self.category_uuid)

        date = self.date.isoformat()

        scope = self.scope

        reported_usage: Union[None, Unset, int]
        if isinstance(self.reported_usage, Unset):
            reported_usage = UNSET
        else:
            reported_usage = self.reported_usage

        fixed_usage: Union[None, Unset, int]
        if isinstance(self.fixed_usage, Unset):
            fixed_usage = UNSET
        else:
            fixed_usage = self.fixed_usage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
                "measured_unit": measured_unit,
                "category_title": category_title,
                "category_uuid": category_uuid,
                "date": date,
                "scope": scope,
            }
        )
        if reported_usage is not UNSET:
            field_dict["reported_usage"] = reported_usage
        if fixed_usage is not UNSET:
            field_dict["fixed_usage"] = fixed_usage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        type_ = d.pop("type")

        measured_unit = d.pop("measured_unit")

        category_title = d.pop("category_title")

        category_uuid = UUID(d.pop("category_uuid"))

        date = isoparse(d.pop("date")).date()

        scope = d.pop("scope")

        def _parse_reported_usage(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        reported_usage = _parse_reported_usage(d.pop("reported_usage", UNSET))

        def _parse_fixed_usage(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        fixed_usage = _parse_fixed_usage(d.pop("fixed_usage", UNSET))

        category_component_usage = cls(
            name=name,
            type_=type_,
            measured_unit=measured_unit,
            category_title=category_title,
            category_uuid=category_uuid,
            date=date,
            scope=scope,
            reported_usage=reported_usage,
            fixed_usage=fixed_usage,
        )

        category_component_usage.additional_properties = d
        return category_component_usage

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
