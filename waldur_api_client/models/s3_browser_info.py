from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.s3_browser_capabilities import S3BrowserCapabilities
    from ..models.s3_quotas import S3Quotas


T = TypeVar("T", bound="S3BrowserInfo")


@_attrs_define
class S3BrowserInfo:
    """
    Attributes:
        endpoint (str):
        region (str):
        access_key (str): The key's access key id, for client instructions; never the secret.
        max_upload_size (int): Largest file, in bytes, that upload accepts; larger ones need an S3 client.
        quotas (S3Quotas):
        capabilities (S3BrowserCapabilities):
    """

    endpoint: str
    region: str
    access_key: str
    max_upload_size: int
    quotas: "S3Quotas"
    capabilities: "S3BrowserCapabilities"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        endpoint = self.endpoint

        region = self.region

        access_key = self.access_key

        max_upload_size = self.max_upload_size

        quotas = self.quotas.to_dict()

        capabilities = self.capabilities.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endpoint": endpoint,
                "region": region,
                "access_key": access_key,
                "max_upload_size": max_upload_size,
                "quotas": quotas,
                "capabilities": capabilities,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.s3_browser_capabilities import S3BrowserCapabilities
        from ..models.s3_quotas import S3Quotas

        d = dict(src_dict)
        endpoint = d.pop("endpoint")

        region = d.pop("region")

        access_key = d.pop("access_key")

        max_upload_size = d.pop("max_upload_size")

        quotas = S3Quotas.from_dict(d.pop("quotas"))

        capabilities = S3BrowserCapabilities.from_dict(d.pop("capabilities"))

        s3_browser_info = cls(
            endpoint=endpoint,
            region=region,
            access_key=access_key,
            max_upload_size=max_upload_size,
            quotas=quotas,
            capabilities=capabilities,
        )

        s3_browser_info.additional_properties = d
        return s3_browser_info

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
