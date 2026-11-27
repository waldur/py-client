from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.k8s_common_flavor import K8SCommonFlavor
    from ..models.k8s_site import K8SSite


T = TypeVar("T", bound="K8SSites")


@_attrs_define
class K8SSites:
    """
    Attributes:
        sites (list['K8SSite']): The sites, in order.
        flavors (list['K8SCommonFlavor']): Flavors every site has under one name with the same vCPUs and RAM, smallest
            first.
    """

    sites: list["K8SSite"]
    flavors: list["K8SCommonFlavor"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sites = []
        for sites_item_data in self.sites:
            sites_item = sites_item_data.to_dict()
            sites.append(sites_item)

        flavors = []
        for flavors_item_data in self.flavors:
            flavors_item = flavors_item_data.to_dict()
            flavors.append(flavors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sites": sites,
                "flavors": flavors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.k8s_common_flavor import K8SCommonFlavor
        from ..models.k8s_site import K8SSite

        d = dict(src_dict)
        sites = []
        _sites = d.pop("sites")
        for sites_item_data in _sites:
            sites_item = K8SSite.from_dict(sites_item_data)

            sites.append(sites_item)

        flavors = []
        _flavors = d.pop("flavors")
        for flavors_item_data in _flavors:
            flavors_item = K8SCommonFlavor.from_dict(flavors_item_data)

            flavors.append(flavors_item)

        k8s_sites = cls(
            sites=sites,
            flavors=flavors,
        )

        k8s_sites.additional_properties = d
        return k8s_sites

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
