from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, Unset

T = TypeVar("T", bound="CallManagingOrganisationRequestMultipart")


@_attrs_define
class CallManagingOrganisationRequestMultipart:
    """
    Attributes:
        customer (str):
        description (Union[Unset, str]):
        image (Union[File, None, Unset]):
        max_active_proposals_per_applicant (Union[None, Unset, int]): How many proposals an applicant may have under
            evaluation or running as a project, across all of this organization's calls, before they may submit another.
            Empty sets no limit.
    """

    customer: str
    description: Union[Unset, str] = UNSET
    image: Union[File, None, Unset] = UNSET
    max_active_proposals_per_applicant: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        customer = self.customer

        description = self.description

        image: Union[None, Unset, types.FileTypes]
        if isinstance(self.image, Unset):
            image = UNSET
        elif isinstance(self.image, File):
            image = self.image.to_tuple()

        else:
            image = self.image

        max_active_proposals_per_applicant: Union[None, Unset, int]
        if isinstance(self.max_active_proposals_per_applicant, Unset):
            max_active_proposals_per_applicant = UNSET
        else:
            max_active_proposals_per_applicant = self.max_active_proposals_per_applicant

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customer": customer,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if image is not UNSET:
            field_dict["image"] = image
        if max_active_proposals_per_applicant is not UNSET:
            field_dict["max_active_proposals_per_applicant"] = max_active_proposals_per_applicant

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("customer", (None, str(self.customer).encode(), "text/plain")))

        if not isinstance(self.description, Unset):
            files.append(("description", (None, str(self.description).encode(), "text/plain")))

        if not isinstance(self.image, Unset):
            if isinstance(self.image, File):
                files.append(("image", self.image.to_tuple()))
            else:
                files.append(("image", (None, str(self.image).encode(), "text/plain")))

        if not isinstance(self.max_active_proposals_per_applicant, Unset):
            if isinstance(self.max_active_proposals_per_applicant, int):
                files.append(
                    (
                        "max_active_proposals_per_applicant",
                        (None, str(self.max_active_proposals_per_applicant).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "max_active_proposals_per_applicant",
                        (None, str(self.max_active_proposals_per_applicant).encode(), "text/plain"),
                    )
                )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        customer = d.pop("customer")

        description = d.pop("description", UNSET)

        def _parse_image(data: object) -> Union[File, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, bytes):
                    raise TypeError()
                image_type_0 = File(payload=BytesIO(data))

                return image_type_0
            except:  # noqa: E722
                pass
            return cast(Union[File, None, Unset], data)

        image = _parse_image(d.pop("image", UNSET))

        def _parse_max_active_proposals_per_applicant(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_active_proposals_per_applicant = _parse_max_active_proposals_per_applicant(
            d.pop("max_active_proposals_per_applicant", UNSET)
        )

        call_managing_organisation_request_multipart = cls(
            customer=customer,
            description=description,
            image=image,
            max_active_proposals_per_applicant=max_active_proposals_per_applicant,
        )

        call_managing_organisation_request_multipart.additional_properties = d
        return call_managing_organisation_request_multipart

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
