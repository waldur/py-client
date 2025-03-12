import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.blank_enum import BlankEnum
from ..models.oecd_fos_2007_code_enum import OecdFos2007CodeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nested_price_estimate import NestedPriceEstimate
    from ..models.project_marketplace_resource_count import ProjectMarketplaceResourceCount


T = TypeVar("T", bound="Project")


@_attrs_define
class Project:
    """
    Attributes:
        url (str):
        uuid (UUID):
        name (str):
        slug (str):
        customer (str):
        customer_uuid (UUID):
        customer_name (str):
        customer_slug (str):
        customer_native_name (str):
        customer_abbreviation (str):
        created (datetime.datetime):
        type_name (str):
        type_uuid (UUID):
        oecd_fos_2007_label (str):
        resources_count (int):
        project_credit (Union[None, float]):
        marketplace_resource_count (ProjectMarketplaceResourceCount):
        billing_price_estimate (NestedPriceEstimate):
        description (Union[Unset, str]):
        type_ (Union[None, Unset, str]):
        backend_id (Union[Unset, str]):
        start_date (Union[None, Unset, datetime.date]):
        end_date (Union[None, Unset, datetime.date]): The date is inclusive. Once reached, all project resource will be
            scheduled for termination.
        end_date_requested_by (Union[None, Unset, str]):
        oecd_fos_2007_code (Union[BlankEnum, None, OecdFos2007CodeEnum, Unset]):
        is_industry (Union[Unset, bool]):
        image (Union[None, Unset, str]):
    """

    url: str
    uuid: UUID
    name: str
    slug: str
    customer: str
    customer_uuid: UUID
    customer_name: str
    customer_slug: str
    customer_native_name: str
    customer_abbreviation: str
    created: datetime.datetime
    type_name: str
    type_uuid: UUID
    oecd_fos_2007_label: str
    resources_count: int
    project_credit: Union[None, float]
    marketplace_resource_count: "ProjectMarketplaceResourceCount"
    billing_price_estimate: "NestedPriceEstimate"
    description: Union[Unset, str] = UNSET
    type_: Union[None, Unset, str] = UNSET
    backend_id: Union[Unset, str] = UNSET
    start_date: Union[None, Unset, datetime.date] = UNSET
    end_date: Union[None, Unset, datetime.date] = UNSET
    end_date_requested_by: Union[None, Unset, str] = UNSET
    oecd_fos_2007_code: Union[BlankEnum, None, OecdFos2007CodeEnum, Unset] = UNSET
    is_industry: Union[Unset, bool] = UNSET
    image: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        uuid = str(self.uuid)

        name = self.name

        slug = self.slug

        customer = self.customer

        customer_uuid = str(self.customer_uuid)

        customer_name = self.customer_name

        customer_slug = self.customer_slug

        customer_native_name = self.customer_native_name

        customer_abbreviation = self.customer_abbreviation

        created = self.created.isoformat()

        type_name = self.type_name

        type_uuid = str(self.type_uuid)

        oecd_fos_2007_label = self.oecd_fos_2007_label

        resources_count = self.resources_count

        project_credit: Union[None, float]
        project_credit = self.project_credit

        marketplace_resource_count = self.marketplace_resource_count.to_dict()

        billing_price_estimate = self.billing_price_estimate.to_dict()

        description = self.description

        type_: Union[None, Unset, str]
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        backend_id = self.backend_id

        start_date: Union[None, Unset, str]
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        elif isinstance(self.start_date, datetime.date):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        end_date: Union[None, Unset, str]
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.date):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        end_date_requested_by: Union[None, Unset, str]
        if isinstance(self.end_date_requested_by, Unset):
            end_date_requested_by = UNSET
        else:
            end_date_requested_by = self.end_date_requested_by

        oecd_fos_2007_code: Union[None, Unset, str]
        if isinstance(self.oecd_fos_2007_code, Unset):
            oecd_fos_2007_code = UNSET
        elif isinstance(self.oecd_fos_2007_code, OecdFos2007CodeEnum):
            oecd_fos_2007_code = self.oecd_fos_2007_code.value
        elif isinstance(self.oecd_fos_2007_code, BlankEnum):
            oecd_fos_2007_code = self.oecd_fos_2007_code.value
        else:
            oecd_fos_2007_code = self.oecd_fos_2007_code

        is_industry = self.is_industry

        image: Union[None, Unset, str]
        if isinstance(self.image, Unset):
            image = UNSET
        else:
            image = self.image

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "uuid": uuid,
                "name": name,
                "slug": slug,
                "customer": customer,
                "customer_uuid": customer_uuid,
                "customer_name": customer_name,
                "customer_slug": customer_slug,
                "customer_native_name": customer_native_name,
                "customer_abbreviation": customer_abbreviation,
                "created": created,
                "type_name": type_name,
                "type_uuid": type_uuid,
                "oecd_fos_2007_label": oecd_fos_2007_label,
                "resources_count": resources_count,
                "project_credit": project_credit,
                "marketplace_resource_count": marketplace_resource_count,
                "billing_price_estimate": billing_price_estimate,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if type_ is not UNSET:
            field_dict["type"] = type_
        if backend_id is not UNSET:
            field_dict["backend_id"] = backend_id
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if end_date_requested_by is not UNSET:
            field_dict["end_date_requested_by"] = end_date_requested_by
        if oecd_fos_2007_code is not UNSET:
            field_dict["oecd_fos_2007_code"] = oecd_fos_2007_code
        if is_industry is not UNSET:
            field_dict["is_industry"] = is_industry
        if image is not UNSET:
            field_dict["image"] = image

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.nested_price_estimate import NestedPriceEstimate
        from ..models.project_marketplace_resource_count import ProjectMarketplaceResourceCount

        d = src_dict.copy()
        url = d.pop("url")

        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        slug = d.pop("slug")

        customer = d.pop("customer")

        customer_uuid = UUID(d.pop("customer_uuid"))

        customer_name = d.pop("customer_name")

        customer_slug = d.pop("customer_slug")

        customer_native_name = d.pop("customer_native_name")

        customer_abbreviation = d.pop("customer_abbreviation")

        created = isoparse(d.pop("created"))

        type_name = d.pop("type_name")

        type_uuid = UUID(d.pop("type_uuid"))

        oecd_fos_2007_label = d.pop("oecd_fos_2007_label")

        resources_count = d.pop("resources_count")

        def _parse_project_credit(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        project_credit = _parse_project_credit(d.pop("project_credit"))

        marketplace_resource_count = ProjectMarketplaceResourceCount.from_dict(d.pop("marketplace_resource_count"))

        billing_price_estimate = NestedPriceEstimate.from_dict(d.pop("billing_price_estimate"))

        description = d.pop("description", UNSET)

        def _parse_type_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        type_ = _parse_type_(d.pop("type", UNSET))

        backend_id = d.pop("backend_id", UNSET)

        def _parse_start_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_type_0 = isoparse(data).date()

                return start_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        start_date = _parse_start_date(d.pop("start_date", UNSET))

        def _parse_end_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = isoparse(data).date()

                return end_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        end_date = _parse_end_date(d.pop("end_date", UNSET))

        def _parse_end_date_requested_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        end_date_requested_by = _parse_end_date_requested_by(d.pop("end_date_requested_by", UNSET))

        def _parse_oecd_fos_2007_code(data: object) -> Union[BlankEnum, None, OecdFos2007CodeEnum, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                oecd_fos_2007_code_type_0 = OecdFos2007CodeEnum(data)

                return oecd_fos_2007_code_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                oecd_fos_2007_code_type_1 = BlankEnum(data)

                return oecd_fos_2007_code_type_1
            except:  # noqa: E722
                pass
            return cast(Union[BlankEnum, None, OecdFos2007CodeEnum, Unset], data)

        oecd_fos_2007_code = _parse_oecd_fos_2007_code(d.pop("oecd_fos_2007_code", UNSET))

        is_industry = d.pop("is_industry", UNSET)

        def _parse_image(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        image = _parse_image(d.pop("image", UNSET))

        project = cls(
            url=url,
            uuid=uuid,
            name=name,
            slug=slug,
            customer=customer,
            customer_uuid=customer_uuid,
            customer_name=customer_name,
            customer_slug=customer_slug,
            customer_native_name=customer_native_name,
            customer_abbreviation=customer_abbreviation,
            created=created,
            type_name=type_name,
            type_uuid=type_uuid,
            oecd_fos_2007_label=oecd_fos_2007_label,
            resources_count=resources_count,
            project_credit=project_credit,
            marketplace_resource_count=marketplace_resource_count,
            billing_price_estimate=billing_price_estimate,
            description=description,
            type_=type_,
            backend_id=backend_id,
            start_date=start_date,
            end_date=end_date,
            end_date_requested_by=end_date_requested_by,
            oecd_fos_2007_code=oecd_fos_2007_code,
            is_industry=is_industry,
            image=image,
        )

        project.additional_properties = d
        return project

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
