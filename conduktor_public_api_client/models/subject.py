from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define, field

from ..models.subject_permissions_item import SubjectPermissionsItem
from ..models.subject_resource_type import SubjectResourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Subject")


@define
class Subject:
    """
    Attributes:
        cluster_id (str):
        subject_pattern (str):
        resource_type (SubjectResourceType):
        permissions (Union[Unset, List[SubjectPermissionsItem]]):
    """

    cluster_id: str
    subject_pattern: str
    resource_type: SubjectResourceType
    permissions: Union[Unset, List[SubjectPermissionsItem]] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cluster_id = self.cluster_id
        subject_pattern = self.subject_pattern
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
                "subjectPattern": subject_pattern,
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

        subject_pattern = d.pop("subjectPattern")

        resource_type = SubjectResourceType(d.pop("resourceType"))

        permissions = []
        _permissions = d.pop("permissions", UNSET)
        for permissions_item_data in _permissions or []:
            permissions_item = SubjectPermissionsItem(permissions_item_data)

            permissions.append(permissions_item)

        subject = cls(
            cluster_id=cluster_id,
            subject_pattern=subject_pattern,
            resource_type=resource_type,
            permissions=permissions,
        )

        subject.additional_properties = d
        return subject

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
