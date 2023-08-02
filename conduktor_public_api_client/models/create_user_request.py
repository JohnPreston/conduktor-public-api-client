from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define, field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateUserRequest")


@define
class CreateUserRequest:
    """
    Attributes:
        email (str):
        last_name (Union[Unset, str]):
        first_name (Union[Unset, str]):
    """

    email: str
    last_name: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email
        last_name = self.last_name
        first_name = self.first_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
            }
        )
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if first_name is not UNSET:
            field_dict["firstName"] = first_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email")

        last_name = d.pop("lastName", UNSET)

        first_name = d.pop("firstName", UNSET)

        create_user_request = cls(
            email=email,
            last_name=last_name,
            first_name=first_name,
        )

        create_user_request.additional_properties = d
        return create_user_request

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
