from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CallTemplateProgramme")


@_attrs_define
class CallTemplateProgramme:
    """
    Attributes:
        key (str):
        name (str):
        organization (str): Who runs the programme.
        organization_url (Union[None, Unset, str]):
        reference_url (Union[None, Unset, str]): Public page describing the programme.
        summary (Union[None, Unset, str]):
    """

    key: str
    name: str
    organization: str
    organization_url: Union[None, Unset, str] = UNSET
    reference_url: Union[None, Unset, str] = UNSET
    summary: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        name = self.name

        organization = self.organization

        organization_url: Union[None, Unset, str]
        if isinstance(self.organization_url, Unset):
            organization_url = UNSET
        else:
            organization_url = self.organization_url

        reference_url: Union[None, Unset, str]
        if isinstance(self.reference_url, Unset):
            reference_url = UNSET
        else:
            reference_url = self.reference_url

        summary: Union[None, Unset, str]
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "name": name,
                "organization": organization,
            }
        )
        if organization_url is not UNSET:
            field_dict["organization_url"] = organization_url
        if reference_url is not UNSET:
            field_dict["reference_url"] = reference_url
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        name = d.pop("name")

        organization = d.pop("organization")

        def _parse_organization_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        organization_url = _parse_organization_url(d.pop("organization_url", UNSET))

        def _parse_reference_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        reference_url = _parse_reference_url(d.pop("reference_url", UNSET))

        def _parse_summary(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        summary = _parse_summary(d.pop("summary", UNSET))

        call_template_programme = cls(
            key=key,
            name=name,
            organization=organization,
            organization_url=organization_url,
            reference_url=reference_url,
            summary=summary,
        )

        call_template_programme.additional_properties = d
        return call_template_programme

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
