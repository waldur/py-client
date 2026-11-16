from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.step_discussion_state_enum import StepDiscussionStateEnum

T = TypeVar("T", bound="StepDiscussionViewer")


@_attrs_define
class StepDiscussionViewer:
    """
    Attributes:
        uuid (Union[None, UUID]): The step's latest discussion, once opened (proposal-step-discussions): the open one,
            else the last closed.
        state (StepDiscussionStateEnum):
        can_open (bool): Whether the viewer may open it now -- or join it, once open: they take part in it, the step is
            active and Matrix chat is enabled. With state closed, the step runs again: opening starts a new discussion, and
            the closed one stays on record.
    """

    uuid: Union[None, UUID]
    state: StepDiscussionStateEnum
    can_open: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid: Union[None, str]
        if isinstance(self.uuid, UUID):
            uuid = str(self.uuid)
        else:
            uuid = self.uuid

        state = self.state.value

        can_open = self.can_open

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "state": state,
                "can_open": can_open,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                uuid_type_0 = UUID(data)

                return uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        uuid = _parse_uuid(d.pop("uuid"))

        state = StepDiscussionStateEnum(d.pop("state"))

        can_open = d.pop("can_open")

        step_discussion_viewer = cls(
            uuid=uuid,
            state=state,
            can_open=can_open,
        )

        step_discussion_viewer.additional_properties = d
        return step_discussion_viewer

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
