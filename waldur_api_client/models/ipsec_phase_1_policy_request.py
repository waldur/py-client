from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ipsec_dh_group_enum import IpsecDhGroupEnum
from ..models.ipsec_encryption_enum import IpsecEncryptionEnum
from ..models.ipsec_integrity_enum import IpsecIntegrityEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ipsec_phase_1_request import IpsecPhase1Request


T = TypeVar("T", bound="IpsecPhase1PolicyRequest")


@_attrs_define
class IpsecPhase1PolicyRequest:
    """
    Attributes:
        encryption (Union[Unset, list[IpsecEncryptionEnum]]): Allowed. Every algorithm when omitted.
        integrity (Union[Unset, list[IpsecIntegrityEnum]]): Allowed. Every algorithm but sha1 when omitted.
        dh_groups (Union[Unset, list[IpsecDhGroupEnum]]): Allowed. Every group but 2 and 5 when omitted.
        lifetime_min (Union[Unset, int]):
        lifetime_max (Union[Unset, int]):
        defaults (Union[Unset, IpsecPhase1Request]):
    """

    encryption: Union[Unset, list[IpsecEncryptionEnum]] = UNSET
    integrity: Union[Unset, list[IpsecIntegrityEnum]] = UNSET
    dh_groups: Union[Unset, list[IpsecDhGroupEnum]] = UNSET
    lifetime_min: Union[Unset, int] = UNSET
    lifetime_max: Union[Unset, int] = UNSET
    defaults: Union[Unset, "IpsecPhase1Request"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        encryption: Union[Unset, list[str]] = UNSET
        if not isinstance(self.encryption, Unset):
            encryption = []
            for encryption_item_data in self.encryption:
                encryption_item = encryption_item_data.value
                encryption.append(encryption_item)

        integrity: Union[Unset, list[str]] = UNSET
        if not isinstance(self.integrity, Unset):
            integrity = []
            for integrity_item_data in self.integrity:
                integrity_item = integrity_item_data.value
                integrity.append(integrity_item)

        dh_groups: Union[Unset, list[int]] = UNSET
        if not isinstance(self.dh_groups, Unset):
            dh_groups = []
            for dh_groups_item_data in self.dh_groups:
                dh_groups_item = dh_groups_item_data.value
                dh_groups.append(dh_groups_item)

        lifetime_min = self.lifetime_min

        lifetime_max = self.lifetime_max

        defaults: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.defaults, Unset):
            defaults = self.defaults.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if encryption is not UNSET:
            field_dict["encryption"] = encryption
        if integrity is not UNSET:
            field_dict["integrity"] = integrity
        if dh_groups is not UNSET:
            field_dict["dh_groups"] = dh_groups
        if lifetime_min is not UNSET:
            field_dict["lifetime_min"] = lifetime_min
        if lifetime_max is not UNSET:
            field_dict["lifetime_max"] = lifetime_max
        if defaults is not UNSET:
            field_dict["defaults"] = defaults

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ipsec_phase_1_request import IpsecPhase1Request

        d = dict(src_dict)
        encryption = []
        _encryption = d.pop("encryption", UNSET)
        for encryption_item_data in _encryption or []:
            encryption_item = IpsecEncryptionEnum(encryption_item_data)

            encryption.append(encryption_item)

        integrity = []
        _integrity = d.pop("integrity", UNSET)
        for integrity_item_data in _integrity or []:
            integrity_item = IpsecIntegrityEnum(integrity_item_data)

            integrity.append(integrity_item)

        dh_groups = []
        _dh_groups = d.pop("dh_groups", UNSET)
        for dh_groups_item_data in _dh_groups or []:
            dh_groups_item = IpsecDhGroupEnum(dh_groups_item_data)

            dh_groups.append(dh_groups_item)

        lifetime_min = d.pop("lifetime_min", UNSET)

        lifetime_max = d.pop("lifetime_max", UNSET)

        _defaults = d.pop("defaults", UNSET)
        defaults: Union[Unset, IpsecPhase1Request]
        if isinstance(_defaults, Unset):
            defaults = UNSET
        else:
            defaults = IpsecPhase1Request.from_dict(_defaults)

        ipsec_phase_1_policy_request = cls(
            encryption=encryption,
            integrity=integrity,
            dh_groups=dh_groups,
            lifetime_min=lifetime_min,
            lifetime_max=lifetime_max,
            defaults=defaults,
        )

        ipsec_phase_1_policy_request.additional_properties = d
        return ipsec_phase_1_policy_request

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
