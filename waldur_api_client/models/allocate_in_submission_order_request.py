from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.on_depleted_enum import OnDepletedEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="AllocateInSubmissionOrderRequest")


@_attrs_define
class AllocateInSubmissionOrderRequest:
    """
    Attributes:
        preview (Union[Unset, bool]): Only plan the decisions and return the plan; decide nothing. Default: True.
        on_depleted (Union[Unset, OnDepletedEnum]):  Default: OnDepletedEnum.DECLINE.
        force (Union[Unset, bool]): Allocate although some proposals of the round have not reached the allocation
            decision yet. Needs a reason. Default: False.
        reason (Union[Unset, str]):  Default: ''.
    """

    preview: Union[Unset, bool] = True
    on_depleted: Union[Unset, OnDepletedEnum] = OnDepletedEnum.DECLINE
    force: Union[Unset, bool] = False
    reason: Union[Unset, str] = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        preview = self.preview

        on_depleted: Union[Unset, str] = UNSET
        if not isinstance(self.on_depleted, Unset):
            on_depleted = self.on_depleted.value

        force = self.force

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if preview is not UNSET:
            field_dict["preview"] = preview
        if on_depleted is not UNSET:
            field_dict["on_depleted"] = on_depleted
        if force is not UNSET:
            field_dict["force"] = force
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        preview = d.pop("preview", UNSET)

        _on_depleted = d.pop("on_depleted", UNSET)
        on_depleted: Union[Unset, OnDepletedEnum]
        if isinstance(_on_depleted, Unset):
            on_depleted = UNSET
        else:
            on_depleted = OnDepletedEnum(_on_depleted)

        force = d.pop("force", UNSET)

        reason = d.pop("reason", UNSET)

        allocate_in_submission_order_request = cls(
            preview=preview,
            on_depleted=on_depleted,
            force=force,
            reason=reason,
        )

        allocate_in_submission_order_request.additional_properties = d
        return allocate_in_submission_order_request

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
