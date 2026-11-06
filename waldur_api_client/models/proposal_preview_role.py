from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProposalPreviewRole")


@_attrs_define
class ProposalPreviewRole:
    """
    Attributes:
        role (str): An actor key of the call's workflow.
        offering (Union[None, int]): For an offering's team: the index of its requested offering.
        label (str):
    """

    role: str
    offering: Union[None, int]
    label: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role = self.role

        offering: Union[None, int]
        offering = self.offering

        label = self.label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
                "offering": offering,
                "label": label,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        role = d.pop("role")

        def _parse_offering(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        offering = _parse_offering(d.pop("offering"))

        label = d.pop("label")

        proposal_preview_role = cls(
            role=role,
            offering=offering,
            label=label,
        )

        proposal_preview_role.additional_properties = d
        return proposal_preview_role

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
