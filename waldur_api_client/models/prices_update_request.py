from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.prices_update_request_prices import PricesUpdateRequestPrices


T = TypeVar("T", bound="PricesUpdateRequest")


@_attrs_define
class PricesUpdateRequest:
    """
    Attributes:
        prices (PricesUpdateRequestPrices):
    """

    prices: "PricesUpdateRequestPrices"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prices = self.prices.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "prices": prices,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.prices_update_request_prices import PricesUpdateRequestPrices

        d = src_dict.copy()
        prices = PricesUpdateRequestPrices.from_dict(d.pop("prices"))

        prices_update_request = cls(
            prices=prices,
        )

        prices_update_request.additional_properties = d
        return prices_update_request

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
