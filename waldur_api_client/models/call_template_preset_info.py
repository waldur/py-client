from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.call_template_preset_info_category_enum import CallTemplatePresetInfoCategoryEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.call_template_programme import CallTemplateProgramme


T = TypeVar("T", bound="CallTemplatePresetInfo")


@_attrs_define
class CallTemplatePresetInfo:
    """
    Attributes:
        organization (Union[None, str]): Who runs the process; the programme's organization for a process of a
            programme, null for a generic pattern naming none.
        process (str): Name of the process modeled.
        category (CallTemplatePresetInfoCategoryEnum):
        summary (str):
        programme (Union['CallTemplateProgramme', None]): The programme the process belongs to; null for a process of no
            programme, such as a generic one.
        organization_url (Union[None, Unset, str]):
        reference_url (Union[None, Unset, str]): Public page describing the process.
        reference_title (Union[None, Unset, str]):
        tags (Union[Unset, list[str]]):
    """

    organization: Union[None, str]
    process: str
    category: CallTemplatePresetInfoCategoryEnum
    summary: str
    programme: Union["CallTemplateProgramme", None]
    organization_url: Union[None, Unset, str] = UNSET
    reference_url: Union[None, Unset, str] = UNSET
    reference_title: Union[None, Unset, str] = UNSET
    tags: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.call_template_programme import CallTemplateProgramme

        organization: Union[None, str]
        organization = self.organization

        process = self.process

        category = self.category.value

        summary = self.summary

        programme: Union[None, dict[str, Any]]
        if isinstance(self.programme, CallTemplateProgramme):
            programme = self.programme.to_dict()
        else:
            programme = self.programme

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

        reference_title: Union[None, Unset, str]
        if isinstance(self.reference_title, Unset):
            reference_title = UNSET
        else:
            reference_title = self.reference_title

        tags: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organization": organization,
                "process": process,
                "category": category,
                "summary": summary,
                "programme": programme,
            }
        )
        if organization_url is not UNSET:
            field_dict["organization_url"] = organization_url
        if reference_url is not UNSET:
            field_dict["reference_url"] = reference_url
        if reference_title is not UNSET:
            field_dict["reference_title"] = reference_title
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.call_template_programme import CallTemplateProgramme

        d = dict(src_dict)

        def _parse_organization(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        organization = _parse_organization(d.pop("organization"))

        process = d.pop("process")

        category = CallTemplatePresetInfoCategoryEnum(d.pop("category"))

        summary = d.pop("summary")

        def _parse_programme(data: object) -> Union["CallTemplateProgramme", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                programme_type_1 = CallTemplateProgramme.from_dict(data)

                return programme_type_1
            except:  # noqa: E722
                pass
            return cast(Union["CallTemplateProgramme", None], data)

        programme = _parse_programme(d.pop("programme"))

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

        def _parse_reference_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        reference_title = _parse_reference_title(d.pop("reference_title", UNSET))

        tags = cast(list[str], d.pop("tags", UNSET))

        call_template_preset_info = cls(
            organization=organization,
            process=process,
            category=category,
            summary=summary,
            programme=programme,
            organization_url=organization_url,
            reference_url=reference_url,
            reference_title=reference_title,
            tags=tags,
        )

        call_template_preset_info.additional_properties = d
        return call_template_preset_info

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
