from typing import Any
from pydantic import BaseModel, Field


class RpcError(BaseModel):
    code: int
    message: str
    data: Any | None = Field(None)

    model_config = {
        "validate_assignment": True,
    }
