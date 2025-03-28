from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mapping_request import MappingRequest


T = TypeVar("T", bound="PatchedMigrationDetailsRequest")


@_attrs_define
class PatchedMigrationDetailsRequest:
    """
    Attributes:
        mappings (Union[Unset, MappingRequest]):
    """

    mappings: Union[Unset, "MappingRequest"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mappings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.mappings, Unset):
            mappings = self.mappings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mappings is not UNSET:
            field_dict["mappings"] = mappings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mapping_request import MappingRequest

        d = dict(src_dict)
        _mappings = d.pop("mappings", UNSET)
        mappings: Union[Unset, MappingRequest]
        if isinstance(_mappings, Unset):
            mappings = UNSET
        else:
            mappings = MappingRequest.from_dict(_mappings)

        patched_migration_details_request = cls(
            mappings=mappings,
        )

        patched_migration_details_request.additional_properties = d
        return patched_migration_details_request

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
