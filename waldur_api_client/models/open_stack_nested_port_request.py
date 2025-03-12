from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenStackNestedPortRequest")


@_attrs_define
class OpenStackNestedPortRequest:
    """
    Attributes:
        subnet (Union[None, Unset, str]):
    """

    subnet: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subnet: Union[None, Unset, str]
        if isinstance(self.subnet, Unset):
            subnet = UNSET
        else:
            subnet = self.subnet

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subnet is not UNSET:
            field_dict["subnet"] = subnet

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_subnet(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        subnet = _parse_subnet(d.pop("subnet", UNSET))

        open_stack_nested_port_request = cls(
            subnet=subnet,
        )

        open_stack_nested_port_request.additional_properties = d
        return open_stack_nested_port_request

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
