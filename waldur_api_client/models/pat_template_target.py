from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pat_template_binding import PatTemplateBinding


T = TypeVar("T", bound="PatTemplateTarget")


@_attrs_define
class PatTemplateTarget:
    """
    Attributes:
        type_ (str):
        uuid (UUID):
        name (str):
        context (str): Where the entity belongs, such as an offering's organization.
        features (list[str]): Optional features of the template the caller can add here.
        suggested_username (str): Staff only, where the template takes a dedicated user for this type of target: the
            username agent_user gives one when none is chosen. Empty otherwise.
        staff_access (bool): Staff only: the caller holds no role that would do here, so the token works only with
            STAFF.ACCESS added to its scopes. Such a token cannot be restricted: bindings is empty, and it can do everything
            the caller can as staff.
        bindings (list['PatTemplateBinding']): What to bind the token to (its allowed_scopes) for it to work on this
            target.
    """

    type_: str
    uuid: UUID
    name: str
    context: str
    features: list[str]
    suggested_username: str
    staff_access: bool
    bindings: list["PatTemplateBinding"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        uuid = str(self.uuid)

        name = self.name

        context = self.context

        features = self.features

        suggested_username = self.suggested_username

        staff_access = self.staff_access

        bindings = []
        for bindings_item_data in self.bindings:
            bindings_item = bindings_item_data.to_dict()
            bindings.append(bindings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "uuid": uuid,
                "name": name,
                "context": context,
                "features": features,
                "suggested_username": suggested_username,
                "staff_access": staff_access,
                "bindings": bindings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pat_template_binding import PatTemplateBinding

        d = dict(src_dict)
        type_ = d.pop("type")

        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        context = d.pop("context")

        features = cast(list[str], d.pop("features"))

        suggested_username = d.pop("suggested_username")

        staff_access = d.pop("staff_access")

        bindings = []
        _bindings = d.pop("bindings")
        for bindings_item_data in _bindings:
            bindings_item = PatTemplateBinding.from_dict(bindings_item_data)

            bindings.append(bindings_item)

        pat_template_target = cls(
            type_=type_,
            uuid=uuid,
            name=name,
            context=context,
            features=features,
            suggested_username=suggested_username,
            staff_access=staff_access,
            bindings=bindings,
        )

        pat_template_target.additional_properties = d
        return pat_template_target

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
