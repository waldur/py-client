from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenStackNestedVolume")


@_attrs_define
class OpenStackNestedVolume:
    """
    Attributes:
        url (str):
        uuid (UUID):
        name (str):
        state (str):
        size (int): Size in MiB
        resource_type (str):
        type_name (str):
        marketplace_resource_uuid (str):
        image_name (Union[Unset, str]):
        bootable (Union[Unset, bool]):
        device (Union[Unset, str]): Name of volume as instance device e.g. /dev/vdb.
        type_ (Union[None, Unset, str]):
    """

    url: str
    uuid: UUID
    name: str
    state: str
    size: int
    resource_type: str
    type_name: str
    marketplace_resource_uuid: str
    image_name: Union[Unset, str] = UNSET
    bootable: Union[Unset, bool] = UNSET
    device: Union[Unset, str] = UNSET
    type_: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        uuid = str(self.uuid)

        name = self.name

        state = self.state

        size = self.size

        resource_type = self.resource_type

        type_name = self.type_name

        marketplace_resource_uuid = self.marketplace_resource_uuid

        image_name = self.image_name

        bootable = self.bootable

        device = self.device

        type_: Union[None, Unset, str]
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "uuid": uuid,
                "name": name,
                "state": state,
                "size": size,
                "resource_type": resource_type,
                "type_name": type_name,
                "marketplace_resource_uuid": marketplace_resource_uuid,
            }
        )
        if image_name is not UNSET:
            field_dict["image_name"] = image_name
        if bootable is not UNSET:
            field_dict["bootable"] = bootable
        if device is not UNSET:
            field_dict["device"] = device
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        state = d.pop("state")

        size = d.pop("size")

        resource_type = d.pop("resource_type")

        type_name = d.pop("type_name")

        marketplace_resource_uuid = d.pop("marketplace_resource_uuid")

        image_name = d.pop("image_name", UNSET)

        bootable = d.pop("bootable", UNSET)

        device = d.pop("device", UNSET)

        def _parse_type_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        type_ = _parse_type_(d.pop("type", UNSET))

        open_stack_nested_volume = cls(
            url=url,
            uuid=uuid,
            name=name,
            state=state,
            size=size,
            resource_type=resource_type,
            type_name=type_name,
            marketplace_resource_uuid=marketplace_resource_uuid,
            image_name=image_name,
            bootable=bootable,
            device=device,
            type_=type_,
        )

        open_stack_nested_volume.additional_properties = d
        return open_stack_nested_volume

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
