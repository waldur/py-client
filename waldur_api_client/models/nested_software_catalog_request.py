from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nested_software_catalog_request_enabled_cpu_family import NestedSoftwareCatalogRequestEnabledCpuFamily
    from ..models.nested_software_catalog_request_enabled_cpu_microarchitectures import (
        NestedSoftwareCatalogRequestEnabledCpuMicroarchitectures,
    )


T = TypeVar("T", bound="NestedSoftwareCatalogRequest")


@_attrs_define
class NestedSoftwareCatalogRequest:
    """
    Attributes:
        enabled_cpu_family (Union[Unset, NestedSoftwareCatalogRequestEnabledCpuFamily]): List of enabled CPU families:
            ['x86_64', 'aarch64']
        enabled_cpu_microarchitectures (Union[Unset, NestedSoftwareCatalogRequestEnabledCpuMicroarchitectures]): List of
            enabled CPU microarchitectures: ['generic', 'zen3']
    """

    enabled_cpu_family: Union[Unset, "NestedSoftwareCatalogRequestEnabledCpuFamily"] = UNSET
    enabled_cpu_microarchitectures: Union[Unset, "NestedSoftwareCatalogRequestEnabledCpuMicroarchitectures"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled_cpu_family: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.enabled_cpu_family, Unset):
            enabled_cpu_family = self.enabled_cpu_family.to_dict()

        enabled_cpu_microarchitectures: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.enabled_cpu_microarchitectures, Unset):
            enabled_cpu_microarchitectures = self.enabled_cpu_microarchitectures.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled_cpu_family is not UNSET:
            field_dict["enabled_cpu_family"] = enabled_cpu_family
        if enabled_cpu_microarchitectures is not UNSET:
            field_dict["enabled_cpu_microarchitectures"] = enabled_cpu_microarchitectures

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nested_software_catalog_request_enabled_cpu_family import (
            NestedSoftwareCatalogRequestEnabledCpuFamily,
        )
        from ..models.nested_software_catalog_request_enabled_cpu_microarchitectures import (
            NestedSoftwareCatalogRequestEnabledCpuMicroarchitectures,
        )

        d = dict(src_dict)
        _enabled_cpu_family = d.pop("enabled_cpu_family", UNSET)
        enabled_cpu_family: Union[Unset, NestedSoftwareCatalogRequestEnabledCpuFamily]
        if isinstance(_enabled_cpu_family, Unset):
            enabled_cpu_family = UNSET
        else:
            enabled_cpu_family = NestedSoftwareCatalogRequestEnabledCpuFamily.from_dict(_enabled_cpu_family)

        _enabled_cpu_microarchitectures = d.pop("enabled_cpu_microarchitectures", UNSET)
        enabled_cpu_microarchitectures: Union[Unset, NestedSoftwareCatalogRequestEnabledCpuMicroarchitectures]
        if isinstance(_enabled_cpu_microarchitectures, Unset):
            enabled_cpu_microarchitectures = UNSET
        else:
            enabled_cpu_microarchitectures = NestedSoftwareCatalogRequestEnabledCpuMicroarchitectures.from_dict(
                _enabled_cpu_microarchitectures
            )

        nested_software_catalog_request = cls(
            enabled_cpu_family=enabled_cpu_family,
            enabled_cpu_microarchitectures=enabled_cpu_microarchitectures,
        )

        nested_software_catalog_request.additional_properties = d
        return nested_software_catalog_request

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
