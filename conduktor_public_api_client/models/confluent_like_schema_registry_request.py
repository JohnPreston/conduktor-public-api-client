from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define, field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.basic_auth import BasicAuth
    from ..models.bearer_token import BearerToken
    from ..models.no_security import NoSecurity
    from ..models.ssl_auth import SSLAuth


T = TypeVar("T", bound="ConfluentLikeSchemaRegistryRequest")


@define
class ConfluentLikeSchemaRegistryRequest:
    """
    Attributes:
        url (str):
        type (str):
        security (Union['BasicAuth', 'BearerToken', 'NoSecurity', 'SSLAuth', Unset]):
        properties (Union[Unset, str]):
        ignore_untrusted_certificate (Union[Unset, bool]):
    """

    url: str
    type: str
    security: Union["BasicAuth", "BearerToken", "NoSecurity", "SSLAuth", Unset] = UNSET
    properties: Union[Unset, str] = UNSET
    ignore_untrusted_certificate: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.basic_auth import BasicAuth
        from ..models.bearer_token import BearerToken
        from ..models.no_security import NoSecurity

        url = self.url
        type = self.type
        security: Union[Dict[str, Any], Unset]
        if isinstance(self.security, Unset):
            security = UNSET

        elif isinstance(self.security, BasicAuth):
            security = self.security.to_dict()

        elif isinstance(self.security, BearerToken):
            security = self.security.to_dict()

        elif isinstance(self.security, NoSecurity):
            security = self.security.to_dict()

        else:
            security = self.security.to_dict()

        properties = self.properties
        ignore_untrusted_certificate = self.ignore_untrusted_certificate

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "type": type,
            }
        )
        if security is not UNSET:
            field_dict["security"] = security
        if properties is not UNSET:
            field_dict["properties"] = properties
        if ignore_untrusted_certificate is not UNSET:
            field_dict["ignoreUntrustedCertificate"] = ignore_untrusted_certificate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.basic_auth import BasicAuth
        from ..models.bearer_token import BearerToken
        from ..models.no_security import NoSecurity
        from ..models.ssl_auth import SSLAuth

        d = src_dict.copy()
        url = d.pop("url")

        type = d.pop("type")

        def _parse_security(
            data: object,
        ) -> Union["BasicAuth", "BearerToken", "NoSecurity", "SSLAuth", Unset]:
            if isinstance(data, Unset):
                return data
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

        security = _parse_security(d.pop("security", UNSET))

        properties = d.pop("properties", UNSET)

        ignore_untrusted_certificate = d.pop("ignoreUntrustedCertificate", UNSET)

        confluent_like_schema_registry_request = cls(
            url=url,
            type=type,
            security=security,
            properties=properties,
            ignore_untrusted_certificate=ignore_untrusted_certificate,
        )

        confluent_like_schema_registry_request.additional_properties = d
        return confluent_like_schema_registry_request

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
