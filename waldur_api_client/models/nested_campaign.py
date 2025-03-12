import datetime
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.discount_type_enum import DiscountTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="NestedCampaign")


@_attrs_define
class NestedCampaign:
    """
    Attributes:
        uuid (UUID):
        name (str):
        start_date (datetime.date): Starting from this date, the campaign is active.
        end_date (datetime.date): The last day the campaign is active.
        discount_type (DiscountTypeEnum):
        discount (int):
        service_provider (str):
        stock (Union[None, Unset, int]):
        description (Union[Unset, str]):
        months (Union[Unset, int]): How many months in a row should the related service (when activated) get special
            deal (0 for indefinitely until active)
    """

    uuid: UUID
    name: str
    start_date: datetime.date
    end_date: datetime.date
    discount_type: DiscountTypeEnum
    discount: int
    service_provider: str
    stock: Union[None, Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    months: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        name = self.name

        start_date = self.start_date.isoformat()

        end_date = self.end_date.isoformat()

        discount_type = self.discount_type.value

        discount = self.discount

        service_provider = self.service_provider

        stock: Union[None, Unset, int]
        if isinstance(self.stock, Unset):
            stock = UNSET
        else:
            stock = self.stock

        description = self.description

        months = self.months

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "name": name,
                "start_date": start_date,
                "end_date": end_date,
                "discount_type": discount_type,
                "discount": discount,
                "service_provider": service_provider,
            }
        )
        if stock is not UNSET:
            field_dict["stock"] = stock
        if description is not UNSET:
            field_dict["description"] = description
        if months is not UNSET:
            field_dict["months"] = months

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        start_date = isoparse(d.pop("start_date")).date()

        end_date = isoparse(d.pop("end_date")).date()

        discount_type = DiscountTypeEnum(d.pop("discount_type"))

        discount = d.pop("discount")

        service_provider = d.pop("service_provider")

        def _parse_stock(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        stock = _parse_stock(d.pop("stock", UNSET))

        description = d.pop("description", UNSET)

        months = d.pop("months", UNSET)

        nested_campaign = cls(
            uuid=uuid,
            name=name,
            start_date=start_date,
            end_date=end_date,
            discount_type=discount_type,
            discount=discount,
            service_provider=service_provider,
            stock=stock,
            description=description,
            months=months,
        )

        nested_campaign.additional_properties = d
        return nested_campaign

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
