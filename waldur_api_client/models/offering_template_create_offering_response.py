from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.offering_configuration_finding import OfferingConfigurationFinding
    from ..models.offering_template_create_offering_response_document import (
        OfferingTemplateCreateOfferingResponseDocument,
    )
    from ..models.offering_template_create_offering_response_parameters import (
        OfferingTemplateCreateOfferingResponseParameters,
    )


T = TypeVar("T", bound="OfferingTemplateCreateOfferingResponse")


@_attrs_define
class OfferingTemplateCreateOfferingResponse:
    """
    Attributes:
        dry_run (bool):
        offering_uuid (Union[None, UUID]): The new offering; null on a dry run.
        offering_name (str):
        template_version (int):
        parameters (OfferingTemplateCreateOfferingResponseParameters): The value of every parameter, defaults included.
        document (OfferingTemplateCreateOfferingResponseDocument): The template's document with the parameters filled
            in: what the offering is created from, in the import_offering format.
        warnings (list[str]): What the import of the document reported.
        findings (list['OfferingConfigurationFinding']): What the site-agent consistency rules find in the filled-in
            document, errors first. A create with an error is refused.
    """

    dry_run: bool
    offering_uuid: Union[None, UUID]
    offering_name: str
    template_version: int
    parameters: "OfferingTemplateCreateOfferingResponseParameters"
    document: "OfferingTemplateCreateOfferingResponseDocument"
    warnings: list[str]
    findings: list["OfferingConfigurationFinding"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dry_run = self.dry_run

        offering_uuid: Union[None, str]
        if isinstance(self.offering_uuid, UUID):
            offering_uuid = str(self.offering_uuid)
        else:
            offering_uuid = self.offering_uuid

        offering_name = self.offering_name

        template_version = self.template_version

        parameters = self.parameters.to_dict()

        document = self.document.to_dict()

        warnings = self.warnings

        findings = []
        for findings_item_data in self.findings:
            findings_item = findings_item_data.to_dict()
            findings.append(findings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dry_run": dry_run,
                "offering_uuid": offering_uuid,
                "offering_name": offering_name,
                "template_version": template_version,
                "parameters": parameters,
                "document": document,
                "warnings": warnings,
                "findings": findings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.offering_configuration_finding import OfferingConfigurationFinding
        from ..models.offering_template_create_offering_response_document import (
            OfferingTemplateCreateOfferingResponseDocument,
        )
        from ..models.offering_template_create_offering_response_parameters import (
            OfferingTemplateCreateOfferingResponseParameters,
        )

        d = dict(src_dict)
        dry_run = d.pop("dry_run")

        def _parse_offering_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                offering_uuid_type_0 = UUID(data)

                return offering_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        offering_uuid = _parse_offering_uuid(d.pop("offering_uuid"))

        offering_name = d.pop("offering_name")

        template_version = d.pop("template_version")

        parameters = OfferingTemplateCreateOfferingResponseParameters.from_dict(d.pop("parameters"))

        document = OfferingTemplateCreateOfferingResponseDocument.from_dict(d.pop("document"))

        warnings = cast(list[str], d.pop("warnings"))

        findings = []
        _findings = d.pop("findings")
        for findings_item_data in _findings:
            findings_item = OfferingConfigurationFinding.from_dict(findings_item_data)

            findings.append(findings_item)

        offering_template_create_offering_response = cls(
            dry_run=dry_run,
            offering_uuid=offering_uuid,
            offering_name=offering_name,
            template_version=template_version,
            parameters=parameters,
            document=document,
            warnings=warnings,
            findings=findings,
        )

        offering_template_create_offering_response.additional_properties = d
        return offering_template_create_offering_response

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
