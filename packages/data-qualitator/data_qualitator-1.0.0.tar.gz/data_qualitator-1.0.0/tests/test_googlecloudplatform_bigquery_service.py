import unittest
from data_qualitator import provider
from data_qualitator.utils import constants


class TestPostgreSQLService(unittest.TestCase):

    def setUp(self):
        config = {
            "project_root_dir": "./tmp/test_postgresql",
            "test_name": "testing_postgresql",
        }
        self.dq = provider.services.get(constants.SQL, **config)

        gcp_project_id = "friendly-folio-418702"
        gcp_dataset_id = "testds"
        gcp_credentials_path = (
            "/Users/jaymilagroso/Downloads/friendly-folio-418702-dcfc537a6a00.json"
        )

        self.validator = self.dq.validator(
            connection_str=f"bigquery://{gcp_project_id}/{gcp_dataset_id}?\
                credentials_path={gcp_credentials_path}",
            sql="""
            SELECT * FROM testtbl;
""",
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
