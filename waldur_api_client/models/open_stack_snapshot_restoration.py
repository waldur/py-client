import datetime
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenStackSnapshotRestoration")


@_attrs_define
class OpenStackSnapshotRestoration:
    """
    Attributes:
        uuid (UUID):
        created (datetime.datetime):
        volume (str):
        volume_name (str):
        volume_state (str):
        volume_runtime_state (str):
        volume_size (int): Size in MiB
        volume_device (str): Name of volume as instance device e.g. /dev/vdb.
        description (Union[Unset, str]): New volume description.
    """

    uuid: UUID
    created: datetime.datetime
    volume: str
    volume_name: str
    volume_state: str
    volume_runtime_state: str
    volume_size: int
    volume_device: str
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        created = self.created.isoformat()

        volume = self.volume

        volume_name = self.volume_name

        volume_state = self.volume_state

        volume_runtime_state = self.volume_runtime_state

        volume_size = self.volume_size

        volume_device = self.volume_device

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "created": created,
                "volume": volume,
                "volume_name": volume_name,
                "volume_state": volume_state,
                "volume_runtime_state": volume_runtime_state,
                "volume_size": volume_size,
                "volume_device": volume_device,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = UUID(d.pop("uuid"))

        created = isoparse(d.pop("created"))

        volume = d.pop("volume")

        volume_name = d.pop("volume_name")

        volume_state = d.pop("volume_state")

        volume_runtime_state = d.pop("volume_runtime_state")

        volume_size = d.pop("volume_size")

        volume_device = d.pop("volume_device")

        description = d.pop("description", UNSET)

        open_stack_snapshot_restoration = cls(
            uuid=uuid,
            created=created,
            volume=volume,
            volume_name=volume_name,
            volume_state=volume_state,
            volume_runtime_state=volume_runtime_state,
            volume_size=volume_size,
            volume_device=volume_device,
            description=description,
        )

        open_stack_snapshot_restoration.additional_properties = d
        return open_stack_snapshot_restoration

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
