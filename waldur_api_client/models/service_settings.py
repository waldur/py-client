from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_settings_state_enum import ServiceSettingsStateEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_settings_options import ServiceSettingsOptions


T = TypeVar("T", bound="ServiceSettings")


@_attrs_define
class ServiceSettings:
    """
    Attributes:
        url (str):
        uuid (UUID):
        name (str):
        type_ (str):
        state (ServiceSettingsStateEnum):
        error_message (str):
        customer_name (str):
        customer_native_name (str):
        scope_uuid (UUID):
        options (ServiceSettingsOptions):
        shared (Union[Unset, bool]): Anybody can use it
        customer (Union[None, Unset, str]):
        terms_of_services (Union[Unset, str]):
        scope (Union[None, Unset, str]):
    """

    url: str
    uuid: UUID
    name: str
    type_: str
    state: ServiceSettingsStateEnum
    error_message: str
    customer_name: str
    customer_native_name: str
    scope_uuid: UUID
    options: "ServiceSettingsOptions"
    shared: Union[Unset, bool] = UNSET
    customer: Union[None, Unset, str] = UNSET
    terms_of_services: Union[Unset, str] = UNSET
    scope: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        uuid = str(self.uuid)

        name = self.name

        type_ = self.type_

        state = self.state.value

        error_message = self.error_message

        customer_name = self.customer_name

        customer_native_name = self.customer_native_name

        scope_uuid = str(self.scope_uuid)

        options = self.options.to_dict()

        shared = self.shared

        customer: Union[None, Unset, str]
        if isinstance(self.customer, Unset):
            customer = UNSET
        else:
            customer = self.customer

        terms_of_services = self.terms_of_services

        scope: Union[None, Unset, str]
        if isinstance(self.scope, Unset):
            scope = UNSET
        else:
            scope = self.scope

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "uuid": uuid,
                "name": name,
                "type": type_,
                "state": state,
                "error_message": error_message,
                "customer_name": customer_name,
                "customer_native_name": customer_native_name,
                "scope_uuid": scope_uuid,
                "options": options,
            }
        )
        if shared is not UNSET:
            field_dict["shared"] = shared
        if customer is not UNSET:
            field_dict["customer"] = customer
        if terms_of_services is not UNSET:
            field_dict["terms_of_services"] = terms_of_services
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_settings_options import ServiceSettingsOptions

        d = dict(src_dict)
        url = d.pop("url")

        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        type_ = d.pop("type")

        state = ServiceSettingsStateEnum(d.pop("state"))

        error_message = d.pop("error_message")

        customer_name = d.pop("customer_name")

        customer_native_name = d.pop("customer_native_name")

        scope_uuid = UUID(d.pop("scope_uuid"))

        options = ServiceSettingsOptions.from_dict(d.pop("options"))

        shared = d.pop("shared", UNSET)

        def _parse_customer(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        customer = _parse_customer(d.pop("customer", UNSET))

        terms_of_services = d.pop("terms_of_services", UNSET)

        def _parse_scope(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        scope = _parse_scope(d.pop("scope", UNSET))

        service_settings = cls(
            url=url,
            uuid=uuid,
            name=name,
            type_=type_,
            state=state,
            error_message=error_message,
            customer_name=customer_name,
            customer_native_name=customer_native_name,
            scope_uuid=scope_uuid,
            options=options,
            shared=shared,
            customer=customer,
            terms_of_services=terms_of_services,
            scope=scope,
        )

        service_settings.additional_properties = d
        return service_settings

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
