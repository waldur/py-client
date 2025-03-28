from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RequestedResourceRequest")


@_attrs_define
class RequestedResourceRequest:
    """
    Attributes:
        requested_offering_uuid (UUID):
        attributes (Union[Unset, Any]):
        limits (Union[Unset, Any]):
        description (Union[Unset, str]):
    """

    requested_offering_uuid: UUID
    attributes: Union[Unset, Any] = UNSET
    limits: Union[Unset, Any] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        requested_offering_uuid = str(self.requested_offering_uuid)

        attributes = self.attributes

        limits = self.limits

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "requested_offering_uuid": requested_offering_uuid,
            }
        )
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if limits is not UNSET:
            field_dict["limits"] = limits
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        requested_offering_uuid = UUID(d.pop("requested_offering_uuid"))

        attributes = d.pop("attributes", UNSET)

        limits = d.pop("limits", UNSET)

        description = d.pop("description", UNSET)

        requested_resource_request = cls(
            requested_offering_uuid=requested_offering_uuid,
            attributes=attributes,
            limits=limits,
            description=description,
        )

        requested_resource_request.additional_properties = d
        return requested_resource_request

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
