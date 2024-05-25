from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.message_message_type import MessageMessageType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Message")


@_attrs_define
class Message:
    """
    Attributes:
        timestamp (Union[Unset, str]):
        text (Union[Unset, str]):
        message_type (Union[Unset, MessageMessageType]):
        correlation_id (Union[Unset, str]):
        code (Union[Unset, str]):
    """

    timestamp: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    message_type: Union[Unset, MessageMessageType] = UNSET
    correlation_id: Union[Unset, str] = UNSET
    code: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timestamp = self.timestamp

        text = self.text

        message_type: Union[Unset, str] = UNSET
        if not isinstance(self.message_type, Unset):
            message_type = self.message_type.value

        correlation_id = self.correlation_id

        code = self.code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if text is not UNSET:
            field_dict["text"] = text
        if message_type is not UNSET:
            field_dict["messageType"] = message_type
        if correlation_id is not UNSET:
            field_dict["correlationId"] = correlation_id
        if code is not UNSET:
            field_dict["code"] = code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        timestamp = d.pop("timestamp", UNSET)

        text = d.pop("text", UNSET)

        _message_type = d.pop("messageType", UNSET)
        message_type: Union[Unset, MessageMessageType]
        if isinstance(_message_type, Unset):
            message_type = UNSET
        else:
            message_type = MessageMessageType(_message_type)

        correlation_id = d.pop("correlationId", UNSET)

        code = d.pop("code", UNSET)

        message = cls(
            timestamp=timestamp,
            text=text,
            message_type=message_type,
            correlation_id=correlation_id,
            code=code,
        )

        message.additional_properties = d
        return message

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
