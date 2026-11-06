from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.resource_pool_cell import ResourcePoolCell


T = TypeVar("T", bound="ResourcePoolUsage")


@_attrs_define
class ResourcePoolUsage:
    """
    Attributes:
        offering_component_uuid (Union[None, UUID]): The component rule, empty while none is set: a proposal may then
            request any amount of it.
        requested_offering_uuid (UUID):
        offering_name (str):
        component_type (str):
        component_name (str):
        measured_unit (str):
        limit_period (str):
        cells (list['ResourcePoolCell']):
    """

    offering_component_uuid: Union[None, UUID]
    requested_offering_uuid: UUID
    offering_name: str
    component_type: str
    component_name: str
    measured_unit: str
    limit_period: str
    cells: list["ResourcePoolCell"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        offering_component_uuid: Union[None, str]
        if isinstance(self.offering_component_uuid, UUID):
            offering_component_uuid = str(self.offering_component_uuid)
        else:
            offering_component_uuid = self.offering_component_uuid

        requested_offering_uuid = str(self.requested_offering_uuid)

        offering_name = self.offering_name

        component_type = self.component_type

        component_name = self.component_name

        measured_unit = self.measured_unit

        limit_period = self.limit_period

        cells = []
        for cells_item_data in self.cells:
            cells_item = cells_item_data.to_dict()
            cells.append(cells_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "offering_component_uuid": offering_component_uuid,
                "requested_offering_uuid": requested_offering_uuid,
                "offering_name": offering_name,
                "component_type": component_type,
                "component_name": component_name,
                "measured_unit": measured_unit,
                "limit_period": limit_period,
                "cells": cells,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_pool_cell import ResourcePoolCell

        d = dict(src_dict)

        def _parse_offering_component_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                offering_component_uuid_type_0 = UUID(data)

                return offering_component_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        offering_component_uuid = _parse_offering_component_uuid(d.pop("offering_component_uuid"))

        requested_offering_uuid = UUID(d.pop("requested_offering_uuid"))

        offering_name = d.pop("offering_name")

        component_type = d.pop("component_type")

        component_name = d.pop("component_name")

        measured_unit = d.pop("measured_unit")

        limit_period = d.pop("limit_period")

        cells = []
        _cells = d.pop("cells")
        for cells_item_data in _cells:
            cells_item = ResourcePoolCell.from_dict(cells_item_data)

            cells.append(cells_item)

        resource_pool_usage = cls(
            offering_component_uuid=offering_component_uuid,
            requested_offering_uuid=requested_offering_uuid,
            offering_name=offering_name,
            component_type=component_type,
            component_name=component_name,
            measured_unit=measured_unit,
            limit_period=limit_period,
            cells=cells,
        )

        resource_pool_usage.additional_properties = d
        return resource_pool_usage

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
