"""GoogleCloudPlatformCloudStorageParquetBuilder"""

from data_qualitator.services.gcp.cloudstorage.parquet.service import (
    GoogleCloudPlatformCloudStorageParquetService,
)


class GoogleCloudPlatformCloudStorageParquetBuilder:
    """GoogleCloudPlatformCloudStorageParquetBuilder"""

    def __init__(self):
        """__init__"""
        self._instance = None

    def __call__(self, **kwargs):
        """__call__"""
        if not self._instance:
            self._instance = GoogleCloudPlatformCloudStorageParquetService(**kwargs)
        return self._instance
