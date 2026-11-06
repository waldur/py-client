from enum import Enum


class PostAwardStatusEnum(str, Enum):
    EXTENSION_IN_ASSESSMENT = "extension_in_assessment"
    EXTENSION_PENDING_RESULTS = "extension_pending_results"
    EXTENSION_REQUESTED = "extension_requested"
    FINAL_REPORT_SUBMITTED = "final_report_submitted"
    PENDING_FINAL_REPORT = "pending_final_report"
    PROJECT_COMPLETED = "project_completed"
    PROJECT_EXTENDED = "project_extended"

    def __str__(self) -> str:
        return str(self.value)
