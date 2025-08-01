from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.role_type import RoleType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RoleDetails")


@_attrs_define
class RoleDetails:
    """
    Attributes:
        uuid (Union[Unset, UUID]):
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        description_en (Union[None, Unset, str]):
        description_et (Union[None, Unset, str]):
        description_lt (Union[None, Unset, str]):
        description_lv (Union[None, Unset, str]):
        description_ru (Union[None, Unset, str]):
        description_it (Union[None, Unset, str]):
        description_de (Union[None, Unset, str]):
        description_da (Union[None, Unset, str]):
        description_sv (Union[None, Unset, str]):
        description_es (Union[None, Unset, str]):
        description_fr (Union[None, Unset, str]):
        description_nb (Union[None, Unset, str]):
        description_ar (Union[None, Unset, str]):
        description_cs (Union[None, Unset, str]):
        permissions (Union[Unset, list[str]]):
        is_system_role (Union[Unset, bool]):
        is_active (Union[Unset, bool]):
        users_count (Union[Unset, int]):
        content_type (Union[Unset, RoleType]):
    """

    uuid: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    description_en: Union[None, Unset, str] = UNSET
    description_et: Union[None, Unset, str] = UNSET
    description_lt: Union[None, Unset, str] = UNSET
    description_lv: Union[None, Unset, str] = UNSET
    description_ru: Union[None, Unset, str] = UNSET
    description_it: Union[None, Unset, str] = UNSET
    description_de: Union[None, Unset, str] = UNSET
    description_da: Union[None, Unset, str] = UNSET
    description_sv: Union[None, Unset, str] = UNSET
    description_es: Union[None, Unset, str] = UNSET
    description_fr: Union[None, Unset, str] = UNSET
    description_nb: Union[None, Unset, str] = UNSET
    description_ar: Union[None, Unset, str] = UNSET
    description_cs: Union[None, Unset, str] = UNSET
    permissions: Union[Unset, list[str]] = UNSET
    is_system_role: Union[Unset, bool] = UNSET
    is_active: Union[Unset, bool] = UNSET
    users_count: Union[Unset, int] = UNSET
    content_type: Union[Unset, RoleType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid: Union[Unset, str] = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        name = self.name

        description = self.description

        description_en: Union[None, Unset, str]
        if isinstance(self.description_en, Unset):
            description_en = UNSET
        else:
            description_en = self.description_en

        description_et: Union[None, Unset, str]
        if isinstance(self.description_et, Unset):
            description_et = UNSET
        else:
            description_et = self.description_et

        description_lt: Union[None, Unset, str]
        if isinstance(self.description_lt, Unset):
            description_lt = UNSET
        else:
            description_lt = self.description_lt

        description_lv: Union[None, Unset, str]
        if isinstance(self.description_lv, Unset):
            description_lv = UNSET
        else:
            description_lv = self.description_lv

        description_ru: Union[None, Unset, str]
        if isinstance(self.description_ru, Unset):
            description_ru = UNSET
        else:
            description_ru = self.description_ru

        description_it: Union[None, Unset, str]
        if isinstance(self.description_it, Unset):
            description_it = UNSET
        else:
            description_it = self.description_it

        description_de: Union[None, Unset, str]
        if isinstance(self.description_de, Unset):
            description_de = UNSET
        else:
            description_de = self.description_de

        description_da: Union[None, Unset, str]
        if isinstance(self.description_da, Unset):
            description_da = UNSET
        else:
            description_da = self.description_da

        description_sv: Union[None, Unset, str]
        if isinstance(self.description_sv, Unset):
            description_sv = UNSET
        else:
            description_sv = self.description_sv

        description_es: Union[None, Unset, str]
        if isinstance(self.description_es, Unset):
            description_es = UNSET
        else:
            description_es = self.description_es

        description_fr: Union[None, Unset, str]
        if isinstance(self.description_fr, Unset):
            description_fr = UNSET
        else:
            description_fr = self.description_fr

        description_nb: Union[None, Unset, str]
        if isinstance(self.description_nb, Unset):
            description_nb = UNSET
        else:
            description_nb = self.description_nb

        description_ar: Union[None, Unset, str]
        if isinstance(self.description_ar, Unset):
            description_ar = UNSET
        else:
            description_ar = self.description_ar

        description_cs: Union[None, Unset, str]
        if isinstance(self.description_cs, Unset):
            description_cs = UNSET
        else:
            description_cs = self.description_cs

        permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions

        is_system_role = self.is_system_role

        is_active = self.is_active

        users_count = self.users_count

        content_type: Union[Unset, str] = UNSET
        if not isinstance(self.content_type, Unset):
            content_type = self.content_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if description_en is not UNSET:
            field_dict["description_en"] = description_en
        if description_et is not UNSET:
            field_dict["description_et"] = description_et
        if description_lt is not UNSET:
            field_dict["description_lt"] = description_lt
        if description_lv is not UNSET:
            field_dict["description_lv"] = description_lv
        if description_ru is not UNSET:
            field_dict["description_ru"] = description_ru
        if description_it is not UNSET:
            field_dict["description_it"] = description_it
        if description_de is not UNSET:
            field_dict["description_de"] = description_de
        if description_da is not UNSET:
            field_dict["description_da"] = description_da
        if description_sv is not UNSET:
            field_dict["description_sv"] = description_sv
        if description_es is not UNSET:
            field_dict["description_es"] = description_es
        if description_fr is not UNSET:
            field_dict["description_fr"] = description_fr
        if description_nb is not UNSET:
            field_dict["description_nb"] = description_nb
        if description_ar is not UNSET:
            field_dict["description_ar"] = description_ar
        if description_cs is not UNSET:
            field_dict["description_cs"] = description_cs
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if is_system_role is not UNSET:
            field_dict["is_system_role"] = is_system_role
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if users_count is not UNSET:
            field_dict["users_count"] = users_count
        if content_type is not UNSET:
            field_dict["content_type"] = content_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _uuid = d.pop("uuid", UNSET)
        uuid: Union[Unset, UUID]
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        def _parse_description_en(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description_en = _parse_description_en(d.pop("description_en", UNSET))

        def _parse_description_et(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description_et = _parse_description_et(d.pop("description_et", UNSET))

        def _parse_description_lt(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description_lt = _parse_description_lt(d.pop("description_lt", UNSET))

        def _parse_description_lv(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description_lv = _parse_description_lv(d.pop("description_lv", UNSET))

        def _parse_description_ru(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description_ru = _parse_description_ru(d.pop("description_ru", UNSET))

        def _parse_description_it(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description_it = _parse_description_it(d.pop("description_it", UNSET))

        def _parse_description_de(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description_de = _parse_description_de(d.pop("description_de", UNSET))

        def _parse_description_da(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description_da = _parse_description_da(d.pop("description_da", UNSET))

        def _parse_description_sv(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description_sv = _parse_description_sv(d.pop("description_sv", UNSET))

        def _parse_description_es(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description_es = _parse_description_es(d.pop("description_es", UNSET))

        def _parse_description_fr(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description_fr = _parse_description_fr(d.pop("description_fr", UNSET))

        def _parse_description_nb(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description_nb = _parse_description_nb(d.pop("description_nb", UNSET))

        def _parse_description_ar(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description_ar = _parse_description_ar(d.pop("description_ar", UNSET))

        def _parse_description_cs(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description_cs = _parse_description_cs(d.pop("description_cs", UNSET))

        permissions = cast(list[str], d.pop("permissions", UNSET))

        is_system_role = d.pop("is_system_role", UNSET)

        is_active = d.pop("is_active", UNSET)

        users_count = d.pop("users_count", UNSET)

        _content_type = d.pop("content_type", UNSET)
        content_type: Union[Unset, RoleType]
        if isinstance(_content_type, Unset):
            content_type = UNSET
        else:
            content_type = RoleType(_content_type)

        role_details = cls(
            uuid=uuid,
            name=name,
            description=description,
            description_en=description_en,
            description_et=description_et,
            description_lt=description_lt,
            description_lv=description_lv,
            description_ru=description_ru,
            description_it=description_it,
            description_de=description_de,
            description_da=description_da,
            description_sv=description_sv,
            description_es=description_es,
            description_fr=description_fr,
            description_nb=description_nb,
            description_ar=description_ar,
            description_cs=description_cs,
            permissions=permissions,
            is_system_role=is_system_role,
            is_active=is_active,
            users_count=users_count,
            content_type=content_type,
        )

        role_details.additional_properties = d
        return role_details

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
