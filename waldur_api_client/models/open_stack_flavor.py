from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OpenStackFlavor")


@_attrs_define
class OpenStackFlavor:
    """
    Attributes:
        url (str):
        uuid (UUID):
        name (str):
        settings (str):
        cores (int): Number of cores in a VM
        ram (int): Memory size in MiB
        disk (int): Root disk size in MiB
        backend_id (str):
        display_name (str):
    """

    url: str
    uuid: UUID
    name: str
    settings: str
    cores: int
    ram: int
    disk: int
    backend_id: str
    display_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        uuid = str(self.uuid)

        name = self.name

        settings = self.settings

        cores = self.cores

        ram = self.ram

        disk = self.disk

        backend_id = self.backend_id

        display_name = self.display_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "uuid": uuid,
                "name": name,
                "settings": settings,
                "cores": cores,
                "ram": ram,
                "disk": disk,
                "backend_id": backend_id,
                "display_name": display_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        settings = d.pop("settings")

        cores = d.pop("cores")

        ram = d.pop("ram")

        disk = d.pop("disk")

        backend_id = d.pop("backend_id")

        display_name = d.pop("display_name")

        open_stack_flavor = cls(
            url=url,
            uuid=uuid,
            name=name,
            settings=settings,
            cores=cores,
            ram=ram,
            disk=disk,
            backend_id=backend_id,
            display_name=display_name,
        )

        open_stack_flavor.additional_properties = d
        return open_stack_flavor

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
