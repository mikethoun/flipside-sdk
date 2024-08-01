from typing import Any, Dict
from pydantic import BaseModel, Field

from .rpc_error import RpcError


class RpcResponse(BaseModel):
    jsonrpc: str
    id: int
    result: Dict[str, Any] | None = Field(None)
    error: RpcError | None = Field(None)

    model_config = {
        "validate_assignment": True,
    }
