from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.payment_type_enum import PaymentTypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.payment_profile_attributes import PaymentProfileAttributes


T = TypeVar("T", bound="PaymentProfile")


@_attrs_define
class PaymentProfile:
    """
    Attributes:
        uuid (UUID):
        url (str):
        name (str):
        organization_uuid (UUID):
        organization (str):
        payment_type (PaymentTypeEnum):
        payment_type_display (str):
        attributes (Union[Unset, PaymentProfileAttributes]):
        is_active (Union[None, Unset, bool]):  Default: True.
    """

    uuid: UUID
    url: str
    name: str
    organization_uuid: UUID
    organization: str
    payment_type: PaymentTypeEnum
    payment_type_display: str
    attributes: Union[Unset, "PaymentProfileAttributes"] = UNSET
    is_active: Union[None, Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        url = self.url

        name = self.name

        organization_uuid = str(self.organization_uuid)

        organization = self.organization

        payment_type = self.payment_type.value

        payment_type_display = self.payment_type_display

        attributes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        is_active: Union[None, Unset, bool]
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "url": url,
                "name": name,
                "organization_uuid": organization_uuid,
                "organization": organization,
                "payment_type": payment_type,
                "payment_type_display": payment_type_display,
            }
        )
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.payment_profile_attributes import PaymentProfileAttributes

        d = src_dict.copy()
        uuid = UUID(d.pop("uuid"))

        url = d.pop("url")

        name = d.pop("name")

        organization_uuid = UUID(d.pop("organization_uuid"))

        organization = d.pop("organization")

        payment_type = PaymentTypeEnum(d.pop("payment_type"))

        payment_type_display = d.pop("payment_type_display")

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, PaymentProfileAttributes]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = PaymentProfileAttributes.from_dict(_attributes)

        def _parse_is_active(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_active = _parse_is_active(d.pop("is_active", UNSET))

        payment_profile = cls(
            uuid=uuid,
            url=url,
            name=name,
            organization_uuid=organization_uuid,
            organization=organization,
            payment_type=payment_type,
            payment_type_display=payment_type_display,
            attributes=attributes,
            is_active=is_active,
        )

        payment_profile.additional_properties = d
        return payment_profile

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
