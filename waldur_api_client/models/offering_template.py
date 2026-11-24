import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.offering_template_document import OfferingTemplateDocument
    from ..models.offering_template_parameter import OfferingTemplateParameter


T = TypeVar("T", bound="OfferingTemplate")


@_attrs_define
class OfferingTemplate:
    """
    Attributes:
        uuid (UUID):
        url (str):
        name (str):
        offering_type (str): Offering type the template creates; only Marketplace.SiteAgent for now.
        document (OfferingTemplateDocument): Offering document in the export_offering format, as a mapping or a YAML
            string, with agent_configuration and parameters. It may not hold secret_options, organization groups,
            screenshots, files, a customer, resources or people. Non-staff see only the offering's name, description and
            type, its components, plans and parameters.
        parameters (list['OfferingTemplateParameter']):
        schema_version (int):
        version (int): Incremented whenever the document changes; name, description and publication leave it as it is.
        created_by (Union[None, UUID]):
        created (datetime.datetime):
        modified (datetime.datetime):
        description (Union[Unset, str]):
        is_published (Union[Unset, bool]):
    """

    uuid: UUID
    url: str
    name: str
    offering_type: str
    document: "OfferingTemplateDocument"
    parameters: list["OfferingTemplateParameter"]
    schema_version: int
    version: int
    created_by: Union[None, UUID]
    created: datetime.datetime
    modified: datetime.datetime
    description: Union[Unset, str] = UNSET
    is_published: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        url = self.url

        name = self.name

        offering_type = self.offering_type

        document = self.document.to_dict()

        parameters = []
        for parameters_item_data in self.parameters:
            parameters_item = parameters_item_data.to_dict()
            parameters.append(parameters_item)

        schema_version = self.schema_version

        version = self.version

        created_by: Union[None, str]
        if isinstance(self.created_by, UUID):
            created_by = str(self.created_by)
        else:
            created_by = self.created_by

        created = self.created.isoformat()

        modified = self.modified.isoformat()

        description = self.description

        is_published = self.is_published

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "url": url,
                "name": name,
                "offering_type": offering_type,
                "document": document,
                "parameters": parameters,
                "schema_version": schema_version,
                "version": version,
                "created_by": created_by,
                "created": created,
                "modified": modified,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if is_published is not UNSET:
            field_dict["is_published"] = is_published

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.offering_template_document import OfferingTemplateDocument
        from ..models.offering_template_parameter import OfferingTemplateParameter

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        url = d.pop("url")

        name = d.pop("name")

        offering_type = d.pop("offering_type")

        document = OfferingTemplateDocument.from_dict(d.pop("document"))

        parameters = []
        _parameters = d.pop("parameters")
        for parameters_item_data in _parameters:
            parameters_item = OfferingTemplateParameter.from_dict(parameters_item_data)

            parameters.append(parameters_item)

        schema_version = d.pop("schema_version")

        version = d.pop("version")

        def _parse_created_by(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_type_0 = UUID(data)

                return created_by_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        created_by = _parse_created_by(d.pop("created_by"))

        created = isoparse(d.pop("created"))

        modified = isoparse(d.pop("modified"))

        description = d.pop("description", UNSET)

        is_published = d.pop("is_published", UNSET)

        offering_template = cls(
            uuid=uuid,
            url=url,
            name=name,
            offering_type=offering_type,
            document=document,
            parameters=parameters,
            schema_version=schema_version,
            version=version,
            created_by=created_by,
            created=created,
            modified=modified,
            description=description,
            is_published=is_published,
        )

        offering_template.additional_properties = d
        return offering_template

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
