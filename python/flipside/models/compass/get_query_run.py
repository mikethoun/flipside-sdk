from typing import List
from pydantic import BaseModel, Field

from .core.query_run import QueryRun
from .core.rpc_request import RpcRequest
from .core.rpc_response import RpcResponse


class GetQueryRunRpcRequestParams(BaseModel):
    queryRunId: str

    model_config = {
        "validate_assignment": True,
    }


class GetQueryRunRpcRequest(RpcRequest):
    method: str = Field("getQueryRun", const=True)
    params: List[GetQueryRunRpcRequestParams]

    model_config = {
        "validate_assignment": True,
    }


class GetQueryRunRpcResult(BaseModel):
    queryRun: QueryRun
    redirectedToQueryRun: QueryRun | None = None

    model_config = {
        "validate_assignment": True,
    }


class GetQueryRunRpcResponse(RpcResponse):
    result: GetQueryRunRpcResult | None = None

    model_config = {
        "validate_assignment": True,
    }
