from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OfferingBackendMetadataRequest")


@_attrs_define
class OfferingBackendMetadataRequest:
    """
    Attributes:
        backend_metadata (Union[Unset, Any]):
    """

    backend_metadata: Union[Unset, Any] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backend_metadata = self.backend_metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backend_metadata is not UNSET:
            field_dict["backend_metadata"] = backend_metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        backend_metadata = d.pop("backend_metadata", UNSET)

        offering_backend_metadata_request = cls(
            backend_metadata=backend_metadata,
        )

        offering_backend_metadata_request.additional_properties = d
        return offering_backend_metadata_request

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
