from typing import Any, Dict, List, Type, TypeVar

from attrs import define, field

T = TypeVar("T", bound="SSLAuth")


@define
class SSLAuth:
    """
    Attributes:
        key (str):
        certificate_chain (str):
        type (str):
    """

    key: str
    certificate_chain: str
    type: str
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key
        certificate_chain = self.certificate_chain
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "certificateChain": certificate_chain,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key = d.pop("key")

        certificate_chain = d.pop("certificateChain")

        type = d.pop("type")

        ssl_auth = cls(
            key=key,
            certificate_chain=certificate_chain,
            type=type,
        )

        ssl_auth.additional_properties = d
        return ssl_auth

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
