from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ManagedProjectApproveRequest")


@_attrs_define
class ManagedProjectApproveRequest:
    """
    Attributes:
        comment (Union[Unset, str]): Optional comment for review
        expected_allocation (Union[None, Unset, str]): The allocation, in credits, the reviewer is approving: the
            managed project's pending_allocation when an allocation increase is waiting, otherwise the credits of the
            requested allocation. The approval is refused with 409 if the figure has changed since. Whether or not it is
            sent, no more than the figure waiting at the time of approval is applied: a later increase waits for review
            again. Omitting it approves whatever figure is waiting when the request arrives, which may be higher than the
            one the reviewer saw.
    """

    comment: Union[Unset, str] = UNSET
    expected_allocation: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment = self.comment

        expected_allocation: Union[None, Unset, str]
        if isinstance(self.expected_allocation, Unset):
            expected_allocation = UNSET
        else:
            expected_allocation = self.expected_allocation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comment is not UNSET:
            field_dict["comment"] = comment
        if expected_allocation is not UNSET:
            field_dict["expected_allocation"] = expected_allocation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comment = d.pop("comment", UNSET)

        def _parse_expected_allocation(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        expected_allocation = _parse_expected_allocation(d.pop("expected_allocation", UNSET))

        managed_project_approve_request = cls(
            comment=comment,
            expected_allocation=expected_allocation,
        )

        managed_project_approve_request.additional_properties = d
        return managed_project_approve_request

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
