from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patched_offering_template_request_document import PatchedOfferingTemplateRequestDocument


T = TypeVar("T", bound="PatchedOfferingTemplateRequest")


@_attrs_define
class PatchedOfferingTemplateRequest:
    """
    Attributes:
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        offering_type (Union[Unset, str]): Offering type the template creates; only Marketplace.SiteAgent for now.
        document (Union[Unset, PatchedOfferingTemplateRequestDocument]): Offering document in the export_offering
            format, as a mapping or a YAML string, with agent_configuration and parameters. It may not hold secret_options,
            organization groups, screenshots, files, a customer, resources or people. Non-staff see only the offering's
            name, description and type, its components, plans and parameters.
        is_published (Union[Unset, bool]):
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    offering_type: Union[Unset, str] = UNSET
    document: Union[Unset, "PatchedOfferingTemplateRequestDocument"] = UNSET
    is_published: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        offering_type = self.offering_type

        document: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.document, Unset):
            document = self.document.to_dict()

        is_published = self.is_published

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if offering_type is not UNSET:
            field_dict["offering_type"] = offering_type
        if document is not UNSET:
            field_dict["document"] = document
        if is_published is not UNSET:
            field_dict["is_published"] = is_published

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patched_offering_template_request_document import PatchedOfferingTemplateRequestDocument

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        offering_type = d.pop("offering_type", UNSET)

        _document = d.pop("document", UNSET)
        document: Union[Unset, PatchedOfferingTemplateRequestDocument]
        if isinstance(_document, Unset):
            document = UNSET
        else:
            document = PatchedOfferingTemplateRequestDocument.from_dict(_document)

        is_published = d.pop("is_published", UNSET)

        patched_offering_template_request = cls(
            name=name,
            description=description,
            offering_type=offering_type,
            document=document,
            is_published=is_published,
        )

        patched_offering_template_request.additional_properties = d
        return patched_offering_template_request

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
