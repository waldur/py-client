from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ResourceOptionSecretSetRequest")


@_attrs_define
class ResourceOptionSecretSetRequest:
    """
    Attributes:
        option_name (str): Name of a secret option of the offering.
        value (str): The secret, checked against the option's length limits; on a single line unless the option is
            multiline. Never returned.
    """

    option_name: str
    value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        option_name = self.option_name

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "option_name": option_name,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        option_name = d.pop("option_name")

        value = d.pop("value")

        resource_option_secret_set_request = cls(
            option_name=option_name,
            value=value,
        )

        resource_option_secret_set_request.additional_properties = d
        return resource_option_secret_set_request

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
