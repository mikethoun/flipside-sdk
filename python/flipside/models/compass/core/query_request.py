from pydantic import BaseModel, Field

from .tags import Tags


class QueryRequest(BaseModel):
    id: str
    sqlStatementId: str
    userId: str
    tags: Tags
    maxAgeMinutes: int
    resultTTLHours: int
    userSkipCache: bool
    triggeredQueryRun: bool
    queryRunId: str
    createdAt: str
    updatedAt: str

    model_config = {
        "validate_assignment": True,
    }
