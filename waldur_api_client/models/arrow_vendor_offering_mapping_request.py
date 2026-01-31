from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArrowVendorOfferingMappingRequest")


@_attrs_define
class ArrowVendorOfferingMappingRequest:
    """
    Attributes:
        settings (str):
        arrow_vendor_name (str): Arrow vendor name (e.g., 'Microsoft', 'Amazon Web Services')
        offering (str): Waldur marketplace offering for this vendor
        is_active (Union[Unset, bool]): Whether this mapping is active
    """

    settings: str
    arrow_vendor_name: str
    offering: str
    is_active: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        settings = self.settings

        arrow_vendor_name = self.arrow_vendor_name

        offering = self.offering

        is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "settings": settings,
                "arrow_vendor_name": arrow_vendor_name,
                "offering": offering,
            }
        )
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        settings = d.pop("settings")

        arrow_vendor_name = d.pop("arrow_vendor_name")

        offering = d.pop("offering")

        is_active = d.pop("is_active", UNSET)

        arrow_vendor_offering_mapping_request = cls(
            settings=settings,
            arrow_vendor_name=arrow_vendor_name,
            offering=offering,
            is_active=is_active,
        )

        arrow_vendor_offering_mapping_request.additional_properties = d
        return arrow_vendor_offering_mapping_request

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
