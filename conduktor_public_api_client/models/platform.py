from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define, field

from ..models.platform_permissions_item import PlatformPermissionsItem
from ..models.platform_resource_type import PlatformResourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Platform")


@define
class Platform:
    """
    Attributes:
        resource_type (PlatformResourceType):
        permissions (Union[Unset, List[PlatformPermissionsItem]]):
    """

    resource_type: PlatformResourceType
    permissions: Union[Unset, List[PlatformPermissionsItem]] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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
                "resourceType": resource_type,
            }
        )
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        resource_type = PlatformResourceType(d.pop("resourceType"))

        permissions = []
        _permissions = d.pop("permissions", UNSET)
        for permissions_item_data in _permissions or []:
            permissions_item = PlatformPermissionsItem(permissions_item_data)

            permissions.append(permissions_item)

        platform = cls(
            resource_type=resource_type,
            permissions=permissions,
        )

        platform.additional_properties = d
        return platform

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
