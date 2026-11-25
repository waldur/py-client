from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.offering_template_parameter_type_enum import OfferingTemplateParameterTypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.offering_template_parameter_choices_item import OfferingTemplateParameterChoicesItem
    from ..models.offering_template_parameter_default_type_0 import OfferingTemplateParameterDefaultType0


T = TypeVar("T", bound="OfferingTemplateParameter")


@_attrs_define
class OfferingTemplateParameter:
    """
    Attributes:
        key (str):
        label (str):
        description (str):
        type_ (OfferingTemplateParameterTypeEnum):
        required (bool):
        default (Union['OfferingTemplateParameterDefaultType0', None]):
        paths (list[str]): Dotted paths into the document that the value fills, such as offering.backend_id; digits
            address list items.
        choices (Union[Unset, list['OfferingTemplateParameterChoicesItem']]): The values allowed, when the parameter is
            limited to some.
        pattern (Union[Unset, str]): A regular expression a string value must match in full.
    """

    key: str
    label: str
    description: str
    type_: OfferingTemplateParameterTypeEnum
    required: bool
    default: Union["OfferingTemplateParameterDefaultType0", None]
    paths: list[str]
    choices: Union[Unset, list["OfferingTemplateParameterChoicesItem"]] = UNSET
    pattern: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.offering_template_parameter_default_type_0 import OfferingTemplateParameterDefaultType0

        key = self.key

        label = self.label

        description = self.description

        type_ = self.type_.value

        required = self.required

        default: Union[None, dict[str, Any]]
        if isinstance(self.default, OfferingTemplateParameterDefaultType0):
            default = self.default.to_dict()
        else:
            default = self.default

        paths = self.paths

        choices: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.choices, Unset):
            choices = []
            for choices_item_data in self.choices:
                choices_item = choices_item_data.to_dict()
                choices.append(choices_item)

        pattern = self.pattern

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "label": label,
                "description": description,
                "type": type_,
                "required": required,
                "default": default,
                "paths": paths,
            }
        )
        if choices is not UNSET:
            field_dict["choices"] = choices
        if pattern is not UNSET:
            field_dict["pattern"] = pattern

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.offering_template_parameter_choices_item import OfferingTemplateParameterChoicesItem
        from ..models.offering_template_parameter_default_type_0 import OfferingTemplateParameterDefaultType0

        d = dict(src_dict)
        key = d.pop("key")

        label = d.pop("label")

        description = d.pop("description")

        type_ = OfferingTemplateParameterTypeEnum(d.pop("type"))

        required = d.pop("required")

        def _parse_default(data: object) -> Union["OfferingTemplateParameterDefaultType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                default_type_0 = OfferingTemplateParameterDefaultType0.from_dict(data)

                return default_type_0
            except:  # noqa: E722
                pass
            return cast(Union["OfferingTemplateParameterDefaultType0", None], data)

        default = _parse_default(d.pop("default"))

        paths = cast(list[str], d.pop("paths"))

        choices = []
        _choices = d.pop("choices", UNSET)
        for choices_item_data in _choices or []:
            choices_item = OfferingTemplateParameterChoicesItem.from_dict(choices_item_data)

            choices.append(choices_item)

        pattern = d.pop("pattern", UNSET)

        offering_template_parameter = cls(
            key=key,
            label=label,
            description=description,
            type_=type_,
            required=required,
            default=default,
            paths=paths,
            choices=choices,
            pattern=pattern,
        )

        offering_template_parameter.additional_properties = d
        return offering_template_parameter

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
