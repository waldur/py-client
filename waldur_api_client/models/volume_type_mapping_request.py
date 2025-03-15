from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="VolumeTypeMappingRequest")


@_attrs_define
class VolumeTypeMappingRequest:
    """
    Attributes:
        src_type_uuid (UUID):
        dst_type_uuid (UUID):
    """

    src_type_uuid: UUID
    dst_type_uuid: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        src_type_uuid = str(self.src_type_uuid)

        dst_type_uuid = str(self.dst_type_uuid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "src_type_uuid": src_type_uuid,
                "dst_type_uuid": dst_type_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        src_type_uuid = UUID(d.pop("src_type_uuid"))

        dst_type_uuid = UUID(d.pop("dst_type_uuid"))

        volume_type_mapping_request = cls(
            src_type_uuid=src_type_uuid,
            dst_type_uuid=dst_type_uuid,
        )

        volume_type_mapping_request.additional_properties = d
        return volume_type_mapping_request

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
