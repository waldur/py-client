from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RancherImportYamlRequest")


@_attrs_define
class RancherImportYamlRequest:
    """
    Attributes:
        yaml (str):
        default_namespace (Union[None, Unset, str]):
        namespace (Union[None, Unset, str]):
    """

    yaml: str
    default_namespace: Union[None, Unset, str] = UNSET
    namespace: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        yaml = self.yaml

        default_namespace: Union[None, Unset, str]
        if isinstance(self.default_namespace, Unset):
            default_namespace = UNSET
        else:
            default_namespace = self.default_namespace

        namespace: Union[None, Unset, str]
        if isinstance(self.namespace, Unset):
            namespace = UNSET
        else:
            namespace = self.namespace

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "yaml": yaml,
            }
        )
        if default_namespace is not UNSET:
            field_dict["default_namespace"] = default_namespace
        if namespace is not UNSET:
            field_dict["namespace"] = namespace

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        yaml = (None, str(self.yaml).encode(), "text/plain")

        default_namespace: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.default_namespace, Unset):
            default_namespace = UNSET
        elif isinstance(self.default_namespace, str):
            default_namespace = (None, str(self.default_namespace).encode(), "text/plain")
        else:
            default_namespace = (None, str(self.default_namespace).encode(), "text/plain")

        namespace: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.namespace, Unset):
            namespace = UNSET
        elif isinstance(self.namespace, str):
            namespace = (None, str(self.namespace).encode(), "text/plain")
        else:
            namespace = (None, str(self.namespace).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "yaml": yaml,
            }
        )
        if default_namespace is not UNSET:
            field_dict["default_namespace"] = default_namespace
        if namespace is not UNSET:
            field_dict["namespace"] = namespace

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        yaml = d.pop("yaml")

        def _parse_default_namespace(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        default_namespace = _parse_default_namespace(d.pop("default_namespace", UNSET))

        def _parse_namespace(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        namespace = _parse_namespace(d.pop("namespace", UNSET))

        rancher_import_yaml_request = cls(
            yaml=yaml,
            default_namespace=default_namespace,
            namespace=namespace,
        )

        rancher_import_yaml_request.additional_properties = d
        return rancher_import_yaml_request

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
