from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define, field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.basic_auth import BasicAuth
    from ..models.bearer_token import BearerToken
    from ..models.no_security import NoSecurity
    from ..models.ssl_auth import SSLAuth


T = TypeVar("T", bound="ConfluentLikeSchemaRegistryResponse")


@define
class ConfluentLikeSchemaRegistryResponse:
    """
    Attributes:
        id (str):
        url (str):
        security (Union['BasicAuth', 'BearerToken', 'NoSecurity', 'SSLAuth']):
        ignore_untrusted_certificate (bool):
        type (str):
        properties (Union[Unset, str]):
    """

    id: str
    url: str
    security: Union["BasicAuth", "BearerToken", "NoSecurity", "SSLAuth"]
    ignore_untrusted_certificate: bool
    type: str
    properties: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.basic_auth import BasicAuth
        from ..models.bearer_token import BearerToken
        from ..models.no_security import NoSecurity

        id = self.id
        url = self.url
        security: Dict[str, Any]

        if isinstance(self.security, BasicAuth):
            security = self.security.to_dict()

        elif isinstance(self.security, BearerToken):
            security = self.security.to_dict()

        elif isinstance(self.security, NoSecurity):
            security = self.security.to_dict()

        else:
            security = self.security.to_dict()

        ignore_untrusted_certificate = self.ignore_untrusted_certificate
        type = self.type
        properties = self.properties

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "security": security,
                "ignoreUntrustedCertificate": ignore_untrusted_certificate,
                "type": type,
            }
        )
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.basic_auth import BasicAuth
        from ..models.bearer_token import BearerToken
        from ..models.no_security import NoSecurity
        from ..models.ssl_auth import SSLAuth

        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        def _parse_security(
            data: object,
        ) -> Union["BasicAuth", "BearerToken", "NoSecurity", "SSLAuth"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_confluent_like_schema_registry_security_type_0 = (
                    BasicAuth.from_dict(data)
                )

                return componentsschemas_confluent_like_schema_registry_security_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_confluent_like_schema_registry_security_type_1 = (
                    BearerToken.from_dict(data)
                )

                return componentsschemas_confluent_like_schema_registry_security_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_confluent_like_schema_registry_security_type_2 = (
                    NoSecurity.from_dict(data)
                )

                return componentsschemas_confluent_like_schema_registry_security_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_confluent_like_schema_registry_security_type_3 = (
                SSLAuth.from_dict(data)
            )

            return componentsschemas_confluent_like_schema_registry_security_type_3

        security = _parse_security(d.pop("security"))

        ignore_untrusted_certificate = d.pop("ignoreUntrustedCertificate")

        type = d.pop("type")

        properties = d.pop("properties", UNSET)

        confluent_like_schema_registry_response = cls(
            id=id,
            url=url,
            security=security,
            ignore_untrusted_certificate=ignore_untrusted_certificate,
            type=type,
            properties=properties,
        )

        confluent_like_schema_registry_response.additional_properties = d
        return confluent_like_schema_registry_response

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
