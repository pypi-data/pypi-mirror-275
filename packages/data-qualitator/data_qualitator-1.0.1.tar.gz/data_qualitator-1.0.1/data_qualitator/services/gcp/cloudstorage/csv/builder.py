"""GoogleCloudPlatformCloudStorageCsvBuilder"""

from data_qualitator.services.gcp.cloudstorage.csv.service import (
    GoogleCloudPlatformCloudStorageCsvService,
)


class GoogleCloudPlatformCloudStorageCsvBuilder:
    """GoogleCloudPlatformCloudStorageCsvBuilder"""

    def __init__(self):
        """__init__"""
        self._instance = None

    def __call__(self, **kwargs):
        """__call__"""
        if not self._instance:
            self._instance = GoogleCloudPlatformCloudStorageCsvService(**kwargs)
        return self._instance
