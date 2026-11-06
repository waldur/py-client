from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProposalReviewerSuggestionCreateRequest")


@_attrs_define
class ProposalReviewerSuggestionCreateRequest:
    """
    Attributes:
        suggested_user (Union[None, UUID, Unset]): An existing user suggested as a reviewer.
        suggested_email (Union[Unset, str]): The e-mail address of a reviewer without a user account.
        note (Union[Unset, str]): Why this reviewer: expertise.
    """

    suggested_user: Union[None, UUID, Unset] = UNSET
    suggested_email: Union[Unset, str] = UNSET
    note: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        suggested_user: Union[None, Unset, str]
        if isinstance(self.suggested_user, Unset):
            suggested_user = UNSET
        elif isinstance(self.suggested_user, UUID):
            suggested_user = str(self.suggested_user)
        else:
            suggested_user = self.suggested_user

        suggested_email = self.suggested_email

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if suggested_user is not UNSET:
            field_dict["suggested_user"] = suggested_user
        if suggested_email is not UNSET:
            field_dict["suggested_email"] = suggested_email
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_suggested_user(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                suggested_user_type_0 = UUID(data)

                return suggested_user_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        suggested_user = _parse_suggested_user(d.pop("suggested_user", UNSET))

        suggested_email = d.pop("suggested_email", UNSET)

        note = d.pop("note", UNSET)

        proposal_reviewer_suggestion_create_request = cls(
            suggested_user=suggested_user,
            suggested_email=suggested_email,
            note=note,
        )

        proposal_reviewer_suggestion_create_request.additional_properties = d
        return proposal_reviewer_suggestion_create_request

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
