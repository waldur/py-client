import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nested_price_estimate import NestedPriceEstimate


T = TypeVar("T", bound="ProviderCustomerProject")


@_attrs_define
class ProviderCustomerProject:
    """
    Attributes:
        uuid (UUID):
        name (str):
        resources_count (int):
        users_count (int):
        billing_price_estimate (NestedPriceEstimate):
        description (Union[Unset, str]):
        end_date (Union[None, Unset, datetime.date]): The date is inclusive. Once reached, all project resource will be
            scheduled for termination.
    """

    uuid: UUID
    name: str
    resources_count: int
    users_count: int
    billing_price_estimate: "NestedPriceEstimate"
    description: Union[Unset, str] = UNSET
    end_date: Union[None, Unset, datetime.date] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        name = self.name

        resources_count = self.resources_count

        users_count = self.users_count

        billing_price_estimate = self.billing_price_estimate.to_dict()

        description = self.description

        end_date: Union[None, Unset, str]
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.date):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "name": name,
                "resources_count": resources_count,
                "users_count": users_count,
                "billing_price_estimate": billing_price_estimate,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if end_date is not UNSET:
            field_dict["end_date"] = end_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nested_price_estimate import NestedPriceEstimate

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        resources_count = d.pop("resources_count")

        users_count = d.pop("users_count")

        billing_price_estimate = NestedPriceEstimate.from_dict(d.pop("billing_price_estimate"))

        description = d.pop("description", UNSET)

        def _parse_end_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = isoparse(data).date()

                return end_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        end_date = _parse_end_date(d.pop("end_date", UNSET))

        provider_customer_project = cls(
            uuid=uuid,
            name=name,
            resources_count=resources_count,
            users_count=users_count,
            billing_price_estimate=billing_price_estimate,
            description=description,
            end_date=end_date,
        )

        provider_customer_project.additional_properties = d
        return provider_customer_project

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
