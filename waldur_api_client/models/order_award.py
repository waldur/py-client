from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.order_award_awarded_limits import OrderAwardAwardedLimits
    from ..models.order_award_requested_limits_type_0 import OrderAwardRequestedLimitsType0


T = TypeVar("T", bound="OrderAward")


@_attrs_define
class OrderAward:
    """
    Attributes:
        proposal_uuid (Union[Unset, UUID]):
        proposal_name (Union[Unset, str]):
        call_uuid (Union[Unset, UUID]):
        call_name (Union[Unset, str]):
        round_name (Union[Unset, str]):
        awarded_limits (Union[Unset, OrderAwardAwardedLimits]): What the award grants on the order's offering.
        requested_limits (Union['OrderAwardRequestedLimitsType0', None, Unset]): What the applicant asked for; null for
            an item the call manager added.
        can_read (Union[Unset, bool]): Whether the viewer may open the proposal.
    """

    proposal_uuid: Union[Unset, UUID] = UNSET
    proposal_name: Union[Unset, str] = UNSET
    call_uuid: Union[Unset, UUID] = UNSET
    call_name: Union[Unset, str] = UNSET
    round_name: Union[Unset, str] = UNSET
    awarded_limits: Union[Unset, "OrderAwardAwardedLimits"] = UNSET
    requested_limits: Union["OrderAwardRequestedLimitsType0", None, Unset] = UNSET
    can_read: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.order_award_requested_limits_type_0 import OrderAwardRequestedLimitsType0

        proposal_uuid: Union[Unset, str] = UNSET
        if not isinstance(self.proposal_uuid, Unset):
            proposal_uuid = str(self.proposal_uuid)

        proposal_name = self.proposal_name

        call_uuid: Union[Unset, str] = UNSET
        if not isinstance(self.call_uuid, Unset):
            call_uuid = str(self.call_uuid)

        call_name = self.call_name

        round_name = self.round_name

        awarded_limits: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.awarded_limits, Unset):
            awarded_limits = self.awarded_limits.to_dict()

        requested_limits: Union[None, Unset, dict[str, Any]]
        if isinstance(self.requested_limits, Unset):
            requested_limits = UNSET
        elif isinstance(self.requested_limits, OrderAwardRequestedLimitsType0):
            requested_limits = self.requested_limits.to_dict()
        else:
            requested_limits = self.requested_limits

        can_read = self.can_read

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if proposal_uuid is not UNSET:
            field_dict["proposal_uuid"] = proposal_uuid
        if proposal_name is not UNSET:
            field_dict["proposal_name"] = proposal_name
        if call_uuid is not UNSET:
            field_dict["call_uuid"] = call_uuid
        if call_name is not UNSET:
            field_dict["call_name"] = call_name
        if round_name is not UNSET:
            field_dict["round_name"] = round_name
        if awarded_limits is not UNSET:
            field_dict["awarded_limits"] = awarded_limits
        if requested_limits is not UNSET:
            field_dict["requested_limits"] = requested_limits
        if can_read is not UNSET:
            field_dict["can_read"] = can_read

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.order_award_awarded_limits import OrderAwardAwardedLimits
        from ..models.order_award_requested_limits_type_0 import OrderAwardRequestedLimitsType0

        d = dict(src_dict)
        _proposal_uuid = d.pop("proposal_uuid", UNSET)
        proposal_uuid: Union[Unset, UUID]
        if isinstance(_proposal_uuid, Unset):
            proposal_uuid = UNSET
        else:
            proposal_uuid = UUID(_proposal_uuid)

        proposal_name = d.pop("proposal_name", UNSET)

        _call_uuid = d.pop("call_uuid", UNSET)
        call_uuid: Union[Unset, UUID]
        if isinstance(_call_uuid, Unset):
            call_uuid = UNSET
        else:
            call_uuid = UUID(_call_uuid)

        call_name = d.pop("call_name", UNSET)

        round_name = d.pop("round_name", UNSET)

        _awarded_limits = d.pop("awarded_limits", UNSET)
        awarded_limits: Union[Unset, OrderAwardAwardedLimits]
        if isinstance(_awarded_limits, Unset):
            awarded_limits = UNSET
        else:
            awarded_limits = OrderAwardAwardedLimits.from_dict(_awarded_limits)

        def _parse_requested_limits(data: object) -> Union["OrderAwardRequestedLimitsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                requested_limits_type_0 = OrderAwardRequestedLimitsType0.from_dict(data)

                return requested_limits_type_0
            except:  # noqa: E722
                pass
            return cast(Union["OrderAwardRequestedLimitsType0", None, Unset], data)

        requested_limits = _parse_requested_limits(d.pop("requested_limits", UNSET))

        can_read = d.pop("can_read", UNSET)

        order_award = cls(
            proposal_uuid=proposal_uuid,
            proposal_name=proposal_name,
            call_uuid=call_uuid,
            call_name=call_name,
            round_name=round_name,
            awarded_limits=awarded_limits,
            requested_limits=requested_limits,
            can_read=can_read,
        )

        order_award.additional_properties = d
        return order_award

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
