from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AzureVirtualMachineRequest")


@_attrs_define
class AzureVirtualMachineRequest:
    """
    Attributes:
        name (str):
        service_settings (str):
        project (str):
        image (str):
        size (str):
        location (str):
        description (Union[Unset, str]):
        ssh_public_key (Union[None, Unset, str]):
        user_data (Union[Unset, str]): Additional data that will be added to instance on provisioning
    """

    name: str
    service_settings: str
    project: str
    image: str
    size: str
    location: str
    description: Union[Unset, str] = UNSET
    ssh_public_key: Union[None, Unset, str] = UNSET
    user_data: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        service_settings = self.service_settings

        project = self.project

        image = self.image

        size = self.size

        location = self.location

        description = self.description

        ssh_public_key: Union[None, Unset, str]
        if isinstance(self.ssh_public_key, Unset):
            ssh_public_key = UNSET
        else:
            ssh_public_key = self.ssh_public_key

        user_data = self.user_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "service_settings": service_settings,
                "project": project,
                "image": image,
                "size": size,
                "location": location,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if ssh_public_key is not UNSET:
            field_dict["ssh_public_key"] = ssh_public_key
        if user_data is not UNSET:
            field_dict["user_data"] = user_data

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        name = (None, str(self.name).encode(), "text/plain")

        service_settings = (None, str(self.service_settings).encode(), "text/plain")

        project = (None, str(self.project).encode(), "text/plain")

        image = (None, str(self.image).encode(), "text/plain")

        size = (None, str(self.size).encode(), "text/plain")

        location = (None, str(self.location).encode(), "text/plain")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        ssh_public_key: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.ssh_public_key, Unset):
            ssh_public_key = UNSET
        elif isinstance(self.ssh_public_key, str):
            ssh_public_key = (None, str(self.ssh_public_key).encode(), "text/plain")
        else:
            ssh_public_key = (None, str(self.ssh_public_key).encode(), "text/plain")

        user_data = (
            self.user_data if isinstance(self.user_data, Unset) else (None, str(self.user_data).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "name": name,
                "service_settings": service_settings,
                "project": project,
                "image": image,
                "size": size,
                "location": location,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if ssh_public_key is not UNSET:
            field_dict["ssh_public_key"] = ssh_public_key
        if user_data is not UNSET:
            field_dict["user_data"] = user_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        service_settings = d.pop("service_settings")

        project = d.pop("project")

        image = d.pop("image")

        size = d.pop("size")

        location = d.pop("location")

        description = d.pop("description", UNSET)

        def _parse_ssh_public_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        ssh_public_key = _parse_ssh_public_key(d.pop("ssh_public_key", UNSET))

        user_data = d.pop("user_data", UNSET)

        azure_virtual_machine_request = cls(
            name=name,
            service_settings=service_settings,
            project=project,
            image=image,
            size=size,
            location=location,
            description=description,
            ssh_public_key=ssh_public_key,
            user_data=user_data,
        )

        azure_virtual_machine_request.additional_properties = d
        return azure_virtual_machine_request

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
