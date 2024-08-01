from typing import List
from pydantic import BaseModel, Field

from .core.query_request import QueryRequest
from .core.query_run import QueryRun
from .core.rpc_request import RpcRequest
from .core.rpc_response import RpcResponse
from .core.sql_statement import SqlStatement
from .core.tags import Tags


class CreateQueryRunRpcParams(BaseModel):
    resultTTLHours: int
    maxAgeMinutes: int
    sql: str
    tags: Tags
    dataSource: str
    dataProvider: str

    model_config = {
        "validate_assignment": True,
    }


class CreateQueryRunRpcRequest(RpcRequest):
    method: str = Field("createQueryRun", const=True)
    params: List[CreateQueryRunRpcParams]

    model_config = {
        "validate_assignment": True,
    }


class CreateQueryRunRpcResult(BaseModel):
    queryRequest: QueryRequest
    queryRun: QueryRun
    sqlStatement: SqlStatement

    model_config = {
        "validate_assignment": True,
    }


class CreateQueryRunRpcResponse(RpcResponse):
    result: CreateQueryRunRpcResult | None = None

    model_config = {
        "validate_assignment": True,
    }
