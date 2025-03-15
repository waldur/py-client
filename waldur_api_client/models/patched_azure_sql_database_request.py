from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedAzureSqlDatabaseRequest")


@_attrs_define
class PatchedAzureSqlDatabaseRequest:
    """
    Attributes:
        description (Union[Unset, str]):
        server (Union[Unset, str]):
        charset (Union[None, Unset, str]):
        collation (Union[None, Unset, str]):
    """

    description: Union[Unset, str] = UNSET
    server: Union[Unset, str] = UNSET
    charset: Union[None, Unset, str] = UNSET
    collation: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        server = self.server

        charset: Union[None, Unset, str]
        if isinstance(self.charset, Unset):
            charset = UNSET
        else:
            charset = self.charset

        collation: Union[None, Unset, str]
        if isinstance(self.collation, Unset):
            collation = UNSET
        else:
            collation = self.collation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if server is not UNSET:
            field_dict["server"] = server
        if charset is not UNSET:
            field_dict["charset"] = charset
        if collation is not UNSET:
            field_dict["collation"] = collation

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        server = self.server if isinstance(self.server, Unset) else (None, str(self.server).encode(), "text/plain")

        charset: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.charset, Unset):
            charset = UNSET
        elif isinstance(self.charset, str):
            charset = (None, str(self.charset).encode(), "text/plain")
        else:
            charset = (None, str(self.charset).encode(), "text/plain")

        collation: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.collation, Unset):
            collation = UNSET
        elif isinstance(self.collation, str):
            collation = (None, str(self.collation).encode(), "text/plain")
        else:
            collation = (None, str(self.collation).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if server is not UNSET:
            field_dict["server"] = server
        if charset is not UNSET:
            field_dict["charset"] = charset
        if collation is not UNSET:
            field_dict["collation"] = collation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        server = d.pop("server", UNSET)

        def _parse_charset(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        charset = _parse_charset(d.pop("charset", UNSET))

        def _parse_collation(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        collation = _parse_collation(d.pop("collation", UNSET))

        patched_azure_sql_database_request = cls(
            description=description,
            server=server,
            charset=charset,
            collation=collation,
        )

        patched_azure_sql_database_request.additional_properties = d
        return patched_azure_sql_database_request

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
