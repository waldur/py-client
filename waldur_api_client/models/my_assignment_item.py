import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="MyAssignmentItem")


@_attrs_define
class MyAssignmentItem:
    """
    Attributes:
        uuid (UUID):
        proposal_uuid (UUID):
        proposal_name (str):
        proposal_slug (str):
        proposal_summary (str):
        status (str): Effective status: a pending item past its deadline reads as expired.
        status_display (str):
        expires_at (Union[None, datetime.datetime]): Deadline for responding to this item.
        is_expired (bool): Whether the item can no longer be answered because its deadline has passed.
        affinity_score (Union[None, float]):
        has_coi (bool):
    """

    uuid: UUID
    proposal_uuid: UUID
    proposal_name: str
    proposal_slug: str
    proposal_summary: str
    status: str
    status_display: str
    expires_at: Union[None, datetime.datetime]
    is_expired: bool
    affinity_score: Union[None, float]
    has_coi: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        proposal_uuid = str(self.proposal_uuid)

        proposal_name = self.proposal_name

        proposal_slug = self.proposal_slug

        proposal_summary = self.proposal_summary

        status = self.status

        status_display = self.status_display

        expires_at: Union[None, str]
        if isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        is_expired = self.is_expired

        affinity_score: Union[None, float]
        affinity_score = self.affinity_score

        has_coi = self.has_coi

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "proposal_uuid": proposal_uuid,
                "proposal_name": proposal_name,
                "proposal_slug": proposal_slug,
                "proposal_summary": proposal_summary,
                "status": status,
                "status_display": status_display,
                "expires_at": expires_at,
                "is_expired": is_expired,
                "affinity_score": affinity_score,
                "has_coi": has_coi,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        proposal_uuid = UUID(d.pop("proposal_uuid"))

        proposal_name = d.pop("proposal_name")

        proposal_slug = d.pop("proposal_slug")

        proposal_summary = d.pop("proposal_summary")

        status = d.pop("status")

        status_display = d.pop("status_display")

        def _parse_expires_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = isoparse(data)

                return expires_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        expires_at = _parse_expires_at(d.pop("expires_at"))

        is_expired = d.pop("is_expired")

        def _parse_affinity_score(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        affinity_score = _parse_affinity_score(d.pop("affinity_score"))

        has_coi = d.pop("has_coi")

        my_assignment_item = cls(
            uuid=uuid,
            proposal_uuid=proposal_uuid,
            proposal_name=proposal_name,
            proposal_slug=proposal_slug,
            proposal_summary=proposal_summary,
            status=status,
            status_display=status_display,
            expires_at=expires_at,
            is_expired=is_expired,
            affinity_score=affinity_score,
            has_coi=has_coi,
        )

        my_assignment_item.additional_properties = d
        return my_assignment_item

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
