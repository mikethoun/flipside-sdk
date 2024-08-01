from typing import List
from pydantic import BaseModel, Field

from .core.query_run import QueryRun
from .core.rpc_request import RpcRequest
from .core.rpc_response import RpcResponse


class CancelQueryRunRpcRequestParams(BaseModel):
    queryRunId: str

    model_config = {
        "validate_assignment": True,
    }


class CancelQueryRunRpcRequest(RpcRequest):
    method: str = Field("cancelQueryRun", const=True)
    params: List[CancelQueryRunRpcRequestParams]

    model_config = {
        "validate_assignment": True,
    }


class CancelQueryRunRpcResult(BaseModel):
    queryRun: QueryRun

    model_config = {
        "validate_assignment": True,
    }


class CancelQueryRunRpcResponse(RpcResponse):
    result: CancelQueryRunRpcResult | None = None

    model_config = {
        "validate_assignment": True,
    }
