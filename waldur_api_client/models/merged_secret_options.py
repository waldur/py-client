from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ip_mapping import IPMapping


T = TypeVar("T", bound="MergedSecretOptions")


@_attrs_define
class MergedSecretOptions:
    """
    Attributes:
        heappe_cluster_password (Union[Unset, str]): HEAppE cluster password
        heappe_password (Union[Unset, str]): HEAppE password
        ipv4_external_ip_mapping (Union[Unset, list['IPMapping']]): OpenStack IPv4 external IP mapping
        openstack_api_tls_certificate (Union[Unset, str]):
        shared_user_password (Union[Unset, str]): GLAuth shared user password
        template_confirmation_comment (Union[Unset, str]): Template confirmation comment
        language (Union[Unset, str]): Script language: Python or Bash
        environ (Union[Unset, Any]): Script environment variables
        create (Union[Unset, str]): Script for resource creation
        terminate (Union[Unset, str]): Script for resource termination
        update (Union[Unset, str]): Script for resource update
        pull (Union[Unset, str]): Script for regular resource pull
        api_url (Union[Unset, str]): API URL
        token (Union[Unset, str]): Waldur access token
        customer_uuid (Union[Unset, str]): Organization UUID
        backend_url (Union[Unset, str]):
        username (Union[Unset, str]):
        password (Union[Unset, str]):
        cloud_init_template (Union[Unset, str]):
    """

    heappe_cluster_password: Union[Unset, str] = UNSET
    heappe_password: Union[Unset, str] = UNSET
    ipv4_external_ip_mapping: Union[Unset, list["IPMapping"]] = UNSET
    openstack_api_tls_certificate: Union[Unset, str] = UNSET
    shared_user_password: Union[Unset, str] = UNSET
    template_confirmation_comment: Union[Unset, str] = UNSET
    language: Union[Unset, str] = UNSET
    environ: Union[Unset, Any] = UNSET
    create: Union[Unset, str] = UNSET
    terminate: Union[Unset, str] = UNSET
    update: Union[Unset, str] = UNSET
    pull: Union[Unset, str] = UNSET
    api_url: Union[Unset, str] = UNSET
    token: Union[Unset, str] = UNSET
    customer_uuid: Union[Unset, str] = UNSET
    backend_url: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    cloud_init_template: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        heappe_cluster_password = self.heappe_cluster_password

        heappe_password = self.heappe_password

        ipv4_external_ip_mapping: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ipv4_external_ip_mapping, Unset):
            ipv4_external_ip_mapping = []
            for ipv4_external_ip_mapping_item_data in self.ipv4_external_ip_mapping:
                ipv4_external_ip_mapping_item = ipv4_external_ip_mapping_item_data.to_dict()
                ipv4_external_ip_mapping.append(ipv4_external_ip_mapping_item)

        openstack_api_tls_certificate = self.openstack_api_tls_certificate

        shared_user_password = self.shared_user_password

        template_confirmation_comment = self.template_confirmation_comment

        language = self.language

        environ = self.environ

        create = self.create

        terminate = self.terminate

        update = self.update

        pull = self.pull

        api_url = self.api_url

        token = self.token

        customer_uuid = self.customer_uuid

        backend_url = self.backend_url

        username = self.username

        password = self.password

        cloud_init_template = self.cloud_init_template

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if heappe_cluster_password is not UNSET:
            field_dict["heappe_cluster_password"] = heappe_cluster_password
        if heappe_password is not UNSET:
            field_dict["heappe_password"] = heappe_password
        if ipv4_external_ip_mapping is not UNSET:
            field_dict["ipv4_external_ip_mapping"] = ipv4_external_ip_mapping
        if openstack_api_tls_certificate is not UNSET:
            field_dict["openstack_api_tls_certificate"] = openstack_api_tls_certificate
        if shared_user_password is not UNSET:
            field_dict["shared_user_password"] = shared_user_password
        if template_confirmation_comment is not UNSET:
            field_dict["template_confirmation_comment"] = template_confirmation_comment
        if language is not UNSET:
            field_dict["language"] = language
        if environ is not UNSET:
            field_dict["environ"] = environ
        if create is not UNSET:
            field_dict["create"] = create
        if terminate is not UNSET:
            field_dict["terminate"] = terminate
        if update is not UNSET:
            field_dict["update"] = update
        if pull is not UNSET:
            field_dict["pull"] = pull
        if api_url is not UNSET:
            field_dict["api_url"] = api_url
        if token is not UNSET:
            field_dict["token"] = token
        if customer_uuid is not UNSET:
            field_dict["customer_uuid"] = customer_uuid
        if backend_url is not UNSET:
            field_dict["backend_url"] = backend_url
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if cloud_init_template is not UNSET:
            field_dict["cloud_init_template"] = cloud_init_template

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ip_mapping import IPMapping

        d = dict(src_dict)
        heappe_cluster_password = d.pop("heappe_cluster_password", UNSET)

        heappe_password = d.pop("heappe_password", UNSET)

        ipv4_external_ip_mapping = []
        _ipv4_external_ip_mapping = d.pop("ipv4_external_ip_mapping", UNSET)
        for ipv4_external_ip_mapping_item_data in _ipv4_external_ip_mapping or []:
            ipv4_external_ip_mapping_item = IPMapping.from_dict(ipv4_external_ip_mapping_item_data)

            ipv4_external_ip_mapping.append(ipv4_external_ip_mapping_item)

        openstack_api_tls_certificate = d.pop("openstack_api_tls_certificate", UNSET)

        shared_user_password = d.pop("shared_user_password", UNSET)

        template_confirmation_comment = d.pop("template_confirmation_comment", UNSET)

        language = d.pop("language", UNSET)

        environ = d.pop("environ", UNSET)

        create = d.pop("create", UNSET)

        terminate = d.pop("terminate", UNSET)

        update = d.pop("update", UNSET)

        pull = d.pop("pull", UNSET)

        api_url = d.pop("api_url", UNSET)

        token = d.pop("token", UNSET)

        customer_uuid = d.pop("customer_uuid", UNSET)

        backend_url = d.pop("backend_url", UNSET)

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        cloud_init_template = d.pop("cloud_init_template", UNSET)

        merged_secret_options = cls(
            heappe_cluster_password=heappe_cluster_password,
            heappe_password=heappe_password,
            ipv4_external_ip_mapping=ipv4_external_ip_mapping,
            openstack_api_tls_certificate=openstack_api_tls_certificate,
            shared_user_password=shared_user_password,
            template_confirmation_comment=template_confirmation_comment,
            language=language,
            environ=environ,
            create=create,
            terminate=terminate,
            update=update,
            pull=pull,
            api_url=api_url,
            token=token,
            customer_uuid=customer_uuid,
            backend_url=backend_url,
            username=username,
            password=password,
            cloud_init_template=cloud_init_template,
        )

        merged_secret_options.additional_properties = d
        return merged_secret_options

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
