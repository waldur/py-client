from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.k8s_site_flavor import K8SSiteFlavor


T = TypeVar("T", bound="K8SCommonFlavor")


@_attrs_define
class K8SCommonFlavor:
    """
    Attributes:
        name (str):
        cores (int):
        ram (int): RAM in MiB.
        disk (int): Root disk in MiB; the smallest among the sites.
        sites (list['K8SSiteFlavor']): The flavor of every site, in site order.
    """

    name: str
    cores: int
    ram: int
    disk: int
    sites: list["K8SSiteFlavor"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        cores = self.cores

        ram = self.ram

        disk = self.disk

        sites = []
        for sites_item_data in self.sites:
            sites_item = sites_item_data.to_dict()
            sites.append(sites_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "cores": cores,
                "ram": ram,
                "disk": disk,
                "sites": sites,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.k8s_site_flavor import K8SSiteFlavor

        d = dict(src_dict)
        name = d.pop("name")

        cores = d.pop("cores")

        ram = d.pop("ram")

        disk = d.pop("disk")

        sites = []
        _sites = d.pop("sites")
        for sites_item_data in _sites:
            sites_item = K8SSiteFlavor.from_dict(sites_item_data)

            sites.append(sites_item)

        k8s_common_flavor = cls(
            name=name,
            cores=cores,
            ram=ram,
            disk=disk,
            sites=sites,
        )

        k8s_common_flavor.additional_properties = d
        return k8s_common_flavor

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
