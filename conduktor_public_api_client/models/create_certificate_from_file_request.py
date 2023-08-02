from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define, field

from ..types import UNSET, File, Unset

T = TypeVar("T", bound="CreateCertificateFromFileRequest")


@define
class CreateCertificateFromFileRequest:
    """
    Attributes:
        file (File):
        jks_password (Union[Unset, str]):
    """

    file: File
    jks_password: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        file = self.file.to_tuple()

        jks_password = self.jks_password

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
            }
        )
        if jks_password is not UNSET:
            field_dict["jksPassword"] = jks_password

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        file = self.file.to_tuple()

        jks_password = (
            self.jks_password
            if isinstance(self.jks_password, Unset)
            else (None, str(self.jks_password).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                key: (None, str(value).encode(), "text/plain")
                for key, value in self.additional_properties.items()
            }
        )
        field_dict.update(
            {
                "file": file,
            }
        )
        if jks_password is not UNSET:
            field_dict["jksPassword"] = jks_password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        file = File(payload=BytesIO(d.pop("file")))

        jks_password = d.pop("jksPassword", UNSET)

        create_certificate_from_file_request = cls(
            file=file,
            jks_password=jks_password,
        )

        create_certificate_from_file_request.additional_properties = d
        return create_certificate_from_file_request

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
