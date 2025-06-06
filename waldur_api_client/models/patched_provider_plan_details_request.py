from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.billing_unit import BillingUnit
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedProviderPlanDetailsRequest")


@_attrs_define
class PatchedProviderPlanDetailsRequest:
    """
    Attributes:
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        article_code (Union[Unset, str]):
        max_amount (Union[None, Unset, int]): Maximum number of plans that could be active. Plan is disabled when
            maximum amount is reached.
        archived (Union[Unset, bool]): Forbids creation of new resources.
        unit_price (Union[Unset, str]):
        unit (Union[Unset, BillingUnit]):
        backend_id (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    article_code: Union[Unset, str] = UNSET
    max_amount: Union[None, Unset, int] = UNSET
    archived: Union[Unset, bool] = UNSET
    unit_price: Union[Unset, str] = UNSET
    unit: Union[Unset, BillingUnit] = UNSET
    backend_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        article_code = self.article_code

        max_amount: Union[None, Unset, int]
        if isinstance(self.max_amount, Unset):
            max_amount = UNSET
        else:
            max_amount = self.max_amount

        archived = self.archived

        unit_price = self.unit_price

        unit: Union[Unset, str] = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit.value

        backend_id = self.backend_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if article_code is not UNSET:
            field_dict["article_code"] = article_code
        if max_amount is not UNSET:
            field_dict["max_amount"] = max_amount
        if archived is not UNSET:
            field_dict["archived"] = archived
        if unit_price is not UNSET:
            field_dict["unit_price"] = unit_price
        if unit is not UNSET:
            field_dict["unit"] = unit
        if backend_id is not UNSET:
            field_dict["backend_id"] = backend_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        article_code = d.pop("article_code", UNSET)

        def _parse_max_amount(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_amount = _parse_max_amount(d.pop("max_amount", UNSET))

        archived = d.pop("archived", UNSET)

        unit_price = d.pop("unit_price", UNSET)

        _unit = d.pop("unit", UNSET)
        unit: Union[Unset, BillingUnit]
        if isinstance(_unit, Unset):
            unit = UNSET
        else:
            unit = BillingUnit(_unit)

        backend_id = d.pop("backend_id", UNSET)

        patched_provider_plan_details_request = cls(
            name=name,
            description=description,
            article_code=article_code,
            max_amount=max_amount,
            archived=archived,
            unit_price=unit_price,
            unit=unit,
            backend_id=backend_id,
        )

        patched_provider_plan_details_request.additional_properties = d
        return patched_provider_plan_details_request

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
