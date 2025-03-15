from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RequestedOfferingRequest")


@_attrs_define
class RequestedOfferingRequest:
    """
    Attributes:
        offering (str):
        attributes (Union[Unset, Any]):
        plan (Union[None, Unset, str]):
        description (Union[Unset, str]):
    """

    offering: str
    attributes: Union[Unset, Any] = UNSET
    plan: Union[None, Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        offering = self.offering

        attributes = self.attributes

        plan: Union[None, Unset, str]
        if isinstance(self.plan, Unset):
            plan = UNSET
        else:
            plan = self.plan

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "offering": offering,
            }
        )
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if plan is not UNSET:
            field_dict["plan"] = plan
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        offering = (None, str(self.offering).encode(), "text/plain")

        attributes = (
            self.attributes
            if isinstance(self.attributes, Unset)
            else (None, str(self.attributes).encode(), "text/plain")
        )

        plan: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.plan, Unset):
            plan = UNSET
        elif isinstance(self.plan, str):
            plan = (None, str(self.plan).encode(), "text/plain")
        else:
            plan = (None, str(self.plan).encode(), "text/plain")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "offering": offering,
            }
        )
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if plan is not UNSET:
            field_dict["plan"] = plan
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        offering = d.pop("offering")

        attributes = d.pop("attributes", UNSET)

        def _parse_plan(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        plan = _parse_plan(d.pop("plan", UNSET))

        description = d.pop("description", UNSET)

        requested_offering_request = cls(
            offering=offering,
            attributes=attributes,
            plan=plan,
            description=description,
        )

        requested_offering_request.additional_properties = d
        return requested_offering_request

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
