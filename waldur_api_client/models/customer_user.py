import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nested_project_permission import NestedProjectPermission


T = TypeVar("T", bound="CustomerUser")


@_attrs_define
class CustomerUser:
    """
    Attributes:
        url (str):
        uuid (UUID):
        username (str): Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters
        full_name (str):
        role (str):
        role_name (str):
        projects (list['NestedProjectPermission']):
        expiration_time (datetime.datetime):
        email (Union[Unset, str]):
        image (Union[None, Unset, str]):
    """

    url: str
    uuid: UUID
    username: str
    full_name: str
    role: str
    role_name: str
    projects: list["NestedProjectPermission"]
    expiration_time: datetime.datetime
    email: Union[Unset, str] = UNSET
    image: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        uuid = str(self.uuid)

        username = self.username

        full_name = self.full_name

        role = self.role

        role_name = self.role_name

        projects = []
        for projects_item_data in self.projects:
            projects_item = projects_item_data.to_dict()
            projects.append(projects_item)

        expiration_time = self.expiration_time.isoformat()

        email = self.email

        image: Union[None, Unset, str]
        if isinstance(self.image, Unset):
            image = UNSET
        else:
            image = self.image

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "uuid": uuid,
                "username": username,
                "full_name": full_name,
                "role": role,
                "role_name": role_name,
                "projects": projects,
                "expiration_time": expiration_time,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if image is not UNSET:
            field_dict["image"] = image

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.nested_project_permission import NestedProjectPermission

        d = src_dict.copy()
        url = d.pop("url")

        uuid = UUID(d.pop("uuid"))

        username = d.pop("username")

        full_name = d.pop("full_name")

        role = d.pop("role")

        role_name = d.pop("role_name")

        projects = []
        _projects = d.pop("projects")
        for projects_item_data in _projects:
            projects_item = NestedProjectPermission.from_dict(projects_item_data)

            projects.append(projects_item)

        expiration_time = isoparse(d.pop("expiration_time"))

        email = d.pop("email", UNSET)

        def _parse_image(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        image = _parse_image(d.pop("image", UNSET))

        customer_user = cls(
            url=url,
            uuid=uuid,
            username=username,
            full_name=full_name,
            role=role,
            role_name=role_name,
            projects=projects,
            expiration_time=expiration_time,
            email=email,
            image=image,
        )

        customer_user.additional_properties = d
        return customer_user

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
