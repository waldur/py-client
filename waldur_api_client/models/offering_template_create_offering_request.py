from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.offering_template_create_offering_request_parameters import (
        OfferingTemplateCreateOfferingRequestParameters,
    )


T = TypeVar("T", bound="OfferingTemplateCreateOfferingRequest")


@_attrs_define
class OfferingTemplateCreateOfferingRequest:
    """
    Attributes:
        customer (UUID): The organization the offering is created for.
        category (UUID): The category the offering is listed in.
        name (str): Name of the new offering.
        parameters (Union[Unset, OfferingTemplateCreateOfferingRequestParameters]): A value for each of the template's
            parameters, by key. A parameter left out takes its default.
        dry_run (Union[Unset, bool]): Check everything and report what would be created, creating nothing. Default:
            False.
    """

    customer: UUID
    category: UUID
    name: str
    parameters: Union[Unset, "OfferingTemplateCreateOfferingRequestParameters"] = UNSET
    dry_run: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        customer = str(self.customer)

        category = str(self.category)

        name = self.name

        parameters: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        dry_run = self.dry_run

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customer": customer,
                "category": category,
                "name": name,
            }
        )
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.offering_template_create_offering_request_parameters import (
            OfferingTemplateCreateOfferingRequestParameters,
        )

        d = dict(src_dict)
        customer = UUID(d.pop("customer"))

        category = UUID(d.pop("category"))

        name = d.pop("name")

        _parameters = d.pop("parameters", UNSET)
        parameters: Union[Unset, OfferingTemplateCreateOfferingRequestParameters]
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = OfferingTemplateCreateOfferingRequestParameters.from_dict(_parameters)

        dry_run = d.pop("dry_run", UNSET)

        offering_template_create_offering_request = cls(
            customer=customer,
            category=category,
            name=name,
            parameters=parameters,
            dry_run=dry_run,
        )

        offering_template_create_offering_request.additional_properties = d
        return offering_template_create_offering_request

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
