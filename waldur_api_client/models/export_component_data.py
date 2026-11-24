from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.export_component_data_spending_limit_periods import ExportComponentDataSpendingLimitPeriods


T = TypeVar("T", bound="ExportComponentData")


@_attrs_define
class ExportComponentData:
    """
    Attributes:
        type_ (str):
        name (str):
        description (str):
        billing_type (str):
        measured_unit (str):
        unit_factor (Union[None, float]):
        limit_period (Union[None, str]):
        limit_amount (Union[None, int]):
        limit_increase_only (bool):
        article_code (str):
        backend_id (str):
        min_value (Union[None, Unset, float]):
        max_value (Union[None, Unset, float]):
        max_available_limit (Union[None, Unset, float]):
        default_limit (Union[None, Unset, float]):
        spending_limit_periods (Union[Unset, ExportComponentDataSpendingLimitPeriods]): Periods customers can set
            spending limits for, each with an optional default and maximum.
    """

    type_: str
    name: str
    description: str
    billing_type: str
    measured_unit: str
    unit_factor: Union[None, float]
    limit_period: Union[None, str]
    limit_amount: Union[None, int]
    limit_increase_only: bool
    article_code: str
    backend_id: str
    min_value: Union[None, Unset, float] = UNSET
    max_value: Union[None, Unset, float] = UNSET
    max_available_limit: Union[None, Unset, float] = UNSET
    default_limit: Union[None, Unset, float] = UNSET
    spending_limit_periods: Union[Unset, "ExportComponentDataSpendingLimitPeriods"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        name = self.name

        description = self.description

        billing_type = self.billing_type

        measured_unit = self.measured_unit

        unit_factor: Union[None, float]
        unit_factor = self.unit_factor

        limit_period: Union[None, str]
        limit_period = self.limit_period

        limit_amount: Union[None, int]
        limit_amount = self.limit_amount

        limit_increase_only = self.limit_increase_only

        article_code = self.article_code

        backend_id = self.backend_id

        min_value: Union[None, Unset, float]
        if isinstance(self.min_value, Unset):
            min_value = UNSET
        else:
            min_value = self.min_value

        max_value: Union[None, Unset, float]
        if isinstance(self.max_value, Unset):
            max_value = UNSET
        else:
            max_value = self.max_value

        max_available_limit: Union[None, Unset, float]
        if isinstance(self.max_available_limit, Unset):
            max_available_limit = UNSET
        else:
            max_available_limit = self.max_available_limit

        default_limit: Union[None, Unset, float]
        if isinstance(self.default_limit, Unset):
            default_limit = UNSET
        else:
            default_limit = self.default_limit

        spending_limit_periods: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.spending_limit_periods, Unset):
            spending_limit_periods = self.spending_limit_periods.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "name": name,
                "description": description,
                "billing_type": billing_type,
                "measured_unit": measured_unit,
                "unit_factor": unit_factor,
                "limit_period": limit_period,
                "limit_amount": limit_amount,
                "limit_increase_only": limit_increase_only,
                "article_code": article_code,
                "backend_id": backend_id,
            }
        )
        if min_value is not UNSET:
            field_dict["min_value"] = min_value
        if max_value is not UNSET:
            field_dict["max_value"] = max_value
        if max_available_limit is not UNSET:
            field_dict["max_available_limit"] = max_available_limit
        if default_limit is not UNSET:
            field_dict["default_limit"] = default_limit
        if spending_limit_periods is not UNSET:
            field_dict["spending_limit_periods"] = spending_limit_periods

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.export_component_data_spending_limit_periods import ExportComponentDataSpendingLimitPeriods

        d = dict(src_dict)
        type_ = d.pop("type")

        name = d.pop("name")

        description = d.pop("description")

        billing_type = d.pop("billing_type")

        measured_unit = d.pop("measured_unit")

        def _parse_unit_factor(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        unit_factor = _parse_unit_factor(d.pop("unit_factor"))

        def _parse_limit_period(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        limit_period = _parse_limit_period(d.pop("limit_period"))

        def _parse_limit_amount(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        limit_amount = _parse_limit_amount(d.pop("limit_amount"))

        limit_increase_only = d.pop("limit_increase_only")

        article_code = d.pop("article_code")

        backend_id = d.pop("backend_id")

        def _parse_min_value(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        min_value = _parse_min_value(d.pop("min_value", UNSET))

        def _parse_max_value(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        max_value = _parse_max_value(d.pop("max_value", UNSET))

        def _parse_max_available_limit(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        max_available_limit = _parse_max_available_limit(d.pop("max_available_limit", UNSET))

        def _parse_default_limit(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        default_limit = _parse_default_limit(d.pop("default_limit", UNSET))

        _spending_limit_periods = d.pop("spending_limit_periods", UNSET)
        spending_limit_periods: Union[Unset, ExportComponentDataSpendingLimitPeriods]
        if isinstance(_spending_limit_periods, Unset):
            spending_limit_periods = UNSET
        else:
            spending_limit_periods = ExportComponentDataSpendingLimitPeriods.from_dict(_spending_limit_periods)

        export_component_data = cls(
            type_=type_,
            name=name,
            description=description,
            billing_type=billing_type,
            measured_unit=measured_unit,
            unit_factor=unit_factor,
            limit_period=limit_period,
            limit_amount=limit_amount,
            limit_increase_only=limit_increase_only,
            article_code=article_code,
            backend_id=backend_id,
            min_value=min_value,
            max_value=max_value,
            max_available_limit=max_available_limit,
            default_limit=default_limit,
            spending_limit_periods=spending_limit_periods,
        )

        export_component_data.additional_properties = d
        return export_component_data

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
