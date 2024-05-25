from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.operation_request_client_timeout_duration import OperationRequestClientTimeoutDuration
    from ..models.operation_variable import OperationVariable


T = TypeVar("T", bound="OperationRequest")


@_attrs_define
class OperationRequest:
    """Operation request object

    Attributes:
        input_arguments (Union[Unset, List['OperationVariable']]):
        inoutput_arguments (Union[Unset, List['OperationVariable']]):
        client_timeout_duration (Union[Unset, OperationRequestClientTimeoutDuration]):
    """

    input_arguments: Union[Unset, List["OperationVariable"]] = UNSET
    inoutput_arguments: Union[Unset, List["OperationVariable"]] = UNSET
    client_timeout_duration: Union[Unset, "OperationRequestClientTimeoutDuration"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        input_arguments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.input_arguments, Unset):
            input_arguments = []
            for input_arguments_item_data in self.input_arguments:
                input_arguments_item = input_arguments_item_data.to_dict()
                input_arguments.append(input_arguments_item)

        inoutput_arguments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.inoutput_arguments, Unset):
            inoutput_arguments = []
            for inoutput_arguments_item_data in self.inoutput_arguments:
                inoutput_arguments_item = inoutput_arguments_item_data.to_dict()
                inoutput_arguments.append(inoutput_arguments_item)

        client_timeout_duration: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.client_timeout_duration, Unset):
            client_timeout_duration = self.client_timeout_duration.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if input_arguments is not UNSET:
            field_dict["inputArguments"] = input_arguments
        if inoutput_arguments is not UNSET:
            field_dict["inoutputArguments"] = inoutput_arguments
        if client_timeout_duration is not UNSET:
            field_dict["clientTimeoutDuration"] = client_timeout_duration

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.operation_request_client_timeout_duration import OperationRequestClientTimeoutDuration
        from ..models.operation_variable import OperationVariable

        d = src_dict.copy()
        input_arguments = []
        _input_arguments = d.pop("inputArguments", UNSET)
        for input_arguments_item_data in _input_arguments or []:
            input_arguments_item = OperationVariable.from_dict(input_arguments_item_data)

            input_arguments.append(input_arguments_item)

        inoutput_arguments = []
        _inoutput_arguments = d.pop("inoutputArguments", UNSET)
        for inoutput_arguments_item_data in _inoutput_arguments or []:
            inoutput_arguments_item = OperationVariable.from_dict(inoutput_arguments_item_data)

            inoutput_arguments.append(inoutput_arguments_item)

        _client_timeout_duration = d.pop("clientTimeoutDuration", UNSET)
        client_timeout_duration: Union[Unset, OperationRequestClientTimeoutDuration]
        if isinstance(_client_timeout_duration, Unset):
            client_timeout_duration = UNSET
        else:
            client_timeout_duration = OperationRequestClientTimeoutDuration.from_dict(_client_timeout_duration)

        operation_request = cls(
            input_arguments=input_arguments,
            inoutput_arguments=inoutput_arguments,
            client_timeout_duration=client_timeout_duration,
        )

        operation_request.additional_properties = d
        return operation_request

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
