from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.sync_resource_historical_consumption_response_errors_item import (
        SyncResourceHistoricalConsumptionResponseErrorsItem,
    )


T = TypeVar("T", bound="SyncResourceHistoricalConsumptionResponse")


@_attrs_define
class SyncResourceHistoricalConsumptionResponse:
    """
    Attributes:
        resource_uuid (UUID):
        resource_name (str):
        periods_synced (int):
        periods_skipped (int):
        errors (list['SyncResourceHistoricalConsumptionResponseErrorsItem']):
    """

    resource_uuid: UUID
    resource_name: str
    periods_synced: int
    periods_skipped: int
    errors: list["SyncResourceHistoricalConsumptionResponseErrorsItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_uuid = str(self.resource_uuid)

        resource_name = self.resource_name

        periods_synced = self.periods_synced

        periods_skipped = self.periods_skipped

        errors = []
        for errors_item_data in self.errors:
            errors_item = errors_item_data.to_dict()
            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource_uuid": resource_uuid,
                "resource_name": resource_name,
                "periods_synced": periods_synced,
                "periods_skipped": periods_skipped,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_resource_historical_consumption_response_errors_item import (
            SyncResourceHistoricalConsumptionResponseErrorsItem,
        )

        d = dict(src_dict)
        resource_uuid = UUID(d.pop("resource_uuid"))

        resource_name = d.pop("resource_name")

        periods_synced = d.pop("periods_synced")

        periods_skipped = d.pop("periods_skipped")

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:
            errors_item = SyncResourceHistoricalConsumptionResponseErrorsItem.from_dict(errors_item_data)

            errors.append(errors_item)

        sync_resource_historical_consumption_response = cls(
            resource_uuid=resource_uuid,
            resource_name=resource_name,
            periods_synced=periods_synced,
            periods_skipped=periods_skipped,
            errors=errors,
        )

        sync_resource_historical_consumption_response.additional_properties = d
        return sync_resource_historical_consumption_response

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
