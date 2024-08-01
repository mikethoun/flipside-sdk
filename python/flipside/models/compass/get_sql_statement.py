from typing import List
from pydantic import BaseModel, Field

from .core.rpc_request import RpcRequest
from .core.rpc_response import RpcResponse
from .core.sql_statement import SqlStatement


class GetSqlStatementParams(BaseModel):
    sqlStatementId: str

    model_config = {
        "validate_assignment": True,
    }


class GetSqlStatementRequest(RpcRequest):
    method: str = Field("getSqlStatement", const=True)
    params: List[GetSqlStatementParams]

    model_config = {
        "validate_assignment": True,
    }


class GetSqlStatementResult(BaseModel):
    sqlStatement: SqlStatement

    model_config = {
        "validate_assignment": True,
    }


class GetSqlStatementResponse(RpcResponse):
    result: GetSqlStatementResult | None = None

    model_config = {
        "validate_assignment": True,
    }
