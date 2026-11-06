from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WorkflowDescriptionRule")


@_attrs_define
class WorkflowDescriptionRule:
    """
    Attributes:
        trigger (str):
        recipient (str):
        proposal_role (Union[None, str]):
        notified_proposal_roles (list[str]):
        days_before (Union[None, int]):
        enabled (bool):
        actors (list[str]):
        mail_type (str): The mail type the rule sends.
        variant (str): The audience the mail is worded for: applicant or call_team.
        customised (bool): Whether the call words this mail itself.
    """

    trigger: str
    recipient: str
    proposal_role: Union[None, str]
    notified_proposal_roles: list[str]
    days_before: Union[None, int]
    enabled: bool
    actors: list[str]
    mail_type: str
    variant: str
    customised: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trigger = self.trigger

        recipient = self.recipient

        proposal_role: Union[None, str]
        proposal_role = self.proposal_role

        notified_proposal_roles = self.notified_proposal_roles

        days_before: Union[None, int]
        days_before = self.days_before

        enabled = self.enabled

        actors = self.actors

        mail_type = self.mail_type

        variant = self.variant

        customised = self.customised

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "trigger": trigger,
                "recipient": recipient,
                "proposal_role": proposal_role,
                "notified_proposal_roles": notified_proposal_roles,
                "days_before": days_before,
                "enabled": enabled,
                "actors": actors,
                "mail_type": mail_type,
                "variant": variant,
                "customised": customised,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        trigger = d.pop("trigger")

        recipient = d.pop("recipient")

        def _parse_proposal_role(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        proposal_role = _parse_proposal_role(d.pop("proposal_role"))

        notified_proposal_roles = cast(list[str], d.pop("notified_proposal_roles"))

        def _parse_days_before(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        days_before = _parse_days_before(d.pop("days_before"))

        enabled = d.pop("enabled")

        actors = cast(list[str], d.pop("actors"))

        mail_type = d.pop("mail_type")

        variant = d.pop("variant")

        customised = d.pop("customised")

        workflow_description_rule = cls(
            trigger=trigger,
            recipient=recipient,
            proposal_role=proposal_role,
            notified_proposal_roles=notified_proposal_roles,
            days_before=days_before,
            enabled=enabled,
            actors=actors,
            mail_type=mail_type,
            variant=variant,
            customised=customised,
        )

        workflow_description_rule.additional_properties = d
        return workflow_description_rule

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
