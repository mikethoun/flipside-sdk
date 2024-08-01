from datetime import datetime
from pydantic import BaseModel, Field


class SqlStatement(BaseModel):
    id: str
    sql: str
    createdAt: datetime
    updatedAt: datetime
    archivedAt: datetime | None = Field(None)

    model_config = {
        "validate_assignment": True,
    }
