from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.docs_search_hit import DocsSearchHit
    from ..models.docs_search_switched_off import DocsSearchSwitchedOff


T = TypeVar("T", bound="DocsSearchResponse")


@_attrs_define
class DocsSearchResponse:
    """
    Attributes:
        query (str):
        sections (list['DocsSearchHit']):
        switched_off_here (list['DocsSearchSwitchedOff']): Features the query is about that are switched off on this
            portal. Their sections are not returned to users without staff or support rights; only the feature is named.
    """

    query: str
    sections: list["DocsSearchHit"]
    switched_off_here: list["DocsSearchSwitchedOff"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        sections = []
        for sections_item_data in self.sections:
            sections_item = sections_item_data.to_dict()
            sections.append(sections_item)

        switched_off_here = []
        for switched_off_here_item_data in self.switched_off_here:
            switched_off_here_item = switched_off_here_item_data.to_dict()
            switched_off_here.append(switched_off_here_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
                "sections": sections,
                "switched_off_here": switched_off_here,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.docs_search_hit import DocsSearchHit
        from ..models.docs_search_switched_off import DocsSearchSwitchedOff

        d = dict(src_dict)
        query = d.pop("query")

        sections = []
        _sections = d.pop("sections")
        for sections_item_data in _sections:
            sections_item = DocsSearchHit.from_dict(sections_item_data)

            sections.append(sections_item)

        switched_off_here = []
        _switched_off_here = d.pop("switched_off_here")
        for switched_off_here_item_data in _switched_off_here:
            switched_off_here_item = DocsSearchSwitchedOff.from_dict(switched_off_here_item_data)

            switched_off_here.append(switched_off_here_item)

        docs_search_response = cls(
            query=query,
            sections=sections,
            switched_off_here=switched_off_here,
        )

        docs_search_response.additional_properties = d
        return docs_search_response

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
