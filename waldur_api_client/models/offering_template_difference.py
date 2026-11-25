from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.offering_template_difference_offering_type_0 import OfferingTemplateDifferenceOfferingType0
    from ..models.offering_template_difference_template_type_0 import OfferingTemplateDifferenceTemplateType0


T = TypeVar("T", bound="OfferingTemplateDifference")


@_attrs_define
class OfferingTemplateDifference:
    """
    Attributes:
        path (str): Where the offering differs, such as components[cpu].unit_factor: list items are named by their type,
            name or version.
        template (Union['OfferingTemplateDifferenceTemplateType0', None]): What the template sets; null when it has
            none.
        offering (Union['OfferingTemplateDifferenceOfferingType0', None]): What the offering has; null when it has none.
    """

    path: str
    template: Union["OfferingTemplateDifferenceTemplateType0", None]
    offering: Union["OfferingTemplateDifferenceOfferingType0", None]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.offering_template_difference_offering_type_0 import OfferingTemplateDifferenceOfferingType0
        from ..models.offering_template_difference_template_type_0 import OfferingTemplateDifferenceTemplateType0

        path = self.path

        template: Union[None, dict[str, Any]]
        if isinstance(self.template, OfferingTemplateDifferenceTemplateType0):
            template = self.template.to_dict()
        else:
            template = self.template

        offering: Union[None, dict[str, Any]]
        if isinstance(self.offering, OfferingTemplateDifferenceOfferingType0):
            offering = self.offering.to_dict()
        else:
            offering = self.offering

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "template": template,
                "offering": offering,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.offering_template_difference_offering_type_0 import OfferingTemplateDifferenceOfferingType0
        from ..models.offering_template_difference_template_type_0 import OfferingTemplateDifferenceTemplateType0

        d = dict(src_dict)
        path = d.pop("path")

        def _parse_template(data: object) -> Union["OfferingTemplateDifferenceTemplateType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                template_type_0 = OfferingTemplateDifferenceTemplateType0.from_dict(data)

                return template_type_0
            except:  # noqa: E722
                pass
            return cast(Union["OfferingTemplateDifferenceTemplateType0", None], data)

        template = _parse_template(d.pop("template"))

        def _parse_offering(data: object) -> Union["OfferingTemplateDifferenceOfferingType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                offering_type_0 = OfferingTemplateDifferenceOfferingType0.from_dict(data)

                return offering_type_0
            except:  # noqa: E722
                pass
            return cast(Union["OfferingTemplateDifferenceOfferingType0", None], data)

        offering = _parse_offering(d.pop("offering"))

        offering_template_difference = cls(
            path=path,
            template=template,
            offering=offering,
        )

        offering_template_difference.additional_properties = d
        return offering_template_difference

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
