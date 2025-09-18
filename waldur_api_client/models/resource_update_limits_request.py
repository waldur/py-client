from collections.abc import Mapping
from io import BytesIO
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, Unset

if TYPE_CHECKING:
    from ..models.resource_update_limits_request_limits import ResourceUpdateLimitsRequestLimits


T = TypeVar("T", bound="ResourceUpdateLimitsRequest")


@_attrs_define
class ResourceUpdateLimitsRequest:
    """
    Attributes:
        limits (ResourceUpdateLimitsRequestLimits):
        request_comment (Union[None, Unset, str]):
        attachment (Union[File, None, Unset]):
    """

    limits: "ResourceUpdateLimitsRequestLimits"
    request_comment: Union[None, Unset, str] = UNSET
    attachment: Union[File, None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        limits = self.limits.to_dict()

        request_comment: Union[None, Unset, str]
        if isinstance(self.request_comment, Unset):
            request_comment = UNSET
        else:
            request_comment = self.request_comment

        attachment: Union[None, Unset, types.FileTypes]
        if isinstance(self.attachment, Unset):
            attachment = UNSET
        elif isinstance(self.attachment, File):
            attachment = self.attachment.to_tuple()

        else:
            attachment = self.attachment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "limits": limits,
            }
        )
        if request_comment is not UNSET:
            field_dict["request_comment"] = request_comment
        if attachment is not UNSET:
            field_dict["attachment"] = attachment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_update_limits_request_limits import ResourceUpdateLimitsRequestLimits

        d = dict(src_dict)
        limits = ResourceUpdateLimitsRequestLimits.from_dict(d.pop("limits"))

        def _parse_request_comment(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        request_comment = _parse_request_comment(d.pop("request_comment", UNSET))

        def _parse_attachment(data: object) -> Union[File, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, bytes):
                    raise TypeError()
                attachment_type_0 = File(payload=BytesIO(data))

                return attachment_type_0
            except:  # noqa: E722
                pass
            return cast(Union[File, None, Unset], data)

        attachment = _parse_attachment(d.pop("attachment", UNSET))

        resource_update_limits_request = cls(
            limits=limits,
            request_comment=request_comment,
            attachment=attachment,
        )

        resource_update_limits_request.additional_properties = d
        return resource_update_limits_request

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
