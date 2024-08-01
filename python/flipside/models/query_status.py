from enum import Enum
from pydantic import BaseModel


class QueryStatusEnum(str, Enum):
    READY = "QUERY_STATE_READY"
    RUNNING = "QUERY_STATE_RUNNING"
    STREAMING_RESULTS = "QUERY_STATE_STREAMING_RESULTS"
    SUCCESS = "QUERY_STATE_SUCCESS"
    FAILED = "QUERY_STATE_FAILED"
    CANCELED = "QUERY_STATE_CANCELED"


class QueryStatus(BaseModel):
    Ready: str = QueryStatusEnum.READY
    Running: str = QueryStatusEnum.RUNNING
    StreamingResults: str = QueryStatusEnum.STREAMING_RESULTS
    Success: str = QueryStatusEnum.SUCCESS
    Failed: str = QueryStatusEnum.FAILED
    Canceled: str = QueryStatusEnum.CANCELED

    model_config = {
        "validate_assignment": True,
    }
