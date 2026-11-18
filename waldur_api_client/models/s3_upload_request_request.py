from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, Unset

T = TypeVar("T", bound="S3UploadRequestRequest")


@_attrs_define
class S3UploadRequestRequest:
    """
    Attributes:
        bucket (str):
        key (str):
        file (File):
        overwrite (Union[Unset, bool]): Replace a file of the same name. Without it, an existing file is refused with
            409 ObjectExists. Default: False.
    """

    bucket: str
    key: str
    file: File
    overwrite: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket = self.bucket

        key = self.key

        file = self.file.to_tuple()

        overwrite = self.overwrite

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bucket": bucket,
                "key": key,
                "file": file,
            }
        )
        if overwrite is not UNSET:
            field_dict["overwrite"] = overwrite

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("bucket", (None, str(self.bucket).encode(), "text/plain")))

        files.append(("key", (None, str(self.key).encode(), "text/plain")))

        files.append(("file", self.file.to_tuple()))

        if not isinstance(self.overwrite, Unset):
            files.append(("overwrite", (None, str(self.overwrite).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bucket = d.pop("bucket")

        key = d.pop("key")

        file = File(payload=BytesIO(d.pop("file")))

        overwrite = d.pop("overwrite", UNSET)

        s3_upload_request_request = cls(
            bucket=bucket,
            key=key,
            file=file,
            overwrite=overwrite,
        )

        s3_upload_request_request.additional_properties = d
        return s3_upload_request_request

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
