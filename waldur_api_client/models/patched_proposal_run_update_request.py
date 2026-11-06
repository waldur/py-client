import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patched_proposal_run_update_request_granted_limits import PatchedProposalRunUpdateRequestGrantedLimits
    from ..models.patched_proposal_run_update_request_requested_limits import (
        PatchedProposalRunUpdateRequestRequestedLimits,
    )


T = TypeVar("T", bound="PatchedProposalRunUpdateRequest")


@_attrs_define
class PatchedProposalRunUpdateRequest:
    """
    Attributes:
        requested_end_date (Union[None, Unset, datetime.date]):
        requested_limits (Union[Unset, PatchedProposalRunUpdateRequestRequestedLimits]):
        granted_end_date (Union[None, Unset, datetime.date]):
        granted_limits (Union[Unset, PatchedProposalRunUpdateRequestGrantedLimits]):
    """

    requested_end_date: Union[None, Unset, datetime.date] = UNSET
    requested_limits: Union[Unset, "PatchedProposalRunUpdateRequestRequestedLimits"] = UNSET
    granted_end_date: Union[None, Unset, datetime.date] = UNSET
    granted_limits: Union[Unset, "PatchedProposalRunUpdateRequestGrantedLimits"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        requested_end_date: Union[None, Unset, str]
        if isinstance(self.requested_end_date, Unset):
            requested_end_date = UNSET
        elif isinstance(self.requested_end_date, datetime.date):
            requested_end_date = self.requested_end_date.isoformat()
        else:
            requested_end_date = self.requested_end_date

        requested_limits: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.requested_limits, Unset):
            requested_limits = self.requested_limits.to_dict()

        granted_end_date: Union[None, Unset, str]
        if isinstance(self.granted_end_date, Unset):
            granted_end_date = UNSET
        elif isinstance(self.granted_end_date, datetime.date):
            granted_end_date = self.granted_end_date.isoformat()
        else:
            granted_end_date = self.granted_end_date

        granted_limits: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.granted_limits, Unset):
            granted_limits = self.granted_limits.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if requested_end_date is not UNSET:
            field_dict["requested_end_date"] = requested_end_date
        if requested_limits is not UNSET:
            field_dict["requested_limits"] = requested_limits
        if granted_end_date is not UNSET:
            field_dict["granted_end_date"] = granted_end_date
        if granted_limits is not UNSET:
            field_dict["granted_limits"] = granted_limits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patched_proposal_run_update_request_granted_limits import (
            PatchedProposalRunUpdateRequestGrantedLimits,
        )
        from ..models.patched_proposal_run_update_request_requested_limits import (
            PatchedProposalRunUpdateRequestRequestedLimits,
        )

        d = dict(src_dict)

        def _parse_requested_end_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                requested_end_date_type_0 = isoparse(data).date()

                return requested_end_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        requested_end_date = _parse_requested_end_date(d.pop("requested_end_date", UNSET))

        _requested_limits = d.pop("requested_limits", UNSET)
        requested_limits: Union[Unset, PatchedProposalRunUpdateRequestRequestedLimits]
        if isinstance(_requested_limits, Unset):
            requested_limits = UNSET
        else:
            requested_limits = PatchedProposalRunUpdateRequestRequestedLimits.from_dict(_requested_limits)

        def _parse_granted_end_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                granted_end_date_type_0 = isoparse(data).date()

                return granted_end_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        granted_end_date = _parse_granted_end_date(d.pop("granted_end_date", UNSET))

        _granted_limits = d.pop("granted_limits", UNSET)
        granted_limits: Union[Unset, PatchedProposalRunUpdateRequestGrantedLimits]
        if isinstance(_granted_limits, Unset):
            granted_limits = UNSET
        else:
            granted_limits = PatchedProposalRunUpdateRequestGrantedLimits.from_dict(_granted_limits)

        patched_proposal_run_update_request = cls(
            requested_end_date=requested_end_date,
            requested_limits=requested_limits,
            granted_end_date=granted_end_date,
            granted_limits=granted_limits,
        )

        patched_proposal_run_update_request.additional_properties = d
        return patched_proposal_run_update_request

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
