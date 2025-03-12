import datetime
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComponentUsage")


@_attrs_define
class ComponentUsage:
    """
    Attributes:
        uuid (UUID):
        created (datetime.datetime):
        type_ (str): Unique internal name of the measured unit, for example floating_ip.
        name (str): Display name for the measured unit, for example, Floating IP.
        measured_unit (str): Unit of measurement, for example, GB.
        usage (int):
        date (datetime.datetime):
        resource_name (str):
        resource_uuid (UUID):
        offering_name (str):
        offering_uuid (UUID):
        project_name (str):
        project_uuid (str):
        customer_name (str):
        customer_uuid (str):
        billing_period (datetime.date):
        description (Union[Unset, str]):
        recurring (Union[Unset, bool]): Reported value is reused every month until changed.
        modified_by (Union[None, Unset, int]):
    """

    uuid: UUID
    created: datetime.datetime
    type_: str
    name: str
    measured_unit: str
    usage: int
    date: datetime.datetime
    resource_name: str
    resource_uuid: UUID
    offering_name: str
    offering_uuid: UUID
    project_name: str
    project_uuid: str
    customer_name: str
    customer_uuid: str
    billing_period: datetime.date
    description: Union[Unset, str] = UNSET
    recurring: Union[Unset, bool] = UNSET
    modified_by: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        created = self.created.isoformat()

        type_ = self.type_

        name = self.name

        measured_unit = self.measured_unit

        usage = self.usage

        date = self.date.isoformat()

        resource_name = self.resource_name

        resource_uuid = str(self.resource_uuid)

        offering_name = self.offering_name

        offering_uuid = str(self.offering_uuid)

        project_name = self.project_name

        project_uuid = self.project_uuid

        customer_name = self.customer_name

        customer_uuid = self.customer_uuid

        billing_period = self.billing_period.isoformat()

        description = self.description

        recurring = self.recurring

        modified_by: Union[None, Unset, int]
        if isinstance(self.modified_by, Unset):
            modified_by = UNSET
        else:
            modified_by = self.modified_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "created": created,
                "type": type_,
                "name": name,
                "measured_unit": measured_unit,
                "usage": usage,
                "date": date,
                "resource_name": resource_name,
                "resource_uuid": resource_uuid,
                "offering_name": offering_name,
                "offering_uuid": offering_uuid,
                "project_name": project_name,
                "project_uuid": project_uuid,
                "customer_name": customer_name,
                "customer_uuid": customer_uuid,
                "billing_period": billing_period,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if recurring is not UNSET:
            field_dict["recurring"] = recurring
        if modified_by is not UNSET:
            field_dict["modified_by"] = modified_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = UUID(d.pop("uuid"))

        created = isoparse(d.pop("created"))

        type_ = d.pop("type")

        name = d.pop("name")

        measured_unit = d.pop("measured_unit")

        usage = d.pop("usage")

        date = isoparse(d.pop("date"))

        resource_name = d.pop("resource_name")

        resource_uuid = UUID(d.pop("resource_uuid"))

        offering_name = d.pop("offering_name")

        offering_uuid = UUID(d.pop("offering_uuid"))

        project_name = d.pop("project_name")

        project_uuid = d.pop("project_uuid")

        customer_name = d.pop("customer_name")

        customer_uuid = d.pop("customer_uuid")

        billing_period = isoparse(d.pop("billing_period")).date()

        description = d.pop("description", UNSET)

        recurring = d.pop("recurring", UNSET)

        def _parse_modified_by(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        modified_by = _parse_modified_by(d.pop("modified_by", UNSET))

        component_usage = cls(
            uuid=uuid,
            created=created,
            type_=type_,
            name=name,
            measured_unit=measured_unit,
            usage=usage,
            date=date,
            resource_name=resource_name,
            resource_uuid=resource_uuid,
            offering_name=offering_name,
            offering_uuid=offering_uuid,
            project_name=project_name,
            project_uuid=project_uuid,
            customer_name=customer_name,
            customer_uuid=customer_uuid,
            billing_period=billing_period,
            description=description,
            recurring=recurring,
            modified_by=modified_by,
        )

        component_usage.additional_properties = d
        return component_usage

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
