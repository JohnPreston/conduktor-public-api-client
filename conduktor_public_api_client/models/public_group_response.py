from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define, field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.public_user_of_group import PublicUserOfGroup


T = TypeVar("T", bound="PublicGroupResponse")


@define
class PublicGroupResponse:
    """
    Attributes:
        group_id (str):
        name (str):
        is_admin (bool):
        description (Union[Unset, str]):
        users (Union[Unset, List['PublicUserOfGroup']]):
        external_groups (Union[Unset, List[str]]):
    """

    group_id: str
    name: str
    is_admin: bool
    description: Union[Unset, str] = UNSET
    users: Union[Unset, List["PublicUserOfGroup"]] = UNSET
    external_groups: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        group_id = self.group_id
        name = self.name
        is_admin = self.is_admin
        description = self.description
        users: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()

                users.append(users_item)

        external_groups: Union[Unset, List[str]] = UNSET
        if not isinstance(self.external_groups, Unset):
            external_groups = self.external_groups

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "groupId": group_id,
                "name": name,
                "isAdmin": is_admin,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if users is not UNSET:
            field_dict["users"] = users
        if external_groups is not UNSET:
            field_dict["externalGroups"] = external_groups

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.public_user_of_group import PublicUserOfGroup

        d = src_dict.copy()
        group_id = d.pop("groupId")

        name = d.pop("name")

        is_admin = d.pop("isAdmin")

        description = d.pop("description", UNSET)

        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = PublicUserOfGroup.from_dict(users_item_data)

            users.append(users_item)

        external_groups = cast(List[str], d.pop("externalGroups", UNSET))

        public_group_response = cls(
            group_id=group_id,
            name=name,
            is_admin=is_admin,
            description=description,
            users=users,
            external_groups=external_groups,
        )

        public_group_response.additional_properties = d
        return public_group_response

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
