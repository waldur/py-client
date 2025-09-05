from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.issue_status_type_enum import IssueStatusTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedIssueStatusRequest")


@_attrs_define
class PatchedIssueStatusRequest:
    """
    Attributes:
        name (Union[Unset, str]): Status name in Jira.
        type_ (Union[Unset, IssueStatusTypeEnum]):
    """

    name: Union[Unset, str] = UNSET
    type_: Union[Unset, IssueStatusTypeEnum] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_: Union[Unset, int] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, IssueStatusTypeEnum]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = IssueStatusTypeEnum(_type_)

        patched_issue_status_request = cls(
            name=name,
            type_=type_,
        )

        patched_issue_status_request.additional_properties = d
        return patched_issue_status_request

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
