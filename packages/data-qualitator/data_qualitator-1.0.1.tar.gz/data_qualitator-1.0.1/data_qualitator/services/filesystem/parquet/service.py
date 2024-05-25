"""
Filesystem parquet service.
"""

import great_expectations as ge
import time


class FilesystemParquetService:
    """FilesystemParquetService"""

    def __init__(self, **kwargs):
        """__init__"""
        self.ge_context = ge.get_context(
            project_root_dir=kwargs.get("project_root_dir", "./tmp/filesystem/parquet")
        )
        self.ge_transaction_name = kwargs.get("test_name")
        self.ge_datasource = None
        self.ge_data_asset = None
        self.ge_batch_request = None
        self.ge_expectation_suite_name = None

    def validator(self, **kwargs):
        """validator"""
        # the parquet file path
        file_path = kwargs.get("file_path")
        # the parquet file path regex pattern
        file_path_regex = kwargs.get("file_path_regex")

        # great expectations data source
        if not self.ge_datasource:
            self.ge_datasource = self.ge_context.sources.add_pandas_filesystem(
                name=f"{self.ge_transaction_name}_datasource_{str(int(time.time()))}",
                base_directory=file_path,
            )

        # great expectations expectation suite
        self.ge_expectation_suite_name = f"{self.ge_transaction_name}_suite"
        self.ge_context.add_or_update_expectation_suite(self.ge_expectation_suite_name)

        # great expectations data asset
        data_asset_name = f"{self.ge_transaction_name}_asset"
        if not self.ge_data_asset:
            self.ge_data_asset = self.ge_datasource.add_parquet_asset(
                name=data_asset_name, batching_regex=file_path_regex
            )

        # great expectations batch request
        self.ge_batch_request = self.ge_data_asset.build_batch_request()

        # return data validator
        return self.ge_context.get_validator(
            batch_request=self.ge_batch_request,
            expectation_suite_name=self.ge_expectation_suite_name,
            data_asset_name=self.ge_data_asset,
        )
