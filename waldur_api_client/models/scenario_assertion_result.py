from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.scenario_assertion_result_actual_type_0 import ScenarioAssertionResultActualType0
    from ..models.scenario_assertion_result_assertion import ScenarioAssertionResultAssertion


T = TypeVar("T", bound="ScenarioAssertionResult")


@_attrs_define
class ScenarioAssertionResult:
    """
    Attributes:
        assertion (ScenarioAssertionResultAssertion):
        passed (bool):
        actual (Union['ScenarioAssertionResultActualType0', None]):
        step (Union[None, str]):
        message (str):
    """

    assertion: "ScenarioAssertionResultAssertion"
    passed: bool
    actual: Union["ScenarioAssertionResultActualType0", None]
    step: Union[None, str]
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.scenario_assertion_result_actual_type_0 import ScenarioAssertionResultActualType0

        assertion = self.assertion.to_dict()

        passed = self.passed

        actual: Union[None, dict[str, Any]]
        if isinstance(self.actual, ScenarioAssertionResultActualType0):
            actual = self.actual.to_dict()
        else:
            actual = self.actual

        step: Union[None, str]
        step = self.step

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assertion": assertion,
                "passed": passed,
                "actual": actual,
                "step": step,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scenario_assertion_result_actual_type_0 import ScenarioAssertionResultActualType0
        from ..models.scenario_assertion_result_assertion import ScenarioAssertionResultAssertion

        d = dict(src_dict)
        assertion = ScenarioAssertionResultAssertion.from_dict(d.pop("assertion"))

        passed = d.pop("passed")

        def _parse_actual(data: object) -> Union["ScenarioAssertionResultActualType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                actual_type_0 = ScenarioAssertionResultActualType0.from_dict(data)

                return actual_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ScenarioAssertionResultActualType0", None], data)

        actual = _parse_actual(d.pop("actual"))

        def _parse_step(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        step = _parse_step(d.pop("step"))

        message = d.pop("message")

        scenario_assertion_result = cls(
            assertion=assertion,
            passed=passed,
            actual=actual,
            step=step,
            message=message,
        )

        scenario_assertion_result.additional_properties = d
        return scenario_assertion_result

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
