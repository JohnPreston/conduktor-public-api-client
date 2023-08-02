from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define, field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cluster import Cluster
    from ..models.consumer_group import ConsumerGroup
    from ..models.kafka_connect_1 import KafkaConnect1
    from ..models.map_type_list_resource_permissions import (
        MapTypeListResourcePermissions,
    )
    from ..models.platform import Platform
    from ..models.subject import Subject
    from ..models.topic import Topic


T = TypeVar("T", bound="UserPermissions")


@define
class UserPermissions:
    """
    Attributes:
        groups (MapTypeListResourcePermissions):
        user (Union[Unset, List[Union['Cluster', 'ConsumerGroup', 'KafkaConnect1', 'Platform', 'Subject', 'Topic']]]):
    """

    groups: "MapTypeListResourcePermissions"
    user: Union[
        Unset,
        List[
            Union[
                "Cluster",
                "ConsumerGroup",
                "KafkaConnect1",
                "Platform",
                "Subject",
                "Topic",
            ]
        ],
    ] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.cluster import Cluster
        from ..models.consumer_group import ConsumerGroup
        from ..models.kafka_connect_1 import KafkaConnect1
        from ..models.platform import Platform
        from ..models.subject import Subject

        groups = self.groups.to_dict()

        user: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.user, Unset):
            user = []
            for user_item_data in self.user:
                user_item: Dict[str, Any]

                if isinstance(user_item_data, Cluster):
                    user_item = user_item_data.to_dict()

                elif isinstance(user_item_data, ConsumerGroup):
                    user_item = user_item_data.to_dict()

                elif isinstance(user_item_data, KafkaConnect1):
                    user_item = user_item_data.to_dict()

                elif isinstance(user_item_data, Platform):
                    user_item = user_item_data.to_dict()

                elif isinstance(user_item_data, Subject):
                    user_item = user_item_data.to_dict()

                else:
                    user_item = user_item_data.to_dict()

                user.append(user_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "groups": groups,
            }
        )
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cluster import Cluster
        from ..models.consumer_group import ConsumerGroup
        from ..models.kafka_connect_1 import KafkaConnect1
        from ..models.map_type_list_resource_permissions import (
            MapTypeListResourcePermissions,
        )
        from ..models.platform import Platform
        from ..models.subject import Subject
        from ..models.topic import Topic

        d = src_dict.copy()
        groups = MapTypeListResourcePermissions.from_dict(d.pop("groups"))

        user = []
        _user = d.pop("user", UNSET)
        for user_item_data in _user or []:

            def _parse_user_item(
                data: object,
            ) -> Union[
                "Cluster",
                "ConsumerGroup",
                "KafkaConnect1",
                "Platform",
                "Subject",
                "Topic",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_resource_permissions_type_0 = Cluster.from_dict(
                        data
                    )

                    return componentsschemas_resource_permissions_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_resource_permissions_type_1 = (
                        ConsumerGroup.from_dict(data)
                    )

                    return componentsschemas_resource_permissions_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_resource_permissions_type_2 = (
                        KafkaConnect1.from_dict(data)
                    )

                    return componentsschemas_resource_permissions_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_resource_permissions_type_3 = Platform.from_dict(
                        data
                    )

                    return componentsschemas_resource_permissions_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_resource_permissions_type_4 = Subject.from_dict(
                        data
                    )

                    return componentsschemas_resource_permissions_type_4
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_resource_permissions_type_5 = Topic.from_dict(data)

                return componentsschemas_resource_permissions_type_5

            user_item = _parse_user_item(user_item_data)

            user.append(user_item)

        user_permissions = cls(
            groups=groups,
            user=user,
        )

        user_permissions.additional_properties = d
        return user_permissions

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
