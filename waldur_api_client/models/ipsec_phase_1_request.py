from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ipsec_dh_group_enum import IpsecDhGroupEnum
from ..models.ipsec_encryption_enum import IpsecEncryptionEnum
from ..models.ipsec_integrity_enum import IpsecIntegrityEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="IpsecPhase1Request")


@_attrs_define
class IpsecPhase1Request:
    """
    Attributes:
        encryption (Union[Unset, IpsecEncryptionEnum]):
        integrity (Union[Unset, IpsecIntegrityEnum]):
        dh_group (Union[Unset, IpsecDhGroupEnum]):
        lifetime (Union[Unset, int]): In seconds.
    """

    encryption: Union[Unset, IpsecEncryptionEnum] = UNSET
    integrity: Union[Unset, IpsecIntegrityEnum] = UNSET
    dh_group: Union[Unset, IpsecDhGroupEnum] = UNSET
    lifetime: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        encryption: Union[Unset, str] = UNSET
        if not isinstance(self.encryption, Unset):
            encryption = self.encryption.value

        integrity: Union[Unset, str] = UNSET
        if not isinstance(self.integrity, Unset):
            integrity = self.integrity.value

        dh_group: Union[Unset, int] = UNSET
        if not isinstance(self.dh_group, Unset):
            dh_group = self.dh_group.value

        lifetime = self.lifetime

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if encryption is not UNSET:
            field_dict["encryption"] = encryption
        if integrity is not UNSET:
            field_dict["integrity"] = integrity
        if dh_group is not UNSET:
            field_dict["dh_group"] = dh_group
        if lifetime is not UNSET:
            field_dict["lifetime"] = lifetime

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _encryption = d.pop("encryption", UNSET)
        encryption: Union[Unset, IpsecEncryptionEnum]
        if isinstance(_encryption, Unset):
            encryption = UNSET
        else:
            encryption = IpsecEncryptionEnum(_encryption)

        _integrity = d.pop("integrity", UNSET)
        integrity: Union[Unset, IpsecIntegrityEnum]
        if isinstance(_integrity, Unset):
            integrity = UNSET
        else:
            integrity = IpsecIntegrityEnum(_integrity)

        _dh_group = d.pop("dh_group", UNSET)
        dh_group: Union[Unset, IpsecDhGroupEnum]
        if isinstance(_dh_group, Unset):
            dh_group = UNSET
        else:
            dh_group = IpsecDhGroupEnum(_dh_group)

        lifetime = d.pop("lifetime", UNSET)

        ipsec_phase_1_request = cls(
            encryption=encryption,
            integrity=integrity,
            dh_group=dh_group,
            lifetime=lifetime,
        )

        ipsec_phase_1_request.additional_properties = d
        return ipsec_phase_1_request

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
