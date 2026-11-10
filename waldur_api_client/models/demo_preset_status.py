from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.demo_preset_load_job import DemoPresetLoadJob
    from ..models.demo_preset_user import DemoPresetUser


T = TypeVar("T", bound="DemoPresetStatus")


@_attrs_define
class DemoPresetStatus:
    """
    Attributes:
        loading (bool): Whether a load is pending or running; the API answers 503 meanwhile.
        load (Union['DemoPresetLoadJob', None]): The latest load, if any.
        users (list['DemoPresetUser']): The loaded preset's users without a staff or support role, for quick login, once
            the latest load is done.
    """

    loading: bool
    load: Union["DemoPresetLoadJob", None]
    users: list["DemoPresetUser"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.demo_preset_load_job import DemoPresetLoadJob

        loading = self.loading

        load: Union[None, dict[str, Any]]
        if isinstance(self.load, DemoPresetLoadJob):
            load = self.load.to_dict()
        else:
            load = self.load

        users = []
        for users_item_data in self.users:
            users_item = users_item_data.to_dict()
            users.append(users_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "loading": loading,
                "load": load,
                "users": users,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.demo_preset_load_job import DemoPresetLoadJob
        from ..models.demo_preset_user import DemoPresetUser

        d = dict(src_dict)
        loading = d.pop("loading")

        def _parse_load(data: object) -> Union["DemoPresetLoadJob", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                load_type_1 = DemoPresetLoadJob.from_dict(data)

                return load_type_1
            except:  # noqa: E722
                pass
            return cast(Union["DemoPresetLoadJob", None], data)

        load = _parse_load(d.pop("load"))

        users = []
        _users = d.pop("users")
        for users_item_data in _users:
            users_item = DemoPresetUser.from_dict(users_item_data)

            users.append(users_item)

        demo_preset_status = cls(
            loading=loading,
            load=load,
            users=users,
        )

        demo_preset_status.additional_properties = d
        return demo_preset_status

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
