from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.call_notification_override import CallNotificationOverride
    from ..models.notification_variable import NotificationVariable
    from ..models.notification_wording import NotificationWording


T = TypeVar("T", bound="CallNotificationMailType")


@_attrs_define
class CallNotificationMailType:
    """
    Attributes:
        key (str):
        mail_type (str):
        variant (str):
        label (str):
        audience (str):
        variables (list['NotificationVariable']):
        portal_wording (NotificationWording):
        portal_overridden (bool): Whether staff reworded this mail for the whole portal.
        override (Union['CallNotificationOverride', None]):
    """

    key: str
    mail_type: str
    variant: str
    label: str
    audience: str
    variables: list["NotificationVariable"]
    portal_wording: "NotificationWording"
    portal_overridden: bool
    override: Union["CallNotificationOverride", None]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.call_notification_override import CallNotificationOverride

        key = self.key

        mail_type = self.mail_type

        variant = self.variant

        label = self.label

        audience = self.audience

        variables = []
        for variables_item_data in self.variables:
            variables_item = variables_item_data.to_dict()
            variables.append(variables_item)

        portal_wording = self.portal_wording.to_dict()

        portal_overridden = self.portal_overridden

        override: Union[None, dict[str, Any]]
        if isinstance(self.override, CallNotificationOverride):
            override = self.override.to_dict()
        else:
            override = self.override

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "mail_type": mail_type,
                "variant": variant,
                "label": label,
                "audience": audience,
                "variables": variables,
                "portal_wording": portal_wording,
                "portal_overridden": portal_overridden,
                "override": override,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.call_notification_override import CallNotificationOverride
        from ..models.notification_variable import NotificationVariable
        from ..models.notification_wording import NotificationWording

        d = dict(src_dict)
        key = d.pop("key")

        mail_type = d.pop("mail_type")

        variant = d.pop("variant")

        label = d.pop("label")

        audience = d.pop("audience")

        variables = []
        _variables = d.pop("variables")
        for variables_item_data in _variables:
            variables_item = NotificationVariable.from_dict(variables_item_data)

            variables.append(variables_item)

        portal_wording = NotificationWording.from_dict(d.pop("portal_wording"))

        portal_overridden = d.pop("portal_overridden")

        def _parse_override(data: object) -> Union["CallNotificationOverride", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                override_type_1 = CallNotificationOverride.from_dict(data)

                return override_type_1
            except:  # noqa: E722
                pass
            return cast(Union["CallNotificationOverride", None], data)

        override = _parse_override(d.pop("override"))

        call_notification_mail_type = cls(
            key=key,
            mail_type=mail_type,
            variant=variant,
            label=label,
            audience=audience,
            variables=variables,
            portal_wording=portal_wording,
            portal_overridden=portal_overridden,
            override=override,
        )

        call_notification_mail_type.additional_properties = d
        return call_notification_mail_type

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
