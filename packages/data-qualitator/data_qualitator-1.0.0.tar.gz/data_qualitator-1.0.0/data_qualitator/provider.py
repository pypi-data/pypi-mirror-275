"""DataQualityProvider"""

from data_qualitator import factory
from data_qualitator.utils import constants
from data_qualitator.services.filesystem.csv.builder import FilesystemCsvBuilder
from data_qualitator.services.filesystem.parquet.builder import FilesystemParquetBuilder
from data_qualitator.services.gcp.cloudstorage.csv.builder import (
    GoogleCloudPlatformCloudStorageCsvBuilder,
)
from data_qualitator.services.gcp.cloudstorage.parquet.builder import (
    GoogleCloudPlatformCloudStorageParquetBuilder,
)
from data_qualitator.services.sql.builder import SQLBuilder


class DataQualityProvider(factory.DataQualityFactory):
    """DataQualityProvider"""

    def get(self, service_id, **kwargs):
        """get"""
        return self.create(service_id, **kwargs)


services = DataQualityProvider()

services.register(constants.FILESYSTEM_CSV, FilesystemCsvBuilder())
services.register(constants.FILESYSTEM_PARQUET, FilesystemParquetBuilder())
services.register(
    constants.GOOGLE_CLOUD_PLATFORM_CLOUDSTORAGE_CSV,
    GoogleCloudPlatformCloudStorageCsvBuilder(),
)
services.register(
    constants.GOOGLE_CLOUD_PLATFORM_CLOUDSTORAGE_PARQUET,
    GoogleCloudPlatformCloudStorageParquetBuilder(),
)
services.register(constants.SQL, SQLBuilder())
