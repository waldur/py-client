from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DocsSearchHit")


@_attrs_define
class DocsSearchHit:
    """
    Attributes:
        title (str):
        breadcrumb (str):
        excerpt (str):
        url (str):
        enabled_here (bool): False when the section describes a feature that is switched off on this portal, or that it
            cannot confirm is switched on. Only staff and support get such sections.
    """

    title: str
    breadcrumb: str
    excerpt: str
    url: str
    enabled_here: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        breadcrumb = self.breadcrumb

        excerpt = self.excerpt

        url = self.url

        enabled_here = self.enabled_here

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "breadcrumb": breadcrumb,
                "excerpt": excerpt,
                "url": url,
                "enabled_here": enabled_here,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        breadcrumb = d.pop("breadcrumb")

        excerpt = d.pop("excerpt")

        url = d.pop("url")

        enabled_here = d.pop("enabled_here")

        docs_search_hit = cls(
            title=title,
            breadcrumb=breadcrumb,
            excerpt=excerpt,
            url=url,
            enabled_here=enabled_here,
        )

        docs_search_hit.additional_properties = d
        return docs_search_hit

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
