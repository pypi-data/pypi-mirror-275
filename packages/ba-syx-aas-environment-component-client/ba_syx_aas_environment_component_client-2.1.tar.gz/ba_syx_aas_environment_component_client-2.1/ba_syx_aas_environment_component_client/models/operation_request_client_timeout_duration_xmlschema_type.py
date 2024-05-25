from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OperationRequestClientTimeoutDurationXmlschemaType")


@_attrs_define
class OperationRequestClientTimeoutDurationXmlschemaType:
    """
    Attributes:
        namespace_uri (Union[Unset, str]):
        local_part (Union[Unset, str]):
        prefix (Union[Unset, str]):
    """

    namespace_uri: Union[Unset, str] = UNSET
    local_part: Union[Unset, str] = UNSET
    prefix: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        namespace_uri = self.namespace_uri

        local_part = self.local_part

        prefix = self.prefix

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if namespace_uri is not UNSET:
            field_dict["namespaceURI"] = namespace_uri
        if local_part is not UNSET:
            field_dict["localPart"] = local_part
        if prefix is not UNSET:
            field_dict["prefix"] = prefix

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        namespace_uri = d.pop("namespaceURI", UNSET)

        local_part = d.pop("localPart", UNSET)

        prefix = d.pop("prefix", UNSET)

        operation_request_client_timeout_duration_xmlschema_type = cls(
            namespace_uri=namespace_uri,
            local_part=local_part,
            prefix=prefix,
        )

        operation_request_client_timeout_duration_xmlschema_type.additional_properties = d
        return operation_request_client_timeout_duration_xmlschema_type

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
