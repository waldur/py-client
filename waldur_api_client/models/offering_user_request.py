import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="OfferingUserRequest")


@_attrs_define
class OfferingUserRequest:
    """
    Attributes:
        user (str):
        offering (str):
        username (Union[None, Unset, str]):
        propagation_date (Union[None, Unset, datetime.datetime]):
    """

    user: str
    offering: str
    username: Union[None, Unset, str] = UNSET
    propagation_date: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user = self.user

        offering = self.offering

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
                "user": user,
                "offering": offering,
            }
        )
        if username is not UNSET:
            field_dict["username"] = username
        if propagation_date is not UNSET:
            field_dict["propagation_date"] = propagation_date

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        user = (None, str(self.user).encode(), "text/plain")

        offering = (None, str(self.offering).encode(), "text/plain")

        username: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.username, Unset):
            username = UNSET
        elif isinstance(self.username, str):
            username = (None, str(self.username).encode(), "text/plain")
        else:
            username = (None, str(self.username).encode(), "text/plain")

        propagation_date: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.propagation_date, Unset):
            propagation_date = UNSET
        elif isinstance(self.propagation_date, datetime.datetime):
            propagation_date = self.propagation_date.isoformat().encode()
        else:
            propagation_date = (None, str(self.propagation_date).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "user": user,
                "offering": offering,
            }
        )
        if username is not UNSET:
            field_dict["username"] = username
        if propagation_date is not UNSET:
            field_dict["propagation_date"] = propagation_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user = d.pop("user")

        offering = d.pop("offering")

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

        offering_user_request = cls(
            user=user,
            offering=offering,
            username=username,
            propagation_date=propagation_date,
        )

        offering_user_request.additional_properties = d
        return offering_user_request

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
