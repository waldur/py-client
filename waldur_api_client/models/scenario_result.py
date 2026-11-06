from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workflow_scenario_status import WorkflowScenarioStatus

if TYPE_CHECKING:
    from ..models.scenario_assertion_result import ScenarioAssertionResult


T = TypeVar("T", bound="ScenarioResult")


@_attrs_define
class ScenarioResult:
    """
    Attributes:
        key (Union[None, str]):
        name (str):
        status (WorkflowScenarioStatus):
        error (Union[None, str]):
        action (Union[None, int]): Index of the action the run stopped at.
        failure (Union['ScenarioAssertionResult', None]):
        assertions (list['ScenarioAssertionResult']):
        path (list[list[str]]): The (step, outcome or status) pairs the proposal took.
        proposal_state (Union[None, str]):
        exercised (list[str]):
    """

    key: Union[None, str]
    name: str
    status: WorkflowScenarioStatus
    error: Union[None, str]
    action: Union[None, int]
    failure: Union["ScenarioAssertionResult", None]
    assertions: list["ScenarioAssertionResult"]
    path: list[list[str]]
    proposal_state: Union[None, str]
    exercised: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.scenario_assertion_result import ScenarioAssertionResult

        key: Union[None, str]
        key = self.key

        name = self.name

        status = self.status.value

        error: Union[None, str]
        error = self.error

        action: Union[None, int]
        action = self.action

        failure: Union[None, dict[str, Any]]
        if isinstance(self.failure, ScenarioAssertionResult):
            failure = self.failure.to_dict()
        else:
            failure = self.failure

        assertions = []
        for assertions_item_data in self.assertions:
            assertions_item = assertions_item_data.to_dict()
            assertions.append(assertions_item)

        path = []
        for path_item_data in self.path:
            path_item = path_item_data

            path.append(path_item)

        proposal_state: Union[None, str]
        proposal_state = self.proposal_state

        exercised = self.exercised

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "name": name,
                "status": status,
                "error": error,
                "action": action,
                "failure": failure,
                "assertions": assertions,
                "path": path,
                "proposal_state": proposal_state,
                "exercised": exercised,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scenario_assertion_result import ScenarioAssertionResult

        d = dict(src_dict)

        def _parse_key(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        key = _parse_key(d.pop("key"))

        name = d.pop("name")

        status = WorkflowScenarioStatus(d.pop("status"))

        def _parse_error(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        error = _parse_error(d.pop("error"))

        def _parse_action(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        action = _parse_action(d.pop("action"))

        def _parse_failure(data: object) -> Union["ScenarioAssertionResult", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                failure_type_1 = ScenarioAssertionResult.from_dict(data)

                return failure_type_1
            except:  # noqa: E722
                pass
            return cast(Union["ScenarioAssertionResult", None], data)

        failure = _parse_failure(d.pop("failure"))

        assertions = []
        _assertions = d.pop("assertions")
        for assertions_item_data in _assertions:
            assertions_item = ScenarioAssertionResult.from_dict(assertions_item_data)

            assertions.append(assertions_item)

        path = []
        _path = d.pop("path")
        for path_item_data in _path:
            path_item = cast(list[str], path_item_data)

            path.append(path_item)

        def _parse_proposal_state(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        proposal_state = _parse_proposal_state(d.pop("proposal_state"))

        exercised = cast(list[str], d.pop("exercised"))

        scenario_result = cls(
            key=key,
            name=name,
            status=status,
            error=error,
            action=action,
            failure=failure,
            assertions=assertions,
            path=path,
            proposal_state=proposal_state,
            exercised=exercised,
        )

        scenario_result.additional_properties = d
        return scenario_result

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
