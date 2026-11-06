from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.workflow_step_user_offering import WorkflowStepUserOffering


T = TypeVar("T", bound="WorkflowStepResponsibleUser")


@_attrs_define
class WorkflowStepResponsibleUser:
    """
    Attributes:
        uuid (UUID):
        username (str):
        full_name (str):
        email (str):
        is_panel_chair (bool):
        is_panel_vice_chair (bool):
        offerings (list['WorkflowStepUserOffering']): The offerings accepted into the call that the user manages; empty
            unless the user takes part as an offering manager.
    """

    uuid: UUID
    username: str
    full_name: str
    email: str
    is_panel_chair: bool
    is_panel_vice_chair: bool
    offerings: list["WorkflowStepUserOffering"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        username = self.username

        full_name = self.full_name

        email = self.email

        is_panel_chair = self.is_panel_chair

        is_panel_vice_chair = self.is_panel_vice_chair

        offerings = []
        for offerings_item_data in self.offerings:
            offerings_item = offerings_item_data.to_dict()
            offerings.append(offerings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "username": username,
                "full_name": full_name,
                "email": email,
                "is_panel_chair": is_panel_chair,
                "is_panel_vice_chair": is_panel_vice_chair,
                "offerings": offerings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_step_user_offering import WorkflowStepUserOffering

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        username = d.pop("username")

        full_name = d.pop("full_name")

        email = d.pop("email")

        is_panel_chair = d.pop("is_panel_chair")

        is_panel_vice_chair = d.pop("is_panel_vice_chair")

        offerings = []
        _offerings = d.pop("offerings")
        for offerings_item_data in _offerings:
            offerings_item = WorkflowStepUserOffering.from_dict(offerings_item_data)

            offerings.append(offerings_item)

        workflow_step_responsible_user = cls(
            uuid=uuid,
            username=username,
            full_name=full_name,
            email=email,
            is_panel_chair=is_panel_chair,
            is_panel_vice_chair=is_panel_vice_chair,
            offerings=offerings,
        )

        workflow_step_responsible_user.additional_properties = d
        return workflow_step_responsible_user

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
