from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define, field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateGroupRequest")


@define
class UpdateGroupRequest:
    """
    Attributes:
        name (str):
        description (Union[Unset, str]):
        external_groups (Union[Unset, List[str]]):
    """

    name: str
    description: Union[Unset, str] = UNSET
    external_groups: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        description = self.description
        external_groups: Union[Unset, List[str]] = UNSET
        if not isinstance(self.external_groups, Unset):
            external_groups = self.external_groups

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if external_groups is not UNSET:
            field_dict["externalGroups"] = external_groups

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        description = d.pop("description", UNSET)

        external_groups = cast(List[str], d.pop("externalGroups", UNSET))

        update_group_request = cls(
            name=name,
            description=description,
            external_groups=external_groups,
        )

        update_group_request.additional_properties = d
        return update_group_request

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
