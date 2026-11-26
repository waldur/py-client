from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cidr_ip_version_enum import CidrIpVersionEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="CidrPolicyRequest")


@_attrs_define
class CidrPolicyRequest:
    """
    Attributes:
        ip_version (Union[Unset, CidrIpVersionEnum]):
        prefix_length_min (Union[Unset, int]): The smallest prefix length allowed, that is the largest network.
        prefix_length_max (Union[Unset, int]): The largest prefix length allowed, that is the smallest network.
        allowed_ranges (Union[Unset, list[str]]): Networks the value must lie inside one of, such as the private ranges
            10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 and fc00::/7. Any network when empty.
        excluded_ranges (Union[Unset, list[str]]): Networks the value must not overlap.
        max_items (Union[Unset, int]): For a list: the most networks it may hold.
    """

    ip_version: Union[Unset, CidrIpVersionEnum] = UNSET
    prefix_length_min: Union[Unset, int] = UNSET
    prefix_length_max: Union[Unset, int] = UNSET
    allowed_ranges: Union[Unset, list[str]] = UNSET
    excluded_ranges: Union[Unset, list[str]] = UNSET
    max_items: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ip_version: Union[Unset, str] = UNSET
        if not isinstance(self.ip_version, Unset):
            ip_version = self.ip_version.value

        prefix_length_min = self.prefix_length_min

        prefix_length_max = self.prefix_length_max

        allowed_ranges: Union[Unset, list[str]] = UNSET
        if not isinstance(self.allowed_ranges, Unset):
            allowed_ranges = self.allowed_ranges

        excluded_ranges: Union[Unset, list[str]] = UNSET
        if not isinstance(self.excluded_ranges, Unset):
            excluded_ranges = self.excluded_ranges

        max_items = self.max_items

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ip_version is not UNSET:
            field_dict["ip_version"] = ip_version
        if prefix_length_min is not UNSET:
            field_dict["prefix_length_min"] = prefix_length_min
        if prefix_length_max is not UNSET:
            field_dict["prefix_length_max"] = prefix_length_max
        if allowed_ranges is not UNSET:
            field_dict["allowed_ranges"] = allowed_ranges
        if excluded_ranges is not UNSET:
            field_dict["excluded_ranges"] = excluded_ranges
        if max_items is not UNSET:
            field_dict["max_items"] = max_items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _ip_version = d.pop("ip_version", UNSET)
        ip_version: Union[Unset, CidrIpVersionEnum]
        if isinstance(_ip_version, Unset):
            ip_version = UNSET
        else:
            ip_version = CidrIpVersionEnum(_ip_version)

        prefix_length_min = d.pop("prefix_length_min", UNSET)

        prefix_length_max = d.pop("prefix_length_max", UNSET)

        allowed_ranges = cast(list[str], d.pop("allowed_ranges", UNSET))

        excluded_ranges = cast(list[str], d.pop("excluded_ranges", UNSET))

        max_items = d.pop("max_items", UNSET)

        cidr_policy_request = cls(
            ip_version=ip_version,
            prefix_length_min=prefix_length_min,
            prefix_length_max=prefix_length_max,
            allowed_ranges=allowed_ranges,
            excluded_ranges=excluded_ranges,
            max_items=max_items,
        )

        cidr_policy_request.additional_properties = d
        return cidr_policy_request

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
