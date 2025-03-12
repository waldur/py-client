from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.offering_options_request_options import OfferingOptionsRequestOptions


T = TypeVar("T", bound="OfferingOptionsRequest")


@_attrs_define
class OfferingOptionsRequest:
    """
    Attributes:
        order (list[str]):
        options (OfferingOptionsRequestOptions):
    """

    order: list[str]
    options: "OfferingOptionsRequestOptions"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order = self.order

        options = self.options.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "order": order,
                "options": options,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.offering_options_request_options import OfferingOptionsRequestOptions

        d = src_dict.copy()
        order = cast(list[str], d.pop("order"))

        options = OfferingOptionsRequestOptions.from_dict(d.pop("options"))

        offering_options_request = cls(
            order=order,
            options=options,
        )

        offering_options_request.additional_properties = d
        return offering_options_request

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
