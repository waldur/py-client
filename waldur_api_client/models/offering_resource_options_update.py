from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.offering_options import OfferingOptions


T = TypeVar("T", bound="OfferingResourceOptionsUpdate")


@_attrs_define
class OfferingResourceOptionsUpdate:
    """
    Attributes:
        resource_options (OfferingOptions):
    """

    resource_options: "OfferingOptions"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_options = self.resource_options.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource_options": resource_options,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.offering_options import OfferingOptions

        d = src_dict.copy()
        resource_options = OfferingOptions.from_dict(d.pop("resource_options"))

        offering_resource_options_update = cls(
            resource_options=resource_options,
        )

        offering_resource_options_update.additional_properties = d
        return offering_resource_options_update

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
