import datetime
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PermissionProject")


@_attrs_define
class PermissionProject:
    """
    Attributes:
        url (str):
        uuid (UUID):
        name (str):
        resource_count (int):
        image (Union[None, Unset, str]):
        end_date (Union[None, Unset, datetime.date]): The date is inclusive. Once reached, all project resource will be
            scheduled for termination.
    """

    url: str
    uuid: UUID
    name: str
    resource_count: int
    image: Union[None, Unset, str] = UNSET
    end_date: Union[None, Unset, datetime.date] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        uuid = str(self.uuid)

        name = self.name

        resource_count = self.resource_count

        image: Union[None, Unset, str]
        if isinstance(self.image, Unset):
            image = UNSET
        else:
            image = self.image

        end_date: Union[None, Unset, str]
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.date):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "uuid": uuid,
                "name": name,
                "resource_count": resource_count,
            }
        )
        if image is not UNSET:
            field_dict["image"] = image
        if end_date is not UNSET:
            field_dict["end_date"] = end_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        resource_count = d.pop("resource_count")

        def _parse_image(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        image = _parse_image(d.pop("image", UNSET))

        def _parse_end_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = isoparse(data).date()

                return end_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        end_date = _parse_end_date(d.pop("end_date", UNSET))

        permission_project = cls(
            url=url,
            uuid=uuid,
            name=name,
            resource_count=resource_count,
            image=image,
            end_date=end_date,
        )

        permission_project.additional_properties = d
        return permission_project

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
