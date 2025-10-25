from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedSoftwarePackageRequest")


@_attrs_define
class PatchedSoftwarePackageRequest:
    """
    Attributes:
        catalog (Union[Unset, str]):
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        homepage (Union[Unset, str]):
    """

    catalog: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    homepage: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        catalog = self.catalog

        name = self.name

        description = self.description

        homepage = self.homepage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if catalog is not UNSET:
            field_dict["catalog"] = catalog
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if homepage is not UNSET:
            field_dict["homepage"] = homepage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        catalog = d.pop("catalog", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        homepage = d.pop("homepage", UNSET)

        patched_software_package_request = cls(
            catalog=catalog,
            name=name,
            description=description,
            homepage=homepage,
        )

        patched_software_package_request.additional_properties = d
        return patched_software_package_request

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
