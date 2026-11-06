from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.check_run_status_enum import CheckRunStatusEnum

if TYPE_CHECKING:
    from ..models.call_scenario_summary import CallScenarioSummary
    from ..models.call_template_reference import CallTemplateReference
    from ..models.scenario_coverage import ScenarioCoverage
    from ..models.scenario_result import ScenarioResult
    from ..models.scenario_totals import ScenarioTotals


T = TypeVar("T", bound="CallWorkflowScenarios")


@_attrs_define
class CallWorkflowScenarios:
    """
    Attributes:
        status (CheckRunStatusEnum):
        requested_at (Union[None, str]): When the latest run was asked for.
        error (Union[None, str]): Why the latest run's results were not kept: the earlier results stay in place.
        template (Union['CallTemplateReference', None]):
        scenarios (list['CallScenarioSummary']):
        version (Union[None, int]):
        checked_at (Union[None, str]):
        results (list['ScenarioResult']):
        totals (Union['ScenarioTotals', None]):
        coverage (Union['ScenarioCoverage', None]):
    """

    status: CheckRunStatusEnum
    requested_at: Union[None, str]
    error: Union[None, str]
    template: Union["CallTemplateReference", None]
    scenarios: list["CallScenarioSummary"]
    version: Union[None, int]
    checked_at: Union[None, str]
    results: list["ScenarioResult"]
    totals: Union["ScenarioTotals", None]
    coverage: Union["ScenarioCoverage", None]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.call_template_reference import CallTemplateReference
        from ..models.scenario_coverage import ScenarioCoverage
        from ..models.scenario_totals import ScenarioTotals

        status = self.status.value

        requested_at: Union[None, str]
        requested_at = self.requested_at

        error: Union[None, str]
        error = self.error

        template: Union[None, dict[str, Any]]
        if isinstance(self.template, CallTemplateReference):
            template = self.template.to_dict()
        else:
            template = self.template

        scenarios = []
        for scenarios_item_data in self.scenarios:
            scenarios_item = scenarios_item_data.to_dict()
            scenarios.append(scenarios_item)

        version: Union[None, int]
        version = self.version

        checked_at: Union[None, str]
        checked_at = self.checked_at

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        totals: Union[None, dict[str, Any]]
        if isinstance(self.totals, ScenarioTotals):
            totals = self.totals.to_dict()
        else:
            totals = self.totals

        coverage: Union[None, dict[str, Any]]
        if isinstance(self.coverage, ScenarioCoverage):
            coverage = self.coverage.to_dict()
        else:
            coverage = self.coverage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "requested_at": requested_at,
                "error": error,
                "template": template,
                "scenarios": scenarios,
                "version": version,
                "checked_at": checked_at,
                "results": results,
                "totals": totals,
                "coverage": coverage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.call_scenario_summary import CallScenarioSummary
        from ..models.call_template_reference import CallTemplateReference
        from ..models.scenario_coverage import ScenarioCoverage
        from ..models.scenario_result import ScenarioResult
        from ..models.scenario_totals import ScenarioTotals

        d = dict(src_dict)
        status = CheckRunStatusEnum(d.pop("status"))

        def _parse_requested_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        requested_at = _parse_requested_at(d.pop("requested_at"))

        def _parse_error(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        error = _parse_error(d.pop("error"))

        def _parse_template(data: object) -> Union["CallTemplateReference", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                template_type_1 = CallTemplateReference.from_dict(data)

                return template_type_1
            except:  # noqa: E722
                pass
            return cast(Union["CallTemplateReference", None], data)

        template = _parse_template(d.pop("template"))

        scenarios = []
        _scenarios = d.pop("scenarios")
        for scenarios_item_data in _scenarios:
            scenarios_item = CallScenarioSummary.from_dict(scenarios_item_data)

            scenarios.append(scenarios_item)

        def _parse_version(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        version = _parse_version(d.pop("version"))

        def _parse_checked_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        checked_at = _parse_checked_at(d.pop("checked_at"))

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = ScenarioResult.from_dict(results_item_data)

            results.append(results_item)

        def _parse_totals(data: object) -> Union["ScenarioTotals", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                totals_type_1 = ScenarioTotals.from_dict(data)

                return totals_type_1
            except:  # noqa: E722
                pass
            return cast(Union["ScenarioTotals", None], data)

        totals = _parse_totals(d.pop("totals"))

        def _parse_coverage(data: object) -> Union["ScenarioCoverage", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                coverage_type_1 = ScenarioCoverage.from_dict(data)

                return coverage_type_1
            except:  # noqa: E722
                pass
            return cast(Union["ScenarioCoverage", None], data)

        coverage = _parse_coverage(d.pop("coverage"))

        call_workflow_scenarios = cls(
            status=status,
            requested_at=requested_at,
            error=error,
            template=template,
            scenarios=scenarios,
            version=version,
            checked_at=checked_at,
            results=results,
            totals=totals,
            coverage=coverage,
        )

        call_workflow_scenarios.additional_properties = d
        return call_workflow_scenarios

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
