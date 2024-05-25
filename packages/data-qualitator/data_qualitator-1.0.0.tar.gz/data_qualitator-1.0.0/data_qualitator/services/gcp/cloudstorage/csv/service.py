"""GoogleCloudPlatformCloudStorageCsvService"""

import great_expectations as ge
import time


class GoogleCloudPlatformCloudStorageCsvService:
    """GoogleCloudPlatformCloudStorageCsvService"""

    def __init__(self, **kwargs):
        """__init__"""
        self.ge_context = ge.get_context(
            project_root_dir=kwargs.get("project_root_dir", "./tmp/gcp/gcs/csv")
        )
        self.ge_transaction_name = kwargs.get("test_name")
        self.ge_datasource = None
        self.ge_data_asset = None
        self.ge_batch_request = None
        self.ge_expectation_suite_name = None

    def validator(self, **kwargs):
        """validator"""
        # the gcp bucket name
        bucket_or_name = kwargs.get("bucket_or_name")
        # the gcp bucket options
        gcs_options = kwargs.get("gcs_options")
        # the gcs file pattern
        batching_regex = kwargs.get("batching_regex")
        # the gcs bucket directory
        gcs_prefix = kwargs.get("gcs_prefix")

        # great expectations data source
        if not self.ge_datasource:
            self.ge_datasource = self.ge_context.sources.add_pandas_gcs(
                name=f"{self.ge_transaction_name}_datasource_{str(int(time.time()))}",
                bucket_or_name=bucket_or_name,
                gcs_options=gcs_options,
            )

        # great expectations data asset
        data_asset_name = f"{self.ge_transaction_name}_asset"
        if not self.ge_data_asset:
            self.ge_data_asset = self.ge_datasource.add_csv_asset(
                name=data_asset_name,
                batching_regex=batching_regex,
                gcs_prefix=gcs_prefix,
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
