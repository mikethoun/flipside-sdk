from datetime import datetime
from typing import Any
from pydantic import BaseModel, Field

from .tags import Tags


class QueryRun(BaseModel):
    id: str
    sqlStatementId: str
    state: str
    path: str
    fileCount: int | None = Field(None)
    lastFileNumber: int | None = Field(None)
    fileNames: str | None = Field(None)
    errorName: str | None = Field(None)
    errorMessage: str | None = Field(None)
    errorData: Any | None = Field(None)
    dataSourceQueryId: str | None = Field(None)
    dataSourceSessionId: str | None = Field(None)
    startedAt: str | None = Field(None)
    queryRunningEndedAt: str | None = Field(None)
    queryStreamingEndedAt: str | None = Field(None)
    endedAt: str | None = Field(None)
    rowCount: int | None = Field(None)
    totalSize: int | None = Field(None)
    tags: Tags
    dataSourceId: str
    userId: str
    createdAt: str
    updatedAt: datetime
    archivedAt: datetime | None = Field(None)

    model_config = {
        "validate_assignment": True,
    }
