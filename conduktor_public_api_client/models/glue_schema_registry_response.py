from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define, field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credentials import Credentials
    from ..models.from_context import FromContext
    from ..models.from_role import FromRole
    from ..models.iam_anywhere import IAMAnywhere


T = TypeVar("T", bound="GlueSchemaRegistryResponse")


@define
class GlueSchemaRegistryResponse:
    """
    Attributes:
        id (str):
        region (str):
        security (Union['Credentials', 'FromContext', 'FromRole', 'IAMAnywhere']):
        type (str):
        registry_name (Union[Unset, str]):
    """

    id: str
    region: str
    security: Union["Credentials", "FromContext", "FromRole", "IAMAnywhere"]
    type: str
    registry_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.credentials import Credentials
        from ..models.from_context import FromContext
        from ..models.from_role import FromRole

        id = self.id
        region = self.region
        security: Dict[str, Any]

        if isinstance(self.security, Credentials):
            security = self.security.to_dict()

        elif isinstance(self.security, FromContext):
            security = self.security.to_dict()

        elif isinstance(self.security, FromRole):
            security = self.security.to_dict()

        else:
            security = self.security.to_dict()

        type = self.type
        registry_name = self.registry_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "region": region,
                "security": security,
                "type": type,
            }
        )
        if registry_name is not UNSET:
            field_dict["registryName"] = registry_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.credentials import Credentials
        from ..models.from_context import FromContext
        from ..models.from_role import FromRole
        from ..models.iam_anywhere import IAMAnywhere

        d = src_dict.copy()
        id = d.pop("id")

        region = d.pop("region")

        def _parse_security(
            data: object,
        ) -> Union["Credentials", "FromContext", "FromRole", "IAMAnywhere"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_amazon_security_type_0 = Credentials.from_dict(data)

                return componentsschemas_amazon_security_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_amazon_security_type_1 = FromContext.from_dict(data)

                return componentsschemas_amazon_security_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_amazon_security_type_2 = FromRole.from_dict(data)

                return componentsschemas_amazon_security_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_amazon_security_type_3 = IAMAnywhere.from_dict(data)

            return componentsschemas_amazon_security_type_3

        security = _parse_security(d.pop("security"))

        type = d.pop("type")

        registry_name = d.pop("registryName", UNSET)

        glue_schema_registry_response = cls(
            id=id,
            region=region,
            security=security,
            type=type,
            registry_name=registry_name,
        )

        glue_schema_registry_response.additional_properties = d
        return glue_schema_registry_response

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
