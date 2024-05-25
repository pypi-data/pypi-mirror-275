"""SQLService"""

import great_expectations as ge
import time


class SQLService:
    """SQLService"""

    def __init__(self, **kwargs):
        """__init__"""
        self.ge_context = ge.get_context(
            project_root_dir=kwargs.get("project_root_dir", "./tmp/sql")
        )
        self.ge_transaction_name = kwargs.get("test_name")
        self.ge_datasource = None
        self.ge_data_asset = None
        self.ge_batch_request = None
        self.ge_expectation_suite_name = None

    def validator(self, **kwargs):
        """validator"""
        connection_str = kwargs.get("connection_str")
        sql = kwargs.get("sql")

        # great expectations data source
        if not self.ge_datasource:
            self.ge_datasource = self.ge_context.sources.add_sql(
                name=f"{self.ge_transaction_name}_datasource_{str(int(time.time()))}",
                connection_string=connection_str,
            )

        # great expectations data asset
        data_asset_name = f"{self.ge_transaction_name}_asset"
        if not self.ge_data_asset:
            self.ge_data_asset = self.ge_datasource.add_query_asset(
                name=data_asset_name, query=sql
            )

        # great expectations expectation suite
        self.ge_expectation_suite_name = f"{self.ge_transaction_name}_suite"
        self.ge_context.add_or_update_expectation_suite(self.ge_expectation_suite_name)

        # great expectations batch request
        self.ge_batch_request = self.ge_data_asset.build_batch_request()

        # return data validator
        return self.ge_context.get_validator(
            batch_request=self.ge_batch_request,
            expectation_suite_name=self.ge_expectation_suite_name,
            data_asset_name=self.ge_data_asset,
        )
