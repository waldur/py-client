from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.message_role_enum import MessageRoleEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="MessageRequest")


@_attrs_define
class MessageRequest:
    """
    Attributes:
        thread (UUID):
        role (MessageRoleEnum):
        content (str):
        replaces (Union[None, UUID, Unset]):
    """

    thread: UUID
    role: MessageRoleEnum
    content: str
    replaces: Union[None, UUID, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        thread = str(self.thread)

        role = self.role.value

        content = self.content

        replaces: Union[None, Unset, str]
        if isinstance(self.replaces, Unset):
            replaces = UNSET
        elif isinstance(self.replaces, UUID):
            replaces = str(self.replaces)
        else:
            replaces = self.replaces

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "thread": thread,
                "role": role,
                "content": content,
            }
        )
        if replaces is not UNSET:
            field_dict["replaces"] = replaces

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        thread = UUID(d.pop("thread"))

        role = MessageRoleEnum(d.pop("role"))

        content = d.pop("content")

        def _parse_replaces(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                replaces_type_0 = UUID(data)

                return replaces_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        replaces = _parse_replaces(d.pop("replaces", UNSET))

        message_request = cls(
            thread=thread,
            role=role,
            content=content,
            replaces=replaces,
        )

        message_request.additional_properties = d
        return message_request

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
