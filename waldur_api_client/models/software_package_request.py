from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.software_package_request_categories import SoftwarePackageRequestCategories
    from ..models.software_package_request_licenses import SoftwarePackageRequestLicenses
    from ..models.software_package_request_maintainers import SoftwarePackageRequestMaintainers


T = TypeVar("T", bound="SoftwarePackageRequest")


@_attrs_define
class SoftwarePackageRequest:
    """
    Attributes:
        catalog (str):
        name (str):
        description (Union[Unset, str]):
        homepage (Union[None, Unset, str]):
        categories (Union[Unset, SoftwarePackageRequestCategories]): Package categories (e.g., ['bio', 'hpc', 'build-
            tools'])
        licenses (Union[Unset, SoftwarePackageRequestLicenses]): Software licenses (e.g., ['GPL-3.0', 'MIT'])
        maintainers (Union[Unset, SoftwarePackageRequestMaintainers]): Package maintainers
        is_extension (Union[Unset, bool]): Whether this package is an extension of another package
    """

    catalog: str
    name: str
    description: Union[Unset, str] = UNSET
    homepage: Union[None, Unset, str] = UNSET
    categories: Union[Unset, "SoftwarePackageRequestCategories"] = UNSET
    licenses: Union[Unset, "SoftwarePackageRequestLicenses"] = UNSET
    maintainers: Union[Unset, "SoftwarePackageRequestMaintainers"] = UNSET
    is_extension: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        catalog = self.catalog

        name = self.name

        description = self.description

        homepage: Union[None, Unset, str]
        if isinstance(self.homepage, Unset):
            homepage = UNSET
        else:
            homepage = self.homepage

        categories: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories.to_dict()

        licenses: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.licenses, Unset):
            licenses = self.licenses.to_dict()

        maintainers: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.maintainers, Unset):
            maintainers = self.maintainers.to_dict()

        is_extension = self.is_extension

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "catalog": catalog,
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if homepage is not UNSET:
            field_dict["homepage"] = homepage
        if categories is not UNSET:
            field_dict["categories"] = categories
        if licenses is not UNSET:
            field_dict["licenses"] = licenses
        if maintainers is not UNSET:
            field_dict["maintainers"] = maintainers
        if is_extension is not UNSET:
            field_dict["is_extension"] = is_extension

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.software_package_request_categories import SoftwarePackageRequestCategories
        from ..models.software_package_request_licenses import SoftwarePackageRequestLicenses
        from ..models.software_package_request_maintainers import SoftwarePackageRequestMaintainers

        d = dict(src_dict)
        catalog = d.pop("catalog")

        name = d.pop("name")

        description = d.pop("description", UNSET)

        def _parse_homepage(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        homepage = _parse_homepage(d.pop("homepage", UNSET))

        _categories = d.pop("categories", UNSET)
        categories: Union[Unset, SoftwarePackageRequestCategories]
        if isinstance(_categories, Unset):
            categories = UNSET
        else:
            categories = SoftwarePackageRequestCategories.from_dict(_categories)

        _licenses = d.pop("licenses", UNSET)
        licenses: Union[Unset, SoftwarePackageRequestLicenses]
        if isinstance(_licenses, Unset):
            licenses = UNSET
        else:
            licenses = SoftwarePackageRequestLicenses.from_dict(_licenses)

        _maintainers = d.pop("maintainers", UNSET)
        maintainers: Union[Unset, SoftwarePackageRequestMaintainers]
        if isinstance(_maintainers, Unset):
            maintainers = UNSET
        else:
            maintainers = SoftwarePackageRequestMaintainers.from_dict(_maintainers)

        is_extension = d.pop("is_extension", UNSET)

        software_package_request = cls(
            catalog=catalog,
            name=name,
            description=description,
            homepage=homepage,
            categories=categories,
            licenses=licenses,
            maintainers=maintainers,
            is_extension=is_extension,
        )

        software_package_request.additional_properties = d
        return software_package_request

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
