from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ImportedOfferingBlock")


@_attrs_define
class ImportedOfferingBlock:
    """
    Attributes:
        index (int):
        name (Union[None, str]):
        waldur_offering_uuid (Union[None, str]):
        matches_offering (bool):
    """

    index: int
    name: Union[None, str]
    waldur_offering_uuid: Union[None, str]
    matches_offering: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        index = self.index

        name: Union[None, str]
        name = self.name

        waldur_offering_uuid: Union[None, str]
        waldur_offering_uuid = self.waldur_offering_uuid

        matches_offering = self.matches_offering

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "index": index,
                "name": name,
                "waldur_offering_uuid": waldur_offering_uuid,
                "matches_offering": matches_offering,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        index = d.pop("index")

        def _parse_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        name = _parse_name(d.pop("name"))

        def _parse_waldur_offering_uuid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        waldur_offering_uuid = _parse_waldur_offering_uuid(d.pop("waldur_offering_uuid"))

        matches_offering = d.pop("matches_offering")

        imported_offering_block = cls(
            index=index,
            name=name,
            waldur_offering_uuid=waldur_offering_uuid,
            matches_offering=matches_offering,
        )

        imported_offering_block.additional_properties = d
        return imported_offering_block

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
