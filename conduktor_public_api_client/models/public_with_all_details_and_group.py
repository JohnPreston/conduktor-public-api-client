from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define, field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.public_group_of_user import PublicGroupOfUser


T = TypeVar("T", bound="PublicWithAllDetailsAndGroup")


@define
class PublicWithAllDetailsAndGroup:
    """
    Attributes:
        user_id (str):
        full_name (str):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        picture_url (Union[Unset, str]):
        phone_number (Union[Unset, str]):
        country (Union[Unset, str]):
        platform_role (Union[Unset, str]):
        groups (Union[Unset, List['PublicGroupOfUser']]):
    """

    user_id: str
    full_name: str
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    picture_url: Union[Unset, str] = UNSET
    phone_number: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    platform_role: Union[Unset, str] = UNSET
    groups: Union[Unset, List["PublicGroupOfUser"]] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id
        full_name = self.full_name
        first_name = self.first_name
        last_name = self.last_name
        picture_url = self.picture_url
        phone_number = self.phone_number
        country = self.country
        platform_role = self.platform_role
        groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()

                groups.append(groups_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
                "fullName": full_name,
            }
        )
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if picture_url is not UNSET:
            field_dict["pictureUrl"] = picture_url
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if country is not UNSET:
            field_dict["country"] = country
        if platform_role is not UNSET:
            field_dict["platformRole"] = platform_role
        if groups is not UNSET:
            field_dict["groups"] = groups

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.public_group_of_user import PublicGroupOfUser

        d = src_dict.copy()
        user_id = d.pop("userId")

        full_name = d.pop("fullName")

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        picture_url = d.pop("pictureUrl", UNSET)

        phone_number = d.pop("phoneNumber", UNSET)

        country = d.pop("country", UNSET)

        platform_role = d.pop("platformRole", UNSET)

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = PublicGroupOfUser.from_dict(groups_item_data)

            groups.append(groups_item)

        public_with_all_details_and_group = cls(
            user_id=user_id,
            full_name=full_name,
            first_name=first_name,
            last_name=last_name,
            picture_url=picture_url,
            phone_number=phone_number,
            country=country,
            platform_role=platform_role,
            groups=groups,
        )

        public_with_all_details_and_group.additional_properties = d
        return public_with_all_details_and_group

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
