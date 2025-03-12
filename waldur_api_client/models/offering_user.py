import datetime
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="OfferingUser")


@_attrs_define
class OfferingUser:
    """
    Attributes:
        url (str):
        uuid (UUID):
        user (str):
        offering (str):
        offering_uuid (UUID):
        offering_name (str):
        user_uuid (UUID):
        user_username (str): Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters
        user_full_name (str):
        created (datetime.datetime):
        modified (datetime.datetime):
        customer_uuid (UUID):
        customer_name (str):
        is_restricted (bool): Signal to service if the user account is restricted or not
        username (Union[None, Unset, str]):
        propagation_date (Union[None, Unset, datetime.datetime]):
    """

    url: str
    uuid: UUID
    user: str
    offering: str
    offering_uuid: UUID
    offering_name: str
    user_uuid: UUID
    user_username: str
    user_full_name: str
    created: datetime.datetime
    modified: datetime.datetime
    customer_uuid: UUID
    customer_name: str
    is_restricted: bool
    username: Union[None, Unset, str] = UNSET
    propagation_date: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        uuid = str(self.uuid)

        user = self.user

        offering = self.offering

        offering_uuid = str(self.offering_uuid)

        offering_name = self.offering_name

        user_uuid = str(self.user_uuid)

        user_username = self.user_username

        user_full_name = self.user_full_name

        created = self.created.isoformat()

        modified = self.modified.isoformat()

        customer_uuid = str(self.customer_uuid)

        customer_name = self.customer_name

        is_restricted = self.is_restricted

        username: Union[None, Unset, str]
        if isinstance(self.username, Unset):
            username = UNSET
        else:
            username = self.username

        propagation_date: Union[None, Unset, str]
        if isinstance(self.propagation_date, Unset):
            propagation_date = UNSET
        elif isinstance(self.propagation_date, datetime.datetime):
            propagation_date = self.propagation_date.isoformat()
        else:
            propagation_date = self.propagation_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "uuid": uuid,
                "user": user,
                "offering": offering,
                "offering_uuid": offering_uuid,
                "offering_name": offering_name,
                "user_uuid": user_uuid,
                "user_username": user_username,
                "user_full_name": user_full_name,
                "created": created,
                "modified": modified,
                "customer_uuid": customer_uuid,
                "customer_name": customer_name,
                "is_restricted": is_restricted,
            }
        )
        if username is not UNSET:
            field_dict["username"] = username
        if propagation_date is not UNSET:
            field_dict["propagation_date"] = propagation_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        uuid = UUID(d.pop("uuid"))

        user = d.pop("user")

        offering = d.pop("offering")

        offering_uuid = UUID(d.pop("offering_uuid"))

        offering_name = d.pop("offering_name")

        user_uuid = UUID(d.pop("user_uuid"))

        user_username = d.pop("user_username")

        user_full_name = d.pop("user_full_name")

        created = isoparse(d.pop("created"))

        modified = isoparse(d.pop("modified"))

        customer_uuid = UUID(d.pop("customer_uuid"))

        customer_name = d.pop("customer_name")

        is_restricted = d.pop("is_restricted")

        def _parse_username(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        username = _parse_username(d.pop("username", UNSET))

        def _parse_propagation_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                propagation_date_type_0 = isoparse(data)

                return propagation_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        propagation_date = _parse_propagation_date(d.pop("propagation_date", UNSET))

        offering_user = cls(
            url=url,
            uuid=uuid,
            user=user,
            offering=offering,
            offering_uuid=offering_uuid,
            offering_name=offering_name,
            user_uuid=user_uuid,
            user_username=user_username,
            user_full_name=user_full_name,
            created=created,
            modified=modified,
            customer_uuid=customer_uuid,
            customer_name=customer_name,
            is_restricted=is_restricted,
            username=username,
            propagation_date=propagation_date,
        )

        offering_user.additional_properties = d
        return offering_user

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
