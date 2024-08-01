from typing import Dict, List
from pydantic import BaseModel, Field

from .core.page import Page
from .core.page_stats import PageStats
from .core.query_run import QueryRun
from .core.result_format import ResultFormat
from .core.rpc_request import RpcRequest
from .core.rpc_response import RpcResponse


class QueryResultsRpcParams(BaseModel):
    query: str
    format: ResultFormat
    page: Page

    model_config = {
        "validate_assignment": True,
    }


class QueryResultsRpcRequest(RpcRequest):
    method: str = Field("queryResults", const=True)
    params: List[QueryResultsRpcParams]

    model_config = {
        "validate_assignment": True,
    }


class QueryResultsRpcResult(BaseModel):
    columnNames: List[str]
    columnTypes: List[str]
    rows: List[Dict]
    page: PageStats
    sql: str
    format: ResultFormat
    originalQueryRun: QueryRun
    redirectedToQueryRun: QueryRun | None = None

    model_config = {
        "validate_assignment": True,
    }


class QueryResultsRpcResponse(RpcResponse):
    result: QueryResultsRpcResult

    model_config = {
        "validate_assignment": True,
    }
