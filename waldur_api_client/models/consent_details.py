from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.elevated_access_enum import ElevatedAccessEnum
from ..models.registration_source_enum import RegistrationSourceEnum

if TYPE_CHECKING:
    from ..models.consent_scope import ConsentScope


T = TypeVar("T", bound="ConsentDetails")


@_attrs_define
class ConsentDetails:
    """
    Attributes:
        client_name (str):
        client_host (Union[None, str]):
        redirect_host (str):
        registration_source (RegistrationSourceEnum):
        scopes (list['ConsentScope']):
        elevated_access (Union[ElevatedAccessEnum, None]):
    """

    client_name: str
    client_host: Union[None, str]
    redirect_host: str
    registration_source: RegistrationSourceEnum
    scopes: list["ConsentScope"]
    elevated_access: Union[ElevatedAccessEnum, None]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_name = self.client_name

        client_host: Union[None, str]
        client_host = self.client_host

        redirect_host = self.redirect_host

        registration_source = self.registration_source.value

        scopes = []
        for scopes_item_data in self.scopes:
            scopes_item = scopes_item_data.to_dict()
            scopes.append(scopes_item)

        elevated_access: Union[None, str]
        if isinstance(self.elevated_access, ElevatedAccessEnum):
            elevated_access = self.elevated_access.value
        else:
            elevated_access = self.elevated_access

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "client_name": client_name,
                "client_host": client_host,
                "redirect_host": redirect_host,
                "registration_source": registration_source,
                "scopes": scopes,
                "elevated_access": elevated_access,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.consent_scope import ConsentScope

        d = dict(src_dict)
        client_name = d.pop("client_name")

        def _parse_client_host(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        client_host = _parse_client_host(d.pop("client_host"))

        redirect_host = d.pop("redirect_host")

        registration_source = RegistrationSourceEnum(d.pop("registration_source"))

        scopes = []
        _scopes = d.pop("scopes")
        for scopes_item_data in _scopes:
            scopes_item = ConsentScope.from_dict(scopes_item_data)

            scopes.append(scopes_item)

        def _parse_elevated_access(data: object) -> Union[ElevatedAccessEnum, None]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                elevated_access_type_0 = ElevatedAccessEnum(data)

                return elevated_access_type_0
            except:  # noqa: E722
                pass
            return cast(Union[ElevatedAccessEnum, None], data)

        elevated_access = _parse_elevated_access(d.pop("elevated_access"))

        consent_details = cls(
            client_name=client_name,
            client_host=client_host,
            redirect_host=redirect_host,
            registration_source=registration_source,
            scopes=scopes,
            elevated_access=elevated_access,
        )

        consent_details.additional_properties = d
        return consent_details

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
