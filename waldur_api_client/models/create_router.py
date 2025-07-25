from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateRouter")


@_attrs_define
class CreateRouter:
    """
    Attributes:
        url (str):
        uuid (UUID):
        tenant (str):
        name (str):
        project (str):
        service_settings (str):
    """

    url: str
    uuid: UUID
    tenant: str
    name: str
    project: str
    service_settings: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        uuid = str(self.uuid)

        tenant = self.tenant

        name = self.name

        project = self.project

        service_settings = self.service_settings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "uuid": uuid,
                "tenant": tenant,
                "name": name,
                "project": project,
                "service_settings": service_settings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        uuid = UUID(d.pop("uuid"))

        tenant = d.pop("tenant")

        name = d.pop("name")

        project = d.pop("project")

        service_settings = d.pop("service_settings")

        create_router = cls(
            url=url,
            uuid=uuid,
            tenant=tenant,
            name=name,
            project=project,
            service_settings=service_settings,
        )

        create_router.additional_properties = d
        return create_router

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
