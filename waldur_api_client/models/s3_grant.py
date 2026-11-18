from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.group_enum import GroupEnum

T = TypeVar("T", bound="S3Grant")


@_attrs_define
class S3Grant:
    """
    Attributes:
        type_ (str):
        grantee (str):
        display_name (str):
        group (Union[GroupEnum, None]): Set when the grant is to a public group.
        permission (str):
    """

    type_: str
    grantee: str
    display_name: str
    group: Union[GroupEnum, None]
    permission: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        grantee = self.grantee

        display_name = self.display_name

        group: Union[None, str]
        if isinstance(self.group, GroupEnum):
            group = self.group.value
        else:
            group = self.group

        permission = self.permission

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "grantee": grantee,
                "display_name": display_name,
                "group": group,
                "permission": permission,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        grantee = d.pop("grantee")

        display_name = d.pop("display_name")

        def _parse_group(data: object) -> Union[GroupEnum, None]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                group_type_0 = GroupEnum(data)

                return group_type_0
            except:  # noqa: E722
                pass
            return cast(Union[GroupEnum, None], data)

        group = _parse_group(d.pop("group"))

        permission = d.pop("permission")

        s3_grant = cls(
            type_=type_,
            grantee=grantee,
            display_name=display_name,
            group=group,
            permission=permission,
        )

        s3_grant.additional_properties = d
        return s3_grant

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
