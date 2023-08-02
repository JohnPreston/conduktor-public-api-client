from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define, field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.confluent_like_schema_registry_request import (
        ConfluentLikeSchemaRegistryRequest,
    )
    from ..models.credentials import Credentials
    from ..models.from_context import FromContext
    from ..models.from_role import FromRole
    from ..models.glue_schema_registry_request import GlueSchemaRegistryRequest
    from ..models.iam_anywhere import IAMAnywhere
    from ..models.kafka_connect import KafkaConnect


T = TypeVar("T", bound="UpsertSharedClusterRequest")


@define
class UpsertSharedClusterRequest:
    """
    Attributes:
        name (str):
        bootstrap_servers (str):
        properties (Union[Unset, str]):
        color (Union[Unset, str]):
        icon (Union[Unset, str]):
        schema_registry (Union['ConfluentLikeSchemaRegistryRequest', 'GlueSchemaRegistryRequest', Unset]):
        kafka_connects (Union[Unset, List['KafkaConnect']]):
        ignore_untrusted_certificate (Union[Unset, bool]):
        amazon_security (Union['Credentials', 'FromContext', 'FromRole', 'IAMAnywhere', Unset]):
    """

    name: str
    bootstrap_servers: str
    properties: Union[Unset, str] = UNSET
    color: Union[Unset, str] = UNSET
    icon: Union[Unset, str] = UNSET
    schema_registry: Union[
        "ConfluentLikeSchemaRegistryRequest", "GlueSchemaRegistryRequest", Unset
    ] = UNSET
    kafka_connects: Union[Unset, List["KafkaConnect"]] = UNSET
    ignore_untrusted_certificate: Union[Unset, bool] = UNSET
    amazon_security: Union[
        "Credentials", "FromContext", "FromRole", "IAMAnywhere", Unset
    ] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.confluent_like_schema_registry_request import (
            ConfluentLikeSchemaRegistryRequest,
        )
        from ..models.credentials import Credentials
        from ..models.from_context import FromContext
        from ..models.from_role import FromRole

        name = self.name
        bootstrap_servers = self.bootstrap_servers
        properties = self.properties
        color = self.color
        icon = self.icon
        schema_registry: Union[Dict[str, Any], Unset]
        if isinstance(self.schema_registry, Unset):
            schema_registry = UNSET

        elif isinstance(self.schema_registry, ConfluentLikeSchemaRegistryRequest):
            schema_registry = self.schema_registry.to_dict()

        else:
            schema_registry = self.schema_registry.to_dict()

        kafka_connects: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.kafka_connects, Unset):
            kafka_connects = []
            for kafka_connects_item_data in self.kafka_connects:
                kafka_connects_item = kafka_connects_item_data.to_dict()

                kafka_connects.append(kafka_connects_item)

        ignore_untrusted_certificate = self.ignore_untrusted_certificate
        amazon_security: Union[Dict[str, Any], Unset]
        if isinstance(self.amazon_security, Unset):
            amazon_security = UNSET

        elif isinstance(self.amazon_security, Credentials):
            amazon_security = self.amazon_security.to_dict()

        elif isinstance(self.amazon_security, FromContext):
            amazon_security = self.amazon_security.to_dict()

        elif isinstance(self.amazon_security, FromRole):
            amazon_security = self.amazon_security.to_dict()

        else:
            amazon_security = self.amazon_security.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "bootstrapServers": bootstrap_servers,
            }
        )
        if properties is not UNSET:
            field_dict["properties"] = properties
        if color is not UNSET:
            field_dict["color"] = color
        if icon is not UNSET:
            field_dict["icon"] = icon
        if schema_registry is not UNSET:
            field_dict["schemaRegistry"] = schema_registry
        if kafka_connects is not UNSET:
            field_dict["kafkaConnects"] = kafka_connects
        if ignore_untrusted_certificate is not UNSET:
            field_dict["ignoreUntrustedCertificate"] = ignore_untrusted_certificate
        if amazon_security is not UNSET:
            field_dict["amazonSecurity"] = amazon_security

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.confluent_like_schema_registry_request import (
            ConfluentLikeSchemaRegistryRequest,
        )
        from ..models.credentials import Credentials
        from ..models.from_context import FromContext
        from ..models.from_role import FromRole
        from ..models.glue_schema_registry_request import GlueSchemaRegistryRequest
        from ..models.iam_anywhere import IAMAnywhere
        from ..models.kafka_connect import KafkaConnect

        d = src_dict.copy()
        name = d.pop("name")

        bootstrap_servers = d.pop("bootstrapServers")

        properties = d.pop("properties", UNSET)

        color = d.pop("color", UNSET)

        icon = d.pop("icon", UNSET)

        def _parse_schema_registry(
            data: object,
        ) -> Union[
            "ConfluentLikeSchemaRegistryRequest", "GlueSchemaRegistryRequest", Unset
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_schema_registry_request_type_0 = (
                    ConfluentLikeSchemaRegistryRequest.from_dict(data)
                )

                return componentsschemas_schema_registry_request_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_schema_registry_request_type_1 = (
                GlueSchemaRegistryRequest.from_dict(data)
            )

            return componentsschemas_schema_registry_request_type_1

        schema_registry = _parse_schema_registry(d.pop("schemaRegistry", UNSET))

        kafka_connects = []
        _kafka_connects = d.pop("kafkaConnects", UNSET)
        for kafka_connects_item_data in _kafka_connects or []:
            kafka_connects_item = KafkaConnect.from_dict(kafka_connects_item_data)

            kafka_connects.append(kafka_connects_item)

        ignore_untrusted_certificate = d.pop("ignoreUntrustedCertificate", UNSET)

        def _parse_amazon_security(
            data: object,
        ) -> Union["Credentials", "FromContext", "FromRole", "IAMAnywhere", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_amazon_security_type_0 = Credentials.from_dict(data)

                return componentsschemas_amazon_security_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_amazon_security_type_1 = FromContext.from_dict(data)

                return componentsschemas_amazon_security_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_amazon_security_type_2 = FromRole.from_dict(data)

                return componentsschemas_amazon_security_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_amazon_security_type_3 = IAMAnywhere.from_dict(data)

            return componentsschemas_amazon_security_type_3

        amazon_security = _parse_amazon_security(d.pop("amazonSecurity", UNSET))

        upsert_shared_cluster_request = cls(
            name=name,
            bootstrap_servers=bootstrap_servers,
            properties=properties,
            color=color,
            icon=icon,
            schema_registry=schema_registry,
            kafka_connects=kafka_connects,
            ignore_untrusted_certificate=ignore_untrusted_certificate,
            amazon_security=amazon_security,
        )

        upsert_shared_cluster_request.additional_properties = d
        return upsert_shared_cluster_request

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
