import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define, field
from dateutil.parser import isoparse

T = TypeVar("T", bound="DecodedCertificate")


@define
class DecodedCertificate:
    """
    Attributes:
        id (int):
        version (int):
        serial_number (int):
        issuer_dn (str):
        subject_dn (str):
        not_before (datetime.datetime):
        not_after (datetime.datetime):
    """

    id: int
    version: int
    serial_number: int
    issuer_dn: str
    subject_dn: str
    not_before: datetime.datetime
    not_after: datetime.datetime
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        version = self.version
        serial_number = self.serial_number
        issuer_dn = self.issuer_dn
        subject_dn = self.subject_dn
        not_before = self.not_before.isoformat()

        not_after = self.not_after.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "version": version,
                "serialNumber": serial_number,
                "issuerDN": issuer_dn,
                "subjectDN": subject_dn,
                "notBefore": not_before,
                "notAfter": not_after,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        version = d.pop("version")

        serial_number = d.pop("serialNumber")

        issuer_dn = d.pop("issuerDN")

        subject_dn = d.pop("subjectDN")

        not_before = isoparse(d.pop("notBefore"))

        not_after = isoparse(d.pop("notAfter"))

        decoded_certificate = cls(
            id=id,
            version=version,
            serial_number=serial_number,
            issuer_dn=issuer_dn,
            subject_dn=subject_dn,
            not_before=not_before,
            not_after=not_after,
        )

        decoded_certificate.additional_properties = d
        return decoded_certificate

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
