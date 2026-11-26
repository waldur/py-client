from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.offering_template_difference import OfferingTemplateDifference


T = TypeVar("T", bound="OfferingTemplateDiff")


@_attrs_define
class OfferingTemplateDiff:
    """
    Attributes:
        template_uuid (UUID):
        template_name (str):
        template_version (int): The version the offering was created from.
        latest_version (Union[None, int]): The template's latest version; null for who may not see the template, as it
            is unpublished.
        created_version_differences (list['OfferingTemplateDifference']): Differences from the version the offering was
            created from.
        latest_version_differences (Union[None, list['OfferingTemplateDifference']]): Differences from the latest
            version; null with latest_version.
    """

    template_uuid: UUID
    template_name: str
    template_version: int
    latest_version: Union[None, int]
    created_version_differences: list["OfferingTemplateDifference"]
    latest_version_differences: Union[None, list["OfferingTemplateDifference"]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        template_uuid = str(self.template_uuid)

        template_name = self.template_name

        template_version = self.template_version

        latest_version: Union[None, int]
        latest_version = self.latest_version

        created_version_differences = []
        for created_version_differences_item_data in self.created_version_differences:
            created_version_differences_item = created_version_differences_item_data.to_dict()
            created_version_differences.append(created_version_differences_item)

        latest_version_differences: Union[None, list[dict[str, Any]]]
        if isinstance(self.latest_version_differences, list):
            latest_version_differences = []
            for latest_version_differences_type_0_item_data in self.latest_version_differences:
                latest_version_differences_type_0_item = latest_version_differences_type_0_item_data.to_dict()
                latest_version_differences.append(latest_version_differences_type_0_item)

        else:
            latest_version_differences = self.latest_version_differences

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "template_uuid": template_uuid,
                "template_name": template_name,
                "template_version": template_version,
                "latest_version": latest_version,
                "created_version_differences": created_version_differences,
                "latest_version_differences": latest_version_differences,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.offering_template_difference import OfferingTemplateDifference

        d = dict(src_dict)
        template_uuid = UUID(d.pop("template_uuid"))

        template_name = d.pop("template_name")

        template_version = d.pop("template_version")

        def _parse_latest_version(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        latest_version = _parse_latest_version(d.pop("latest_version"))

        created_version_differences = []
        _created_version_differences = d.pop("created_version_differences")
        for created_version_differences_item_data in _created_version_differences:
            created_version_differences_item = OfferingTemplateDifference.from_dict(
                created_version_differences_item_data
            )

            created_version_differences.append(created_version_differences_item)

        def _parse_latest_version_differences(data: object) -> Union[None, list["OfferingTemplateDifference"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                latest_version_differences_type_0 = []
                _latest_version_differences_type_0 = data
                for latest_version_differences_type_0_item_data in _latest_version_differences_type_0:
                    latest_version_differences_type_0_item = OfferingTemplateDifference.from_dict(
                        latest_version_differences_type_0_item_data
                    )

                    latest_version_differences_type_0.append(latest_version_differences_type_0_item)

                return latest_version_differences_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["OfferingTemplateDifference"]], data)

        latest_version_differences = _parse_latest_version_differences(d.pop("latest_version_differences"))

        offering_template_diff = cls(
            template_uuid=template_uuid,
            template_name=template_name,
            template_version=template_version,
            latest_version=latest_version,
            created_version_differences=created_version_differences,
            latest_version_differences=latest_version_differences,
        )

        offering_template_diff.additional_properties = d
        return offering_template_diff

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
