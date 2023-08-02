from typing import Any, Dict, List, Type, TypeVar

from attrs import define, field

T = TypeVar("T", bound="PublicUserOfGroup")


@define
class PublicUserOfGroup:
    """
    Attributes:
        email (str):
        external_mapping (bool):
    """

    email: str
    external_mapping: bool
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email
        external_mapping = self.external_mapping

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "externalMapping": external_mapping,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email")

        external_mapping = d.pop("externalMapping")

        public_user_of_group = cls(
            email=email,
            external_mapping=external_mapping,
        )

        public_user_of_group.additional_properties = d
        return public_user_of_group

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
