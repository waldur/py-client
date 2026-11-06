from enum import Enum


class ProposalRankingOEnum(str, Enum):
    FINAL_SCORE = "final_score"
    MODIFIED = "modified"
    PROPOSAL_NAME = "proposal_name"
    RANK = "rank"
    VALUE_0 = "-final_score"
    VALUE_1 = "-modified"
    VALUE_2 = "-proposal_name"
    VALUE_3 = "-rank"

    def __str__(self) -> str:
        return str(self.value)
