from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patched_call_template_request_document import PatchedCallTemplateRequestDocument
    from ..models.patched_call_template_request_scenarios_item import PatchedCallTemplateRequestScenariosItem


T = TypeVar("T", bound="PatchedCallTemplateRequest")


@_attrs_define
class PatchedCallTemplateRequest:
    """
    Attributes:
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        document (Union[Unset, PatchedCallTemplateRequestDocument]): Call document in the export format, as a mapping or
            a YAML string: call settings and workflow, without rounds, requested offerings or documents.
        is_published (Union[Unset, bool]):
        scenarios (Union[Unset, list['PatchedCallTemplateRequestScenariosItem']]): Named paths through the workflow:
            {key, name, description, request: {offerings, actions}, assertions}. Definitions only: they run as dry runs on
            each call created from the template.
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    document: Union[Unset, "PatchedCallTemplateRequestDocument"] = UNSET
    is_published: Union[Unset, bool] = UNSET
    scenarios: Union[Unset, list["PatchedCallTemplateRequestScenariosItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        document: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.document, Unset):
            document = self.document.to_dict()

        is_published = self.is_published

        scenarios: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.scenarios, Unset):
            scenarios = []
            for scenarios_item_data in self.scenarios:
                scenarios_item = scenarios_item_data.to_dict()
                scenarios.append(scenarios_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if document is not UNSET:
            field_dict["document"] = document
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if scenarios is not UNSET:
            field_dict["scenarios"] = scenarios

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patched_call_template_request_document import PatchedCallTemplateRequestDocument
        from ..models.patched_call_template_request_scenarios_item import PatchedCallTemplateRequestScenariosItem

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _document = d.pop("document", UNSET)
        document: Union[Unset, PatchedCallTemplateRequestDocument]
        if isinstance(_document, Unset):
            document = UNSET
        else:
            document = PatchedCallTemplateRequestDocument.from_dict(_document)

        is_published = d.pop("is_published", UNSET)

        scenarios = []
        _scenarios = d.pop("scenarios", UNSET)
        for scenarios_item_data in _scenarios or []:
            scenarios_item = PatchedCallTemplateRequestScenariosItem.from_dict(scenarios_item_data)

            scenarios.append(scenarios_item)

        patched_call_template_request = cls(
            name=name,
            description=description,
            document=document,
            is_published=is_published,
            scenarios=scenarios,
        )

        patched_call_template_request.additional_properties = d
        return patched_call_template_request

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
