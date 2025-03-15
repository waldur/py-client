from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SshKey")


@_attrs_define
class SshKey:
    """
    Attributes:
        url (str):
        uuid (UUID):
        public_key (str):
        fingerprint_md5 (str):
        fingerprint_sha256 (str):
        fingerprint_sha512 (str):
        user_uuid (UUID):
        is_shared (bool):
        type_ (str):
        name (Union[Unset, str]):
    """

    url: str
    uuid: UUID
    public_key: str
    fingerprint_md5: str
    fingerprint_sha256: str
    fingerprint_sha512: str
    user_uuid: UUID
    is_shared: bool
    type_: str
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        uuid = str(self.uuid)

        public_key = self.public_key

        fingerprint_md5 = self.fingerprint_md5

        fingerprint_sha256 = self.fingerprint_sha256

        fingerprint_sha512 = self.fingerprint_sha512

        user_uuid = str(self.user_uuid)

        is_shared = self.is_shared

        type_ = self.type_

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "uuid": uuid,
                "public_key": public_key,
                "fingerprint_md5": fingerprint_md5,
                "fingerprint_sha256": fingerprint_sha256,
                "fingerprint_sha512": fingerprint_sha512,
                "user_uuid": user_uuid,
                "is_shared": is_shared,
                "type": type_,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        uuid = UUID(d.pop("uuid"))

        public_key = d.pop("public_key")

        fingerprint_md5 = d.pop("fingerprint_md5")

        fingerprint_sha256 = d.pop("fingerprint_sha256")

        fingerprint_sha512 = d.pop("fingerprint_sha512")

        user_uuid = UUID(d.pop("user_uuid"))

        is_shared = d.pop("is_shared")

        type_ = d.pop("type")

        name = d.pop("name", UNSET)

        ssh_key = cls(
            url=url,
            uuid=uuid,
            public_key=public_key,
            fingerprint_md5=fingerprint_md5,
            fingerprint_sha256=fingerprint_sha256,
            fingerprint_sha512=fingerprint_sha512,
            user_uuid=user_uuid,
            is_shared=is_shared,
            type_=type_,
            name=name,
        )

        ssh_key.additional_properties = d
        return ssh_key

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
