import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.offering_template_version_document import OfferingTemplateVersionDocument


T = TypeVar("T", bound="OfferingTemplateVersion")


@_attrs_define
class OfferingTemplateVersion:
    """
    Attributes:
        number (int):
        document (OfferingTemplateVersionDocument):
        document_hash (str):
        created_by (Union[None, UUID]):
        created (datetime.datetime):
    """

    number: int
    document: "OfferingTemplateVersionDocument"
    document_hash: str
    created_by: Union[None, UUID]
    created: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        number = self.number

        document = self.document.to_dict()

        document_hash = self.document_hash

        created_by: Union[None, str]
        if isinstance(self.created_by, UUID):
            created_by = str(self.created_by)
        else:
            created_by = self.created_by

        created = self.created.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "number": number,
                "document": document,
                "document_hash": document_hash,
                "created_by": created_by,
                "created": created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.offering_template_version_document import OfferingTemplateVersionDocument

        d = dict(src_dict)
        number = d.pop("number")

        document = OfferingTemplateVersionDocument.from_dict(d.pop("document"))

        document_hash = d.pop("document_hash")

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

        offering_template_version = cls(
            number=number,
            document=document,
            document_hash=document_hash,
            created_by=created_by,
            created=created,
        )

        offering_template_version.additional_properties = d
        return offering_template_version

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
