from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.micro_app_mode_enum import MicroAppModeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedMicroAppSettingRequest")


@_attrs_define
class PatchedMicroAppSettingRequest:
    """
    Attributes:
        name (Union[Unset, str]): The app's directory under apps/ and its path under the portal.
        mode (Union[Unset, MicroAppModeEnum]):
    """

    name: Union[Unset, str] = UNSET
    mode: Union[Unset, MicroAppModeEnum] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, MicroAppModeEnum]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = MicroAppModeEnum(_mode)

        patched_micro_app_setting_request = cls(
            name=name,
            mode=mode,
        )

        patched_micro_app_setting_request.additional_properties = d
        return patched_micro_app_setting_request

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
