from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CallOfferingComponentBounds")


@_attrs_define
class CallOfferingComponentBounds:
    """
    Attributes:
        uuid (Union[Unset, UUID]):
        requested_offering_uuid (Union[Unset, UUID]):
        component_type (Union[Unset, str]): Type of the offering component: one billed by its limit that the call
            offering's plan prices.
        measured_unit (Union[Unset, str]):
        limit_period (Union[Unset, str]):
        min_per_proposal (Union[None, Unset, float]):
        max_per_proposal (Union[None, Unset, float]):
        default_amount (Union[None, Unset, float]):
        is_fixed (Union[Unset, bool]): Every proposal requests exactly default_amount; the applicant cannot change it.
    """

    uuid: Union[Unset, UUID] = UNSET
    requested_offering_uuid: Union[Unset, UUID] = UNSET
    component_type: Union[Unset, str] = UNSET
    measured_unit: Union[Unset, str] = UNSET
    limit_period: Union[Unset, str] = UNSET
    min_per_proposal: Union[None, Unset, float] = UNSET
    max_per_proposal: Union[None, Unset, float] = UNSET
    default_amount: Union[None, Unset, float] = UNSET
    is_fixed: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid: Union[Unset, str] = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        requested_offering_uuid: Union[Unset, str] = UNSET
        if not isinstance(self.requested_offering_uuid, Unset):
            requested_offering_uuid = str(self.requested_offering_uuid)

        component_type = self.component_type

        measured_unit = self.measured_unit

        limit_period = self.limit_period

        min_per_proposal: Union[None, Unset, float]
        if isinstance(self.min_per_proposal, Unset):
            min_per_proposal = UNSET
        else:
            min_per_proposal = self.min_per_proposal

        max_per_proposal: Union[None, Unset, float]
        if isinstance(self.max_per_proposal, Unset):
            max_per_proposal = UNSET
        else:
            max_per_proposal = self.max_per_proposal

        default_amount: Union[None, Unset, float]
        if isinstance(self.default_amount, Unset):
            default_amount = UNSET
        else:
            default_amount = self.default_amount

        is_fixed = self.is_fixed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if requested_offering_uuid is not UNSET:
            field_dict["requested_offering_uuid"] = requested_offering_uuid
        if component_type is not UNSET:
            field_dict["component_type"] = component_type
        if measured_unit is not UNSET:
            field_dict["measured_unit"] = measured_unit
        if limit_period is not UNSET:
            field_dict["limit_period"] = limit_period
        if min_per_proposal is not UNSET:
            field_dict["min_per_proposal"] = min_per_proposal
        if max_per_proposal is not UNSET:
            field_dict["max_per_proposal"] = max_per_proposal
        if default_amount is not UNSET:
            field_dict["default_amount"] = default_amount
        if is_fixed is not UNSET:
            field_dict["is_fixed"] = is_fixed

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

        _requested_offering_uuid = d.pop("requested_offering_uuid", UNSET)
        requested_offering_uuid: Union[Unset, UUID]
        if isinstance(_requested_offering_uuid, Unset):
            requested_offering_uuid = UNSET
        else:
            requested_offering_uuid = UUID(_requested_offering_uuid)

        component_type = d.pop("component_type", UNSET)

        measured_unit = d.pop("measured_unit", UNSET)

        limit_period = d.pop("limit_period", UNSET)

        def _parse_min_per_proposal(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        min_per_proposal = _parse_min_per_proposal(d.pop("min_per_proposal", UNSET))

        def _parse_max_per_proposal(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        max_per_proposal = _parse_max_per_proposal(d.pop("max_per_proposal", UNSET))

        def _parse_default_amount(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        default_amount = _parse_default_amount(d.pop("default_amount", UNSET))

        is_fixed = d.pop("is_fixed", UNSET)

        call_offering_component_bounds = cls(
            uuid=uuid,
            requested_offering_uuid=requested_offering_uuid,
            component_type=component_type,
            measured_unit=measured_unit,
            limit_period=limit_period,
            min_per_proposal=min_per_proposal,
            max_per_proposal=max_per_proposal,
            default_amount=default_amount,
            is_fixed=is_fixed,
        )

        call_offering_component_bounds.additional_properties = d
        return call_offering_component_bounds

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
