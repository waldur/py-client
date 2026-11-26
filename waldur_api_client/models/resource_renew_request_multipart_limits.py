from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ResourceRenewRequestMultipartLimits")


@_attrs_define
class ResourceRenewRequestMultipartLimits:
    """Optional new limits for the resource; components left out keep their current limits. A raised prepaid limit is also
    charged for the rest of the current term. A renewal that only lowers limits gets no credit; if the offering's
    renewal_limit_decrease_policy is stretch_paid_term, the value already paid for the rest of the term is spread over
    the lower limits and the extension starts when it runs out.

    """

    additional_properties: dict[str, float] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resource_renew_request_multipart_limits = cls()

        resource_renew_request_multipart_limits.additional_properties = d
        return resource_renew_request_multipart_limits

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> float:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: float) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
