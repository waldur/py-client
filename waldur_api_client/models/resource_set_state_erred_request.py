from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResourceSetStateErredRequest")


@_attrs_define
class ResourceSetStateErredRequest:
    """
    Attributes:
        error_message (Union[Unset, str]):
        error_traceback (Union[Unset, str]):
    """

    error_message: Union[Unset, str] = UNSET
    error_traceback: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error_message = self.error_message

        error_traceback = self.error_traceback

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if error_traceback is not UNSET:
            field_dict["error_traceback"] = error_traceback

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        error_message = (
            self.error_message
            if isinstance(self.error_message, Unset)
            else (None, str(self.error_message).encode(), "text/plain")
        )

        error_traceback = (
            self.error_traceback
            if isinstance(self.error_traceback, Unset)
            else (None, str(self.error_traceback).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if error_traceback is not UNSET:
            field_dict["error_traceback"] = error_traceback

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error_message = d.pop("error_message", UNSET)

        error_traceback = d.pop("error_traceback", UNSET)

        resource_set_state_erred_request = cls(
            error_message=error_message,
            error_traceback=error_traceback,
        )

        resource_set_state_erred_request.additional_properties = d
        return resource_set_state_erred_request

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
