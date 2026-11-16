from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.step_discussion_state_enum import StepDiscussionStateEnum

T = TypeVar("T", bound="RoundStepDiscussion")


@_attrs_define
class RoundStepDiscussion:
    """
    Attributes:
        uuid (Union[None, UUID]): The step's latest discussion, once opened (proposal-step-discussions): the open one,
            else the last closed.
        state (StepDiscussionStateEnum):
        can_open (bool): Whether the viewer may open it now -- or join it, once open: they take part in it, the step is
            active and Matrix chat is enabled. With state closed, the step runs again: opening starts a new discussion, and
            the closed one stays on record.
        panel_uuid (Union[None, UUID]): The panel whose discussion it is; null on a call without panels.
        panel_name (Union[None, str]):
    """

    uuid: Union[None, UUID]
    state: StepDiscussionStateEnum
    can_open: bool
    panel_uuid: Union[None, UUID]
    panel_name: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid: Union[None, str]
        if isinstance(self.uuid, UUID):
            uuid = str(self.uuid)
        else:
            uuid = self.uuid

        state = self.state.value

        can_open = self.can_open

        panel_uuid: Union[None, str]
        if isinstance(self.panel_uuid, UUID):
            panel_uuid = str(self.panel_uuid)
        else:
            panel_uuid = self.panel_uuid

        panel_name: Union[None, str]
        panel_name = self.panel_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "state": state,
                "can_open": can_open,
                "panel_uuid": panel_uuid,
                "panel_name": panel_name,
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

        def _parse_panel_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                panel_uuid_type_0 = UUID(data)

                return panel_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        panel_uuid = _parse_panel_uuid(d.pop("panel_uuid"))

        def _parse_panel_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        panel_name = _parse_panel_name(d.pop("panel_name"))

        round_step_discussion = cls(
            uuid=uuid,
            state=state,
            can_open=can_open,
            panel_uuid=panel_uuid,
            panel_name=panel_name,
        )

        round_step_discussion.additional_properties = d
        return round_step_discussion

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
