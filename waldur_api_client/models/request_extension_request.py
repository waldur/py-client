import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.request_extension_request_requested_limits import RequestExtensionRequestRequestedLimits


T = TypeVar("T", bound="RequestExtensionRequest")


@_attrs_define
class RequestExtensionRequest:
    """
    Attributes:
        requested_end_date (Union[None, Unset, datetime.date]):
        requested_limits (Union[Unset, RequestExtensionRequestRequestedLimits]):
    """

    requested_end_date: Union[None, Unset, datetime.date] = UNSET
    requested_limits: Union[Unset, "RequestExtensionRequestRequestedLimits"] = UNSET
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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if requested_end_date is not UNSET:
            field_dict["requested_end_date"] = requested_end_date
        if requested_limits is not UNSET:
            field_dict["requested_limits"] = requested_limits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.request_extension_request_requested_limits import RequestExtensionRequestRequestedLimits

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
        requested_limits: Union[Unset, RequestExtensionRequestRequestedLimits]
        if isinstance(_requested_limits, Unset):
            requested_limits = UNSET
        else:
            requested_limits = RequestExtensionRequestRequestedLimits.from_dict(_requested_limits)

        request_extension_request = cls(
            requested_end_date=requested_end_date,
            requested_limits=requested_limits,
        )

        request_extension_request.additional_properties = d
        return request_extension_request

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
