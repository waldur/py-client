from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LoadCallTemplatePresetRequest")


@_attrs_define
class LoadCallTemplatePresetRequest:
    """
    Attributes:
        presets (list[str]): Keys of the presets to load, as the presets action lists them.
        publish (Union[Unset, bool]): Publish the templates created, so call managers see them. Default: False.
    """

    presets: list[str]
    publish: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        presets = self.presets

        publish = self.publish

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "presets": presets,
            }
        )
        if publish is not UNSET:
            field_dict["publish"] = publish

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        presets = cast(list[str], d.pop("presets"))

        publish = d.pop("publish", UNSET)

        load_call_template_preset_request = cls(
            presets=presets,
            publish=publish,
        )

        load_call_template_preset_request.additional_properties = d
        return load_call_template_preset_request

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
