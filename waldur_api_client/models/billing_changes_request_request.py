from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.billing_changes_request_action_enum import BillingChangesRequestActionEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="BillingChangesRequestRequest")


@_attrs_define
class BillingChangesRequestRequest:
    """
    Attributes:
        action (BillingChangesRequestActionEnum):
        year (int):
        month (int):
        resource_uuid (Union[None, UUID, Unset]): Limit billing or consumption sync to one resource.
        dry_run (Union[Unset, bool]): Preview the changes and keep nothing; false applies them. Default: True.
    """

    action: BillingChangesRequestActionEnum
    year: int
    month: int
    resource_uuid: Union[None, UUID, Unset] = UNSET
    dry_run: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

        year = self.year

        month = self.month

        resource_uuid: Union[None, Unset, str]
        if isinstance(self.resource_uuid, Unset):
            resource_uuid = UNSET
        elif isinstance(self.resource_uuid, UUID):
            resource_uuid = str(self.resource_uuid)
        else:
            resource_uuid = self.resource_uuid

        dry_run = self.dry_run

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "year": year,
                "month": month,
            }
        )
        if resource_uuid is not UNSET:
            field_dict["resource_uuid"] = resource_uuid
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = BillingChangesRequestActionEnum(d.pop("action"))

        year = d.pop("year")

        month = d.pop("month")

        def _parse_resource_uuid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resource_uuid_type_0 = UUID(data)

                return resource_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        resource_uuid = _parse_resource_uuid(d.pop("resource_uuid", UNSET))

        dry_run = d.pop("dry_run", UNSET)

        billing_changes_request_request = cls(
            action=action,
            year=year,
            month=month,
            resource_uuid=resource_uuid,
            dry_run=dry_run,
        )

        billing_changes_request_request.additional_properties = d
        return billing_changes_request_request

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
