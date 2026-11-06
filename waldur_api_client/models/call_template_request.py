from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.call_template_request_document import CallTemplateRequestDocument
    from ..models.call_template_request_scenarios_item import CallTemplateRequestScenariosItem


T = TypeVar("T", bound="CallTemplateRequest")


@_attrs_define
class CallTemplateRequest:
    """
    Attributes:
        name (str):
        document (CallTemplateRequestDocument): Call document in the export format, as a mapping or a YAML string: call
            settings and workflow, without rounds, requested offerings or documents.
        description (Union[Unset, str]):
        is_published (Union[Unset, bool]):
        scenarios (Union[Unset, list['CallTemplateRequestScenariosItem']]): Named paths through the workflow: {key,
            name, description, request: {offerings, actions}, assertions}. Definitions only: they run as dry runs on each
            call created from the template.
    """

    name: str
    document: "CallTemplateRequestDocument"
    description: Union[Unset, str] = UNSET
    is_published: Union[Unset, bool] = UNSET
    scenarios: Union[Unset, list["CallTemplateRequestScenariosItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        document = self.document.to_dict()

        description = self.description

        is_published = self.is_published

        scenarios: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.scenarios, Unset):
            scenarios = []
            for scenarios_item_data in self.scenarios:
                scenarios_item = scenarios_item_data.to_dict()
                scenarios.append(scenarios_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "document": document,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if scenarios is not UNSET:
            field_dict["scenarios"] = scenarios

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.call_template_request_document import CallTemplateRequestDocument
        from ..models.call_template_request_scenarios_item import CallTemplateRequestScenariosItem

        d = dict(src_dict)
        name = d.pop("name")

        document = CallTemplateRequestDocument.from_dict(d.pop("document"))

        description = d.pop("description", UNSET)

        is_published = d.pop("is_published", UNSET)

        scenarios = []
        _scenarios = d.pop("scenarios", UNSET)
        for scenarios_item_data in _scenarios or []:
            scenarios_item = CallTemplateRequestScenariosItem.from_dict(scenarios_item_data)

            scenarios.append(scenarios_item)

        call_template_request = cls(
            name=name,
            document=document,
            description=description,
            is_published=is_published,
            scenarios=scenarios,
        )

        call_template_request.additional_properties = d
        return call_template_request

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
