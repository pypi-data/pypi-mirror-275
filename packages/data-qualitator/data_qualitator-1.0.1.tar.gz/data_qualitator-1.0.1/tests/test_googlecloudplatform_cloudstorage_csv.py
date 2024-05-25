import unittest
from data_qualitator import provider
from data_qualitator.utils import constants


class TestGoogleCloudPlatformCloudStorageCsv(unittest.TestCase):

    def setUp(self):
        config = {
            "project_root_dir": "./tmp/test_gcp_gcs_csv",
            "test_name": "testing_gcp_gcs_csv",
        }
        self.dq = provider.services.get(
            constants.GOOGLE_CLOUD_PLATFORM_CLOUDSTORAGE_CSV, **config
        )

        self.validator = self.dq.validator(
            bucket_or_name="testdev2024",
            gcs_options={},
            batching_regex=r"test_(?P<year>\d{4})(?P<month>\d{2})(?P<day>\d{2})\.csv",
            gcs_prefix="csv/",
        )

    def test_build_docs(self):
        context = self.dq.ge_context
        result = self.validator.expect_table_column_count_to_equal(5)
        assert result["success"] is True

        result = self.validator.expect_column_values_to_not_be_null(
            column="id", mostly=0.99
        )
        assert result["success"] is True

        result = self.validator.expect_column_values_to_be_between(
            column="age", min_value=1, max_value=100, mostly=0.99
        )
        assert result["success"] is True

        result = self.validator.expect_table_columns_to_match_ordered_list(
            ["id", "name", "mobile", "age", "date"]
        )
        assert result["success"] is True

        result = self.validator.expect_column_values_to_match_regex(
            column="mobile", regex="^9\d{9}$", mostly=0.99
        )
        assert result["success"] is True

        self.validator.save_expectation_suite(discard_failed_expectations=False)
        checkpoint = context.add_or_update_checkpoint(
            name="test_build_docs", validator=self.validator
        )
        checkpoint.run()
        context.build_data_docs()
        assert checkpoint is not None
