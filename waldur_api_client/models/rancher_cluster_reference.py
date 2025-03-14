from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RancherClusterReference")


@_attrs_define
class RancherClusterReference:
    """
    Attributes:
        uuid (UUID):
        name (str):
        marketplace_uuid (str):
    """

    uuid: UUID
    name: str
    marketplace_uuid: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        name = self.name

        marketplace_uuid = self.marketplace_uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "name": name,
                "marketplace_uuid": marketplace_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        marketplace_uuid = d.pop("marketplace_uuid")

        rancher_cluster_reference = cls(
            uuid=uuid,
            name=name,
            marketplace_uuid=marketplace_uuid,
        )

        rancher_cluster_reference.additional_properties = d
        return rancher_cluster_reference

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
