import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fingerprint import Fingerprint


T = TypeVar("T", bound="RobotAccount")


@_attrs_define
class RobotAccount:
    """
    Attributes:
        url (str):
        uuid (UUID):
        created (datetime.datetime):
        modified (datetime.datetime):
        type_ (str):
        resource (str):
        backend_id (str):
        fingerprints (list['Fingerprint']):
        error_message (str):
        error_traceback (str):
        username (Union[Unset, str]):
        users (Union[Unset, list[str]]):
        keys (Union[Unset, Any]):
        responsible_user (Union[None, Unset, str]):
        state (Union[Unset, str]):
    """

    url: str
    uuid: UUID
    created: datetime.datetime
    modified: datetime.datetime
    type_: str
    resource: str
    backend_id: str
    fingerprints: list["Fingerprint"]
    error_message: str
    error_traceback: str
    username: Union[Unset, str] = UNSET
    users: Union[Unset, list[str]] = UNSET
    keys: Union[Unset, Any] = UNSET
    responsible_user: Union[None, Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        uuid = str(self.uuid)

        created = self.created.isoformat()

        modified = self.modified.isoformat()

        type_ = self.type_

        resource = self.resource

        backend_id = self.backend_id

        fingerprints = []
        for fingerprints_item_data in self.fingerprints:
            fingerprints_item = fingerprints_item_data.to_dict()
            fingerprints.append(fingerprints_item)

        error_message = self.error_message

        error_traceback = self.error_traceback

        username = self.username

        users: Union[Unset, list[str]] = UNSET
        if not isinstance(self.users, Unset):
            users = self.users

        keys = self.keys

        responsible_user: Union[None, Unset, str]
        if isinstance(self.responsible_user, Unset):
            responsible_user = UNSET
        else:
            responsible_user = self.responsible_user

        state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "uuid": uuid,
                "created": created,
                "modified": modified,
                "type": type_,
                "resource": resource,
                "backend_id": backend_id,
                "fingerprints": fingerprints,
                "error_message": error_message,
                "error_traceback": error_traceback,
            }
        )
        if username is not UNSET:
            field_dict["username"] = username
        if users is not UNSET:
            field_dict["users"] = users
        if keys is not UNSET:
            field_dict["keys"] = keys
        if responsible_user is not UNSET:
            field_dict["responsible_user"] = responsible_user
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fingerprint import Fingerprint

        d = dict(src_dict)
        url = d.pop("url")

        uuid = UUID(d.pop("uuid"))

        created = isoparse(d.pop("created"))

        modified = isoparse(d.pop("modified"))

        type_ = d.pop("type")

        resource = d.pop("resource")

        backend_id = d.pop("backend_id")

        fingerprints = []
        _fingerprints = d.pop("fingerprints")
        for fingerprints_item_data in _fingerprints:
            fingerprints_item = Fingerprint.from_dict(fingerprints_item_data)

            fingerprints.append(fingerprints_item)

        error_message = d.pop("error_message")

        error_traceback = d.pop("error_traceback")

        username = d.pop("username", UNSET)

        users = cast(list[str], d.pop("users", UNSET))

        keys = d.pop("keys", UNSET)

        def _parse_responsible_user(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        responsible_user = _parse_responsible_user(d.pop("responsible_user", UNSET))

        state = d.pop("state", UNSET)

        robot_account = cls(
            url=url,
            uuid=uuid,
            created=created,
            modified=modified,
            type_=type_,
            resource=resource,
            backend_id=backend_id,
            fingerprints=fingerprints,
            error_message=error_message,
            error_traceback=error_traceback,
            username=username,
            users=users,
            keys=keys,
            responsible_user=responsible_user,
            state=state,
        )

        robot_account.additional_properties = d
        return robot_account

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
