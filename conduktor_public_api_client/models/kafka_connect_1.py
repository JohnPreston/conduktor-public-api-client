from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define, field

from ..models.kafka_connect_1_permissions_item import KafkaConnect1PermissionsItem
from ..models.kafka_connect_1_resource_type import KafkaConnect1ResourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="KafkaConnect1")


@define
class KafkaConnect1:
    """
    Attributes:
        cluster_id (str):
        connect_cluster_id (str):
        connector_name_pattern (str):
        resource_type (KafkaConnect1ResourceType):
        permissions (Union[Unset, List[KafkaConnect1PermissionsItem]]):
    """

    cluster_id: str
    connect_cluster_id: str
    connector_name_pattern: str
    resource_type: KafkaConnect1ResourceType
    permissions: Union[Unset, List[KafkaConnect1PermissionsItem]] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cluster_id = self.cluster_id
        connect_cluster_id = self.connect_cluster_id
        connector_name_pattern = self.connector_name_pattern
        resource_type = self.resource_type.value

        permissions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = []
            for permissions_item_data in self.permissions:
                permissions_item = permissions_item_data.value

                permissions.append(permissions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clusterId": cluster_id,
                "connectClusterId": connect_cluster_id,
                "connectorNamePattern": connector_name_pattern,
                "resourceType": resource_type,
            }
        )
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cluster_id = d.pop("clusterId")

        connect_cluster_id = d.pop("connectClusterId")

        connector_name_pattern = d.pop("connectorNamePattern")

        resource_type = KafkaConnect1ResourceType(d.pop("resourceType"))

        permissions = []
        _permissions = d.pop("permissions", UNSET)
        for permissions_item_data in _permissions or []:
            permissions_item = KafkaConnect1PermissionsItem(permissions_item_data)

            permissions.append(permissions_item)

        kafka_connect_1 = cls(
            cluster_id=cluster_id,
            connect_cluster_id=connect_cluster_id,
            connector_name_pattern=connector_name_pattern,
            resource_type=resource_type,
            permissions=permissions,
        )

        kafka_connect_1.additional_properties = d
        return kafka_connect_1

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
