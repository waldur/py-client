from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedAzurePublicIPRequest")


@_attrs_define
class PatchedAzurePublicIPRequest:
    """
    Attributes:
        description (Union[Unset, str]):
        location (Union[Unset, str]):
        resource_group (Union[Unset, str]):
    """

    description: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    resource_group: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        location = self.location

        resource_group = self.resource_group

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if location is not UNSET:
            field_dict["location"] = location
        if resource_group is not UNSET:
            field_dict["resource_group"] = resource_group

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        location = (
            self.location if isinstance(self.location, Unset) else (None, str(self.location).encode(), "text/plain")
        )

        resource_group = (
            self.resource_group
            if isinstance(self.resource_group, Unset)
            else (None, str(self.resource_group).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if location is not UNSET:
            field_dict["location"] = location
        if resource_group is not UNSET:
            field_dict["resource_group"] = resource_group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        location = d.pop("location", UNSET)

        resource_group = d.pop("resource_group", UNSET)

        patched_azure_public_ip_request = cls(
            description=description,
            location=location,
            resource_group=resource_group,
        )

        patched_azure_public_ip_request.additional_properties = d
        return patched_azure_public_ip_request

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
