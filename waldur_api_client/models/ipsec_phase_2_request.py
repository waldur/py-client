from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ipsec_dh_group_enum import IpsecDhGroupEnum
from ..models.ipsec_encryption_enum import IpsecEncryptionEnum
from ..models.ipsec_integrity_enum import IpsecIntegrityEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="IpsecPhase2Request")


@_attrs_define
class IpsecPhase2Request:
    """
    Attributes:
        encryption (Union[Unset, IpsecEncryptionEnum]):
        integrity (Union[Unset, IpsecIntegrityEnum]):
        pfs_group (Union[IpsecDhGroupEnum, None, Unset]): Null for no perfect forward secrecy.
        lifetime (Union[Unset, int]): In seconds.
    """

    encryption: Union[Unset, IpsecEncryptionEnum] = UNSET
    integrity: Union[Unset, IpsecIntegrityEnum] = UNSET
    pfs_group: Union[IpsecDhGroupEnum, None, Unset] = UNSET
    lifetime: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        encryption: Union[Unset, str] = UNSET
        if not isinstance(self.encryption, Unset):
            encryption = self.encryption.value

        integrity: Union[Unset, str] = UNSET
        if not isinstance(self.integrity, Unset):
            integrity = self.integrity.value

        pfs_group: Union[None, Unset, int]
        if isinstance(self.pfs_group, Unset):
            pfs_group = UNSET
        elif isinstance(self.pfs_group, IpsecDhGroupEnum):
            pfs_group = self.pfs_group.value
        else:
            pfs_group = self.pfs_group

        lifetime = self.lifetime

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if encryption is not UNSET:
            field_dict["encryption"] = encryption
        if integrity is not UNSET:
            field_dict["integrity"] = integrity
        if pfs_group is not UNSET:
            field_dict["pfs_group"] = pfs_group
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

        def _parse_pfs_group(data: object) -> Union[IpsecDhGroupEnum, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, int):
                    raise TypeError()
                pfs_group_type_0 = IpsecDhGroupEnum(data)

                return pfs_group_type_0
            except:  # noqa: E722
                pass
            return cast(Union[IpsecDhGroupEnum, None, Unset], data)

        pfs_group = _parse_pfs_group(d.pop("pfs_group", UNSET))

        lifetime = d.pop("lifetime", UNSET)

        ipsec_phase_2_request = cls(
            encryption=encryption,
            integrity=integrity,
            pfs_group=pfs_group,
            lifetime=lifetime,
        )

        ipsec_phase_2_request.additional_properties = d
        return ipsec_phase_2_request

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
