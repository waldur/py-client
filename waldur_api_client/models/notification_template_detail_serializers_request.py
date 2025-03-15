from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="NotificationTemplateDetailSerializersRequest")


@_attrs_define
class NotificationTemplateDetailSerializersRequest:
    """
    Attributes:
        path (str): Example: 'flatpages/default.html'
        name (str):
    """

    path: str
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "name": name,
            }
        )

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        path = (None, str(self.path).encode(), "text/plain")

        name = (None, str(self.name).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "path": path,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path")

        name = d.pop("name")

        notification_template_detail_serializers_request = cls(
            path=path,
            name=name,
        )

        notification_template_detail_serializers_request.additional_properties = d
        return notification_template_detail_serializers_request

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
