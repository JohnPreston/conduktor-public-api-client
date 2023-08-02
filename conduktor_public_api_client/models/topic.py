from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define, field

from ..models.topic_permissions_item import TopicPermissionsItem
from ..models.topic_resource_type import TopicResourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Topic")


@define
class Topic:
    """
    Attributes:
        cluster_id (str):
        topic_pattern (str):
        resource_type (TopicResourceType):
        permissions (Union[Unset, List[TopicPermissionsItem]]):
    """

    cluster_id: str
    topic_pattern: str
    resource_type: TopicResourceType
    permissions: Union[Unset, List[TopicPermissionsItem]] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cluster_id = self.cluster_id
        topic_pattern = self.topic_pattern
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
                "topicPattern": topic_pattern,
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

        topic_pattern = d.pop("topicPattern")

        resource_type = TopicResourceType(d.pop("resourceType"))

        permissions = []
        _permissions = d.pop("permissions", UNSET)
        for permissions_item_data in _permissions or []:
            permissions_item = TopicPermissionsItem(permissions_item_data)

            permissions.append(permissions_item)

        topic = cls(
            cluster_id=cluster_id,
            topic_pattern=topic_pattern,
            resource_type=resource_type,
            permissions=permissions,
        )

        topic.additional_properties = d
        return topic

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
