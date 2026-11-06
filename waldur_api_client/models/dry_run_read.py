from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dry_run_read_data_type_0 import DryRunReadDataType0


T = TypeVar("T", bound="DryRunRead")


@_attrs_define
class DryRunRead:
    """
    Attributes:
        status (int):
        data (Union['DryRunReadDataType0', None]):
    """

    status: int
    data: Union["DryRunReadDataType0", None]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.dry_run_read_data_type_0 import DryRunReadDataType0

        status = self.status

        data: Union[None, dict[str, Any]]
        if isinstance(self.data, DryRunReadDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dry_run_read_data_type_0 import DryRunReadDataType0

        d = dict(src_dict)
        status = d.pop("status")

        def _parse_data(data: object) -> Union["DryRunReadDataType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = DryRunReadDataType0.from_dict(data)

                return data_type_0
            except:  # noqa: E722
                pass
            return cast(Union["DryRunReadDataType0", None], data)

        data = _parse_data(d.pop("data"))

        dry_run_read = cls(
            status=status,
            data=data,
        )

        dry_run_read.additional_properties = d
        return dry_run_read

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
