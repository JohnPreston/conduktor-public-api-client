from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define, field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.kafka_connect_basic_auth import KafkaConnectBasicAuth
    from ..models.kafka_connect_bearer_token import KafkaConnectBearerToken
    from ..models.kafka_connect_no_security import KafkaConnectNoSecurity
    from ..models.kafka_connect_ssl_auth import KafkaConnectSSLAuth


T = TypeVar("T", bound="KafkaConnect")


@define
class KafkaConnect:
    """
    Attributes:
        url (str):
        name (str):
        slug (Union[Unset, str]):
        security (Union['KafkaConnectBasicAuth', 'KafkaConnectBearerToken', 'KafkaConnectNoSecurity',
            'KafkaConnectSSLAuth', Unset]):
        headers (Union[Unset, str]):
        ignore_untrusted_certificate (Union[Unset, bool]):
    """

    url: str
    name: str
    slug: Union[Unset, str] = UNSET
    security: Union[
        "KafkaConnectBasicAuth",
        "KafkaConnectBearerToken",
        "KafkaConnectNoSecurity",
        "KafkaConnectSSLAuth",
        Unset,
    ] = UNSET
    headers: Union[Unset, str] = UNSET
    ignore_untrusted_certificate: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.kafka_connect_basic_auth import KafkaConnectBasicAuth
        from ..models.kafka_connect_bearer_token import KafkaConnectBearerToken
        from ..models.kafka_connect_no_security import KafkaConnectNoSecurity

        url = self.url
        name = self.name
        slug = self.slug
        security: Union[Dict[str, Any], Unset]
        if isinstance(self.security, Unset):
            security = UNSET

        elif isinstance(self.security, KafkaConnectBasicAuth):
            security = self.security.to_dict()

        elif isinstance(self.security, KafkaConnectBearerToken):
            security = self.security.to_dict()

        elif isinstance(self.security, KafkaConnectNoSecurity):
            security = self.security.to_dict()

        else:
            security = self.security.to_dict()

        headers = self.headers
        ignore_untrusted_certificate = self.ignore_untrusted_certificate

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "name": name,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if security is not UNSET:
            field_dict["security"] = security
        if headers is not UNSET:
            field_dict["headers"] = headers
        if ignore_untrusted_certificate is not UNSET:
            field_dict["ignoreUntrustedCertificate"] = ignore_untrusted_certificate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.kafka_connect_basic_auth import KafkaConnectBasicAuth
        from ..models.kafka_connect_bearer_token import KafkaConnectBearerToken
        from ..models.kafka_connect_no_security import KafkaConnectNoSecurity
        from ..models.kafka_connect_ssl_auth import KafkaConnectSSLAuth

        d = src_dict.copy()
        url = d.pop("url")

        name = d.pop("name")

        slug = d.pop("slug", UNSET)

        def _parse_security(
            data: object,
        ) -> Union[
            "KafkaConnectBasicAuth",
            "KafkaConnectBearerToken",
            "KafkaConnectNoSecurity",
            "KafkaConnectSSLAuth",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_kafka_connect_security_type_0 = (
                    KafkaConnectBasicAuth.from_dict(data)
                )

                return componentsschemas_kafka_connect_security_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_kafka_connect_security_type_1 = (
                    KafkaConnectBearerToken.from_dict(data)
                )

                return componentsschemas_kafka_connect_security_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_kafka_connect_security_type_2 = (
                    KafkaConnectNoSecurity.from_dict(data)
                )

                return componentsschemas_kafka_connect_security_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_kafka_connect_security_type_3 = (
                KafkaConnectSSLAuth.from_dict(data)
            )

            return componentsschemas_kafka_connect_security_type_3

        security = _parse_security(d.pop("security", UNSET))

        headers = d.pop("headers", UNSET)

        ignore_untrusted_certificate = d.pop("ignoreUntrustedCertificate", UNSET)

        kafka_connect = cls(
            url=url,
            name=name,
            slug=slug,
            security=security,
            headers=headers,
            ignore_untrusted_certificate=ignore_untrusted_certificate,
        )

        kafka_connect.additional_properties = d
        return kafka_connect

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
