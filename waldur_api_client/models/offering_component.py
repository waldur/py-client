from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.billing_type_enum import BillingTypeEnum
from ..models.blank_enum import BlankEnum
from ..models.limit_period_enum import LimitPeriodEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="OfferingComponent")


@_attrs_define
class OfferingComponent:
    """
    Attributes:
        uuid (Union[Unset, UUID]):
        billing_type (Union[Unset, BillingTypeEnum]):
        type_ (Union[Unset, str]): Unique internal name of the measured unit, for example floating_ip.
        name (Union[Unset, str]): Display name for the measured unit, for example, Floating IP.
        description (Union[Unset, str]):
        measured_unit (Union[Unset, str]): Unit of measurement, for example, GB.
        unit_factor (Union[Unset, int]): The conversion factor from backend units to measured_unit
        limit_period (Union[BlankEnum, LimitPeriodEnum, None, Unset]):
        limit_amount (Union[None, Unset, int]):
        article_code (Union[Unset, str]):
        max_value (Union[None, Unset, int]):
        min_value (Union[None, Unset, int]):
        max_available_limit (Union[None, Unset, int]):
        is_boolean (Union[Unset, bool]):
        default_limit (Union[None, Unset, int]):
        factor (Union[Unset, int]):
        is_builtin (Union[Unset, bool]):
    """

    uuid: Union[Unset, UUID] = UNSET
    billing_type: Union[Unset, BillingTypeEnum] = UNSET
    type_: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    measured_unit: Union[Unset, str] = UNSET
    unit_factor: Union[Unset, int] = UNSET
    limit_period: Union[BlankEnum, LimitPeriodEnum, None, Unset] = UNSET
    limit_amount: Union[None, Unset, int] = UNSET
    article_code: Union[Unset, str] = UNSET
    max_value: Union[None, Unset, int] = UNSET
    min_value: Union[None, Unset, int] = UNSET
    max_available_limit: Union[None, Unset, int] = UNSET
    is_boolean: Union[Unset, bool] = UNSET
    default_limit: Union[None, Unset, int] = UNSET
    factor: Union[Unset, int] = UNSET
    is_builtin: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid: Union[Unset, str] = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        billing_type: Union[Unset, str] = UNSET
        if not isinstance(self.billing_type, Unset):
            billing_type = self.billing_type.value

        type_ = self.type_

        name = self.name

        description = self.description

        measured_unit = self.measured_unit

        unit_factor = self.unit_factor

        limit_period: Union[None, Unset, str]
        if isinstance(self.limit_period, Unset):
            limit_period = UNSET
        elif isinstance(self.limit_period, LimitPeriodEnum):
            limit_period = self.limit_period.value
        elif isinstance(self.limit_period, BlankEnum):
            limit_period = self.limit_period.value
        else:
            limit_period = self.limit_period

        limit_amount: Union[None, Unset, int]
        if isinstance(self.limit_amount, Unset):
            limit_amount = UNSET
        else:
            limit_amount = self.limit_amount

        article_code = self.article_code

        max_value: Union[None, Unset, int]
        if isinstance(self.max_value, Unset):
            max_value = UNSET
        else:
            max_value = self.max_value

        min_value: Union[None, Unset, int]
        if isinstance(self.min_value, Unset):
            min_value = UNSET
        else:
            min_value = self.min_value

        max_available_limit: Union[None, Unset, int]
        if isinstance(self.max_available_limit, Unset):
            max_available_limit = UNSET
        else:
            max_available_limit = self.max_available_limit

        is_boolean = self.is_boolean

        default_limit: Union[None, Unset, int]
        if isinstance(self.default_limit, Unset):
            default_limit = UNSET
        else:
            default_limit = self.default_limit

        factor = self.factor

        is_builtin = self.is_builtin

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if billing_type is not UNSET:
            field_dict["billing_type"] = billing_type
        if type_ is not UNSET:
            field_dict["type"] = type_
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if measured_unit is not UNSET:
            field_dict["measured_unit"] = measured_unit
        if unit_factor is not UNSET:
            field_dict["unit_factor"] = unit_factor
        if limit_period is not UNSET:
            field_dict["limit_period"] = limit_period
        if limit_amount is not UNSET:
            field_dict["limit_amount"] = limit_amount
        if article_code is not UNSET:
            field_dict["article_code"] = article_code
        if max_value is not UNSET:
            field_dict["max_value"] = max_value
        if min_value is not UNSET:
            field_dict["min_value"] = min_value
        if max_available_limit is not UNSET:
            field_dict["max_available_limit"] = max_available_limit
        if is_boolean is not UNSET:
            field_dict["is_boolean"] = is_boolean
        if default_limit is not UNSET:
            field_dict["default_limit"] = default_limit
        if factor is not UNSET:
            field_dict["factor"] = factor
        if is_builtin is not UNSET:
            field_dict["is_builtin"] = is_builtin

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _uuid = d.pop("uuid", UNSET)
        uuid: Union[Unset, UUID]
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        _billing_type = d.pop("billing_type", UNSET)
        billing_type: Union[Unset, BillingTypeEnum]
        if isinstance(_billing_type, Unset):
            billing_type = UNSET
        else:
            billing_type = BillingTypeEnum(_billing_type)

        type_ = d.pop("type", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        measured_unit = d.pop("measured_unit", UNSET)

        unit_factor = d.pop("unit_factor", UNSET)

        def _parse_limit_period(data: object) -> Union[BlankEnum, LimitPeriodEnum, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                limit_period_type_0 = LimitPeriodEnum(data)

                return limit_period_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                limit_period_type_1 = BlankEnum(data)

                return limit_period_type_1
            except:  # noqa: E722
                pass
            return cast(Union[BlankEnum, LimitPeriodEnum, None, Unset], data)

        limit_period = _parse_limit_period(d.pop("limit_period", UNSET))

        def _parse_limit_amount(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        limit_amount = _parse_limit_amount(d.pop("limit_amount", UNSET))

        article_code = d.pop("article_code", UNSET)

        def _parse_max_value(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_value = _parse_max_value(d.pop("max_value", UNSET))

        def _parse_min_value(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        min_value = _parse_min_value(d.pop("min_value", UNSET))

        def _parse_max_available_limit(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_available_limit = _parse_max_available_limit(d.pop("max_available_limit", UNSET))

        is_boolean = d.pop("is_boolean", UNSET)

        def _parse_default_limit(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        default_limit = _parse_default_limit(d.pop("default_limit", UNSET))

        factor = d.pop("factor", UNSET)

        is_builtin = d.pop("is_builtin", UNSET)

        offering_component = cls(
            uuid=uuid,
            billing_type=billing_type,
            type_=type_,
            name=name,
            description=description,
            measured_unit=measured_unit,
            unit_factor=unit_factor,
            limit_period=limit_period,
            limit_amount=limit_amount,
            article_code=article_code,
            max_value=max_value,
            min_value=min_value,
            max_available_limit=max_available_limit,
            is_boolean=is_boolean,
            default_limit=default_limit,
            factor=factor,
            is_builtin=is_builtin,
        )

        offering_component.additional_properties = d
        return offering_component

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
