from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AzurePublicIPRequest")


@_attrs_define
class AzurePublicIPRequest:
    """
    Attributes:
        name (str):
        service_settings (str):
        project (str):
        location (str):
        resource_group (str):
        description (Union[Unset, str]):
    """

    name: str
    service_settings: str
    project: str
    location: str
    resource_group: str
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        service_settings = self.service_settings

        project = self.project

        location = self.location

        resource_group = self.resource_group

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "service_settings": service_settings,
                "project": project,
                "location": location,
                "resource_group": resource_group,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        service_settings = d.pop("service_settings")

        project = d.pop("project")

        location = d.pop("location")

        resource_group = d.pop("resource_group")

        description = d.pop("description", UNSET)

        azure_public_ip_request = cls(
            name=name,
            service_settings=service_settings,
            project=project,
            location=location,
            resource_group=resource_group,
            description=description,
        )

        azure_public_ip_request.additional_properties = d
        return azure_public_ip_request

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
