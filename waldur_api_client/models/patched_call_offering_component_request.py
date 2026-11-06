from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedCallOfferingComponentRequest")


@_attrs_define
class PatchedCallOfferingComponentRequest:
    """
    Attributes:
        requested_offering_uuid (Union[Unset, UUID]): An offering of the call.
        component_type (Union[Unset, str]): Type of the offering component: one billed by its limit that the call
            offering's plan prices.
        min_per_proposal (Union[None, Unset, float]):
        max_per_proposal (Union[None, Unset, float]):
        default_amount (Union[None, Unset, float]):
        is_fixed (Union[Unset, bool]): Every proposal requests exactly default_amount; the applicant cannot change it.
    """

    requested_offering_uuid: Union[Unset, UUID] = UNSET
    component_type: Union[Unset, str] = UNSET
    min_per_proposal: Union[None, Unset, float] = UNSET
    max_per_proposal: Union[None, Unset, float] = UNSET
    default_amount: Union[None, Unset, float] = UNSET
    is_fixed: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        requested_offering_uuid: Union[Unset, str] = UNSET
        if not isinstance(self.requested_offering_uuid, Unset):
            requested_offering_uuid = str(self.requested_offering_uuid)

        component_type = self.component_type

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
        if requested_offering_uuid is not UNSET:
            field_dict["requested_offering_uuid"] = requested_offering_uuid
        if component_type is not UNSET:
            field_dict["component_type"] = component_type
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
        _requested_offering_uuid = d.pop("requested_offering_uuid", UNSET)
        requested_offering_uuid: Union[Unset, UUID]
        if isinstance(_requested_offering_uuid, Unset):
            requested_offering_uuid = UNSET
        else:
            requested_offering_uuid = UUID(_requested_offering_uuid)

        component_type = d.pop("component_type", UNSET)

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

        patched_call_offering_component_request = cls(
            requested_offering_uuid=requested_offering_uuid,
            component_type=component_type,
            min_per_proposal=min_per_proposal,
            max_per_proposal=max_per_proposal,
            default_amount=default_amount,
            is_fixed=is_fixed,
        )

        patched_call_offering_component_request.additional_properties = d
        return patched_call_offering_component_request

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
