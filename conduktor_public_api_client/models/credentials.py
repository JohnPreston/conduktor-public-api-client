from typing import Any, Dict, List, Type, TypeVar

from attrs import define, field

T = TypeVar("T", bound="Credentials")


@define
class Credentials:
    """
    Attributes:
        access_key_id (str):
        secret_key (str):
        type (str):
    """

    access_key_id: str
    secret_key: str
    type: str
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access_key_id = self.access_key_id
        secret_key = self.secret_key
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accessKeyId": access_key_id,
                "secretKey": secret_key,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        access_key_id = d.pop("accessKeyId")

        secret_key = d.pop("secretKey")

        type = d.pop("type")

        credentials = cls(
            access_key_id=access_key_id,
            secret_key=secret_key,
            type=type,
        )

        credentials.additional_properties = d
        return credentials

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
