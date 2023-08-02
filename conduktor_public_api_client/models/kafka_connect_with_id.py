from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define, field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.kafka_connect_basic_auth import KafkaConnectBasicAuth
    from ..models.kafka_connect_bearer_token import KafkaConnectBearerToken
    from ..models.kafka_connect_no_security import KafkaConnectNoSecurity
    from ..models.kafka_connect_ssl_auth import KafkaConnectSSLAuth


T = TypeVar("T", bound="KafkaConnectWithId")


@define
class KafkaConnectWithId:
    """
    Attributes:
        id (str):
        slug (str):
        url (str):
        name (str):
        security (Union['KafkaConnectBasicAuth', 'KafkaConnectBearerToken', 'KafkaConnectNoSecurity',
            'KafkaConnectSSLAuth']):
        ignore_untrusted_certificate (bool):
        headers (Union[Unset, str]):
    """

    id: str
    slug: str
    url: str
    name: str
    security: Union[
        "KafkaConnectBasicAuth",
        "KafkaConnectBearerToken",
        "KafkaConnectNoSecurity",
        "KafkaConnectSSLAuth",
    ]
    ignore_untrusted_certificate: bool
    headers: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.kafka_connect_basic_auth import KafkaConnectBasicAuth
        from ..models.kafka_connect_bearer_token import KafkaConnectBearerToken
        from ..models.kafka_connect_no_security import KafkaConnectNoSecurity

        id = self.id
        slug = self.slug
        url = self.url
        name = self.name
        security: Dict[str, Any]

        if isinstance(self.security, KafkaConnectBasicAuth):
            security = self.security.to_dict()

        elif isinstance(self.security, KafkaConnectBearerToken):
            security = self.security.to_dict()

        elif isinstance(self.security, KafkaConnectNoSecurity):
            security = self.security.to_dict()

        else:
            security = self.security.to_dict()

        ignore_untrusted_certificate = self.ignore_untrusted_certificate
        headers = self.headers

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "slug": slug,
                "url": url,
                "name": name,
                "security": security,
                "ignoreUntrustedCertificate": ignore_untrusted_certificate,
            }
        )
        if headers is not UNSET:
            field_dict["headers"] = headers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.kafka_connect_basic_auth import KafkaConnectBasicAuth
        from ..models.kafka_connect_bearer_token import KafkaConnectBearerToken
        from ..models.kafka_connect_no_security import KafkaConnectNoSecurity
        from ..models.kafka_connect_ssl_auth import KafkaConnectSSLAuth

        d = src_dict.copy()
        id = d.pop("id")

        slug = d.pop("slug")

        url = d.pop("url")

        name = d.pop("name")

        def _parse_security(
            data: object,
        ) -> Union[
            "KafkaConnectBasicAuth",
            "KafkaConnectBearerToken",
            "KafkaConnectNoSecurity",
            "KafkaConnectSSLAuth",
        ]:
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

        security = _parse_security(d.pop("security"))

        ignore_untrusted_certificate = d.pop("ignoreUntrustedCertificate")

        headers = d.pop("headers", UNSET)

        kafka_connect_with_id = cls(
            id=id,
            slug=slug,
            url=url,
            name=name,
            security=security,
            ignore_untrusted_certificate=ignore_untrusted_certificate,
            headers=headers,
        )

        kafka_connect_with_id.additional_properties = d
        return kafka_connect_with_id

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
