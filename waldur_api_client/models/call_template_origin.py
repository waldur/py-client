from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CallTemplateOrigin")


@_attrs_define
class CallTemplateOrigin:
    """
    Attributes:
        organization (str):
        process (str):
        reference_url (Union[None, str]):
        programme (Union[None, str]): Name of the programme the process belongs to, if any.
    """

    organization: str
    process: str
    reference_url: Union[None, str]
    programme: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organization = self.organization

        process = self.process

        reference_url: Union[None, str]
        reference_url = self.reference_url

        programme: Union[None, str]
        programme = self.programme

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organization": organization,
                "process": process,
                "reference_url": reference_url,
                "programme": programme,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        organization = d.pop("organization")

        process = d.pop("process")

        def _parse_reference_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        reference_url = _parse_reference_url(d.pop("reference_url"))

        def _parse_programme(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        programme = _parse_programme(d.pop("programme"))

        call_template_origin = cls(
            organization=organization,
            process=process,
            reference_url=reference_url,
            programme=programme,
        )

        call_template_origin.additional_properties = d
        return call_template_origin

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
