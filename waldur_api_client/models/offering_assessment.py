import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.blank_enum import BlankEnum
from ..models.contribution_outcome_enum import ContributionOutcomeEnum
from ..models.step_contribution_status import StepContributionStatus

T = TypeVar("T", bound="OfferingAssessment")


@_attrs_define
class OfferingAssessment:
    """
    Attributes:
        contribution_uuid (UUID):
        call_step_uuid (UUID):
        step_name (str):
        requested_offering_uuid (UUID):
        offering_uuid (UUID):
        offering_name (str):
        status (StepContributionStatus):
        outcome (Union[BlankEnum, ContributionOutcomeEnum]):
        conditions (str):
        comment (str):
        submitted_at (Union[None, datetime.datetime]):
    """

    contribution_uuid: UUID
    call_step_uuid: UUID
    step_name: str
    requested_offering_uuid: UUID
    offering_uuid: UUID
    offering_name: str
    status: StepContributionStatus
    outcome: Union[BlankEnum, ContributionOutcomeEnum]
    conditions: str
    comment: str
    submitted_at: Union[None, datetime.datetime]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contribution_uuid = str(self.contribution_uuid)

        call_step_uuid = str(self.call_step_uuid)

        step_name = self.step_name

        requested_offering_uuid = str(self.requested_offering_uuid)

        offering_uuid = str(self.offering_uuid)

        offering_name = self.offering_name

        status = self.status.value

        outcome: str
        if isinstance(self.outcome, ContributionOutcomeEnum):
            outcome = self.outcome.value
        else:
            outcome = self.outcome.value

        conditions = self.conditions

        comment = self.comment

        submitted_at: Union[None, str]
        if isinstance(self.submitted_at, datetime.datetime):
            submitted_at = self.submitted_at.isoformat()
        else:
            submitted_at = self.submitted_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contribution_uuid": contribution_uuid,
                "call_step_uuid": call_step_uuid,
                "step_name": step_name,
                "requested_offering_uuid": requested_offering_uuid,
                "offering_uuid": offering_uuid,
                "offering_name": offering_name,
                "status": status,
                "outcome": outcome,
                "conditions": conditions,
                "comment": comment,
                "submitted_at": submitted_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        contribution_uuid = UUID(d.pop("contribution_uuid"))

        call_step_uuid = UUID(d.pop("call_step_uuid"))

        step_name = d.pop("step_name")

        requested_offering_uuid = UUID(d.pop("requested_offering_uuid"))

        offering_uuid = UUID(d.pop("offering_uuid"))

        offering_name = d.pop("offering_name")

        status = StepContributionStatus(d.pop("status"))

        def _parse_outcome(data: object) -> Union[BlankEnum, ContributionOutcomeEnum]:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                outcome_type_0 = ContributionOutcomeEnum(data)

                return outcome_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            outcome_type_1 = BlankEnum(data)

            return outcome_type_1

        outcome = _parse_outcome(d.pop("outcome"))

        conditions = d.pop("conditions")

        comment = d.pop("comment")

        def _parse_submitted_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                submitted_at_type_0 = isoparse(data)

                return submitted_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        submitted_at = _parse_submitted_at(d.pop("submitted_at"))

        offering_assessment = cls(
            contribution_uuid=contribution_uuid,
            call_step_uuid=call_step_uuid,
            step_name=step_name,
            requested_offering_uuid=requested_offering_uuid,
            offering_uuid=offering_uuid,
            offering_name=offering_name,
            status=status,
            outcome=outcome,
            conditions=conditions,
            comment=comment,
            submitted_at=submitted_at,
        )

        offering_assessment.additional_properties = d
        return offering_assessment

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
