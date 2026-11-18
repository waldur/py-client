from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.s3_acl import S3Acl
    from ..models.s3_cors_rule import S3CorsRule
    from ..models.s3_lifecycle_rule import S3LifecycleRule
    from ..models.s3_object_lock import S3ObjectLock
    from ..models.s3_public_access_block import S3PublicAccessBlock
    from ..models.s3_tag import S3Tag
    from ..models.s3_versioning import S3Versioning


T = TypeVar("T", bound="S3BucketDetails")


@_attrs_define
class S3BucketDetails:
    """
    Attributes:
        bucket (str):
        objects (Union[None, int]):
        size_bytes (Union[None, int]):
        location (Union[None, str]):
        versioning (Union['S3Versioning', None]):
        object_lock (Union['S3ObjectLock', None]):
        acl (Union['S3Acl', None]):
        policy (Union[None, str]): The bucket policy as JSON.
        policy_public (Union[None, bool]):
        public_access_block (Union['S3PublicAccessBlock', None]):
        lifecycle_rules (Union[None, list['S3LifecycleRule']]):
        encryption (Union[None, str]): Default server-side encryption algorithm.
        cors_rules (Union[None, list['S3CorsRule']]):
        tags (Union[None, list['S3Tag']]):
        public_acl_groups (list[str]):
        is_public (bool): Readable by anyone: through an ACL grant to a public group, or a policy the gateway reports as
            public.
        unavailable (list[str]): Parts the gateway refused or does not implement.
    """

    bucket: str
    objects: Union[None, int]
    size_bytes: Union[None, int]
    location: Union[None, str]
    versioning: Union["S3Versioning", None]
    object_lock: Union["S3ObjectLock", None]
    acl: Union["S3Acl", None]
    policy: Union[None, str]
    policy_public: Union[None, bool]
    public_access_block: Union["S3PublicAccessBlock", None]
    lifecycle_rules: Union[None, list["S3LifecycleRule"]]
    encryption: Union[None, str]
    cors_rules: Union[None, list["S3CorsRule"]]
    tags: Union[None, list["S3Tag"]]
    public_acl_groups: list[str]
    is_public: bool
    unavailable: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.s3_acl import S3Acl
        from ..models.s3_object_lock import S3ObjectLock
        from ..models.s3_public_access_block import S3PublicAccessBlock
        from ..models.s3_versioning import S3Versioning

        bucket = self.bucket

        objects: Union[None, int]
        objects = self.objects

        size_bytes: Union[None, int]
        size_bytes = self.size_bytes

        location: Union[None, str]
        location = self.location

        versioning: Union[None, dict[str, Any]]
        if isinstance(self.versioning, S3Versioning):
            versioning = self.versioning.to_dict()
        else:
            versioning = self.versioning

        object_lock: Union[None, dict[str, Any]]
        if isinstance(self.object_lock, S3ObjectLock):
            object_lock = self.object_lock.to_dict()
        else:
            object_lock = self.object_lock

        acl: Union[None, dict[str, Any]]
        if isinstance(self.acl, S3Acl):
            acl = self.acl.to_dict()
        else:
            acl = self.acl

        policy: Union[None, str]
        policy = self.policy

        policy_public: Union[None, bool]
        policy_public = self.policy_public

        public_access_block: Union[None, dict[str, Any]]
        if isinstance(self.public_access_block, S3PublicAccessBlock):
            public_access_block = self.public_access_block.to_dict()
        else:
            public_access_block = self.public_access_block

        lifecycle_rules: Union[None, list[dict[str, Any]]]
        if isinstance(self.lifecycle_rules, list):
            lifecycle_rules = []
            for lifecycle_rules_type_0_item_data in self.lifecycle_rules:
                lifecycle_rules_type_0_item = lifecycle_rules_type_0_item_data.to_dict()
                lifecycle_rules.append(lifecycle_rules_type_0_item)

        else:
            lifecycle_rules = self.lifecycle_rules

        encryption: Union[None, str]
        encryption = self.encryption

        cors_rules: Union[None, list[dict[str, Any]]]
        if isinstance(self.cors_rules, list):
            cors_rules = []
            for cors_rules_type_0_item_data in self.cors_rules:
                cors_rules_type_0_item = cors_rules_type_0_item_data.to_dict()
                cors_rules.append(cors_rules_type_0_item)

        else:
            cors_rules = self.cors_rules

        tags: Union[None, list[dict[str, Any]]]
        if isinstance(self.tags, list):
            tags = []
            for tags_type_0_item_data in self.tags:
                tags_type_0_item = tags_type_0_item_data.to_dict()
                tags.append(tags_type_0_item)

        else:
            tags = self.tags

        public_acl_groups = self.public_acl_groups

        is_public = self.is_public

        unavailable = self.unavailable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bucket": bucket,
                "objects": objects,
                "size_bytes": size_bytes,
                "location": location,
                "versioning": versioning,
                "object_lock": object_lock,
                "acl": acl,
                "policy": policy,
                "policy_public": policy_public,
                "public_access_block": public_access_block,
                "lifecycle_rules": lifecycle_rules,
                "encryption": encryption,
                "cors_rules": cors_rules,
                "tags": tags,
                "public_acl_groups": public_acl_groups,
                "is_public": is_public,
                "unavailable": unavailable,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.s3_acl import S3Acl
        from ..models.s3_cors_rule import S3CorsRule
        from ..models.s3_lifecycle_rule import S3LifecycleRule
        from ..models.s3_object_lock import S3ObjectLock
        from ..models.s3_public_access_block import S3PublicAccessBlock
        from ..models.s3_tag import S3Tag
        from ..models.s3_versioning import S3Versioning

        d = dict(src_dict)
        bucket = d.pop("bucket")

        def _parse_objects(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        objects = _parse_objects(d.pop("objects"))

        def _parse_size_bytes(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        size_bytes = _parse_size_bytes(d.pop("size_bytes"))

        def _parse_location(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        location = _parse_location(d.pop("location"))

        def _parse_versioning(data: object) -> Union["S3Versioning", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                versioning_type_1 = S3Versioning.from_dict(data)

                return versioning_type_1
            except:  # noqa: E722
                pass
            return cast(Union["S3Versioning", None], data)

        versioning = _parse_versioning(d.pop("versioning"))

        def _parse_object_lock(data: object) -> Union["S3ObjectLock", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                object_lock_type_1 = S3ObjectLock.from_dict(data)

                return object_lock_type_1
            except:  # noqa: E722
                pass
            return cast(Union["S3ObjectLock", None], data)

        object_lock = _parse_object_lock(d.pop("object_lock"))

        def _parse_acl(data: object) -> Union["S3Acl", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                acl_type_1 = S3Acl.from_dict(data)

                return acl_type_1
            except:  # noqa: E722
                pass
            return cast(Union["S3Acl", None], data)

        acl = _parse_acl(d.pop("acl"))

        def _parse_policy(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        policy = _parse_policy(d.pop("policy"))

        def _parse_policy_public(data: object) -> Union[None, bool]:
            if data is None:
                return data
            return cast(Union[None, bool], data)

        policy_public = _parse_policy_public(d.pop("policy_public"))

        def _parse_public_access_block(data: object) -> Union["S3PublicAccessBlock", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                public_access_block_type_1 = S3PublicAccessBlock.from_dict(data)

                return public_access_block_type_1
            except:  # noqa: E722
                pass
            return cast(Union["S3PublicAccessBlock", None], data)

        public_access_block = _parse_public_access_block(d.pop("public_access_block"))

        def _parse_lifecycle_rules(data: object) -> Union[None, list["S3LifecycleRule"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                lifecycle_rules_type_0 = []
                _lifecycle_rules_type_0 = data
                for lifecycle_rules_type_0_item_data in _lifecycle_rules_type_0:
                    lifecycle_rules_type_0_item = S3LifecycleRule.from_dict(lifecycle_rules_type_0_item_data)

                    lifecycle_rules_type_0.append(lifecycle_rules_type_0_item)

                return lifecycle_rules_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["S3LifecycleRule"]], data)

        lifecycle_rules = _parse_lifecycle_rules(d.pop("lifecycle_rules"))

        def _parse_encryption(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        encryption = _parse_encryption(d.pop("encryption"))

        def _parse_cors_rules(data: object) -> Union[None, list["S3CorsRule"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cors_rules_type_0 = []
                _cors_rules_type_0 = data
                for cors_rules_type_0_item_data in _cors_rules_type_0:
                    cors_rules_type_0_item = S3CorsRule.from_dict(cors_rules_type_0_item_data)

                    cors_rules_type_0.append(cors_rules_type_0_item)

                return cors_rules_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["S3CorsRule"]], data)

        cors_rules = _parse_cors_rules(d.pop("cors_rules"))

        def _parse_tags(data: object) -> Union[None, list["S3Tag"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = []
                _tags_type_0 = data
                for tags_type_0_item_data in _tags_type_0:
                    tags_type_0_item = S3Tag.from_dict(tags_type_0_item_data)

                    tags_type_0.append(tags_type_0_item)

                return tags_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["S3Tag"]], data)

        tags = _parse_tags(d.pop("tags"))

        public_acl_groups = cast(list[str], d.pop("public_acl_groups"))

        is_public = d.pop("is_public")

        unavailable = cast(list[str], d.pop("unavailable"))

        s3_bucket_details = cls(
            bucket=bucket,
            objects=objects,
            size_bytes=size_bytes,
            location=location,
            versioning=versioning,
            object_lock=object_lock,
            acl=acl,
            policy=policy,
            policy_public=policy_public,
            public_access_block=public_access_block,
            lifecycle_rules=lifecycle_rules,
            encryption=encryption,
            cors_rules=cors_rules,
            tags=tags,
            public_acl_groups=public_acl_groups,
            is_public=is_public,
            unavailable=unavailable,
        )

        s3_bucket_details.additional_properties = d
        return s3_bucket_details

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
