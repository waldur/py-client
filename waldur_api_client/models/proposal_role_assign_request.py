from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProposalRoleAssignRequest")


@_attrs_define
class ProposalRoleAssignRequest:
    """
    Attributes:
        role_uuid (UUID): The call's evaluator role.
        user_uuid (UUID): The user to hold it.
        is_lead (Union[Unset, bool]): Mark the holder as the role's lead, in place of any other. Default: False.
    """

    role_uuid: UUID
    user_uuid: UUID
    is_lead: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role_uuid = str(self.role_uuid)

        user_uuid = str(self.user_uuid)

        is_lead = self.is_lead

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role_uuid": role_uuid,
                "user_uuid": user_uuid,
            }
        )
        if is_lead is not UNSET:
            field_dict["is_lead"] = is_lead

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        role_uuid = UUID(d.pop("role_uuid"))

        user_uuid = UUID(d.pop("user_uuid"))

        is_lead = d.pop("is_lead", UNSET)

        proposal_role_assign_request = cls(
            role_uuid=role_uuid,
            user_uuid=user_uuid,
            is_lead=is_lead,
        )

        proposal_role_assign_request.additional_properties = d
        return proposal_role_assign_request

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
