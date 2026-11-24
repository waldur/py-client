from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.offering_template_request_document import OfferingTemplateRequestDocument


T = TypeVar("T", bound="OfferingTemplateRequest")


@_attrs_define
class OfferingTemplateRequest:
    """
    Attributes:
        name (str):
        offering_type (str): Offering type the template creates; only Marketplace.SiteAgent for now.
        document (OfferingTemplateRequestDocument): Offering document in the export_offering format, as a mapping or a
            YAML string, with agent_configuration and parameters. It may not hold secret_options, organization groups,
            screenshots, files, a customer, resources or people. Non-staff see only the offering's name, description and
            type, its components, plans and parameters.
        description (Union[Unset, str]):
        is_published (Union[Unset, bool]):
    """

    name: str
    offering_type: str
    document: "OfferingTemplateRequestDocument"
    description: Union[Unset, str] = UNSET
    is_published: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        offering_type = self.offering_type

        document = self.document.to_dict()

        description = self.description

        is_published = self.is_published

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "offering_type": offering_type,
                "document": document,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if is_published is not UNSET:
            field_dict["is_published"] = is_published

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.offering_template_request_document import OfferingTemplateRequestDocument

        d = dict(src_dict)
        name = d.pop("name")

        offering_type = d.pop("offering_type")

        document = OfferingTemplateRequestDocument.from_dict(d.pop("document"))

        description = d.pop("description", UNSET)

        is_published = d.pop("is_published", UNSET)

        offering_template_request = cls(
            name=name,
            offering_type=offering_type,
            document=document,
            description=description,
            is_published=is_published,
        )

        offering_template_request.additional_properties = d
        return offering_template_request

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
