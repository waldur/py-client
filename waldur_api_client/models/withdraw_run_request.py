from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WithdrawRunRequest")


@_attrs_define
class WithdrawRunRequest:
    """
    Attributes:
        run_uuid (Union[Unset, UUID]): The run to call off; the proposal's open one when left out.
    """

    run_uuid: Union[Unset, UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        run_uuid: Union[Unset, str] = UNSET
        if not isinstance(self.run_uuid, Unset):
            run_uuid = str(self.run_uuid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if run_uuid is not UNSET:
            field_dict["run_uuid"] = run_uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _run_uuid = d.pop("run_uuid", UNSET)
        run_uuid: Union[Unset, UUID]
        if isinstance(_run_uuid, Unset):
            run_uuid = UNSET
        else:
            run_uuid = UUID(_run_uuid)

        withdraw_run_request = cls(
            run_uuid=run_uuid,
        )

        withdraw_run_request.additional_properties = d
        return withdraw_run_request

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
