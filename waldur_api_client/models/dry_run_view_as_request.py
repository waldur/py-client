from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DryRunViewAsRequest")


@_attrs_define
class DryRunViewAsRequest:
    """
    Attributes:
        role (str): An actor key of the call's workflow description, never a user: applicant, reviewer, offering_team,
            proposal_role:<key>, ...
        offering (Union[None, Unset, int]): For an offering team: the index of the requested offering.
        at (Union[None, Unset, int]): Preview after this many actions; all of them by default.
    """

    role: str
    offering: Union[None, Unset, int] = UNSET
    at: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role = self.role

        offering: Union[None, Unset, int]
        if isinstance(self.offering, Unset):
            offering = UNSET
        else:
            offering = self.offering

        at: Union[None, Unset, int]
        if isinstance(self.at, Unset):
            at = UNSET
        else:
            at = self.at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
            }
        )
        if offering is not UNSET:
            field_dict["offering"] = offering
        if at is not UNSET:
            field_dict["at"] = at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        role = d.pop("role")

        def _parse_offering(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        offering = _parse_offering(d.pop("offering", UNSET))

        def _parse_at(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        at = _parse_at(d.pop("at", UNSET))

        dry_run_view_as_request = cls(
            role=role,
            offering=offering,
            at=at,
        )

        dry_run_view_as_request.additional_properties = d
        return dry_run_view_as_request

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
