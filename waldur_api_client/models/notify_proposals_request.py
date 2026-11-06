from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.recipients_enum import RecipientsEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="NotifyProposalsRequest")


@_attrs_define
class NotifyProposalsRequest:
    """
    Attributes:
        proposal_uuids (list[UUID]): Proposals of this call whose applicants receive the message
        subject (str):
        body (str):
        recipients (Union[Unset, RecipientsEnum]):  Default: RecipientsEnum.APPLICANT.
    """

    proposal_uuids: list[UUID]
    subject: str
    body: str
    recipients: Union[Unset, RecipientsEnum] = RecipientsEnum.APPLICANT
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        proposal_uuids = []
        for proposal_uuids_item_data in self.proposal_uuids:
            proposal_uuids_item = str(proposal_uuids_item_data)
            proposal_uuids.append(proposal_uuids_item)

        subject = self.subject

        body = self.body

        recipients: Union[Unset, str] = UNSET
        if not isinstance(self.recipients, Unset):
            recipients = self.recipients.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "proposal_uuids": proposal_uuids,
                "subject": subject,
                "body": body,
            }
        )
        if recipients is not UNSET:
            field_dict["recipients"] = recipients

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        proposal_uuids = []
        _proposal_uuids = d.pop("proposal_uuids")
        for proposal_uuids_item_data in _proposal_uuids:
            proposal_uuids_item = UUID(proposal_uuids_item_data)

            proposal_uuids.append(proposal_uuids_item)

        subject = d.pop("subject")

        body = d.pop("body")

        _recipients = d.pop("recipients", UNSET)
        recipients: Union[Unset, RecipientsEnum]
        if isinstance(_recipients, Unset):
            recipients = UNSET
        else:
            recipients = RecipientsEnum(_recipients)

        notify_proposals_request = cls(
            proposal_uuids=proposal_uuids,
            subject=subject,
            body=body,
            recipients=recipients,
        )

        notify_proposals_request.additional_properties = d
        return notify_proposals_request

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
