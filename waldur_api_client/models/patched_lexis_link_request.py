from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedLexisLinkRequest")


@_attrs_define
class PatchedLexisLinkRequest:
    """
    Attributes:
        heappe_project_id (Union[None, Unset, int]):
    """

    heappe_project_id: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        heappe_project_id: Union[None, Unset, int]
        if isinstance(self.heappe_project_id, Unset):
            heappe_project_id = UNSET
        else:
            heappe_project_id = self.heappe_project_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if heappe_project_id is not UNSET:
            field_dict["heappe_project_id"] = heappe_project_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_heappe_project_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        heappe_project_id = _parse_heappe_project_id(d.pop("heappe_project_id", UNSET))

        patched_lexis_link_request = cls(
            heappe_project_id=heappe_project_id,
        )

        patched_lexis_link_request.additional_properties = d
        return patched_lexis_link_request

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
