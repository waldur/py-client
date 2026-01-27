import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.resource_version_revision_user_type_0 import ResourceVersionRevisionUserType0
    from ..models.resource_version_serialized_data import ResourceVersionSerializedData


T = TypeVar("T", bound="ResourceVersion")


@_attrs_define
class ResourceVersion:
    """
    Attributes:
        id (int):
        revision_date (datetime.datetime):
        revision_user (Union['ResourceVersionRevisionUserType0', None]):
        revision_comment (str):
        serialized_data (ResourceVersionSerializedData):
    """

    id: int
    revision_date: datetime.datetime
    revision_user: Union["ResourceVersionRevisionUserType0", None]
    revision_comment: str
    serialized_data: "ResourceVersionSerializedData"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.resource_version_revision_user_type_0 import ResourceVersionRevisionUserType0

        id = self.id

        revision_date = self.revision_date.isoformat()

        revision_user: Union[None, dict[str, Any]]
        if isinstance(self.revision_user, ResourceVersionRevisionUserType0):
            revision_user = self.revision_user.to_dict()
        else:
            revision_user = self.revision_user

        revision_comment = self.revision_comment

        serialized_data = self.serialized_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "revision_date": revision_date,
                "revision_user": revision_user,
                "revision_comment": revision_comment,
                "serialized_data": serialized_data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_version_revision_user_type_0 import ResourceVersionRevisionUserType0
        from ..models.resource_version_serialized_data import ResourceVersionSerializedData

        d = dict(src_dict)
        id = d.pop("id")

        revision_date = isoparse(d.pop("revision_date"))

        def _parse_revision_user(data: object) -> Union["ResourceVersionRevisionUserType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                revision_user_type_0 = ResourceVersionRevisionUserType0.from_dict(data)

                return revision_user_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ResourceVersionRevisionUserType0", None], data)

        revision_user = _parse_revision_user(d.pop("revision_user"))

        revision_comment = d.pop("revision_comment")

        serialized_data = ResourceVersionSerializedData.from_dict(d.pop("serialized_data"))

        resource_version = cls(
            id=id,
            revision_date=revision_date,
            revision_user=revision_user,
            revision_comment=revision_comment,
            serialized_data=serialized_data,
        )

        resource_version.additional_properties = d
        return resource_version

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
