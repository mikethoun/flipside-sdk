from typing import Any, Dict, List
from pydantic import BaseModel, Field


class RpcRequest(BaseModel):
    jsonrpc: str = Field("2.0", const=True)
    method: str
    params: List[Dict[str, Any]]
    id: int = Field(1, const=True)

    model_config = {
        "validate_assignment": True,
    }
