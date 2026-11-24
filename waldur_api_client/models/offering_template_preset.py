from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.offering_template_parameter import OfferingTemplateParameter


T = TypeVar("T", bound="OfferingTemplatePreset")


@_attrs_define
class OfferingTemplatePreset:
    """
    Attributes:
        key (str):
        name (str):
        description (str):
        offering_type (str):
        parameters (list['OfferingTemplateParameter']):
        name_taken (bool): An offering template already holds the name this preset would be loaded under: rename or
            delete it to load the preset.
    """

    key: str
    name: str
    description: str
    offering_type: str
    parameters: list["OfferingTemplateParameter"]
    name_taken: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        name = self.name

        description = self.description

        offering_type = self.offering_type

        parameters = []
        for parameters_item_data in self.parameters:
            parameters_item = parameters_item_data.to_dict()
            parameters.append(parameters_item)

        name_taken = self.name_taken

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "name": name,
                "description": description,
                "offering_type": offering_type,
                "parameters": parameters,
                "name_taken": name_taken,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.offering_template_parameter import OfferingTemplateParameter

        d = dict(src_dict)
        key = d.pop("key")

        name = d.pop("name")

        description = d.pop("description")

        offering_type = d.pop("offering_type")

        parameters = []
        _parameters = d.pop("parameters")
        for parameters_item_data in _parameters:
            parameters_item = OfferingTemplateParameter.from_dict(parameters_item_data)

            parameters.append(parameters_item)

        name_taken = d.pop("name_taken")

        offering_template_preset = cls(
            key=key,
            name=name,
            description=description,
            offering_type=offering_type,
            parameters=parameters,
            name_taken=name_taken,
        )

        offering_template_preset.additional_properties = d
        return offering_template_preset

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
