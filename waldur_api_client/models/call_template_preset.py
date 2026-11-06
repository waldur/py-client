from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.call_template_preset_info import CallTemplatePresetInfo
    from ..models.call_template_step import CallTemplateStep


T = TypeVar("T", bound="CallTemplatePreset")


@_attrs_define
class CallTemplatePreset:
    """
    Attributes:
        key (str):
        name (str):
        description (str):
        steps (list['CallTemplateStep']):
        preset (Union['CallTemplatePresetInfo', None]): Organization and process the preset models; null when it does
            not say.
        name_taken (bool): A call template already holds the name this preset would be loaded under: rename or delete it
            to load the preset.
    """

    key: str
    name: str
    description: str
    steps: list["CallTemplateStep"]
    preset: Union["CallTemplatePresetInfo", None]
    name_taken: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.call_template_preset_info import CallTemplatePresetInfo

        key = self.key

        name = self.name

        description = self.description

        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()
            steps.append(steps_item)

        preset: Union[None, dict[str, Any]]
        if isinstance(self.preset, CallTemplatePresetInfo):
            preset = self.preset.to_dict()
        else:
            preset = self.preset

        name_taken = self.name_taken

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "name": name,
                "description": description,
                "steps": steps,
                "preset": preset,
                "name_taken": name_taken,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.call_template_preset_info import CallTemplatePresetInfo
        from ..models.call_template_step import CallTemplateStep

        d = dict(src_dict)
        key = d.pop("key")

        name = d.pop("name")

        description = d.pop("description")

        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = CallTemplateStep.from_dict(steps_item_data)

            steps.append(steps_item)

        def _parse_preset(data: object) -> Union["CallTemplatePresetInfo", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                preset_type_1 = CallTemplatePresetInfo.from_dict(data)

                return preset_type_1
            except:  # noqa: E722
                pass
            return cast(Union["CallTemplatePresetInfo", None], data)

        preset = _parse_preset(d.pop("preset"))

        name_taken = d.pop("name_taken")

        call_template_preset = cls(
            key=key,
            name=name,
            description=description,
            steps=steps,
            preset=preset,
            name_taken=name_taken,
        )

        call_template_preset.additional_properties = d
        return call_template_preset

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
