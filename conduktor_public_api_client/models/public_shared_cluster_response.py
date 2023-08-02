import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define, field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.confluent_like_schema_registry_response import (
        ConfluentLikeSchemaRegistryResponse,
    )
    from ..models.credentials import Credentials
    from ..models.from_context import FromContext
    from ..models.from_role import FromRole
    from ..models.glue_schema_registry_response import GlueSchemaRegistryResponse
    from ..models.iam_anywhere import IAMAnywhere
    from ..models.kafka_connect_with_id import KafkaConnectWithId


T = TypeVar("T", bound="PublicSharedClusterResponse")


@define
class PublicSharedClusterResponse:
    """
    Attributes:
        technical_id (str):
        name (str):
        bootstrap_servers (str):
        ignore_untrusted_certificate (bool):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        zookeeper_server (Union[Unset, str]):
        properties (Union[Unset, str]):
        color (Union[Unset, str]):
        icon (Union[Unset, str]):
        schema_registry (Union['ConfluentLikeSchemaRegistryResponse', 'GlueSchemaRegistryResponse', Unset]):
        kafka_connects (Union[Unset, List['KafkaConnectWithId']]):
        server_ca (Union[Unset, str]):
        access_cert (Union[Unset, str]):
        access_key (Union[Unset, str]):
        amazon_security (Union['Credentials', 'FromContext', 'FromRole', 'IAMAnywhere', Unset]):
    """

    technical_id: str
    name: str
    bootstrap_servers: str
    ignore_untrusted_certificate: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    zookeeper_server: Union[Unset, str] = UNSET
    properties: Union[Unset, str] = UNSET
    color: Union[Unset, str] = UNSET
    icon: Union[Unset, str] = UNSET
    schema_registry: Union[
        "ConfluentLikeSchemaRegistryResponse", "GlueSchemaRegistryResponse", Unset
    ] = UNSET
    kafka_connects: Union[Unset, List["KafkaConnectWithId"]] = UNSET
    server_ca: Union[Unset, str] = UNSET
    access_cert: Union[Unset, str] = UNSET
    access_key: Union[Unset, str] = UNSET
    amazon_security: Union[
        "Credentials", "FromContext", "FromRole", "IAMAnywhere", Unset
    ] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.confluent_like_schema_registry_response import (
            ConfluentLikeSchemaRegistryResponse,
        )
        from ..models.credentials import Credentials
        from ..models.from_context import FromContext
        from ..models.from_role import FromRole

        technical_id = self.technical_id
        name = self.name
        bootstrap_servers = self.bootstrap_servers
        ignore_untrusted_certificate = self.ignore_untrusted_certificate
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        zookeeper_server = self.zookeeper_server
        properties = self.properties
        color = self.color
        icon = self.icon
        schema_registry: Union[Dict[str, Any], Unset]
        if isinstance(self.schema_registry, Unset):
            schema_registry = UNSET

        elif isinstance(self.schema_registry, ConfluentLikeSchemaRegistryResponse):
            schema_registry = self.schema_registry.to_dict()

        else:
            schema_registry = self.schema_registry.to_dict()

        kafka_connects: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.kafka_connects, Unset):
            kafka_connects = []
            for kafka_connects_item_data in self.kafka_connects:
                kafka_connects_item = kafka_connects_item_data.to_dict()

                kafka_connects.append(kafka_connects_item)

        server_ca = self.server_ca
        access_cert = self.access_cert
        access_key = self.access_key
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
                "technicalId": technical_id,
                "name": name,
                "bootstrapServers": bootstrap_servers,
                "ignoreUntrustedCertificate": ignore_untrusted_certificate,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if zookeeper_server is not UNSET:
            field_dict["zookeeperServer"] = zookeeper_server
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
        if server_ca is not UNSET:
            field_dict["serverCa"] = server_ca
        if access_cert is not UNSET:
            field_dict["accessCert"] = access_cert
        if access_key is not UNSET:
            field_dict["accessKey"] = access_key
        if amazon_security is not UNSET:
            field_dict["amazonSecurity"] = amazon_security

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.confluent_like_schema_registry_response import (
            ConfluentLikeSchemaRegistryResponse,
        )
        from ..models.credentials import Credentials
        from ..models.from_context import FromContext
        from ..models.from_role import FromRole
        from ..models.glue_schema_registry_response import GlueSchemaRegistryResponse
        from ..models.iam_anywhere import IAMAnywhere
        from ..models.kafka_connect_with_id import KafkaConnectWithId

        d = src_dict.copy()
        technical_id = d.pop("technicalId")

        name = d.pop("name")

        bootstrap_servers = d.pop("bootstrapServers")

        ignore_untrusted_certificate = d.pop("ignoreUntrustedCertificate")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        zookeeper_server = d.pop("zookeeperServer", UNSET)

        properties = d.pop("properties", UNSET)

        color = d.pop("color", UNSET)

        icon = d.pop("icon", UNSET)

        def _parse_schema_registry(
            data: object,
        ) -> Union[
            "ConfluentLikeSchemaRegistryResponse", "GlueSchemaRegistryResponse", Unset
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_schema_registry_with_id_type_0 = (
                    ConfluentLikeSchemaRegistryResponse.from_dict(data)
                )

                return componentsschemas_schema_registry_with_id_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_schema_registry_with_id_type_1 = (
                GlueSchemaRegistryResponse.from_dict(data)
            )

            return componentsschemas_schema_registry_with_id_type_1

        try:
            schema_registry = _parse_schema_registry(d.pop("schemaRegistry", UNSET))
        except TypeError:
            schema_registry = {}

        kafka_connects = []
        _kafka_connects = d.pop("kafkaConnects", UNSET)
        for kafka_connects_item_data in _kafka_connects or []:
            kafka_connects_item = KafkaConnectWithId.from_dict(kafka_connects_item_data)

            kafka_connects.append(kafka_connects_item)

        server_ca = d.pop("serverCa", UNSET)

        access_cert = d.pop("accessCert", UNSET)

        access_key = d.pop("accessKey", UNSET)

        def _parse_amazon_security(
            data: object,
        ) -> Union["Credentials", "FromContext", "FromRole", "IAMAnywhere", Unset]:
            if not data or data is None:
                return Unset
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

        public_shared_cluster_response = cls(
            technical_id=technical_id,
            name=name,
            bootstrap_servers=bootstrap_servers,
            ignore_untrusted_certificate=ignore_untrusted_certificate,
            created_at=created_at,
            updated_at=updated_at,
            zookeeper_server=zookeeper_server,
            properties=properties,
            color=color,
            icon=icon,
            schema_registry=schema_registry,
            kafka_connects=kafka_connects,
            server_ca=server_ca,
            access_cert=access_cert,
            access_key=access_key,
            amazon_security=amazon_security,
        )

        public_shared_cluster_response.additional_properties = d
        return public_shared_cluster_response

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
