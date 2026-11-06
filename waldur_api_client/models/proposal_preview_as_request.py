from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProposalPreviewAsRequest")


@_attrs_define
class ProposalPreviewAsRequest:
    """
    Attributes:
        role (str): One of the proposal's preview-roles: an actor key, never a user.
        offering (Union[None, Unset, int]): For an offering's team: the index of its requested offering.
    """

    role: str
    offering: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role = self.role

        offering: Union[None, Unset, int]
        if isinstance(self.offering, Unset):
            offering = UNSET
        else:
            offering = self.offering

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
            }
        )
        if offering is not UNSET:
            field_dict["offering"] = offering

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

        proposal_preview_as_request = cls(
            role=role,
            offering=offering,
        )

        proposal_preview_as_request.additional_properties = d
        return proposal_preview_as_request

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
