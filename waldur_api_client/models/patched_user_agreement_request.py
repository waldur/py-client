from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.agreement_type_enum import AgreementTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedUserAgreementRequest")


@_attrs_define
class PatchedUserAgreementRequest:
    """
    Attributes:
        content (Union[Unset, str]):
        agreement_type (Union[Unset, AgreementTypeEnum]):
    """

    content: Union[Unset, str] = UNSET
    agreement_type: Union[Unset, AgreementTypeEnum] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        agreement_type: Union[Unset, str] = UNSET
        if not isinstance(self.agreement_type, Unset):
            agreement_type = self.agreement_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if agreement_type is not UNSET:
            field_dict["agreement_type"] = agreement_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content = d.pop("content", UNSET)

        _agreement_type = d.pop("agreement_type", UNSET)
        agreement_type: Union[Unset, AgreementTypeEnum]
        if isinstance(_agreement_type, Unset):
            agreement_type = UNSET
        else:
            agreement_type = AgreementTypeEnum(_agreement_type)

        patched_user_agreement_request = cls(
            content=content,
            agreement_type=agreement_type,
        )

        patched_user_agreement_request.additional_properties = d
        return patched_user_agreement_request

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
