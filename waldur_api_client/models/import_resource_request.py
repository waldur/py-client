from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.import_resource_request_additional_details_type_0 import ImportResourceRequestAdditionalDetailsType0


T = TypeVar("T", bound="ImportResourceRequest")


@_attrs_define
class ImportResourceRequest:
    """
    Attributes:
        backend_id (str): Backend identifier of the resource
        project (UUID): Target project for the resource
        plan (Union[Unset, UUID]):
        additional_details (Union['ImportResourceRequestAdditionalDetailsType0', None, Unset]):
    """

    backend_id: str
    project: UUID
    plan: Union[Unset, UUID] = UNSET
    additional_details: Union["ImportResourceRequestAdditionalDetailsType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.import_resource_request_additional_details_type_0 import (
            ImportResourceRequestAdditionalDetailsType0,
        )

        backend_id = self.backend_id

        project = str(self.project)

        plan: Union[Unset, str] = UNSET
        if not isinstance(self.plan, Unset):
            plan = str(self.plan)

        additional_details: Union[None, Unset, dict[str, Any]]
        if isinstance(self.additional_details, Unset):
            additional_details = UNSET
        elif isinstance(self.additional_details, ImportResourceRequestAdditionalDetailsType0):
            additional_details = self.additional_details.to_dict()
        else:
            additional_details = self.additional_details

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "backend_id": backend_id,
                "project": project,
            }
        )
        if plan is not UNSET:
            field_dict["plan"] = plan
        if additional_details is not UNSET:
            field_dict["additional_details"] = additional_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_resource_request_additional_details_type_0 import (
            ImportResourceRequestAdditionalDetailsType0,
        )

        d = dict(src_dict)
        backend_id = d.pop("backend_id")

        project = UUID(d.pop("project"))

        _plan = d.pop("plan", UNSET)
        plan: Union[Unset, UUID]
        if isinstance(_plan, Unset):
            plan = UNSET
        else:
            plan = UUID(_plan)

        def _parse_additional_details(
            data: object,
        ) -> Union["ImportResourceRequestAdditionalDetailsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                additional_details_type_0 = ImportResourceRequestAdditionalDetailsType0.from_dict(data)

                return additional_details_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ImportResourceRequestAdditionalDetailsType0", None, Unset], data)

        additional_details = _parse_additional_details(d.pop("additional_details", UNSET))

        import_resource_request = cls(
            backend_id=backend_id,
            project=project,
            plan=plan,
            additional_details=additional_details,
        )

        import_resource_request.additional_properties = d
        return import_resource_request

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
