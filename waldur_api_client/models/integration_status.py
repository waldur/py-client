import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="IntegrationStatus")


@_attrs_define
class IntegrationStatus:
    """
    Attributes:
        agent_type (str):
        status (str):
        last_request_timestamp (Union[None, datetime.datetime]):
    """

    agent_type: str
    status: str
    last_request_timestamp: Union[None, datetime.datetime]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_type = self.agent_type

        status = self.status

        last_request_timestamp: Union[None, str]
        if isinstance(self.last_request_timestamp, datetime.datetime):
            last_request_timestamp = self.last_request_timestamp.isoformat()
        else:
            last_request_timestamp = self.last_request_timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_type": agent_type,
                "status": status,
                "last_request_timestamp": last_request_timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        agent_type = d.pop("agent_type")

        status = d.pop("status")

        def _parse_last_request_timestamp(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_request_timestamp_type_0 = isoparse(data)

                return last_request_timestamp_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        last_request_timestamp = _parse_last_request_timestamp(d.pop("last_request_timestamp"))

        integration_status = cls(
            agent_type=agent_type,
            status=status,
            last_request_timestamp=last_request_timestamp,
        )

        integration_status.additional_properties = d
        return integration_status

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
