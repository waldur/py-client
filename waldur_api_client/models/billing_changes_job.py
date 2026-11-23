from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.billing_changes_job_state_enum import BillingChangesJobStateEnum

if TYPE_CHECKING:
    from ..models.billing_changes_response import BillingChangesResponse


T = TypeVar("T", bound="BillingChangesJob")


@_attrs_define
class BillingChangesJob:
    """
    Attributes:
        job_id (str):
        state (BillingChangesJobStateEnum):
        report (Union['BillingChangesResponse', None]):
        error (Union[None, str]):
    """

    job_id: str
    state: BillingChangesJobStateEnum
    report: Union["BillingChangesResponse", None]
    error: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.billing_changes_response import BillingChangesResponse

        job_id = self.job_id

        state = self.state.value

        report: Union[None, dict[str, Any]]
        if isinstance(self.report, BillingChangesResponse):
            report = self.report.to_dict()
        else:
            report = self.report

        error: Union[None, str]
        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "job_id": job_id,
                "state": state,
                "report": report,
                "error": error,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.billing_changes_response import BillingChangesResponse

        d = dict(src_dict)
        job_id = d.pop("job_id")

        state = BillingChangesJobStateEnum(d.pop("state"))

        def _parse_report(data: object) -> Union["BillingChangesResponse", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                report_type_1 = BillingChangesResponse.from_dict(data)

                return report_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BillingChangesResponse", None], data)

        report = _parse_report(d.pop("report"))

        def _parse_error(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        error = _parse_error(d.pop("error"))

        billing_changes_job = cls(
            job_id=job_id,
            state=state,
            report=report,
            error=error,
        )

        billing_changes_job.additional_properties = d
        return billing_changes_job

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
