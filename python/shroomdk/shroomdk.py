from typing import List, Optional, Union

from shroomdk.integrations.query_integration.compass_query_integration import (
    CompassQueryIntegration,
)
from shroomdk.models import Query
from shroomdk.models.compass.core.query_run import QueryRun
from shroomdk.models.compass.core.sql_statement import SqlStatement
from shroomdk.models.compass.get_sql_statement import GetSqlStatementParams
from shroomdk.models.query_result_set import QueryResultSet
from shroomdk.rpc import RPC

from .models import Filter, SortBy

API_BASE_URL = "https://rpc-prod.flompass.pizza"

SDK_VERSION = "2.0.0"
SDK_PACKAGE = "python"


class ShroomDK(object):
    def __init__(self, api_key: str, api_base_url: str = API_BASE_URL):
        self.rpc = RPC(api_base_url, api_key)
        self.query_integration = CompassQueryIntegration(self.rpc)

    def query(
        self,
        sql,
        ttl_minutes=60,
        max_age_minutes=60,
        cached=True,
        timeout_minutes=20,
        retry_interval_seconds=1,
        page_size=100000,
        page_number=1,
        data_source="snowflake-default",
        data_provider="flipside",
    ) -> QueryResultSet:
        query_integration = CompassQueryIntegration(self.rpc)

        return query_integration.run(
            Query(
                sql=sql,
                ttl_minutes=ttl_minutes,
                timeout_minutes=timeout_minutes,
                max_age_minutes=max_age_minutes,
                retry_interval_seconds=retry_interval_seconds,
                page_size=page_size,
                page_number=page_number,
                cached=cached,
                sdk_package=SDK_PACKAGE,
                sdk_version=SDK_VERSION,
                data_source=data_source,
                data_provider=data_provider,
            )
        )

    def get_query_run(self, query_run_id: str) -> QueryRun:
        return self.query_integration.get_query_run(query_run_id)

    def get_query_results(
        self,
        query_run_id: str,
        page_number: int = 1,
        page_size: int = 10000,
        filters: Optional[Union[List[Filter], None]] = [],
        sort_by: Optional[Union[List[SortBy], None]] = [],
    ) -> QueryResultSet:
        return self.query_integration.get_query_results(
            query_run_id,
            page_number=page_number,
            page_size=page_size,
            filters=filters,
            sort_by=sort_by,
        )

    def get_sql_statement(self, sql_statement_id: str) -> SqlStatement:
        return self.query_integration.get_sql_statement(sql_statement_id)
