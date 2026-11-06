from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProposalSetPanelRequest")


@_attrs_define
class ProposalSetPanelRequest:
    """
    Attributes:
        panel (Union[None, UUID]): The panel of the proposal's call that evaluates it from now on; null takes it off any
            panel.
    """

    panel: Union[None, UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        panel: Union[None, str]
        if isinstance(self.panel, UUID):
            panel = str(self.panel)
        else:
            panel = self.panel

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "panel": panel,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_panel(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                panel_type_0 = UUID(data)

                return panel_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        panel = _parse_panel(d.pop("panel"))

        proposal_set_panel_request = cls(
            panel=panel,
        )

        proposal_set_panel_request.additional_properties = d
        return proposal_set_panel_request

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
