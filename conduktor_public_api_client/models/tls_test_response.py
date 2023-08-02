from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define, field

if TYPE_CHECKING:
    from ..models.checked_certificate import CheckedCertificate
    from ..models.tls_not_supported import TlsNotSupported
    from ..models.unchecked_certificate import UncheckedCertificate
    from ..models.unexpected_status import UnexpectedStatus
    from ..models.unreachable_target import UnreachableTarget


T = TypeVar("T", bound="TlsTestResponse")


@define
class TlsTestResponse:
    """
    Attributes:
        status (Union['CheckedCertificate', 'TlsNotSupported', 'UncheckedCertificate', 'UnexpectedStatus',
            'UnreachableTarget']):
    """

    status: Union[
        "CheckedCertificate",
        "TlsNotSupported",
        "UncheckedCertificate",
        "UnexpectedStatus",
        "UnreachableTarget",
    ]
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.checked_certificate import CheckedCertificate
        from ..models.tls_not_supported import TlsNotSupported
        from ..models.unchecked_certificate import UncheckedCertificate
        from ..models.unexpected_status import UnexpectedStatus

        status: Dict[str, Any]

        if isinstance(self.status, CheckedCertificate):
            status = self.status.to_dict()

        elif isinstance(self.status, TlsNotSupported):
            status = self.status.to_dict()

        elif isinstance(self.status, UncheckedCertificate):
            status = self.status.to_dict()

        elif isinstance(self.status, UnexpectedStatus):
            status = self.status.to_dict()

        else:
            status = self.status.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.checked_certificate import CheckedCertificate
        from ..models.tls_not_supported import TlsNotSupported
        from ..models.unchecked_certificate import UncheckedCertificate
        from ..models.unexpected_status import UnexpectedStatus
        from ..models.unreachable_target import UnreachableTarget

        d = src_dict.copy()

        def _parse_status(
            data: object,
        ) -> Union[
            "CheckedCertificate",
            "TlsNotSupported",
            "UncheckedCertificate",
            "UnexpectedStatus",
            "UnreachableTarget",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_tls_status_type_0 = CheckedCertificate.from_dict(data)

                return componentsschemas_tls_status_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_tls_status_type_1 = TlsNotSupported.from_dict(data)

                return componentsschemas_tls_status_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_tls_status_type_2 = UncheckedCertificate.from_dict(
                    data
                )

                return componentsschemas_tls_status_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_tls_status_type_3 = UnexpectedStatus.from_dict(data)

                return componentsschemas_tls_status_type_3
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_tls_status_type_4 = UnreachableTarget.from_dict(data)

            return componentsschemas_tls_status_type_4

        status = _parse_status(d.pop("status"))

        tls_test_response = cls(
            status=status,
        )

        tls_test_response.additional_properties = d
        return tls_test_response

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
