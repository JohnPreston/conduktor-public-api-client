from typing import Any, Dict, List, Type, TypeVar

from attrs import define, field

T = TypeVar("T", bound="IAMAnywhere")


@define
class IAMAnywhere:
    """
    Attributes:
        trust_anchor_arn (str):
        profile_arn (str):
        role_arn (str):
        certificate (str):
        private_key (str):
        type (str):
    """

    trust_anchor_arn: str
    profile_arn: str
    role_arn: str
    certificate: str
    private_key: str
    type: str
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        trust_anchor_arn = self.trust_anchor_arn
        profile_arn = self.profile_arn
        role_arn = self.role_arn
        certificate = self.certificate
        private_key = self.private_key
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "trustAnchorArn": trust_anchor_arn,
                "profileArn": profile_arn,
                "roleArn": role_arn,
                "certificate": certificate,
                "privateKey": private_key,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        trust_anchor_arn = d.pop("trustAnchorArn")

        profile_arn = d.pop("profileArn")

        role_arn = d.pop("roleArn")

        certificate = d.pop("certificate")

        private_key = d.pop("privateKey")

        type = d.pop("type")

        iam_anywhere = cls(
            trust_anchor_arn=trust_anchor_arn,
            profile_arn=profile_arn,
            role_arn=role_arn,
            certificate=certificate,
            private_key=private_key,
            type=type,
        )

        iam_anywhere.additional_properties = d
        return iam_anywhere

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
