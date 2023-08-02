from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define, field

if TYPE_CHECKING:
    from ..models.cluster import Cluster
    from ..models.consumer_group import ConsumerGroup
    from ..models.kafka_connect_1 import KafkaConnect1
    from ..models.platform import Platform
    from ..models.subject import Subject
    from ..models.topic import Topic


T = TypeVar("T", bound="MapTypeListResourcePermissions")


@define
class MapTypeListResourcePermissions:
    """ """

    additional_properties: Dict[
        str,
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
    ] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.cluster import Cluster
        from ..models.consumer_group import ConsumerGroup
        from ..models.kafka_connect_1 import KafkaConnect1
        from ..models.platform import Platform
        from ..models.subject import Subject

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = []
            for additional_property_item_data in prop:
                additional_property_item: Dict[str, Any]

                if isinstance(additional_property_item_data, Cluster):
                    additional_property_item = additional_property_item_data.to_dict()

                elif isinstance(additional_property_item_data, ConsumerGroup):
                    additional_property_item = additional_property_item_data.to_dict()

                elif isinstance(additional_property_item_data, KafkaConnect1):
                    additional_property_item = additional_property_item_data.to_dict()

                elif isinstance(additional_property_item_data, Platform):
                    additional_property_item = additional_property_item_data.to_dict()

                elif isinstance(additional_property_item_data, Subject):
                    additional_property_item = additional_property_item_data.to_dict()

                else:
                    additional_property_item = additional_property_item_data.to_dict()

                field_dict[prop_name].append(additional_property_item)

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cluster import Cluster
        from ..models.consumer_group import ConsumerGroup
        from ..models.kafka_connect_1 import KafkaConnect1
        from ..models.platform import Platform
        from ..models.subject import Subject
        from ..models.topic import Topic

        d = src_dict.copy()
        map_type_list_resource_permissions = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = []
            _additional_property = prop_dict
            for additional_property_item_data in _additional_property:

                def _parse_additional_property_item(
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
                        componentsschemas_resource_permissions_type_0 = (
                            Cluster.from_dict(data)
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
                        componentsschemas_resource_permissions_type_3 = (
                            Platform.from_dict(data)
                        )

                        return componentsschemas_resource_permissions_type_3
                    except:  # noqa: E722
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_resource_permissions_type_4 = (
                            Subject.from_dict(data)
                        )

                        return componentsschemas_resource_permissions_type_4
                    except:  # noqa: E722
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_resource_permissions_type_5 = Topic.from_dict(
                        data
                    )

                    return componentsschemas_resource_permissions_type_5

                additional_property_item = _parse_additional_property_item(
                    additional_property_item_data
                )

                additional_property.append(additional_property_item)

            additional_properties[prop_name] = additional_property

        map_type_list_resource_permissions.additional_properties = additional_properties
        return map_type_list_resource_permissions

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> List[
        Union[
            "Cluster", "ConsumerGroup", "KafkaConnect1", "Platform", "Subject", "Topic"
        ]
    ]:
        return self.additional_properties[key]

    def __setitem__(
        self,
        key: str,
        value: List[
            Union[
                "Cluster",
                "ConsumerGroup",
                "KafkaConnect1",
                "Platform",
                "Subject",
                "Topic",
            ]
        ],
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
