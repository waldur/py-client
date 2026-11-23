from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.attribute_type_enum import AttributeTypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attribute_create_request_default_type_0 import AttributeCreateRequestDefaultType0
    from ..models.attribute_option_item_request import AttributeOptionItemRequest


T = TypeVar("T", bound="AttributeCreateRequest")


@_attrs_define
class AttributeCreateRequest:
    """
    Attributes:
        title (str):
        section (str):
        type_ (AttributeTypeEnum):
        key (Union[Unset, str]):
        required (Union[Unset, bool]): A value must be provided for the attribute.
        default (Union['AttributeCreateRequestDefaultType0', None, Unset]):
        options (Union[Unset, list['AttributeOptionItemRequest']]):
    """

    title: str
    section: str
    type_: AttributeTypeEnum
    key: Union[Unset, str] = UNSET
    required: Union[Unset, bool] = UNSET
    default: Union["AttributeCreateRequestDefaultType0", None, Unset] = UNSET
    options: Union[Unset, list["AttributeOptionItemRequest"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.attribute_create_request_default_type_0 import AttributeCreateRequestDefaultType0

        title = self.title

        section = self.section

        type_ = self.type_.value

        key = self.key

        required = self.required

        default: Union[None, Unset, dict[str, Any]]
        if isinstance(self.default, Unset):
            default = UNSET
        elif isinstance(self.default, AttributeCreateRequestDefaultType0):
            default = self.default.to_dict()
        else:
            default = self.default

        options: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "section": section,
                "type": type_,
            }
        )
        if key is not UNSET:
            field_dict["key"] = key
        if required is not UNSET:
            field_dict["required"] = required
        if default is not UNSET:
            field_dict["default"] = default
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attribute_create_request_default_type_0 import AttributeCreateRequestDefaultType0
        from ..models.attribute_option_item_request import AttributeOptionItemRequest

        d = dict(src_dict)
        title = d.pop("title")

        section = d.pop("section")

        type_ = AttributeTypeEnum(d.pop("type"))

        key = d.pop("key", UNSET)

        required = d.pop("required", UNSET)

        def _parse_default(data: object) -> Union["AttributeCreateRequestDefaultType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                default_type_0 = AttributeCreateRequestDefaultType0.from_dict(data)

                return default_type_0
            except:  # noqa: E722
                pass
            return cast(Union["AttributeCreateRequestDefaultType0", None, Unset], data)

        default = _parse_default(d.pop("default", UNSET))

        options = []
        _options = d.pop("options", UNSET)
        for options_item_data in _options or []:
            options_item = AttributeOptionItemRequest.from_dict(options_item_data)

            options.append(options_item)

        attribute_create_request = cls(
            title=title,
            section=section,
            type_=type_,
            key=key,
            required=required,
            default=default,
            options=options,
        )

        attribute_create_request.additional_properties = d
        return attribute_create_request

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
