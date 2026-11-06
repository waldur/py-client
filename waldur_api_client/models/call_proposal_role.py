import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.eligible_from_enum import EligibleFromEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="CallProposalRole")


@_attrs_define
class CallProposalRole:
    """
    Attributes:
        uuid (UUID):
        created (datetime.datetime):
        modified (datetime.datetime):
        call_uuid (UUID):
        name (str):
        eligible_count (Union[None, int]): How many people may hold the role on the call now; null when any user may.
        holders_warning (Union[None, str]): Why the call cannot staff the role on a proposal: fewer people may hold it
            than its minimum of holders. Null when it can.
        key (Union[Unset, str]): Identifier of the role within its call. Derived from the name when left out. Cannot
            change once the role exists.
        description (Union[Unset, str]):
        eligible_from (Union[Unset, EligibleFromEnum]):
        min_holders (Union[Unset, int]): How many holders an assignment step for this role needs before it can complete.
        max_holders (Union[None, Unset, int]): How many people may hold the role on one proposal. Empty: no limit.
        allows_lead (Union[Unset, bool]): Whether one holder is marked as the lead.
    """

    uuid: UUID
    created: datetime.datetime
    modified: datetime.datetime
    call_uuid: UUID
    name: str
    eligible_count: Union[None, int]
    holders_warning: Union[None, str]
    key: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    eligible_from: Union[Unset, EligibleFromEnum] = UNSET
    min_holders: Union[Unset, int] = UNSET
    max_holders: Union[None, Unset, int] = UNSET
    allows_lead: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        created = self.created.isoformat()

        modified = self.modified.isoformat()

        call_uuid = str(self.call_uuid)

        name = self.name

        eligible_count: Union[None, int]
        eligible_count = self.eligible_count

        holders_warning: Union[None, str]
        holders_warning = self.holders_warning

        key = self.key

        description = self.description

        eligible_from: Union[Unset, str] = UNSET
        if not isinstance(self.eligible_from, Unset):
            eligible_from = self.eligible_from.value

        min_holders = self.min_holders

        max_holders: Union[None, Unset, int]
        if isinstance(self.max_holders, Unset):
            max_holders = UNSET
        else:
            max_holders = self.max_holders

        allows_lead = self.allows_lead

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "created": created,
                "modified": modified,
                "call_uuid": call_uuid,
                "name": name,
                "eligible_count": eligible_count,
                "holders_warning": holders_warning,
            }
        )
        if key is not UNSET:
            field_dict["key"] = key
        if description is not UNSET:
            field_dict["description"] = description
        if eligible_from is not UNSET:
            field_dict["eligible_from"] = eligible_from
        if min_holders is not UNSET:
            field_dict["min_holders"] = min_holders
        if max_holders is not UNSET:
            field_dict["max_holders"] = max_holders
        if allows_lead is not UNSET:
            field_dict["allows_lead"] = allows_lead

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        created = isoparse(d.pop("created"))

        modified = isoparse(d.pop("modified"))

        call_uuid = UUID(d.pop("call_uuid"))

        name = d.pop("name")

        def _parse_eligible_count(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        eligible_count = _parse_eligible_count(d.pop("eligible_count"))

        def _parse_holders_warning(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        holders_warning = _parse_holders_warning(d.pop("holders_warning"))

        key = d.pop("key", UNSET)

        description = d.pop("description", UNSET)

        _eligible_from = d.pop("eligible_from", UNSET)
        eligible_from: Union[Unset, EligibleFromEnum]
        if isinstance(_eligible_from, Unset):
            eligible_from = UNSET
        else:
            eligible_from = EligibleFromEnum(_eligible_from)

        min_holders = d.pop("min_holders", UNSET)

        def _parse_max_holders(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_holders = _parse_max_holders(d.pop("max_holders", UNSET))

        allows_lead = d.pop("allows_lead", UNSET)

        call_proposal_role = cls(
            uuid=uuid,
            created=created,
            modified=modified,
            call_uuid=call_uuid,
            name=name,
            eligible_count=eligible_count,
            holders_warning=holders_warning,
            key=key,
            description=description,
            eligible_from=eligible_from,
            min_holders=min_holders,
            max_holders=max_holders,
            allows_lead=allows_lead,
        )

        call_proposal_role.additional_properties = d
        return call_proposal_role

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
