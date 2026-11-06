from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dry_run_view_as_result_responses import DryRunViewAsResultResponses
    from ..models.dry_run_viewer import DryRunViewer


T = TypeVar("T", bound="DryRunViewAsResult")


@_attrs_define
class DryRunViewAsResult:
    """
    Attributes:
        role (str):
        offering (Union[None, int]):
        at (Union[None, int]):
        viewer (DryRunViewer):
        described_as (str):
        proposal_uuid (UUID):
        responses (DryRunViewAsResultResponses):
    """

    role: str
    offering: Union[None, int]
    at: Union[None, int]
    viewer: "DryRunViewer"
    described_as: str
    proposal_uuid: UUID
    responses: "DryRunViewAsResultResponses"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role = self.role

        offering: Union[None, int]
        offering = self.offering

        at: Union[None, int]
        at = self.at

        viewer = self.viewer.to_dict()

        described_as = self.described_as

        proposal_uuid = str(self.proposal_uuid)

        responses = self.responses.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
                "offering": offering,
                "at": at,
                "viewer": viewer,
                "described_as": described_as,
                "proposal_uuid": proposal_uuid,
                "responses": responses,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dry_run_view_as_result_responses import DryRunViewAsResultResponses
        from ..models.dry_run_viewer import DryRunViewer

        d = dict(src_dict)
        role = d.pop("role")

        def _parse_offering(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        offering = _parse_offering(d.pop("offering"))

        def _parse_at(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        at = _parse_at(d.pop("at"))

        viewer = DryRunViewer.from_dict(d.pop("viewer"))

        described_as = d.pop("described_as")

        proposal_uuid = UUID(d.pop("proposal_uuid"))

        responses = DryRunViewAsResultResponses.from_dict(d.pop("responses"))

        dry_run_view_as_result = cls(
            role=role,
            offering=offering,
            at=at,
            viewer=viewer,
            described_as=described_as,
            proposal_uuid=proposal_uuid,
            responses=responses,
        )

        dry_run_view_as_result.additional_properties = d
        return dry_run_view_as_result

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
