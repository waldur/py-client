import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.validation_decision_enum import ValidationDecisionEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.onboarding_justification_documentation import OnboardingJustificationDocumentation


T = TypeVar("T", bound="OnboardingJustification")


@_attrs_define
class OnboardingJustification:
    """
    Attributes:
        uuid (UUID):
        verification (int):
        user (int):
        validated_by (Union[None, int]):
        validated_at (Union[None, datetime.datetime]):
        validation_decision (ValidationDecisionEnum):
        staff_notes (str): Administrator notes on the review decision
        supporting_documentation (list['OnboardingJustificationDocumentation']):
        created (datetime.datetime):
        modified (datetime.datetime):
        user_justification (Union[None, Unset, str]): User's explanation for why they should be authorized
    """

    uuid: UUID
    verification: int
    user: int
    validated_by: Union[None, int]
    validated_at: Union[None, datetime.datetime]
    validation_decision: ValidationDecisionEnum
    staff_notes: str
    supporting_documentation: list["OnboardingJustificationDocumentation"]
    created: datetime.datetime
    modified: datetime.datetime
    user_justification: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        verification = self.verification

        user = self.user

        validated_by: Union[None, int]
        validated_by = self.validated_by

        validated_at: Union[None, str]
        if isinstance(self.validated_at, datetime.datetime):
            validated_at = self.validated_at.isoformat()
        else:
            validated_at = self.validated_at

        validation_decision = self.validation_decision.value

        staff_notes = self.staff_notes

        supporting_documentation = []
        for supporting_documentation_item_data in self.supporting_documentation:
            supporting_documentation_item = supporting_documentation_item_data.to_dict()
            supporting_documentation.append(supporting_documentation_item)

        created = self.created.isoformat()

        modified = self.modified.isoformat()

        user_justification: Union[None, Unset, str]
        if isinstance(self.user_justification, Unset):
            user_justification = UNSET
        else:
            user_justification = self.user_justification

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "verification": verification,
                "user": user,
                "validated_by": validated_by,
                "validated_at": validated_at,
                "validation_decision": validation_decision,
                "staff_notes": staff_notes,
                "supporting_documentation": supporting_documentation,
                "created": created,
                "modified": modified,
            }
        )
        if user_justification is not UNSET:
            field_dict["user_justification"] = user_justification

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.onboarding_justification_documentation import OnboardingJustificationDocumentation

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        verification = d.pop("verification")

        user = d.pop("user")

        def _parse_validated_by(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        validated_by = _parse_validated_by(d.pop("validated_by"))

        def _parse_validated_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                validated_at_type_0 = isoparse(data)

                return validated_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        validated_at = _parse_validated_at(d.pop("validated_at"))

        validation_decision = ValidationDecisionEnum(d.pop("validation_decision"))

        staff_notes = d.pop("staff_notes")

        supporting_documentation = []
        _supporting_documentation = d.pop("supporting_documentation")
        for supporting_documentation_item_data in _supporting_documentation:
            supporting_documentation_item = OnboardingJustificationDocumentation.from_dict(
                supporting_documentation_item_data
            )

            supporting_documentation.append(supporting_documentation_item)

        created = isoparse(d.pop("created"))

        modified = isoparse(d.pop("modified"))

        def _parse_user_justification(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_justification = _parse_user_justification(d.pop("user_justification", UNSET))

        onboarding_justification = cls(
            uuid=uuid,
            verification=verification,
            user=user,
            validated_by=validated_by,
            validated_at=validated_at,
            validation_decision=validation_decision,
            staff_notes=staff_notes,
            supporting_documentation=supporting_documentation,
            created=created,
            modified=modified,
            user_justification=user_justification,
        )

        onboarding_justification.additional_properties = d
        return onboarding_justification

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
