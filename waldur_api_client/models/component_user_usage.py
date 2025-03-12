import datetime
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComponentUserUsage")


@_attrs_define
class ComponentUserUsage:
    """
    Attributes:
        uuid (UUID):
        user (str):
        username (str):
        component_usage (str):
        usage (int):
        measured_unit (str): Unit of measurement, for example, GB.
        created (datetime.datetime):
        modified (datetime.datetime):
        resource_name (str):
        resource_uuid (UUID):
        offering_name (str):
        offering_uuid (UUID):
        project_name (str):
        project_uuid (UUID):
        customer_name (str):
        customer_uuid (UUID):
        component_type (str): Unique internal name of the measured unit, for example floating_ip.
        date (datetime.datetime):
        billing_period (datetime.date):
        description (Union[Unset, str]):
        backend_id (Union[Unset, str]):
    """

    uuid: UUID
    user: str
    username: str
    component_usage: str
    usage: int
    measured_unit: str
    created: datetime.datetime
    modified: datetime.datetime
    resource_name: str
    resource_uuid: UUID
    offering_name: str
    offering_uuid: UUID
    project_name: str
    project_uuid: UUID
    customer_name: str
    customer_uuid: UUID
    component_type: str
    date: datetime.datetime
    billing_period: datetime.date
    description: Union[Unset, str] = UNSET
    backend_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        user = self.user

        username = self.username

        component_usage = self.component_usage

        usage = self.usage

        measured_unit = self.measured_unit

        created = self.created.isoformat()

        modified = self.modified.isoformat()

        resource_name = self.resource_name

        resource_uuid = str(self.resource_uuid)

        offering_name = self.offering_name

        offering_uuid = str(self.offering_uuid)

        project_name = self.project_name

        project_uuid = str(self.project_uuid)

        customer_name = self.customer_name

        customer_uuid = str(self.customer_uuid)

        component_type = self.component_type

        date = self.date.isoformat()

        billing_period = self.billing_period.isoformat()

        description = self.description

        backend_id = self.backend_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "user": user,
                "username": username,
                "component_usage": component_usage,
                "usage": usage,
                "measured_unit": measured_unit,
                "created": created,
                "modified": modified,
                "resource_name": resource_name,
                "resource_uuid": resource_uuid,
                "offering_name": offering_name,
                "offering_uuid": offering_uuid,
                "project_name": project_name,
                "project_uuid": project_uuid,
                "customer_name": customer_name,
                "customer_uuid": customer_uuid,
                "component_type": component_type,
                "date": date,
                "billing_period": billing_period,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if backend_id is not UNSET:
            field_dict["backend_id"] = backend_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = UUID(d.pop("uuid"))

        user = d.pop("user")

        username = d.pop("username")

        component_usage = d.pop("component_usage")

        usage = d.pop("usage")

        measured_unit = d.pop("measured_unit")

        created = isoparse(d.pop("created"))

        modified = isoparse(d.pop("modified"))

        resource_name = d.pop("resource_name")

        resource_uuid = UUID(d.pop("resource_uuid"))

        offering_name = d.pop("offering_name")

        offering_uuid = UUID(d.pop("offering_uuid"))

        project_name = d.pop("project_name")

        project_uuid = UUID(d.pop("project_uuid"))

        customer_name = d.pop("customer_name")

        customer_uuid = UUID(d.pop("customer_uuid"))

        component_type = d.pop("component_type")

        date = isoparse(d.pop("date"))

        billing_period = isoparse(d.pop("billing_period")).date()

        description = d.pop("description", UNSET)

        backend_id = d.pop("backend_id", UNSET)

        component_user_usage = cls(
            uuid=uuid,
            user=user,
            username=username,
            component_usage=component_usage,
            usage=usage,
            measured_unit=measured_unit,
            created=created,
            modified=modified,
            resource_name=resource_name,
            resource_uuid=resource_uuid,
            offering_name=offering_name,
            offering_uuid=offering_uuid,
            project_name=project_name,
            project_uuid=project_uuid,
            customer_name=customer_name,
            customer_uuid=customer_uuid,
            component_type=component_type,
            date=date,
            billing_period=billing_period,
            description=description,
            backend_id=backend_id,
        )

        component_user_usage.additional_properties = d
        return component_user_usage

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
