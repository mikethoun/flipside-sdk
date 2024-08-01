from typing import Any, List
from pydantic import BaseModel, Field

from .core.page import Page
from .core.page_stats import PageStats
from .core.query_run import QueryRun
from .core.result_format import ResultFormat
from .core.rpc_request import RpcRequest
from .core.rpc_response import RpcResponse


class Filter(BaseModel):
    column: str
    eq: Any | None = None
    neq: Any | None = None
    gt: Any | None = None
    gte: Any | None = None
    lt: Any | None = None
    lte: Any | None = None
    like: Any | None = None
    in_: List[Any] | None = Field(None, alias="in")
    notIn: List[Any] | None = None

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
    }

    def dict(self, *args, **kwargs) -> dict:
        kwargs.setdefault("exclude_none", True)
        result = super().dict(*args, **kwargs)
        if "in_" in result:
            result["in"] = result.pop("in_")
        return result


class SortBy(BaseModel):
    column: str
    direction: str

    model_config = {
        "validate_assignment": True,
    }


class GetQueryRunResultsRpcParams(BaseModel):
    queryRunId: str
    format: ResultFormat
    filters: List[Filter] | None = []
    sortBy: List[SortBy] | None = []
    page: Page

    model_config = {
        "validate_assignment": True,
    }

    def dict(self, *args, **kwargs) -> dict:
        kwargs.setdefault("exclude_none", True)
        return super().dict(*args, **kwargs)


class GetQueryRunResultsRpcRequest(RpcRequest):
    method: str = Field("getQueryRunResults", const=True)
    params: List[GetQueryRunResultsRpcParams]

    model_config = {
        "validate_assignment": True,
    }

    def dict(self, *args, **kwargs) -> dict:
        kwargs.setdefault("exclude_none", True)
        return super().dict(*args, **kwargs)


class GetQueryRunResultsRpcResult(BaseModel):
    columnNames: List[str] | None = None
    columnTypes: List[str] | None = None
    rows: List[Any] | None = None
    page: PageStats | None = None
    sql: str | None = None
    format: ResultFormat | None = None
    originalQueryRun: QueryRun
    redirectedToQueryRun: QueryRun | None = None

    model_config = {
        "validate_assignment": True,
    }


class GetQueryRunResultsRpcResponse(RpcResponse):
    result: GetQueryRunResultsRpcResult | None = None

    model_config = {
        "validate_assignment": True,
    }
