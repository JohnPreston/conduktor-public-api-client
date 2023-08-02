from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define, field

from ..models.cluster_permissions_item import ClusterPermissionsItem
from ..models.cluster_resource_type import ClusterResourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Cluster")


@define
class Cluster:
    """
    Attributes:
        cluster_id (str):
        resource_type (ClusterResourceType):
        permissions (Union[Unset, List[ClusterPermissionsItem]]):
    """

    cluster_id: str
    resource_type: ClusterResourceType
    permissions: Union[Unset, List[ClusterPermissionsItem]] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cluster_id = self.cluster_id
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

        resource_type = ClusterResourceType(d.pop("resourceType"))

        permissions = []
        _permissions = d.pop("permissions", UNSET)
        for permissions_item_data in _permissions or []:
            permissions_item = ClusterPermissionsItem(permissions_item_data)

            permissions.append(permissions_item)

        cluster = cls(
            cluster_id=cluster_id,
            resource_type=resource_type,
            permissions=permissions,
        )

        cluster.additional_properties = d
        return cluster

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
