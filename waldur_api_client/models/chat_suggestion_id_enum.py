from enum import Enum


class ChatSuggestionIdEnum(str, Enum):
    ANALYZE_USAGE = "analyze_usage"
    CALL_INSIGHTS = "call_insights"
    CHECK_CREDIT = "check_credit"
    CREATE_VM = "create_vm"
    FIND_CALL = "find_call"
    FIND_SERVICE = "find_service"
    HPC_JOBS = "hpc_jobs"
    HPC_SOFTWARE = "hpc_software"
    LIST_INVOICES = "list_invoices"
    LOOK_UP_USER = "look_up_user"
    MY_RESOURCES = "my_resources"
    OVERDRAWN_PROJECTS = "overdrawn_projects"
    PENDING_ORDERS = "pending_orders"
    PROPOSAL_HELP = "proposal_help"
    RESOURCE_PAUSED = "resource_paused"
    REVIEW_WORKLOAD = "review_workload"
    SEARCH_DOCS = "search_docs"
    VISUALIZE_COSTS = "visualize_costs"

    def __str__(self) -> str:
        return str(self.value)
