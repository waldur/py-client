from enum import Enum


class OfferingDependentChangeEnum(str, Enum):
    COMPONENT_CHANGED = "component_changed"
    COMPONENT_REMOVED = "component_removed"
    OFFERING_DELETED = "offering_deleted"
    OFFERING_TEAM_DROPPED = "offering_team_dropped"
    OFFERING_WITHDRAWN = "offering_withdrawn"
    PLAN_ARCHIVED = "plan_archived"
    PLAN_DELETED = "plan_deleted"

    def __str__(self) -> str:
        return str(self.value)
