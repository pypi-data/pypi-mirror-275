from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.operation_request_client_timeout_duration_xmlschema_type import (
        OperationRequestClientTimeoutDurationXmlschemaType,
    )


T = TypeVar("T", bound="OperationRequestClientTimeoutDuration")


@_attrs_define
class OperationRequestClientTimeoutDuration:
    """
    Attributes:
        sign (Union[Unset, int]):
        xmlschema_type (Union[Unset, OperationRequestClientTimeoutDurationXmlschemaType]):
        months (Union[Unset, int]):
        seconds (Union[Unset, int]):
        days (Union[Unset, int]):
        years (Union[Unset, int]):
        hours (Union[Unset, int]):
        minutes (Union[Unset, int]):
    """

    sign: Union[Unset, int] = UNSET
    xmlschema_type: Union[Unset, "OperationRequestClientTimeoutDurationXmlschemaType"] = UNSET
    months: Union[Unset, int] = UNSET
    seconds: Union[Unset, int] = UNSET
    days: Union[Unset, int] = UNSET
    years: Union[Unset, int] = UNSET
    hours: Union[Unset, int] = UNSET
    minutes: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sign = self.sign

        xmlschema_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.xmlschema_type, Unset):
            xmlschema_type = self.xmlschema_type.to_dict()

        months = self.months

        seconds = self.seconds

        days = self.days

        years = self.years

        hours = self.hours

        minutes = self.minutes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sign is not UNSET:
            field_dict["sign"] = sign
        if xmlschema_type is not UNSET:
            field_dict["xmlschemaType"] = xmlschema_type
        if months is not UNSET:
            field_dict["months"] = months
        if seconds is not UNSET:
            field_dict["seconds"] = seconds
        if days is not UNSET:
            field_dict["days"] = days
        if years is not UNSET:
            field_dict["years"] = years
        if hours is not UNSET:
            field_dict["hours"] = hours
        if minutes is not UNSET:
            field_dict["minutes"] = minutes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.operation_request_client_timeout_duration_xmlschema_type import (
            OperationRequestClientTimeoutDurationXmlschemaType,
        )

        d = src_dict.copy()
        sign = d.pop("sign", UNSET)

        _xmlschema_type = d.pop("xmlschemaType", UNSET)
        xmlschema_type: Union[Unset, OperationRequestClientTimeoutDurationXmlschemaType]
        if isinstance(_xmlschema_type, Unset):
            xmlschema_type = UNSET
        else:
            xmlschema_type = OperationRequestClientTimeoutDurationXmlschemaType.from_dict(_xmlschema_type)

        months = d.pop("months", UNSET)

        seconds = d.pop("seconds", UNSET)

        days = d.pop("days", UNSET)

        years = d.pop("years", UNSET)

        hours = d.pop("hours", UNSET)

        minutes = d.pop("minutes", UNSET)

        operation_request_client_timeout_duration = cls(
            sign=sign,
            xmlschema_type=xmlschema_type,
            months=months,
            seconds=seconds,
            days=days,
            years=years,
            hours=hours,
            minutes=minutes,
        )

        operation_request_client_timeout_duration.additional_properties = d
        return operation_request_client_timeout_duration

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
