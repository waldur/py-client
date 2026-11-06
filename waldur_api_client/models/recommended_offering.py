from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.recommended_component import RecommendedComponent


T = TypeVar("T", bound="RecommendedOffering")


@_attrs_define
class RecommendedOffering:
    """
    Attributes:
        requested_offering_uuid (str):
        offering_name (str):
        components (list['RecommendedComponent']):
    """

    requested_offering_uuid: str
    offering_name: str
    components: list["RecommendedComponent"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        requested_offering_uuid = self.requested_offering_uuid

        offering_name = self.offering_name

        components = []
        for components_item_data in self.components:
            components_item = components_item_data.to_dict()
            components.append(components_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "requested_offering_uuid": requested_offering_uuid,
                "offering_name": offering_name,
                "components": components,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.recommended_component import RecommendedComponent

        d = dict(src_dict)
        requested_offering_uuid = d.pop("requested_offering_uuid")

        offering_name = d.pop("offering_name")

        components = []
        _components = d.pop("components")
        for components_item_data in _components:
            components_item = RecommendedComponent.from_dict(components_item_data)

            components.append(components_item)

        recommended_offering = cls(
            requested_offering_uuid=requested_offering_uuid,
            offering_name=offering_name,
            components=components,
        )

        recommended_offering.additional_properties = d
        return recommended_offering

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
