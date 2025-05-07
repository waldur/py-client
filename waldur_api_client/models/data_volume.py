from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mount_point_enum import MountPointEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="DataVolume")


@_attrs_define
class DataVolume:
    """
    Attributes:
        size (int):
        volume_type (Union[None, Unset, str]):
        filesystem (Union[Unset, str]):
        mount_point (Union[Unset, MountPointEnum]):
    """

    size: int
    volume_type: Union[None, Unset, str] = UNSET
    filesystem: Union[Unset, str] = UNSET
    mount_point: Union[Unset, MountPointEnum] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        size = self.size

        volume_type: Union[None, Unset, str]
        if isinstance(self.volume_type, Unset):
            volume_type = UNSET
        else:
            volume_type = self.volume_type

        filesystem = self.filesystem

        mount_point: Union[Unset, str] = UNSET
        if not isinstance(self.mount_point, Unset):
            mount_point = self.mount_point.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "size": size,
            }
        )
        if volume_type is not UNSET:
            field_dict["volume_type"] = volume_type
        if filesystem is not UNSET:
            field_dict["filesystem"] = filesystem
        if mount_point is not UNSET:
            field_dict["mount_point"] = mount_point

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        size = d.pop("size")

        def _parse_volume_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        volume_type = _parse_volume_type(d.pop("volume_type", UNSET))

        filesystem = d.pop("filesystem", UNSET)

        _mount_point = d.pop("mount_point", UNSET)
        mount_point: Union[Unset, MountPointEnum]
        if isinstance(_mount_point, Unset):
            mount_point = UNSET
        else:
            mount_point = MountPointEnum(_mount_point)

        data_volume = cls(
            size=size,
            volume_type=volume_type,
            filesystem=filesystem,
            mount_point=mount_point,
        )

        data_volume.additional_properties = d
        return data_volume

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
