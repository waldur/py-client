from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.offering_configuration_finding_severity_enum import OfferingConfigurationFindingSeverityEnum
from ..models.rule_enum import RuleEnum

T = TypeVar("T", bound="OfferingConfigurationFinding")


@_attrs_define
class OfferingConfigurationFinding:
    """
    Attributes:
        rule (RuleEnum):
        severity (OfferingConfigurationFindingSeverityEnum):
        field (str): Dotted path into the offering document, list items by index, such as components.0.type or
            agent_configuration.backend_settings.cluster_name.
        message (str):
    """

    rule: RuleEnum
    severity: OfferingConfigurationFindingSeverityEnum
    field: str
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rule = self.rule.value

        severity = self.severity.value

        field = self.field

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rule": rule,
                "severity": severity,
                "field": field,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rule = RuleEnum(d.pop("rule"))

        severity = OfferingConfigurationFindingSeverityEnum(d.pop("severity"))

        field = d.pop("field")

        message = d.pop("message")

        offering_configuration_finding = cls(
            rule=rule,
            severity=severity,
            field=field,
            message=message,
        )

        offering_configuration_finding.additional_properties = d
        return offering_configuration_finding

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
