from typing import Union
from pydantic import BaseModel, Field


class Query(BaseModel):
    sql: str = Field(None, description="SQL query to execute")
    ttl_minutes: int | None = Field(
        None, description="The number of minutes to cache the query results"
    )
    max_age_minutes: int | None = Field(
        5, description="The max age of the query results in minutes"
    )
    timeout_minutes: int | None = Field(
        None, description="The number of minutes to timeout the query"
    )
    retry_interval_seconds: int | float | None = Field(
        1, description="The number of seconds to use between retries"
    )
    cached: bool | None = Field(
        None,
        description="An override on the cache. A value of true will Re-Execute the query.",
    )
    page_size: int | None = Field(None, description="The number of results to return per page")
    page_number: int | None = Field(None, description="The page number to return")
    sdk_package: str | None = Field(
        None, description="The SDK package used for the query"
    )
    sdk_version: str | None = Field(
        None, description="The SDK version used for the query"
    )
    data_source: str | None = Field(
        None, description="The data source to execute the query against"
    )
    data_provider: str | None = Field(
        None, description="The owner of the data source"
    )

    model_config = {
        "validate_assignment": True,
    }
