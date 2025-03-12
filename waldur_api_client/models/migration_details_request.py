import json
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.mapping_request import MappingRequest


T = TypeVar("T", bound="MigrationDetailsRequest")


@_attrs_define
class MigrationDetailsRequest:
    """
    Attributes:
        mappings (MappingRequest):
    """

    mappings: "MappingRequest"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mappings = self.mappings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mappings": mappings,
            }
        )

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        mappings = (None, json.dumps(self.mappings.to_dict()).encode(), "application/json")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "mappings": mappings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.mapping_request import MappingRequest

        d = src_dict.copy()
        mappings = MappingRequest.from_dict(d.pop("mappings"))

        migration_details_request = cls(
            mappings=mappings,
        )

        migration_details_request.additional_properties = d
        return migration_details_request

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
