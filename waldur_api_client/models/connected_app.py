import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.registration_source_enum import RegistrationSourceEnum

if TYPE_CHECKING:
    from ..models.consent_scope import ConsentScope


T = TypeVar("T", bound="ConnectedApp")


@_attrs_define
class ConnectedApp:
    """
    Attributes:
        uuid (UUID):
        client_name (str):
        client_host (Union[None, str]):
        redirect_hosts (list[str]):
        registration_source (RegistrationSourceEnum):
        scopes (list['ConsentScope']):
        authorized_at (datetime.datetime):
        last_used_at (Union[None, datetime.datetime]):
    """

    uuid: UUID
    client_name: str
    client_host: Union[None, str]
    redirect_hosts: list[str]
    registration_source: RegistrationSourceEnum
    scopes: list["ConsentScope"]
    authorized_at: datetime.datetime
    last_used_at: Union[None, datetime.datetime]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        client_name = self.client_name

        client_host: Union[None, str]
        client_host = self.client_host

        redirect_hosts = self.redirect_hosts

        registration_source = self.registration_source.value

        scopes = []
        for scopes_item_data in self.scopes:
            scopes_item = scopes_item_data.to_dict()
            scopes.append(scopes_item)

        authorized_at = self.authorized_at.isoformat()

        last_used_at: Union[None, str]
        if isinstance(self.last_used_at, datetime.datetime):
            last_used_at = self.last_used_at.isoformat()
        else:
            last_used_at = self.last_used_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "client_name": client_name,
                "client_host": client_host,
                "redirect_hosts": redirect_hosts,
                "registration_source": registration_source,
                "scopes": scopes,
                "authorized_at": authorized_at,
                "last_used_at": last_used_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.consent_scope import ConsentScope

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        client_name = d.pop("client_name")

        def _parse_client_host(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        client_host = _parse_client_host(d.pop("client_host"))

        redirect_hosts = cast(list[str], d.pop("redirect_hosts"))

        registration_source = RegistrationSourceEnum(d.pop("registration_source"))

        scopes = []
        _scopes = d.pop("scopes")
        for scopes_item_data in _scopes:
            scopes_item = ConsentScope.from_dict(scopes_item_data)

            scopes.append(scopes_item)

        authorized_at = isoparse(d.pop("authorized_at"))

        def _parse_last_used_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_used_at_type_0 = isoparse(data)

                return last_used_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        last_used_at = _parse_last_used_at(d.pop("last_used_at"))

        connected_app = cls(
            uuid=uuid,
            client_name=client_name,
            client_host=client_host,
            redirect_hosts=redirect_hosts,
            registration_source=registration_source,
            scopes=scopes,
            authorized_at=authorized_at,
            last_used_at=last_used_at,
        )

        connected_app.additional_properties = d
        return connected_app

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
