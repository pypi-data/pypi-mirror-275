"""FilesystemCsvBuilder"""

from data_qualitator.services.filesystem.csv.service import FilesystemCsvService


class FilesystemCsvBuilder:
    """FilesystemCsvBuilder"""

    def __init__(self):
        """__init__"""
        self._instance = None

    def __call__(self, **kwargs):
        """__call__"""
        if not self._instance:
            self._instance = FilesystemCsvService(**kwargs)
        return self._instance
